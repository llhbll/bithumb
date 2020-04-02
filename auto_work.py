import time
import pybithumb
import datetime

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price(“BTC”)

def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    bithumb.buy_market_order(ticker, unit)

def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

# 빗썸에서 connect key와 Secret key 받아서 bithumb.txt에 2줄로 넣기
with open("bithumb.txt") as f:
lines = f.readlines()
key = lines[0].strip()
secret = lines[1].strip()
bithumb = pybithumb.Bithumb(key, secret)

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5("BTC")
target_price = get_target_price(“BTC”)

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10):
            target_price = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5("BTC")
            sell_crypto_currency("BTC")

        current_price = pybithumb.get_current_price("BTC")
        if (current_price > target_price) and (current_price > ma5):
            buy_crypto_currency("BTC")
    except:
        print("에러 발생")
    time.sleep(1)

"""
변동성 돌파 전략의 매수 조건을 업데이트해 봅시다. 기존에는 현재 가격이 목표가보다 높을 경우 buy_crypto_currency() 함수를 호출해서 
암호 화폐를 매수했습니다. 여기에 상승장에만 변동성 돌파 전략이 실행되도록 매수 조건식에 이동 평균과 현재가를 비교하는 코드를 추가합니다. 
Ch06/06_20.py는 상승장 투자 전략이 반영된 변동성 돌파 전략 전체 코드입니다.

라인 32~36: 전일의 5일 이동평균을 계산하는 get_yesterday_ma5() 함수를 정의합니다.
라인 40: 프로그램이 시작될 때 전일의 5일 이동평균값을 계산합니다.
라인 49: 매일 자정 5일 이동평균값을 업데이트합니다.
라인 53: 목표가뿐만 아니라 이동평균과 현재가를 비교합니다.
"""