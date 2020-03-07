import re
import json
import urllib.request

from slackbot.bot import respond_to

url = 'https://tetsudo.rti-giken.jp/free/delay.json'


def deferred_train_search(name):
    delay_info = {}
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        # body = res.read()
        delay_info = json.loads(res.read())

    for delay_train in delay_info:
        print(delay_train["name"])
        if delay_train["name"] == name:
            return True


@respond_to(r'^遅延\s.*$')
def delay_train(message):

    text = message.body['text']
    name = re.match(".*\\s([0-9]+):([0-9]+)", text)
    if deferred_train_search(name):
        message.reply(name + "は遅延情報があります")
    else:
        message.reply(name + "に遅延情報はありません")
