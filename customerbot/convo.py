import json
from asgiref.sync import sync_to_async
from django.db import IntegrityError
from telegram import Update
from telegram.ext import ConversationHandler, ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters
"""
from customer.models import CustomerUser
from store.models import Store
from . import template
from .utils import BotPost
from .const import MAIN_HOST


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if isinstance(context.args, list) and len(context.args) == 1:
        if context.args[0] == 'loggedIn':
            context.user_data['loggedIn'] = True
        elif context.args[0] == 'loggedOut':
            context.user_data['loggedIn'] = False
    if context.user_data.get('loggedIn', True):  # TODO flipped this just for development test
        return await BotPost(template.HOME, var_key=[[update.effective_user.id], [update.effective_user.id], [update.effective_user.id]]).printer(update.effective_chat.id)
    else:
        return await BotPost(template.GATE, var_menu=[update.effective_user.id]).printer(update.effective_chat.id)


async def register_btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['tgcontact'] = update.message.contact
    return await BotPost(template.ACCEPT_PASSWORD).printer(update.effective_chat.id)


async def auth_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('tgcontact') is None:
        return await start_command(update, context)
    given = update.message.text  # TODO SQL INJECTION handle it
    if not given.isdigit():
        return await BotPost({'text': "Only numbers allowed"}, group=1).printer(update.effective_chat.id)
    if len(given) != 4:
        return await BotPost({'text': "It must be 4 digit"}, group=1).printer(update.effective_chat.id)
    context.user_data['tgcontact_password'] = given
    return await BotPost(template.CONFIRM_PASSWORD, var_text=[given]).printer(update.effective_chat.id)


async def confirm_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    given = update.callback_query.data
    if given == 'yes':
        if context.user_data.get('tgcontact') is None or context.user_data.get('tgcontact_password') is None:
            await update.callback_query.answer("Failed", show_alert=True)
            return await start_command(update, context)
        try:
            await sync_to_async(CustomerUser.objects.create_user)(
                username=context.user_data['tgcontact'].user_id,
                first_name=context.user_data['tgcontact'].first_name,
                last_name=context.user_data['tgcontact'].last_name if context.user_data['tgcontact'].last_name is not None else "",
                password=context.user_data['tgcontact_password'],
                tgusername=update.effective_user.username if update.effective_user.username is not None else "",
                tgphone_number=context.user_data['tgcontact'].phone_number[4:] if context.user_data['tgcontact'].phone_number[0] == "+" else context.user_data['tgcontact'].phone_number[3:],
                phone_number=context.user_data['tgcontact'].phone_number[4:] if context.user_data['tgcontact'].phone_number[0] == "+" else context.user_data['tgcontact'].phone_number[3:],
            )
        except IntegrityError as e:  # TODO for users who deleted their telegram account what i ca do here is,
            # check if their tguid is different.
            print(e)  # log this
            print('Xx customerbot.convo.confirm_password IntegrityError => ', e)
            await update.callback_query.answer("Failed: It seems like you are already registered\nplease contact the "
                                               "admins if that is not the case", show_alert=True)
        except Exception as e:  # this might catch uniqueness problem. if yes handle em properly
            print('Xx customerbot.convo.confirm_password Exception => ', e)
            await update.callback_query.answer("Failed: something went wrong, please contact the admins", show_alert=True)
        else:  # TODO what if i just don't use else, instead write inside try
            await update.callback_query.answer("Successful.\nPlease login now", show_alert=True)
        finally:  # TODO what if i just don't use finally at all
            return await start_command(update, context)
    else:
        context.user_data['tgcontact_password'] = None
        await update.callback_query.answer("Canceled")
        return await BotPost(template.ACCEPT_PASSWORD).printer(update.effective_chat.id)


async def cancel_auth_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['tgcontact'] = None
    return await start_command(update, context)


async def help_btn(update: Update, _: ContextTypes.DEFAULT_TYPE):
    return await BotPost(template.HELP).printer(update.effective_chat.id)


async def contactus_btn(update: Update, _: ContextTypes.DEFAULT_TYPE):
    return await BotPost(template.CONTACTUS).printer(update.effective_chat.id)


async def about_btn(update: Update, _: ContextTypes.DEFAULT_TYPE):
    return await BotPost(template.ABOUT).printer(update.effective_chat.id)


# HOME
async def store_list(update: Update, _: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    row = []
    i = 0
    opened_symbol = "🟩"
    closed_symbol = "🟥"
    async for x in Store.objects.all().order_by('suid'):
        row.append([f"{opened_symbol if x.is_open else closed_symbol} {x.name}", "webapp", f"{MAIN_HOST}/customer/{update.effective_chat.id}/store/{x.suid}/"])
        i += 1
        if i == 2:
            keyboard.append(row)
            row = []
            i = 0
    if row:
        keyboard.append(row)
    keyboard.append([["Back"]])
    return await BotPost(template.STORE, new_key=keyboard).printer(update.effective_chat.id)


async def message_from_webapp(update: Update, _: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.effective_message.web_app_data.data)
    print(data)

conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start_command)
    ],
    states={
        template.GATE['state']: [
            MessageHandler(filters.CONTACT, register_btn),
            MessageHandler(filters.Regex(f"^{template.GATE['keyboard'][1][0][0]}$"), help_btn),
            MessageHandler(filters.Regex(f"^{template.GATE['keyboard'][1][1][0]}$"), about_btn),
        ],
        template.HOME['state']: [
            MessageHandler(filters.Regex(f"^{template.HOME['keyboard'][0][0][0]}$"), store_list),
            MessageHandler(filters.Regex(f"^{template.HOME['keyboard'][2][0][0]}$"), help_btn),
            MessageHandler(filters.Regex(f"^{template.HOME['keyboard'][2][1][0]}$"), about_btn),
        ],
        template.ACCEPT_PASSWORD['state']: [
            MessageHandler(filters.Regex(f"^{template.ACCEPT_PASSWORD['keyboard'][0][0][0]}$"), cancel_auth_password),
            MessageHandler(filters.TEXT, auth_password),
        ],
        template.CONFIRM_PASSWORD['state']: [
            CallbackQueryHandler(confirm_password, pattern="^(yes|no)$"),
        ],
        template.HELP['state']: [
            MessageHandler(filters.Regex(f"^{template.HELP['keyboard'][0][0][0]}$"), start_command),
        ],
        template.ABOUT['state']: [
            MessageHandler(filters.Regex(f"^{template.ABOUT['keyboard'][0][0][0]}$"), start_command),
        ],
        template.STORE['state']: [
            MessageHandler(filters.Regex("Back"), start_command),
        ],

    },
    fallbacks=[
        CommandHandler("start", start_command),  # or may be capture every thing filters.All and call start_command
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, message_from_webapp)
    ],
)


async def waiting_order(var_text, chat_id):
    return await BotPost(template.WAITING_ORDER, var_text=var_text, group=-1).printer(chat_id)
"""