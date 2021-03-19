import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score
from scipy import signal


#3つのCSVファイルを読み込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def input_csv(name1, name2, name3):
    csv_1 = pd.read_csv("csv_data/" + name1 + ".csv", nrows=step_size)
    csv_2 = pd.read_csv("csv_data/" + name2 + ".csv", nrows=step_size)
    csv_3 = pd.read_csv("csv_data/" + name3 + ".csv", nrows=step_size)
    return name1, name2, name3, csv_1, csv_2, csv_3
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# ステップ数をぶち込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def input_step():
    list = []
    for i in range(step_size):
        list.append(i + 1)
    list = np.array(list)
    return list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 単純移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def SMA(csv, label):
    sma = []
    rolling_list = csv[label].rolling(window, min_periods=1).mean()
    for i in range(step_size):
        sma.append(rolling_list[i])
    sma = np.array(sma)
    return sma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 極限値を探す
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def select_kyokugen(data):
    max_list = []
    min_list = []
    for i in range(first_step, end_step):
        if data[i] > data[i - 1] and data[i] > data[i + 1] and data[i] > 0:
            max_list.append(step_csv[i-1])
        if data[i] < data[i - 1] and data[i] < data[i + 1] and data[i] < -25:
            min_list.append(step_csv[i-1])
    np.array(max_list)
    np.array(min_list)
    return max_list, min_list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------



# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph():
    fig = plt.figure()

    plt.plot(step_csv, x_csv1_sma, "r", label = "kouhai1")
    plt.plot(step_csv, x_csv2_rolling, "b", label = "kouhai2")
    plt.plot(step_csv, x_csv3_rolling, "g", label = "kouhai3")
    plt.plot(step_csv[max_csv1], x_csv1_sma[max_csv1], "ro")
    plt.plot(step_csv[max_csv2], x_csv2_rolling[max_csv2], "bo")
    plt.plot(step_csv[max_csv3], x_csv3_rolling[max_csv3], "go")
    plt.plot(step_csv[min_csv1], x_csv1_sma[min_csv1], "ro")
    plt.plot(step_csv[min_csv2], x_csv2_rolling[min_csv2], "bo")
    plt.plot(step_csv[min_csv3], x_csv3_rolling[min_csv3], "go")
    plt.legend()
    plt.grid()
    plt.show()
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# できるだけデータが合わさるように調整する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def Wave_List(plot_move, plot_not_move):
    plot_roll = 0
    plot_maxroll = np.roll(plot_move, 0)
    for i in range(len(step_csv)):
            plot_roll = np.roll(plot_move,i)
            if r2_score(plot_roll, plot_not_move) > r2_score(plot_maxroll, plot_not_move):
                plot_maxroll = plot_roll
    return plot_maxroll
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# cols = ["Time (s)", "Linear Acceleration x (m/s^2)","Linear Acceleration y (m/s^2)","Linear Acceleration z (m/s^2)","Absolute acceleration (m/s^2)"]
step_size = 1200                                            ## リストの要素数

x_label = "Linear Acceleration x (m/s^2)"                   ## csv の Xラベル
y_label = "Linear Acceleration y (m/s^2)"                   ## csv の Yラベル
z_label = "Linear Acceleration z (m/s^2)"                   ## csv の Zラベル
abs_label = "Absolute acceleration (m/s^2)"                 ## csv の 絶対速度ラベル
window = 10                                                 ## 単純移動平均法の変数
order_number = 70
first_step = 400
end_step = 800

name1, name2, name3, csv_1, csv_2, csv_3 = input_csv("kouhai1", "kouhai2", "kouhai3")

step_csv = input_step()

x_csv1_sma = SMA(csv_1, y_label)
x_csv2_sma = SMA(csv_2, y_label)
x_csv3_sma = SMA(csv_3, y_label)

x_csv2_rolling = Wave_List(x_csv2_sma, x_csv1_sma)
x_csv3_rolling = Wave_List(x_csv3_sma, x_csv1_sma)

def max_min_csv(data):
    max = signal.argrelmax(data, order=order_number)
    min = signal.argrelmin(data, order=order_number)
    return max, min


max_csv1, min_csv1 = max_min_csv(x_csv1_sma)
max_csv2, min_csv2 = max_min_csv(x_csv2_rolling)
max_csv3, min_csv3 = max_min_csv(x_csv3_rolling)


a, b = select_kyokugen(x_csv1_sma)

print(a)
print(b)

print("\n")
print(max_csv1[0])
print(min_csv1[0])

plot_graph()