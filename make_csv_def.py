import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score


#3つのCSVファイルを読み込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def input_csv(name1, name2, name3):
    csv_1 = pd.read_csv("csv_data/" + name1 + ".csv", nrows=step_size, usecols=cols)
    csv_2 = pd.read_csv("csv_data/" + name2 + ".csv", nrows=step_size, usecols=cols)
    csv_3 = pd.read_csv("csv_data/" + name3 + ".csv", nrows=step_size, usecols=cols)
    return name1, name2, name3, csv_1, csv_2, csv_3
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


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
    sma = np.array(sma)
    return sma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# できるだけデータが合わさるように調整する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# def Wave_List(plot_move, plot_not_move):
#     plot_roll = 0
#     plot_maxroll = np.roll(plot_move, 0)
#     for i in range(step_size):
#             plot_roll = np.roll(plot_move,i)
#             if r2_score(plot_roll, plot_not_move) > r2_score(plot_maxroll, plot_not_move):
#                 plot_maxroll = plot_roll
#     return plot_maxroll
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph(graph1, graph2, graph3, label1, label2, label3, title):
    fig = plt.figure()

    plt.plot(plot_step, graph1, label = label1)
    plt.plot(plot_step, graph2, label = label2)
    plt.plot(plot_step, graph3, label = label3)

    plt.title(title)
    plt.legend()
    plt.grid()
    # 計測時間による
    # plt.xlim(1.5, 4.5)

    fig.savefig("graph/" + label1 + "_" + label2 + "_" + label3 + "_" + title + ".png")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------
cols = ["Linear Acceleration x (m/s^2)","Linear Acceleration y (m/s^2)","Linear Acceleration z (m/s^2)","Absolute acceleration (m/s^2)"]
step_size = 1200                                            ## リストの要素数

x_label = "Linear Acceleration x (m/s^2)"                   ## csv の Xラベル
y_label = "Linear Acceleration y (m/s^2)"                   ## csv の Yラベル
z_label = "Linear Acceleration z (m/s^2)"                   ## csv の Zラベル
abs_label = "Absolute acceleration (m/s^2)"                 ## csv の 絶対速度ラベル

window = 10                                                 ## 単純移動平均法の変数

name1, name2, name3, csv_1, csv_2, csv_3 = input_csv("hiromu1", "kouhai1", "nakajima1")


# 移動平均線にしてノイズをとる
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
plot_x_csv1_sma = SMA(csv_1, x_label)
plot_x_csv2_sma = SMA(csv_2, x_label)
plot_x_csv3_sma = SMA(csv_3, x_label)
plot_y_csv1_sma = SMA(csv_1, y_label)
plot_y_csv2_sma = SMA(csv_2, y_label)
plot_y_csv3_sma = SMA(csv_3, y_label)
plot_z_csv1_sma = SMA(csv_1, z_label)
plot_z_csv2_sma = SMA(csv_2, z_label)
plot_z_csv3_sma = SMA(csv_3, z_label)
plot_abs_csv1_sma = SMA(csv_1, abs_label)
plot_abs_csv2_sma = SMA(csv_2, abs_label)
plot_abs_csv3_sma = SMA(csv_3, abs_label)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 時間とcsv ファイルの各列要素をぶち込む
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# 6秒間を約0.005秒間隔で測定しているので1200個の要素を抽出
plot_step = []
for i in range(step_size):
    plot_step.append((i + 1))

plot_x_csv1 = makelist_and_input(csv_1, 0)
plot_x_csv2 = makelist_and_input(csv_2, 0)
plot_x_csv3 = makelist_and_input(csv_3, 0)
plot_y_csv1 = makelist_and_input(csv_1, 1)
plot_y_csv2 = makelist_and_input(csv_2, 1)
plot_y_csv3 = makelist_and_input(csv_3, 1)
plot_z_csv1 = makelist_and_input(csv_1, 2)
plot_z_csv2 = makelist_and_input(csv_2, 2)
plot_z_csv3 = makelist_and_input(csv_3, 2)
plot_abs_csv1 = makelist_and_input(csv_1, 3)
plot_abs_csv2 = makelist_and_input(csv_2, 3)
plot_abs_csv3 = makelist_and_input(csv_3, 3)

# for i in range(10):
#     print(plot_x_csv1[i])
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# データを合わせる
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# plot_x_csv2_roll = Wave_List(plot_x_csv2_sma, plot_x_csv1_sma)
# plot_x_csv3_roll = Wave_List(plot_x_csv3_sma, plot_x_csv1_sma)
# plot_y_csv2_roll = Wave_List(plot_y_csv2_sma, plot_y_csv1_sma)
# plot_y_csv3_roll = Wave_List(plot_y_csv3_sma, plot_y_csv1_sma)
# plot_z_csv2_roll = Wave_List(plot_z_csv2_sma, plot_z_csv1_sma)
# plot_z_csv3_roll = Wave_List(plot_z_csv3_sma, plot_z_csv1_sma)
# plot_abs_csv2_roll = Wave_List(plot_abs_csv2_sma, plot_abs_csv1_sma)
# plot_abs_csv3_roll = Wave_List(plot_abs_csv3_sma, plot_abs_csv1_sma)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# グラフを保存
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
plot_graph(plot_x_csv1, plot_x_csv2, plot_x_csv3, name1, name2, name3, "dimension_x")
plot_graph(plot_y_csv1, plot_y_csv2, plot_y_csv3, name1, name2, name3, "dimension_y")
plot_graph(plot_z_csv1, plot_z_csv2, plot_z_csv3, name1, name2, name3, "dimension_z")
plot_graph(plot_abs_csv1, plot_abs_csv2, plot_abs_csv3, name1, name2, name3, "dimension_abs")

# plot_graph(plot_x_csv1_sma, plot_x_csv2_sma, plot_x_csv3_sma, name1, name2, name3, "dimension_x")
# plot_graph(plot_y_csv1_sma, plot_y_csv2_sma, plot_y_csv3_sma, name1, name2, name3, "dimension_y")
# plot_graph(plot_z_csv1_sma, plot_z_csv2_sma, plot_z_csv3_sma, name1, name2, name3, "dimension_z")
# plot_graph(plot_abs_csv1_sma, plot_abs_csv2_sma, plot_abs_csv3_sma, name1, name2, name3, "dimension_abs")

# plot_graph(plot_x_csv1_sma, plot_x_csv2_roll, plot_x_csv3_roll, name1, name2, name3, "dimension_x")
# plot_graph(plot_y_csv1_sma, plot_y_csv2_roll, plot_y_csv3_roll, name1, name2, name3, "dimension_y")
# plot_graph(plot_z_csv1_sma, plot_z_csv2_roll, plot_z_csv3_roll, name1, name2, name3, "dimension_z")
# plot_graph(plot_abs_csv1_sma, plot_abs_csv2_roll, plot_abs_csv3_roll, name1, name2, name3, "dimension_abs")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------