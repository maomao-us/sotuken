import csv
# from operator import le
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.nanfunctions import _nanprod_dispatcher
# import pprint
import pandas as pd
# from sklearn.metrics import r2_score
from scipy import signal
from sklearn import preprocessing
# from scipy.stats import zscore

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
    for i in range(15, len(data) - 16):
        for j in range(i - 20, i + 16):
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
    
    min_ev.pop(len(min_ev) - 1)
    # min_ev.pop(len(min_ev) - 1)
    step_list.pop(len(step_list) - 1)
    # step_list.pop(len(step_list) - 1)
    min_ev = np.array(min_ev)
    return min_ev, step_list

# 最初にcsvに書き込む関数
##################################################################################################################################################
##################################################################################################################################################
def first_input_csv():
    with open("output/" + csv_file + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(ev)

# csvに新たに書き込む関数
##################################################################################################################################################
##################################################################################################################################################
def later_input_csv():
    with open("output/" + csv_file + ".csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(ev)

# csvに新たに書き込む関数
##################################################################################################################################################
##################################################################################################################################################
def graph():
    plt.plot(step, wma)
    plt.grid()
    plt.show()

# ここから本番
##################################################################################################################################################
file_name = ["hiromu1", "hiromu2", "hiromu3", "kouhai1", "kouhai2", "kouhai3"]
csv_file ="kouhai_z"
label = ["Time (s)", "Linear Acceleration z (m/s^2)"]

average_count = 5
window = 5

file_number = 5
df = pd.read_csv("csv_data/" + file_name[file_number] + ".csv")

step = df[label[0]] 
data = df[label[1]]
step = np.array(step)
data = np.array(data)

wma = df[label[1]].rolling(window, min_periods=1).apply(WMA)
for i in range(average_count - 1):
    wma = wma.rolling(window, min_periods=1).apply(WMA)
wma = np.array(wma)

ev, ev_step = MIN_EV(wma)

print(ev)
print(ev_step)

graph()
# first_input_csv()
later_input_csv()