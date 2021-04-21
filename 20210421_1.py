import csv
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score

# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma


# 各移動平均法を行う関数
##################################################################################################################################################
##################################################################################################################################################
def sma(count):
    sma = csv_1[label[label_number]].rolling(window, center =True, min_periods=1).mean()
    wma = csv_1[label[label_number]].rolling(window, min_periods=1).apply(WMA)
    ewa = csv_1[label[label_number]].ewm(span = window, adjust=False).mean()

    for i in range(count - 1):
        sma = sma.rolling(window, center = True, min_periods=1).mean()
        wma = wma.rolling(window, min_periods=1).apply(WMA)
        ewa = ewa.ewm(span = window, adjust=False).mean()
    sma = np.array(sma)
    wma = np.array(wma)
    ewa = np.array(ewa)

    return sma, wma, ewa

# ずらして一致させる関数
##################################################################################################################################################
##################################################################################################################################################
def roll(data):
    count = 0
    max_roll = np.roll(data, 0)
    for i in range(100):
        roll = np.roll(data, -i)
        if r2_score(df_1, roll) > r2_score(df_1, max_roll):
            max_roll = roll
            count += 1
    print("count : ", count)
    return max_roll

# グラフを出力する関数
##################################################################################################################################################
##################################################################################################################################################
def graph(step, data1, data2, data3, data4):
    fig = plt.figure()
    plt.plot(step, data1, label = "original")
    plt.plot(step, data2, label = "sma")
    plt.plot(step, data3, label = "wma")
    plt.plot(step, data4, label = "ewa")
    # plt.plot(step, data4, label = "ewa")
    plt.legend()
    plt.grid()
    plt.show()
    # fig.savefig("graph/KP2_20210416_average.png")
    # fig.savefig("graph/KP2_20210416_average.eps")

# 定義
##################################################################################################################################################
file_name = "kouhai1"

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
label_number = 2

average_count = 5
window = 5

component = ["x", "y", "z", "abs"]


# csvの読み込みとリスト化
##################################################################################################################################################
csv_1 = pd.read_csv("csv_data/" + file_name + ".csv")
df_1 = csv_1[label[label_number]]
df_1 = np.array(df_1)

# csvデータの総ステップ数
##################################################################################################################################################
step_1 = []
for i in range(len(df_1)):
    step_1.append(i + 1)
step_1 = np.array(step_1)

# 移動平均のデータを出力
##################################################################################################################################################
sma_1, wma_1, ewa_1 = sma(average_count)

graph(step_1, df_1, sma_1, wma_1, ewa_1)
