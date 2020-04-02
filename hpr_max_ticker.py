import pybithumb
import numpy as np


def get_hpr(ticker):
    try:
        df = pybithumb.get_ohlcv(ticker)
        df = df['2018']

        df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
        df['range'] = (df['high'] - df['low']) * 0.5
        df['target'] = df['open'] + df['range'].shift(1)
        df['bull'] = df['open'] > df['ma5']

        fee = 0.0032
        df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                              df['close'] / df['target'] - fee,
                              1)

        df['hpr'] = df['ror'].cumprod()
        df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
        return df['hpr'][-2]
    except:
        return 1


tickers = pybithumb.get_tickers()

hprs = []
for ticker in tickers:
    hpr = get_hpr(ticker)
    hprs.append((ticker, hpr))

sorted_hprs = sorted(hprs, key=lambda x:x[1], reverse=True)
print(sorted_hprs[:5])

"""
라인 5~24: 기존의 백테스팅 코드를 함수로 만들어줍니다. 2018년도에 대해서만 백테스팅하며 예외처리를 위해 try ~ except 구문을 사용합니다. 
라인 27: 빗썸 거래소에서 거래되는 모든 코인의 티커 목록을 얻어옵니다. 라인 29: for 루프를 실행하기 전에 리스트를 만들어줍니다. 
라인 32: 리스트에 코인의 티커와 코인의 기간수익률을 저장합니다. 
라인 34: 기간수익률을 기준으로 오름차순 정렬합니다. 
라인 35: 기간수익률이 높은 5개의 코인 정보를 화면에 출력합니다.
"""