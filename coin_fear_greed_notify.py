#-*- encoding: utf-8 -*-
#

import requests

from app.BinanceAPI import BinanceAPI
from app.dingding import Message
from app.dingdingapi import senddingding_news


def get_fear_greed():
    url ="https://api.alternative.me/fng/"
    result = requests.get(url).json()


if __name__ == '__main__':
    instance = BinanceAPI()
    msg = Message()
    url = "https://api.alternative.me/fng/"
    price = instance.get_ticker_price("BTCUSDT")
    result = requests.get(url).json()
    infos=[]
    for index in result["data"]:
       item = {}
       item['title']= "BTC价格：{},".format(price) + index["value_classification"] + ": " + index["value"] + "\n\n> ![img](https://alternative.me/crypto/fear-and-greed-index.png)\n\n"
       item['link']="https://alternative.me/crypto/fear-and-greed-index/"
       item['subtype'] = "flow 市场情绪指数"
       infos.append(item)
    senddingding_news("数字货币", infos)
