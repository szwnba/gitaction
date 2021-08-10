from app.BinanceAPI import BinanceAPI
from app.dingding import Message

if __name__ == "__main__":
    # instance = BinanceAPI(api_key,api_secret)
    instance = BinanceAPI()
    msg = Message()
    # print(instance.buy_limit("EOSUSDT",5,2))
    # print(instance.get_ticker_price("WINGUSDT"))
    price = instance.get_ticker_price("BTCUSDT")
    print(price)

    msg.dingding_warn("flow:BTC Price is {}".format(price))