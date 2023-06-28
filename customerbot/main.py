import logging
from pprint import pprint

from telegram import Update
from telegram.ext import Application, CallbackContext, MessageHandler, filters, ContextTypes
from .utils import BotPost
from .const import BOT_TOKEN, MAIN_HOST
# from .convo import conv_handler

logging.basicConfig(
    format='========================> %(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class CustomerBotApplication:
    instance = None

    def __init__(self):
        if self.__class__.instance is not None:
            pass
        self.application = Application.builder().token(BOT_TOKEN).updater(None).build()
        self.application.add_handler(MessageHandler(filters.ALL, effective_delete), -1)
        # self.application.add_handler(conv_handler)
        self.application.add_error_handler(error_handler)

    async def run(self):
        print("CUSTOMER BOT STARTING..\n.\n. ")
        await self.application.bot.set_webhook(url=f'{MAIN_HOST}/customerbot/{BOT_TOKEN}/webhook/', drop_pending_updates=True)
        await self.application.initialize()
        BotPost.dispatcher = self.application
        self.__class__.instance = self
        print("CUSTOMER BOT RUNNING.. ")

    async def handle(self, data):
        update = Update.de_json(data=data, bot=self.application.bot)
        await self.application.process_update(update)


# handlers
async def error_handler(err: CallbackContext, exterr=None):
    print('error begin\n--------------------------------------------')
    pprint(err)
    if exterr and exterr.error:
        print(exterr.error)
    print('error end\n---------------------------------')


async def effective_delete(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.delete()
