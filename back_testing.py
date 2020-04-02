import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")

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
print("MDD: ", df['dd'].max())
print("HPR: ", df['hpr'][-2])
df.to_excel("larry_ma.xlsx")

"""
라인 6: ‘close’ 컬럼을 사용해서 각 거래일에 대해 5일 이동평균을 계산합니다. shift(1)을 호출해서 계산된 5일 이동평균 값을 한 행 밑으로 내려 저장합니다. 
라인 9: 거래일의 시가가 전일 종가까지 계산된 5일 이동평균보다 크면 ‘bull’ 컬럼에 True를 저장하고 그렇지 않으면 False를 저장합니다. 
라인 12: 매수 조건에 ‘상승장’ 여부를 저장하고 있는 ‘bull’ 컬럼을 추가로 확인합니다. 조건을 추가할 때 and가 아니라 ‘&’를 사용해야 합니다.
"""