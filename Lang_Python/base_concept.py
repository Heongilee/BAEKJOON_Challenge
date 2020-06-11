음소 (phoneme) : 가장 작은 소리의 단위
자소 (grapheme)
Ex)
help -> h / e / l / p
shop -> sh/ o / p	sh가 1개의 자소

monophoneme : 하나씩 나열하는 것
h / e / l / p

triphone : 좌-현재+우 형식으로 표기
h + e / h - e + l / e - l + p / l - p

Acoustic Model
오디오 -> phoneme 나 grapheme을 예측해주는 모델

Phoneme Dictionary
word -> phoneme가 기록된 정보. 즉, 발음 기호 사전

G2P Model
대규모 발음 기호 사전을 학습해서, 임의의 단어에 대한 phoneme을 예측해줌.
Phoneme Dictionary와의 차이점은 Dictionary에 없는 단어에 대해서도 발음을 예측할 수 있다.

Pitch
사람의 목소리의 Hz가 저주파일때 민감하고 고주파일때 둔감하다는 점에서 출발한 개념.
즉, 사람이 인지하는 음의 높낮이는 Hz와 비례관계가 아니라 Exponential 관계를 가짐.

log scale
사람 인지적관점에서 log scale을 취해 normalize해서 표현해야함. -> Mel-scale

데시벨(dB)
10 * log_10^(P / Pref)
1B = 10dB

Mel- scale : Melody scale 
pitch에서 발견된 사람의 음을 인지하는 기준을 반영한 scale 변환 함수.
[Hz -> 음계]의 관계는 Exponential -> log 함수 통과 -> mel-scale(의의 : linear하게 다루기 위함.)
mel-scale 역변환 -> Hz

MFCC (Mel-Frequeny cepstral coefficients)
hand-made feature
소리의 고유한 특징을 나타낼 수 있는 수치.

STFT = Spectrogram 
통상 N을 256 혹은 512로 셋업. (frame의 길이, window size와 같게 한다.)

FFT = Fast Fourier Transform
Spectrogram(x축 시간, y축 주파수, color값 magnitude)
-> 3차원의 heat map 데이터가 된다.
-> y축에서는 log scale을 취할 수도 있고, 그냥 둘 수도 있다. (선택 가능한 옵션)
-> 픽셀 값에 log scale을 취함. (dB)
-> Spectrogram의 y축(주파수)은 Nyquist limit에 따라 sampling rate의 1/2 이다.

Take log -> (Log) Mel Spectrogram

이산 코사인 변환 -> MFCC

시간축과 주파수축은 Tradeoff(한 가지를 얻으려면 하나를 포기해야하는)관계를 가져,
window size ↑, 더 많은 FFT, resolution ↑ (즉, 1Hz와 2Hz를 구분할 수 있다.)
하지만, 어느 시점에서 frequency event가 발생했는지 불 명확

window size ↓, 적은 FFT, resolution ↓
frequency event 명확

Spectral Leaking
