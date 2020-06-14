# --> 이 코드 다음부터 배워보기 (2020-06-11 23:52)
# https://banana-media-lab.tistory.com/entry/Librosa-python-library%EB%A1%9C-%EC%9D%8C%EC%84%B1%ED%8C%8C%EC%9D%BC-%EB%B6%84%EC%84%9D%ED%95%98%EA%B8%B0
import librosa
import librosa.display
import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

file_name = "0"
ori_sent = '영'
abs_path = "C:/Users/gjsrl/Documents/Git_space/BAEKJOON_Challenge/Lang_Python/"
audio_path = abs_path + "assets/wave/" + file_name + ".wav"
y, sr = librosa.load(audio_path)
##############################################################
# magnitude 값 구하기
##############################################################
# IPython.display.Audio(data=y, rate=sr)

# D = librosa.amplitude_to_db(librosa.stft(y[:1024]), ref=np.max)
# plt.plot(D.flatten())
# plt.show()

##############################################################
# MFCC 구하기
##############################################################
# S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
# log_S = librosa.amplitude_to_db(S, ref=np.max)

# plt.figure(figsize=(12, 4))
# librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
# plt.title('mel power spectrogram')
# plt.tight_layout()
# plt.show()

##############################################################
# Normalization
##############################################################
# S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
# log_S = librosa.amplitude_to_db(S, ref=np.max)
# min_level_db = -100

# def _normalize(S):
#     return np.clip((S - min_level_db) / -min_level_db, 0, 1)

# norm_S = _normalize(log_S)

# plt.figure(figsize=(12, 4))
# librosa.display.specshow(norm_S, sr=sr, x_axis='time', y_axis='mel')
# plt.title('norm mel power spectrogram')
# plt.colorbar(format='%+0.1f dB')
# plt.tight_layout()
# plt.show()

##############################################################
# 자소 단위로 쪼개기
##############################################################
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
log_S = librosa.amplitude_to_db(S, ref=np.max)
min_level_db = -100

def _normalize(S):
    return np.clip((S - min_level_db) / -min_level_db, 0, 1)

norm_S = _normalize(log_S)

import hgtk

for o in ori_sent:
    jamo_sent = hgtk.text.decompose(ori_sent)
jamo_sent = jamo_sent.replace('ᴥ', '')
print(jamo_sent)
##############################################################
# Clipping audio data (자소 개수만큼 자르기)
##############################################################
#               time_frame_num              mel_freq_num
# 영                    22                      80
# 일                    25                      80
# 이                    22                      80
# 삼                    30                      80
# 사                    50                      80
# 오                    30                      80
# 육                    20                      80
# 칠                    20                      80
# 팔                    10                      80
# 구                    13                      80

time_frame_num = 13
char_frame_num = int(time_frame_num / len(jamo_sent))
mel_freq_num = 80

plt.figure(figsize=(20, 150))
jamo_sent_size = len(jamo_sent)
for i in range(0, jamo_sent_size):
    plt.subplot(jamo_sent_size, 5, i + 1)
    start_position = (i * char_frame_num) - 1
    end_position = ((i + 1) * char_frame_num) + 1
    if(start_position < 0):
        start_position = 0
        end_position = end_position + 1
    if(end_position > time_frame_num):
        start_position = start_position - (end_position - time_frame_num)
        end_position = time_frame_num
    window = norm_S[0:mel_freq_num, start_position:end_position]
    plt.pcolor(window, cmap='jet')
    plt.title(str(jamo_sent[i]))
    plt.colorbar()
plt.show()