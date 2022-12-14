# -*- coding: utf-8 -*-

import datetime
import logging
import uuid
import re
import os

from django.conf import settings


logger = logging.getLogger('default')


def extract_user_data_from_update(update):
    """ python-telegram-bot's Update instance --> User info """
    if update.message is not None:
        user = update.message.from_user.to_dict()
    elif update.inline_query is not None:
        user = update.inline_query.from_user.to_dict()
    elif update.chosen_inline_result is not None:
        user = update.chosen_inline_result.from_user.to_dict()
    elif update.callback_query is not None and update.callback_query.from_user is not None:
        user = update.callback_query.from_user.to_dict()
    elif update.callback_query is not None and update.callback_query.message is not None:
        user = update.callback_query.message.chat.to_dict()
    elif update.poll_answer is not None:
        user = update.poll_answer.user.to_dict()
    else:
        raise Exception(f"Can't extract user data from update: {update}")

    return dict(
        user_id=user["id"],
        is_blocked_bot=False,
        **{
            k: user[k]
            for k in ["username", "first_name", "last_name", "language_code"]
            if k in user and user[k] is not None
        },
    )


def get_chat_id(update, context):
    """Extract chat_id based on the incoming object."""

    chat_id = -1

    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id
    elif update.poll is not None:
        chat_id = context.bot_data[update.poll.id]

    return chat_id


def get_file_path(instance, filename):
    """Create random unique filename for files, uploaded via admin."""

    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


def convert_2_user_time(date: datetime.datetime):
    """Получает дату в UTC. Возвращает в Мск."""

    return date + datetime.datetime.timedelta(hours=3)

def is_date(str_date: str):
    try:
        date = datetime.datetime.strptime(str_date,"%d.%m.%Y")
        return date
    except Exception:
        return False

def is_email(email: str):
    email = email.replace(" ", "")
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if email_regex.match(email):
        return email
    else:
        return False

def mystr(val)->str:
    if val == None:
        return ""
    else:
        if isinstance(val,datetime.date):
            return val.strftime("%d.%m.%Y")
        elif isinstance(val,datetime.datetime):
            return val.strftime("%H:%M, %d.%m.%Y")
        else:
            return str(val)

def get_uniq_file_name(path, name, ext):
    for num in range(999999):
        filename = f"{path}/{name}-{num}.{ext}"
        if not os.path.exists(filename):
            return f"{name}-{num}.{ext}"