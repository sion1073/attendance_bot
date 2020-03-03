import random
from datetime import datetime, timedelta, timezone

from slackbot.bot import respond_to

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))


@respond_to('出勤')
def work_time(message):

    JST = timezone(timedelta(hours=+9), 'JST')
    start_now = datetime.now(JST)
    end_time = start_now + timedelta(hours=8, minutes=45)
    message.reply(end_time.strftime("%H:%M"))
