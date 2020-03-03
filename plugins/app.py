import random
import datetime

from slackbot.bot import respond_to

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))


@respond_to('出勤')
def work_time(message):
    start_now = datetime.datetime.now()
    end_time = start_now + datetime.timedelta(hours=8, minutes=45)
    message.reply(end_time.strftime("%H:%M"))
