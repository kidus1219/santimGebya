import hmac, hashlib
from urllib.parse import unquote
from copy import deepcopy
from functools import wraps
from telegram.constants import ChatAction
from telegram import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, ForceReply, MenuButtonWebApp, MenuButtonDefault
from .const import P_H, BOT_TOKEN


class BotPost:
    dispatcher = None

    def __init__(self, template: dict, var_text: list = None, var_key: list = None, var_menu: list = None,
                 new_key: list = None,
                 group: int = 0):
        self.id = template.get('id')
        self.text = template.get('text', ".")
        self.keyboard_type = template.get('keyboard_type')
        self.markup = None
        self.state = template.get('state')
        self.group = group
        if new_key is None:
            self.raw_keyboard = deepcopy(template.get('keyboard', []))
        else:
            self.raw_keyboard = new_key
        if var_text is not None:
            self.text = self.text_molder(self.text, var_text)  # by reference or by value
        if var_key is not None:
            self.key_molder(self.raw_keyboard, var_key)
        if not self.raw_keyboard:
            self.markup = None
        else:
            self.markup = self.keyboard_builder(self.keyboard_type, self.raw_keyboard)

        if template.get('menu_button') is not None and isinstance(template.get('menu_button'), list) and len(
                template.get('menu_button')) == 2:
            self.menu_button = template.get('menu_button')
            if var_menu is not None:
                self.menu_button[1] = self.text_molder(self.menu_button[1], var_menu)  # by reference or by value
        else:
            self.menu_button = None

    @staticmethod
    def text_molder(text, var_text):
        for x in var_text:
            text = text.replace(P_H, str(x), 1)
        text = text.replace(P_H, "...")
        return text

    @staticmethod
    def key_molder(raw_keyboard, var_key):  # TODO test this Extensively
        for row in raw_keyboard:
            for btn in row:
                for i in range(len(btn)):
                    if not var_key:
                        return
                    if P_H in btn[i]:
                        while var_key[0] and P_H in btn[i]:
                            jj = btn[i].replace(P_H, str(var_key[0][0]), 1)
                            btn[i] = jj
                            del var_key[0][0]
                        del var_key[0]

    @staticmethod
    def keyboard_builder(keyboard_type, raw_keyboard, input_field_placeholder="..."):
        keyrow = []
        keyboard = []
        if keyboard_type == "inline":
            for x in raw_keyboard:
                for y in x:
                    if len(y) < 3 or None in y or P_H in y:
                        continue
                    if y[1] == "callback":
                        keyrow.append(InlineKeyboardButton(text=y[0], callback_data=y[2]))
                    elif y[1] == "webapp":
                        keyrow.append(InlineKeyboardButton(text=y[0], web_app=WebAppInfo(url=y[2])))
                keyboard.append(keyrow)
                keyrow = []
            return InlineKeyboardMarkup(keyboard)
        elif keyboard_type == "reply":
            for x in raw_keyboard:
                for y in x:
                    if not y or None in y or P_H in y:
                        continue
                    if len(y) == 1:
                        keyrow.append(y[0])
                    elif len(y) == 2:
                        if y[1] == "contact":
                            keyrow.append(KeyboardButton(text=y[0], request_contact=True))
                        elif y[1] == "location":
                            keyrow.append(KeyboardButton(text=y[0], request_location=True))
                        # check more type, like poll ..
                    elif len(y) == 3:
                        if y[1] == "webapp":
                            keyrow.append(KeyboardButton(text=y[0], web_app=WebAppInfo(url=y[2])))
                keyboard.append(keyrow)
                keyrow = []
            return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        elif keyboard_type == "remove":
            return ReplyKeyboardRemove()
        elif keyboard_type == "force_reply":
            return ForceReply(input_field_placeholder=input_field_placeholder)  # get(x, None)

    async def printer(self, chat_id, overwrite=False) -> int:
        dispatcher = self.__class__.dispatcher
        msg_store = dispatcher.user_data[chat_id].setdefault('msg_store', {})
        msg_store_sorted = sorted(msg_store)
        # if self.group in msg_store:
            # target = msg_store_sorted[msg_store_sorted.index(self.group) + int(overwrite):]
        for x in msg_store_sorted:
            if x < self.group:
                continue
            try:
                await dispatcher.bot.delete_message(chat_id=chat_id, message_id=msg_store[x])
            except Exception as e:
                await dispatcher.bot.send_message(chat_id=chat_id,
                                                  text="🔲🔲🔲<code> RESTART </code>🔲🔲🔲",
                                                  parse_mode="html")
                print("Delete Failed", e)
                try:
                    await dispatcher.bot.edit_message_text(chat_id=chat_id,
                                                           text="Delete Failed | Edit Succeed",
                                                           message_id=msg_store[x], parse_mode="html",
                                                           reply_markup=self.markup)
                except Exception as e:
                    print("Edit Failed", e)
            finally:
                del msg_store[x]

        if overwrite:
            # TODO: come up with something to.. editing a message deleted by user
            try:
                temp_oci = dispatcher.user_data[chat_id]['overwrite_char_index'] = abs(
                    dispatcher.user_data[chat_id].get('overwrite_char_index', 1) - 1)
                await dispatcher.bot.edit_message_text(chat_id=chat_id,
                                                       text=self.text + "\n" + [">>", ">"][
                                                           temp_oci],
                                                       message_id=msg_store[self.group],
                                                       parse_mode="html", reply_markup=self.markup)

            except Exception as e:
                print("Edit Failed", e)
        else:
            msg_store[self.group] = (await dispatcher.bot.send_message(chat_id=chat_id, text=self.text,
                                                                       parse_mode="html",
                                                                       reply_markup=self.markup)).message_id
    # else:
        #     msg_store[self.group] = (await dispatcher.bot.send_message(chat_id=chat_id, text=self.text, parse_mode="html", reply_markup=self.markup)).message_id

        try:
            if self.menu_button is not None:
                await dispatcher.bot.set_chat_menu_button(chat_id, MenuButtonWebApp(self.menu_button[0],
                                                                                    WebAppInfo(self.menu_button[1])))
            else:  # TODO find a better way so useless request wont be sent on every non web_menu_button, comeback after implementing persistance
                await dispatcher.bot.set_chat_menu_button(chat_id, MenuButtonDefault())
        except Exception as e:
            print("customerbot.utils.BotPost.printer menu_button Exception => ", e)

        return self.state

    def __repr__(self):
        return self.text



def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context, *args, **kwargs)

        return command_func

    return decorator


send_typing_action = send_action(ChatAction.TYPING)


# send_upload_video_action = send_action(ChatAction.UPLOAD_VIDEO)
# send_upload_photo_action = send_action(ChatAction.UPLOAD_PHOTO)


def validate_webapp_data(init_data):
    data_check_string = []
    hash_string = ""
    for chunk in unquote(init_data).split("&"):
        chunk_rry = chunk.split("=")
        if chunk_rry[0] == "hash":
            hash_string = chunk_rry[1]
        else:
            data_check_string.append(chunk_rry)
    data_check_string = sorted(data_check_string, key=lambda x: x[0])
    data_check_string = "\n".join([f"{x[0]}={x[1]}" for x in data_check_string])

    secret_key = hmac.new("WebAppData".encode(), BOT_TOKEN.encode(),
                          hashlib.sha256).digest()
    data_check = hmac.new(secret_key, data_check_string.encode(),
                          hashlib.sha256)
    return data_check.hexdigest() == hash_string


def extract_webapp_data(init_data):
    return {x.split("=")[0]: x.split("=")[1] for x in unquote(init_data).split("&")}
