import os
import getpass
import matplotlib.pyplot as plt

from scipy import signal
from scipy.io import wavfile

user_name = getpass.getuser()
# 파이썬 파일 절대 경로 지정.
abspath_path = 'C:/Users/' + str(user_name) + '/Documents/Git_space/BAEKJOON_Challenge/Lang_Python'
# wav 파일 경로 지정.
voice_path = abspath_path + '/asset/wav/'
# 해당 디렉토리의 파일들 가져옴.
voice_listdir = os.listdir(voice_path)

# 디렉토리 내부의 파일 갯수
listdir_number = len(voice_listdir)

my_idx = 0
# from wav 파일 경로 지정.
wav_file_path = voice_path + str(my_idx) + '.wav'
# to jpeg  파일 경로 지정.
postprocessing_image_path = abspath_path + '/asset/images/' + str(my_idx) + '.png'
# wav 파일을 읽어 들임.
sample_frequency, signalData = wavfile.read(wav_file_path)
plt.specgram(signalData, Fs=sample_frequency)

plt.savefig(postprocessing_image_path)