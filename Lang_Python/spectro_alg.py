import scipy.signal as signal
import math
import librosa
import numpy as np

# 내적을 구하는 것.
# 어느 한 성분을 기준으로 다른 성분이 기준 성분에 포함되어 있는 양을 뜻함.
# 즉, 두 신호가 얼마나 유사한가(혹은 얼마나 많은 공통 성분을 가졌는가)가 correlation 이 된다.
# 그런데, 입력신호가 크다고 해서 더 닮았다고 판정을 해버릴 수 있기 때문에,
# 정규화란 작업을 거친다. (정규화 : 입력된 신호의 에너지의 총합을 각각의 신호의 값과 나눠서 신호의 총 합이 1이 되게 하는 것.)

# 자기 상관계수 (Auto Correlation)
# 의의 : 현재의 신호 안에서 주기성을 찾기 위해 계산함.
# 계산 : 임의의 신호와 한 주기동안 이동시킨(Shifting) 신호의 적분값
# correlation( x(n) , x(n + T) )    //의사코드
# pitch를 추출하는 과정에서 많이 사용됨.


x = [0.1, 0.1, 0.2, 0.3, 0.4]
result = np.correlate(x, x, mode='full')
print(result)
# autocorrelation 결과. peak의 위치를 찾는 것.

y = [0.5, 0.6]
result = np.correlate(x, y, mode='full')

print(result)