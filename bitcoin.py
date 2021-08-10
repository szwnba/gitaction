from BinanceAPI import BinanceAPI

if __name__ == "__main__":
    # instance = BinanceAPI(api_key,api_secret)
    instance = BinanceAPI()
    # print(instance.buy_limit("EOSUSDT",5,2))
    # print(instance.get_ticker_price("WINGUSDT"))
    print(instance.get_ticker_price("BTCUSDT"))