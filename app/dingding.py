import requests,json

# windows
from app.BinanceAPI import BinanceAPI
from app.authorization import dingding_token, recv_window,api_secret,api_key


class Message:

    def buy_limit_msg(self,market, quantity, rate):
        try:
            # res = BinanceAPI(api_key,api_secret).buy_limit(market, quantity, rate)
            res = BinanceAPI.buy_limit(market, quantity, rate)
            if res=={}:#:or res['orderId']:
                buy_info = "flow报警：币种为：{cointype}。买单价为：{price}。买单量为：{num}".format(cointype=market,price=rate,num=quantity)
                self.dingding_warn(buy_info)
                return res
        except BaseException as e:
            error_info = "flow报警：币种为：{cointype},买单失败.api返回内容为:{reject}".format(cointype=market,reject=res)
            print(error_info)
            self.dingding_warn(error_info)


    def sell_limit_msg(self,market, quantity, rate):
        '''
        :param market:
        :param quantity: 数量
        :param rate: 价格
        :return:
        '''
        try:
            # res = BinanceAPI(api_key,api_secret).sell_limit(market, quantity, rate)
            res = BinanceAPI().sell_limit(market, quantity, rate)
            if res=={} : #or res['orderId']:
                buy_info = "报警：币种为：{cointype}。卖单价为：{price}。卖单量为：{num}".format(cointype=market,price=rate,num=quantity)
                self.dingding_warn(buy_info)
                return res
        except BaseException as e:
            error_info = "报警：币种为：{cointype},卖单失败.api返回内容为:{reject}".format(cointype=market,reject=res)
            self.dingding_warn(error_info+str(res))
            print(error_info)
            return res

    def dingding_warn(self,text):
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % dingding_token
        json_text = self._msg(text)
        requests.post(api_url, json.dumps(json_text), headers=headers).content

    def _msg(self,text):
        json_text = {
            "msgtype": "text",
            "at": {
                "atMobiles": [
                    "11111"
                ],
                "isAtAll": False
            },
            "title": "flow"+text,
            "text": {
                "content": text
            }
        }
        return json_text

if __name__ == "__main__":
    msg = Message()
    print(msg.buy_limit_msg("BTCUSDT",0.01,40000))