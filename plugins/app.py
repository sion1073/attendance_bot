import re
import random
from datetime import datetime, timedelta, timezone

from slackbot.bot import respond_to

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))


@listen_to(r'^出勤\s[0-9]+:[0-9]+$')
def work_time(message):

    JST = timezone(timedelta(hours=+9), 'JST')
    current = datetime.now(JST)

    text = message.body['text']
    result = re.match(".*\s([0-9]+):([0-9]+)", content)

    hour = result.group(1)
    minute = result.group(2)

    start_now = datetime.datetime(
        year=current.year,
        month=current.month,
        day=current.day,
        hour=hour,
        minute=minute,
        second=0)
    end_time = start_now + timedelta(hours=8, minutes=45)
    message.reply(end_time.strftime("%H:%M"))
