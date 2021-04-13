import csv
from operator import le 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
from scipy import signal
from sklearn import preprocessing

name1 = "csv_data/hiromu1.csv"
name2 = "csv_data/kouhai1.csv"
order_number = 30
window = 10
x_label = "Linear Acceleration x (m/s^2)"

hiromu_csv = pd.read_csv(name1)
kouhai_csv = pd.read_csv(name2)

# 空リストを生成して要素をぶち込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def makelist_and_input(csv):
    list = []
    for i in range(len(csv)):
        list += [csv.iloc[i, 1]]
    list = np.array(list)
    return list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

hiromu_data = makelist_and_input(hiromu_csv)
kouhai_data = makelist_and_input(kouhai_csv)

# ステップ数と単純移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def sma(csv):
    sma = []
    step = []
    rolling_list = csv[x_label].rolling(window, min_periods=1).mean()
    for i in range(len(rolling_list)):
        sma.append(rolling_list[i])
        step.append(i + 1)
    sma = np.array(sma)
    step = np.array(step)
    return sma, step
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

hiromu_sma, hiromu_step = sma(hiromu_csv)
kouhai_sma, kouhai_step = sma(kouhai_csv)

# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph(step1, step2, data1, data2, file_name):
    fig = plt.figure()
    plt.plot(step1, data1, "r")
    plt.plot(step2, data2, "b")
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig("graph/" + file_name + ".png")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

KP_graph_1 = plot_graph(hiromu_step, kouhai_step, hiromu_sma, kouhai_sma, "KP_1_sma")