import pybithumb
import numpy as np


def get_ror(k=0.5):
    df = pybithumb.get_ohlcv("BTC")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))

"""    
라인 5: ror(rate of returns)를 계산하는 코드를 함수로 만들어줍니다. 이때 함수는 k 값을 함수의 인자(parameter)로 입력받습니다. 
라인 19: 0.1부터 1.0까지(미 포함) 0.1씩 증가한 값으로 for loop을 만들기 위해 numpy 모듈의 arange() 함수를 사용하면 됩니다. 
참고로 파이썬의 range() 함수는 정숫값만 사용 가능합니다. 라인 20: get_ror() 함수를 호출하여 입력된 k 값에 따른 수익률을 계산합니다. 
라인 21: k 값과 수익률을 화면에 출력해줍니다.

위 코드를 실행하는 시점에 따라 결괏값은 다르겠지만 필자가 2018년 12월에 실행한 데이터에 의하면 비트코인에 대해서는 
k 값이 0.8일 때 가장 높은 수익률이 나오는 것을 확인할 수 있습니다. 
참고로 수수료(fee)를 고려하지 않는 경우에는 0.5일 때가 가장 높은 기간수익률이 나왔습니다.
"""