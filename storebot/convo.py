from telegram import Update
from telegram.ext import ConversationHandler, ContextTypes, CommandHandler, MessageHandler, filters
from . import template
from .utils import BotPost
from core.models import Store


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    astore = 1 #Store.objects.filter(ownerId=update.effective_chat.id)
    print(astore)
    if astore:
        return await BotPost(template.HOME, var_key=[[update.effective_user.id], [update.effective_user.id]]).printer(update.effective_chat.id)
    else:
        return await BotPost(template.GATE).printer(update.effective_chat.id)


async def help_btn(update: Update, _: ContextTypes.DEFAULT_TYPE):
    return await BotPost(template.HELP).printer(update.effective_chat.id)


async def about_btn(update: Update, _: ContextTypes.DEFAULT_TYPE):
    return await BotPost(template.ABOUT).printer(update.effective_chat.id)


conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start_command)
    ],
    states={
        template.GATE['state']: [
            MessageHandler(filters.Regex(f"^{template.GATE['keyboard'][0][0][0]}$"), help_btn),
            MessageHandler(filters.Regex(f"^{template.GATE['keyboard'][0][1][0]}$"), about_btn),
        ],
        template.HOME['state']: [
            MessageHandler(filters.Regex(f"^{template.HOME['keyboard'][1][0][0]}$"), help_btn),
            MessageHandler(filters.Regex(f"^{template.HOME['keyboard'][1][1][0]}$"), about_btn),
        ],
        template.HELP['state']: [
            MessageHandler(filters.Regex(f"^{template.HELP['keyboard'][0][0][0]}$"), start_command),
        ],
        template.ABOUT['state']: [  # ABOUT
            MessageHandler(filters.Regex(f"^{template.ABOUT['keyboard'][0][0][0]}$"), start_command),
        ],
    },
    fallbacks=[
        CommandHandler("start", start_command)
    ],
)
