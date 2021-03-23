import csv
from operator import le 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score
from scipy import signal
from sklearn import preprocessing
from scipy.stats import zscore


# ステップ数をぶち込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def input_step(first_step, end_step):
    list = []
    for i in range(first_step, end_step):
        list.append(i)
    list = np.array(list)
    return list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 空リストを生成して要素をぶち込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def makelist_and_input(csv):
    list = []
    for i in range(step_size):
        list += [csv.iloc[i, 1]]
    return list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 単純移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def SMA(csv, first_step, end_step):
    sma = []
    rolling_list = csv[x_label].rolling(window, min_periods=1).mean()
    for i in range(first_step, end_step):
        sma.append(rolling_list[i])
    sma = np.array(sma)
    return sma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph():
    plt.plot(hiromu_step, hiromu_sma, "r", label = name_hiromu)
    plt.plot(hiromu_step[hiromu_max], hiromu_sma[hiromu_max], "ro")
    plt.plot(hiromu_step[hiromu_min], hiromu_sma[hiromu_min], "ro")

    plt.plot(kouhai_step, kouhai_sma, "b", label = name_kouhai)
    plt.plot(kouhai_step[kouhai_max], kouhai_sma[kouhai_max], "bo")
    plt.plot(kouhai_step[kouhai_min], kouhai_sma[kouhai_min], "bo")

    plt.legend()
    plt.grid()
    plt.show()
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 極限のステップ数を出す関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def max_min_csv(list):
    max = signal.argrelmax(list, order=order_number)
    min = signal.argrelmin(list, order=order_number)
    return max, min
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
name_hiromu = "hiromu1"
name_kouhai = "kouhai1"

window = 10                                                 ## 移動平均
order_number = 30                                           ## 極限を調べる範囲
step_size = 800                                             ## リストの要素数
x_label = "Linear Acceleration x (m/s^2)"                   ## csv の Xラベル


# csv出力
hiromu_csv = pd.read_csv("csv_data/" + name_hiromu + ".csv", nrows=step_size)
kouhai_csv = pd.read_csv("csv_data/" + name_kouhai + ".csv", nrows=step_size)

# ステップ数
hiromu_step = input_step(500, 700)
kouhai_step = input_step(420, 750)

# 移動平均でノイズ削除
hiromu_sma = SMA(hiromu_csv, 500, 700)
kouhai_sma = SMA(kouhai_csv, 420, 750)

# 極大値極小値を出す
hiromu_max, hiromu_min = max_min_csv(hiromu_sma)
kouhai_max, kouhai_min = max_min_csv(kouhai_sma)

# 極値の場所出力
# print("hiromu 極大値 : ", hiromu_max[0])
# print("hiromu 極小値 : ", hiromu_min[0])
# print("\n")
# print("kouhai 極大値 : ", kouhai_max[0])
# print("kouhai 極小値 : ", kouhai_min[0])
# print("\n")

a = zscore(hiromu_sma)
plt.hist(a, bins=50)
plt.show()
# 極値の合計
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def list_kyokuthi(sma, n1, n2, n3, n4, n5, n6):
    list = []
    list.append(sma[n1])
    list.append(sma[n2])
    list.append(sma[n3])
    list.append(sma[n4])
    list.append(sma[n5])
    list.append(sma[n6])
    list = np.array(list)

    mean = 0
    std = 0
    mean = np.mean(list)
    std = np.var(list, ddof=1)
    return mean, std
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# hiromu_mean, hiromu_std = list_kyokuthi(hiromu_sma, 45, 105, 165, 24, 83, 140)
# kouhai_mean, kouhai_std = list_kyokuthi(kouhai_sma, 79, 196, 314, 42, 157, 269)

# 平均を出力
# print("hiromu の平均 : ", hiromu_mean)
# print("kouhai の平均 : ", kouhai_mean)
# print("\n")
# 分散を出力
# print("hiromu の分散 : ", hiromu_std)
# print("kouhai の分散 : ", kouhai_std)
# print("\n")
# 最終的な分散
# std = (5*(hiromu_std + kouhai_std)) / 5*2 - 2
# print("最終的な分散", std)
# print("\n")

# T = (hiromu_mean - kouhai_mean) / (std * (1/6 * 2))**(1/2)
# 検定統計量を出力
# print("検定統計量 : ", T)

# plot_graph()