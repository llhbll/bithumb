import pybithumb as bt
import datetime

# tickers = bt.get_tickers()
#
# for i in str(1)*3:
#     price = bt.get_current_price("BTC")
#     print(price)
#     time.sleep(1)

detail = bt.get_market_detail("BTC")
print(detail)

# orderbook = bt.get_orderbook("BTC")
# bids = orderbook['bids']
# asks = orderbook['asks']
#
# for bid in bids:
#     price = bid['price']
#     quant = bid['quantity']
#     print("매수호가:", price, "매수잔량:", quant)
#
# for ask in asks:
#     print(ask)
# ms = int(orderbook["timestamp"])
# dt = datetime.datetime.fromtimestamp(ms/1000)
# print(dt)
# for k in orderbook:
#     print(k)
#
# all = bt.get_current_price("ALL")
#
# for ticker, data in all.items():
#     print(ticker, data["closing_price"])

# btc = bt.get_ohlcv("BTC")
# close = btc['close']
# print(close)



