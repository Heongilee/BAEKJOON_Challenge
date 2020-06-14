import librosa
import librosa.display
import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Level_increment = 26
def X_axis_Level(idx):
    if(idx >=0 and idx < 11):
        return "Left"
    elif(idx >= 11 and idx < 22):
        return "Center"
    elif(idx >= 22 and idx < 33):
        return "Right"
    else:
        return "NA"

def Y_axis_Level(idx):
    if(idx >= 0 and idx < 26):
        return "A" # A Level
    elif(idx >=26 and idx < 52):
        return "B" # B Level
    elif(idx >=52 and idx < 78):
        return "C" # C Level
    elif(idx >=78 and idx < 104):
        return "D" # D Level
    elif(idx >=104 and idx < 128):
        return "E" # E Level
    else:
        return "NA"

def _ColorLevel(number):
    if(number >= 0.0 and number <= 0.400):
        return "Low"
    elif(number > 0.400 and number <= 0.700):
        return "Middle"
    elif(number > 0.700 and number < 1.0):
        return "High"
    else:
        return "NA"


# 분류기
def _classification(norm_S):
    # 조건에 부합하는지 비트로 검사 [9][8][7][6][5][4][3][2][1][0]
    bin_status = 0
    i = 0
    for array in norm_S:
        j = 0
        for elem in array:
            # 2020-06-14(17:23) -> 알고리즘 다시 짜기...
            j += 1
        i += 1
    
    print(bin_status)
    if(bin_status == 0b0000000001):
        print("Recognition result :", classes[0])
    elif(bin_status == 0b0000000010):
        print("Recognition result :", classes[1])
    elif(bin_status == 0b0000000100):
        print("Recognition result :", classes[2])
    elif(bin_status == 0b0000001000):
        print("Recognition result :", classes[3])
    elif(bin_status == 0b0000010000):
        print("Recognition result :", classes[4])
    elif(bin_status == 0b0000100000):
        print("Recognition result :", classes[5])
    elif(bin_status == 0b0001000000):
        print("Recognition result :", classes[6])
    elif(bin_status == 0b0010000000):
        print("Recognition result :", classes[7])
    elif(bin_status == 0b0100000000):
        print("Recognition result :", classes[8])
    elif(bin_status == 0b1000000000):
        print("Recognition result :", classes[9])
    else:
        print("Failed...")

student_id = "15012970"
file_name = student_id + "_0"
abs_path = "C:/Users/gjsrl/Documents/Git_space/BAEKJOON_Challenge/Lang_Python/"
audio_path = abs_path + "assets/wave/" + student_id + "/" + file_name + ".wav"
y, sr = librosa.load(audio_path)

S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
log_S = librosa.amplitude_to_db(S, ref=np.max)
min_level_db = -100

def _normalize(S):
    return np.clip((S - min_level_db) / -min_level_db, 0, 1)

norm_S = _normalize(log_S)

# TEST_OUTPUT
_classification(norm_S)

plt.figure(figsize=(12, 4))
librosa.display.specshow(norm_S, sr=sr, x_axis='time', y_axis='mel')
plt.title('norm mel power spectrogram')
plt.colorbar(format='%+0.1f dB')
plt.tight_layout()
plt.show()