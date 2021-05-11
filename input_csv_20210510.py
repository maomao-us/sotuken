import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
l2 = ["2x", "2y", "2z", "2abs"]
l3 = ["3x", "3y", "3z", "3abs"]
l4 = ["4x", "4y", "4z", "4abs"]
l5 = ["5x", "5y", "5z", "5abs"]
# label_number = 3
# average_count = 5
window = 5

sampling_number1 = 30
sampling_number2 = sampling_number1 + 1

count = 0

# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma

# 極小値を格納
##################################################################################################################################################
##################################################################################################################################################
def MIN_EV():
    min_ev = []
    list = []
    step_list = []

    # 前後20個のデータを格納
    for i in range(sampling_number1, len(data) - sampling_number2):
        for j in range(i - sampling_number1, i + sampling_number2):
            list.append(data[j])

        # バブルソート
        for j in range(len(list)):
            for k in range(len(list) - 1, j, -1):
                if list[k] < list[k - 1]:
                    list[k], list[k - 1] =  list[k - 1], list[k]

        if count < 3:
            if list[0] == data[i] and -2 > data[i]:
                min_ev.append(data[i])
                step_list.append(step[i])

        if count == 3:
            if (list[len(list) - 1] == data[i] and 9 < data[i]):
                min_ev.append(data[i])
                step_list.append(step[i])

        list.clear()

    min_ev = np.array(min_ev)
    print(min_ev)
    print(step_list)
    return min_ev, step_list

# 極小値をcsvファイルに格納
##################################################################################################################################################
##################################################################################################################################################
def input_ev_csv(ev):
    with open("sotuken_data/kisimoto/kisimoto_ev" + l5[z] + ".csv", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(ev)

# 極小値のステップをcsvファイルに格納
##################################################################################################################################################
##################################################################################################################################################
def input_step_csv(step):
    with open("step/kisimoto/kisimoto_step" + l5[z] + ".csv", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(step)


for z in range(4):
    for i in range(10, 30):
        file_name = "kisimoto_" + str(i)
        print(file_name)

        df = pd.read_csv("kisimoto_5/" + file_name + ".csv")
        data = df[label[z]].rolling(window, min_periods=1).apply(WMA)
        for i in range(5 - 1):
            data = data.rolling(window, min_periods=1).apply(WMA)
        data = np.array(data)

        step = []
        for i in range(len(data)):
            step.append(i + 1)
        step = np.array(step)

        ev, ev_step = MIN_EV()

        input_ev_csv(ev)
        input_step_csv(ev_step)

    count += 1
    print(count)








# 定義
##################################################################################################################################################


