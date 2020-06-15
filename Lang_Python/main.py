import librosa
import librosa.display
import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
##############################################################################################
# 파일 로드 (읽어오는데 문제가 있어 상대경로 대신 절대경로를 사용했습니다.)

student_id = "15011139"
file_name = student_id + "_9"
abs_path = "C:/Users/gjsrl/Documents/Git_space/BAEKJOON_Challenge/Lang_Python/"
audio_path = abs_path + "assets/wave/" + student_id + "/" + file_name + ".wav"
y, sr = librosa.load(audio_path)

classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Feature_Tot = [5, 9, 8, 9, 8, 9, 7, 2, 6, 6]
def _Percentage(my_number_state, i):
    if(_success(my_number_state, i) == 0):
        return 0.0
    else:
        return _success(my_number_state, i) / Feature_Tot[i] * 100.0

def _success(my_number_state, digits):
    return int((my_number_state % pow(10, digits + 1)) / (pow(10, digits)))

def X_axis_Level(x_max, idx):
    if(idx >=0 and idx < ((x_max / 4.0) * 1.0)):
        return "One"
    elif(idx >= ((x_max / 4.0) * 1.0) * 1.0 and idx < ((x_max / 4.0) * 2.0)):
        return "Two"
    elif(idx >= ((x_max / 4.0) * 2.0) and idx < ((x_max / 4.0) * 3.0)):
        return "Three"
    elif(idx >= ((x_max / 4.0) * 3.0) and idx < x_max):
        return "Four"
    else:
        return "NA"

def Y_axis_Level(y_max, idx):
    if(idx >= 0 and idx < ((y_max / 5.0) * 1.0)):
        return "A" # A Level
    elif(idx >=((y_max / 5.0) * 1.0) and idx < ((y_max / 5.0) * 2.0)):
        return "B" # B Level
    elif(idx >=((y_max / 5.0) * 2.0) and idx < ((y_max / 5.0) * 3.0)):
        return "C" # C Level
    elif(idx >=((y_max / 5.0) * 3.0) and idx < ((y_max / 5.0) * 4.0)):
        return "D" # D Level
    elif(idx >= ((y_max / 5.0) * 4.0) and idx < y_max):
        return "E" # E Level
    else:
        return "NA"

def _ColorLevel(number):
    if(number >= 0.2 and number < 0.244):
        return "Lv1"
    elif(number >= 0.244 and number < 0.266):
        return "Lv2"
    elif(number >= 0.266 and number < 0.288):
        return "Lv3"
    elif(number >= 0.288 and number < 0.300):
        return "Lv4"
    elif(number >= 0.300 and number < 0.333):
        return "Lv5"
    elif(number >= 0.333 and number < 0.666):
        return "Lv6"
    elif(number >= 0.666 and number < 1.0):
        return "Lv7"
    else:
        return "NA"

# 분류기
def _classification(x_max, y_max, norm_S):
    X_inc = int(x_max / 4.0)
    Y_inc = int(y_max / 5.0)
    X_start = int((x_max / 4.0) / 2.0)
    Y_start = int((y_max / 5.0) / 2.0)
    # 조건에 일치하는지 자릿수로 검사 [9][8][7][6][5][4][3][2][1][0]
    my_number_state = 0
    x = X_start
    while(x <= x_max):
        y = Y_start
        while(y <= y_max):
            # print("[", X_axis_Level(x_max, x), ", ", Y_axis_Level(y_max, y), "]")
            # print("{", x, ", ", y, "}")
            # 테스트 출력
            # if(X_axis_Level(x_max, x) == "Three" and Y_axis_Level(y_max, y) == "A"):
            #     print("TEST_OUTPUT01 => ", _ColorLevel(norm_S[y][x]), ", ", norm_S[y][x])
            # if(X_axis_Level(x_max, x) == "Three" and Y_axis_Level(y_max, y) == "B"):
            #     print("TEST_OUTPUT02 => ", _ColorLevel(norm_S[y][x]), ", ", norm_S[y][x])
            ############################################################################
            # 0 특징 검사
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "LV7")):
                my_number_state += 1
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv3" or _ColorLevel(norm_S[y][x]) == "Lv4" or _ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv3" or _ColorLevel(norm_S[y][x]) == "Lv4" or _ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1
            ############################################################################
            # 1 특징 검사
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 10
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 10
            ############################################################################
            # 2 특징 검사
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100
            ############################################################################
            # 3 특징 검사
            if((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000
            ############################################################################
            # 4 특징 검사
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "E") and (_ColorLevel(norm_S[y][x]) == "Lv3" or _ColorLevel(norm_S[y][x]) == "Lv4" or _ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 10000
            ############################################################################
            # 5 특징 검사
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv3" or _ColorLevel(norm_S[y][x]) == "Lv4" or _ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000
            ############################################################################
            # 6 특징 검사 (7개로 잡기)
            if((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000000
            ############################################################################
            # 7 특징 검사 (1이 어느정도 맞고 7이 둘 중 하나 맞을 때)
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "D") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "E") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 10000000
            ############################################################################
            # 8 특징 검사
            if((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000000
            elif((X_axis_Level(x_max, x) == "One") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "B") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 100000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 100000000
            ############################################################################
            # 9 특징 검사
            if((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6" or _ColorLevel(norm_S[y][x]) == "Lv7")):
                my_number_state += 1000000000
            elif((X_axis_Level(x_max, x) == "Two") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv4" or _ColorLevel(norm_S[y][x]) == "Lv5" or _ColorLevel(norm_S[y][x]) == "Lv6")):
                my_number_state += 1000000000
            elif((X_axis_Level(x_max, x) == "Three") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000000000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "A") and (_ColorLevel(norm_S[y][x]) == "Lv3" or _ColorLevel(norm_S[y][x]) == "Lv4" or _ColorLevel(norm_S[y][x]) == "Lv5")):
                my_number_state += 1000000000
            elif((X_axis_Level(x_max, x) == "Four") and (Y_axis_Level(y_max, y) == "C") and (_ColorLevel(norm_S[y][x]) == "Lv1" or _ColorLevel(norm_S[y][x]) == "Lv2")):
                my_number_state += 1000000000
            y += Y_inc
        print("\n")
        x += X_inc
    return my_number_state

# 원래 여기

S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
log_S = librosa.amplitude_to_db(S, ref=np.max)
min_level_db = -100

def _normalize(S):
    return np.clip((S - min_level_db) / -min_level_db, 0, 1)

norm_S = _normalize(log_S)

# OUTPUT
res = _classification(len(norm_S[0]), len(norm_S), norm_S)
max_P = 0.0
max_N = 0
for i in range(0, 10):
    # print("[", i, "] : ", _Percentage(res, i), "%")
    if(_Percentage(res, i) > max_P):
        max_P = _Percentage(res, i)
        max_N = i
print("My number is : ", max_N, "\t{", max_P, "%}")


plt.figure(figsize=(12, 4))
librosa.display.specshow(norm_S, sr=sr, x_axis='time', y_axis='mel')
plt.title('norm mel power spectrogram')
plt.colorbar(format='%+0.1f dB')
plt.tight_layout()
plt.show()