# 참고자료 (2020-06-13 :: 17:43)
# C:\Users\gjsrl\Documents\Git_space\BAEKJOON_Challenge\Lang_Python\assets\pitch값_분석하기
# pitch 값을 이용한 특징 분석하기
import librosa
import librosa.display
import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl    
import matplotlib.font_manager as fm

# loading wav file
file_name = "0"
ori_sent = '영'
abs_path = "C:/Users/gjsrl/Documents/Git_space/BAEKJOON_Challenge/Lang_Python/"
audio_path = abs_path + "assets/wave/" + file_name + ".wav"
y, sr = librosa.load(audio_path)

IPython.display.Audio(data=y, rate=sr)

D = librosa.amplitude_to_db(librosa.stft(y[:1024]), ref=np.max)
plt.plot(D.flatten())
plt.show()
