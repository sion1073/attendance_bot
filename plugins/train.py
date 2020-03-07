import re
import json
import urllib.request

from slackbot.bot import respond_to

url = 'https://tetsudo.rti-giken.jp/free/delay.json'


def deferred_train_search(name):
    delay_info = {}
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        delay_info = json.loads(res.read())

    for delay_train in delay_info:
        if delay_train["name"] == name:
            return True


@respond_to(r'^遅延\s.*$')
def delay_train(message):

    text = message.body['text']
    result = re.match("遅延\\s(.*)", text)
    name = result.group(1)
    if deferred_train_search(name):
        message.reply(name + "は遅延情報があります")
    else:
        message.reply(name + "に関する情報はありません")
