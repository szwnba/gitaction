#-*- encoding: utf-8 -*-
#
import sys

import requests

from app.dingdingapi import senddingding_news

sys.path.append('.')

import json
from urllib.request import urlopen


def get_fear_greed():
    url ="https://api.alternative.me/fng/"
    result = requests.get(url).json()


if __name__ == '__main__':
    url = "https://api.alternative.me/fng/"
    result = requests.get(url).json()
    infos=[]
    for index in result["data"]:
       item = {}
       item['title']=  index["value_classification"] + ": " + index["value"] + "\n\n> ![img](https://alternative.me/crypto/fear-and-greed-index.png)\n\n"
       item['link']="https://alternative.me/crypto/fear-and-greed-index/"
       item['subtype'] = "flow 市场情绪指数"
       infos.append(item)
    senddingding_news("数字货币", infos)
