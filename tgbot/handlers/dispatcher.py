# -*- coding: utf-8 -*-

"""Telegram event handlers."""
import pytz
import telegram

from telegram.ext import (
    Updater, Dispatcher, Filters,
    MessageHandler,JobQueue,
    CommandHandler,
    InlineQueryHandler, CallbackQueryHandler,
    ChosenInlineResultHandler, PollAnswerHandler, Defaults
)

from dtb.settings import TELEGRAM_TOKEN

from tgbot.handlers import commands
from tgbot.handlers.registration.handlers import setup_dispatcher_conv as setup_dispatcher_reg
from tgbot.handlers.main.handlers import setup_dispatcher_conv as setup_dispatcher_main
from tgbot.handlers.profile.handlers import setup_dispatcher_conv as setup_dispatcher_prof
from payments.handlers import setup_dispatcher_conv as setup_dispatcher_pay
from tgbot.handlers.manage_members.handlers import setup_dispatcher_conv as setup_dispatcher_manage_memb
from tgbot.handlers.messages.handlers import setup_dispatcher_conv as setup_dispatcher_mess
from events.handlers import setup_dispatcher_conv as setup_dispatcher_events
from tgbot.handlers.groups.handlers import setup_dispatcher_conv as setup_dispatcher_groups
from statistic.handlers import setup_dispatcher_group as setup_dispatcher_tg_group
from subscribe.handlers import setup_dispatcher_conv as setup_dispatcher_pkgs
from advert.handlers import setup_dispatcher_conv as setup_dispatcher_advert
from advert.handlers_reqw import setup_dispatcher_conv as setup_dispatcher_reqw
from sheduler.tasks import restarts_tasks

from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
# Отладочный пререхватчик. Ловит все апдейты 
# Когда основные хендлеры не ловят апдейт он ловится тут
# и можно узнать причину
def catch_all_updates(update: Update, context: CallbackContext):
    #print(update.update_id)
    pass

def setup_dispatcher(dp: Dispatcher):
    """
    Adding handlers for events from Telegram
    """
    dp.add_handler(MessageHandler(None,catch_all_updates), group = 2)
    dp.add_handler(CallbackQueryHandler(catch_all_updates), group = 2)

    dp.add_handler(CommandHandler("start", commands.command_start, Filters.chat_type.private))
    dp.add_handler(CommandHandler("restart_tasks", commands.command_restart_tasks, Filters.chat_type.private))

    setup_dispatcher_reg(dp) #заполнение обработчиков регистрации
    setup_dispatcher_main(dp) #заполнение обработчиков главного диалога
    setup_dispatcher_prof(dp) #заполнение обработчиков работы с профайлом
    setup_dispatcher_pay(dp) #заполнение обработчиков работы с платежами
    setup_dispatcher_manage_memb(dp) #заполнение обработчиков работы с поиском
    setup_dispatcher_mess(dp) #заполнение обработчиков работы с сообщениями
    setup_dispatcher_events(dp) #заполнение обработчиков работы с мероприятиями
    setup_dispatcher_groups(dp) #заполнение обработчиков работы с группами пользователей
    setup_dispatcher_pkgs(dp) #заполнение обработчиков работы с пакетами участия
    setup_dispatcher_advert(dp) #заполнение обработчиков работы с рекламными рассылками
    setup_dispatcher_reqw(dp) #заполнение обработчиков работы с разными заявками

    setup_dispatcher_tg_group(dp) #заполнение обработчиков сообщений в группах(каналах) телеграм

    dp.add_handler(MessageHandler(Filters.text & Filters.chat_type.private, commands.command_start))


    return dp


def run_pooling():

    defaults = Defaults(parse_mode=telegram.ParseMode.HTML, tzinfo=pytz.timezone('Europe/Moscow'))
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True, defaults=defaults)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)
    jq = updater.job_queue
    restarts_tasks(jq)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    # global POLLING_IS_RUNNING
    # POLLING_IS_RUNNING = True
    updater.start_polling(timeout=123, drop_pending_updates=True)
    updater.idle()


def process_telegram_event(update_json):
    update = telegram.Update.de_json(update_json,bot)
    dispatcher.process_update(update)

# Global variable - best way I found to init Telegram bot
bot = telegram.Bot(TELEGRAM_TOKEN)
dispatcher = setup_dispatcher(Dispatcher(bot, None, workers=4, use_context=True))
TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
