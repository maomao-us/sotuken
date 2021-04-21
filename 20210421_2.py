import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd

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
def MIN_EV(data):
    min_ev = []
    list = []
    step_list = []

    # 前後20個のデータを格納
    for i in range(20, len(data) - 21):
        for j in range(i - 20, i + 20):
            list.append(data[j])

        # バブルソート
        for j in range(len(list)):
            for k in range(len(list) - 1, j, -1):
                if list[k] < list[k - 1]:
                    list[k], list[k - 1] =  list[k - 1], list[k]

        # 照合
        if list[0] == data[i] and -2 > data[i] :
            min_ev.append(data[i])
            step_list.append(step[i])
        # 格納したデータをリセット
        list.clear()

    # 前後20個のデータを格納 --> 絶対値
    for i in range(10, len(data) - 21):
        for j in range(i - 10, i + 10):
            list.append(data[j])

        # バブルソート
        for j in range(len(list)):
            for k in range(len(list) - 1, j, -1):
                if list[k] < list[k - 1]:
                    list[k], list[k - 1] =  list[k - 1], list[k]

        # 照合
        if list[len(list) - 1] == data[i] and 20 < data[i] :
            min_ev.append(data[i])
            step_list.append(step[i])
        # 格納したデータをリセット
        list.clear()

    # min_ev.pop(len(min_ev) - 1)
    # min_ev.pop(len(min_ev) - 1)
    # step_list.pop(len(step_list) - 1)
    # step_list.pop(len(step_list) - 1)
    min_ev = np.array(min_ev)
    return min_ev, step_list

# csvに書き込む関数
##################################################################################################################################################
##################################################################################################################################################
def input_csv():
    with open("output2/" + csv_file + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(ev)

# ここから本番
##################################################################################################################################################
file_name = ["hiromu1", "kouhai1"]
csv_file ="wma_abs2"
label = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
label_number = 4
average_count = 5
window = 5

file_number = 1
average_number = 1
df = pd.read_csv("csv_data/" + file_name[file_number] + ".csv")

step = []
for i in range(len(df)):
    step.append(i + 1)
data = df[label[label_number]]
step = np.array(step)
data = np.array(data)

sma = df[label[label_number]].rolling(window, min_periods=1).mean()
wma = df[label[label_number]].rolling(window, min_periods=1).apply(WMA)
ewa = df[label[label_number]].ewm(span = window, adjust=False).mean()

for i in range(average_count - 1):
    sma = sma.rolling(window, min_periods=1).mean()
    wma = wma.rolling(window, min_periods=1).apply(WMA)
    ewa = ewa.ewm(span = window, adjust=False).mean()

sma = np.array(sma)
wma = np.array(wma)
ewa = np.array(ewa)
average_label = [sma, wma, ewa]

ev, ev_step = MIN_EV(average_label[average_number])
average = ["sma", "wma", "ewa"]
print(ev)
print(ev_step)

fig = plt.figure()
plt.plot(step, data, label = "original")
plt.plot(step, average_label[average_number], label = average[average_number])
plt.legend()
plt.grid()
plt.show()

input_csv()