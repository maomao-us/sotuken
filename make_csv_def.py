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
    csv_1 = pd.read_csv("csv_data/" + name1 + ".csv")
    csv_2 = pd.read_csv("csv_data/" + name2 + ".csv")
    csv_3 = pd.read_csv("csv_data/" + name3 + ".csv")
    return name1, name2, name3, csv_1, csv_2, csv_3
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 空リストを生成して要素をぶち込む関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def makelist_and_input(csv, datasize, Column):
    list = []
    for i in range(datasize):
        list += [csv.iloc[i, Column]]
    return list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 移動平均線にしてノイズを除去するための関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
x_label = "Linear Acceleration x (m/s^2)"
y_label = "Linear Acceleration y (m/s^2)"
z_label = "Linear Acceleration z (m/s^2)"
abs_label = "Absolute acceleration (m/s^2)"

def average_line(csv, label, window, datasize):
    plot_mean = []
    list = csv[label].rolling(window).mean()
    for i in range(datasize):
        plot_mean.append(list[i])
    
    for i in range(window - 1):
        plot_mean[i] = 0
    
    return plot_mean
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# できるだけデータが合わさるように調整する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def wave_list(plot_move, plot_not_move, datasize):
    plot_roll = 0
    plot_maxroll = np.roll(plot_move, 0)
    for i in range(datasize):
            plot_roll = np.roll(plot_move,i)
            if r2_score(plot_roll, plot_not_move) > r2_score(plot_maxroll, plot_not_move):
                plot_maxroll = plot_roll
    return plot_maxroll
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph(graph1, graph2, graph3, label1, label2, label3, title):
    fig = plt.figure()

    plt.plot(plot_time, graph1, label = label1)
    plt.plot(plot_time, graph2, label = label2)
    plt.plot(plot_time, graph3, label = label3)

    plt.title(title)
    plt.legend()
    plt.grid()
    # 計測時間による
    plt.xlim(1.5, 4.5)

    fig.savefig("graph/" + label1 + "_" + label2 + "_" + label3 + "_" + title + ".png")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------


name1, name2, name3, csv_1, csv_2, csv_3 = input_csv("hiromu1", "kouhai1", "nakajima1")


# 時間とcsv ファイルの各列要素をぶち込む
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# 6秒間を約0.005秒間隔で測定しているので1200個の要素を抽出
plot_time = []
for i in range(1200):
    plot_time.append((i + 1) * 0.005)

plot_x_csv1 = makelist_and_input(csv_1, 1200, 1)
plot_x_csv2 = makelist_and_input(csv_2, 1200, 1)
plot_x_csv3 = makelist_and_input(csv_3, 1200, 1)
plot_y_csv1 = makelist_and_input(csv_1, 1200, 2)
plot_y_csv2 = makelist_and_input(csv_2, 1200, 2)
plot_y_csv3 = makelist_and_input(csv_3, 1200, 2)
plot_z_csv1 = makelist_and_input(csv_1, 1200, 3)
plot_z_csv2 = makelist_and_input(csv_2, 1200, 3)
plot_z_csv3 = makelist_and_input(csv_3, 1200, 3)
plot_abs_csv1 = makelist_and_input(csv_1, 1200, 4)
plot_abs_csv2 = makelist_and_input(csv_2, 1200, 4)
plot_abs_csv3 = makelist_and_input(csv_3, 1200, 4)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 移動平均線にしてノイズをとる
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
plot_x_csv1_mean = average_line(csv_1, x_label, 10, 1200)
plot_x_csv2_mean = average_line(csv_2, x_label, 10, 1200)
plot_x_csv3_mean = average_line(csv_3, x_label, 10, 1200)
plot_y_csv1_mean = average_line(csv_1, y_label, 10, 1200)
plot_y_csv2_mean = average_line(csv_2, y_label, 10, 1200)
plot_y_csv3_mean = average_line(csv_3, y_label, 10, 1200)
plot_z_csv1_mean = average_line(csv_1, z_label, 10, 1200)
plot_z_csv2_mean = average_line(csv_2, z_label, 10, 1200)
plot_z_csv3_mean = average_line(csv_3, z_label, 10, 1200)
plot_abs_csv1_mean = average_line(csv_1, abs_label, 10, 1200)
plot_abs_csv2_mean = average_line(csv_2, abs_label, 10, 1200)
plot_abs_csv3_mean = average_line(csv_3, abs_label, 10, 1200)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# データを合わせる
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
plot_x_csv2_roll = wave_list(plot_x_csv2_mean, plot_x_csv1_mean, 1200)
plot_x_csv3_roll = wave_list(plot_x_csv3_mean, plot_x_csv1_mean, 1200)
plot_y_csv2_roll = wave_list(plot_y_csv2_mean, plot_y_csv1_mean, 1200)
plot_y_csv3_roll = wave_list(plot_y_csv3_mean, plot_y_csv1_mean, 1200)
plot_z_csv2_roll = wave_list(plot_z_csv2_mean, plot_z_csv1_mean, 1200)
plot_z_csv3_roll = wave_list(plot_z_csv3_mean, plot_z_csv1_mean, 1200)
plot_abs_csv2_roll = wave_list(plot_abs_csv2_mean, plot_abs_csv1_mean, 1200)
plot_abs_csv3_roll = wave_list(plot_abs_csv3_mean, plot_abs_csv1_mean, 1200)
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# グラフを保存
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# plot_graph(plot_x_csv1, plot_x_csv2, plot_x_csv3, name1, name2, name3, "dimension_x")
# plot_graph(plot_y_csv1, plot_y_csv2, plot_y_csv3, name1, name2, name3, "dimension_y")
# plot_graph(plot_z_csv1, plot_z_csv2, plot_z_csv3, name1, name2, name3, "dimension_z")
# plot_graph(plot_abs_csv1, plot_abs_csv2, plot_abs_csv3, name1, name2, name3, "dimension_abs")

plot_graph(plot_x_csv1_mean, plot_x_csv2_mean, plot_x_csv3_mean, name1, name2, name3, "dimension_x")
plot_graph(plot_y_csv1_mean, plot_y_csv2_mean, plot_y_csv3_mean, name1, name2, name3, "dimension_y")
plot_graph(plot_z_csv1_mean, plot_z_csv2_mean, plot_z_csv3_mean, name1, name2, name3, "dimension_z")
plot_graph(plot_abs_csv1_mean, plot_abs_csv2_mean, plot_abs_csv3_mean, name1, name2, name3, "dimension_abs")

# plot_graph(plot_x_csv1_mean, plot_x_csv2_roll, plot_x_csv3_roll, name1, name2, name3, "dimension_x")
# plot_graph(plot_y_csv1_mean, plot_y_csv2_roll, plot_y_csv3_roll, name1, name2, name3, "dimension_y")
# plot_graph(plot_z_csv1_mean, plot_z_csv2_roll, plot_z_csv3_roll, name1, name2, name3, "dimension_z")
# plot_graph(plot_abs_csv1_mean, plot_abs_csv2_roll, plot_abs_csv3_roll, name1, name2, name3, "dimension_abs")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------



