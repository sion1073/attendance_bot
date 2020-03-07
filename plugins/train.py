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


@respond_to(r'^遅延\s.*$')
def delay_train(message):

    text = message.body['text']
    result = re.match(".*\\s([0-9]+):([0-9]+)", text)
    deferred_train_search(result)
