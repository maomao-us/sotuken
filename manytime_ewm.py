import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import itertools


# 空リストを生成して要素をぶち込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def makelist_and_input(csv, Column):
    list = []
    for i in range(step_size):
        list += [csv.iloc[i, Column]]
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

    return sma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 加重移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


x_label = "Linear Acceleration x (m/s^2)"
y_label = "Linear Acceleration y (m/s^2)"
z_label = "Linear Acceleration z (m/s^2)"
abs_label = "Absolute acceleration (m/s^2)"
step_size = 1200
window = 5
span_size = 5

csv_1 = pd.read_csv("csv_data/kouhai1.csv")

plot_step = []
for i in range(step_size):
    plot_step.append((i + 1))

plot_kouhai = makelist_and_input(csv_1, 1)

kouhai_sma = SMA(csv_1, x_label)

kouhai_wma = []
wma_data = csv_1[x_label].rolling(window, min_periods=1).apply(WMA)
for i in range(step_size):
    kouhai_wma.append(wma_data[i])

kouhai_ewm = []
ewm_data = csv_1[x_label].ewm(span = span_size, adjust=False).mean()
for i in range(3):
    ewm_data = ewm_data.ewm(span = span_size, adjust=False).mean()
for i in range(step_size):
    kouhai_ewm.append(ewm_data[i])




# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph():
    fig = plt.figure()

    plt.plot(plot_step, plot_kouhai, label = "kouhai")
    # plt.plot(plot_step, kouhai_sma, label = "sma")
    # plt.plot(plot_step, kouhai_wma, label = "wma")
    plt.plot(plot_step, kouhai_ewm, label = "ewm")
    plt.legend()
    plt.grid()
    plt.show()
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
plot_graph()

print("window = ", window)
print("span = ", span_size)
print("\n")


# 平均二乗誤差(MSE)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
print("平均二乗誤差(MSE)")
print("sma : ", mean_squared_error(plot_kouhai, kouhai_sma))
print("wma : ", mean_squared_error(plot_kouhai, kouhai_wma))
print("ewm : ", mean_squared_error(plot_kouhai, kouhai_ewm))
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
print("\n")


# 二乗平均平方根誤差 (RMSE)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
print("二乗平均平方根誤差 (RMSE)")
print("sma : ", np.sqrt(mean_squared_error(plot_kouhai, kouhai_sma)))
print("wma : ", np.sqrt(mean_squared_error(plot_kouhai, kouhai_wma)))
print("ewm : ", np.sqrt(mean_squared_error(plot_kouhai, kouhai_ewm)))
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
print("\n")


# 決定係数 (R2)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
print("決定係数 (R2)")
print("sma : ", 1 - r2_score(plot_kouhai, kouhai_sma))
print("wma : ", 1 - r2_score(plot_kouhai, kouhai_wma))
print("ewm : ", 1 - r2_score(plot_kouhai, kouhai_ewm))
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------