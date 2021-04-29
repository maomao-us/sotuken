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
    plt.legend()
    plt.grid()
    plt.show()
    # fig.savefig("graph/KP2_20210416_average.png")
    # fig.savefig("graph/KP2_20210416_average.eps")

# データを別々にグラフ化
##################################################################################################################################################
##################################################################################################################################################
def individual_graph(step, data1, data2, data3, data4):
    #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
    fig = plt.figure()

    #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    c1,c2,c3,c4 = "blue","green","red","black"      # 各プロットの色
    l1,l2,l3,l4 = "original","sma","wma","ewa"      # 各ラベル

    ax1.plot(step, data1, color=c1, label=l1)
    ax1.grid(True)
    ax2.plot(step, data2, color=c2, label=l2)
    ax2.grid(True)
    ax3.plot(step, data3, color=c3, label=l3)
    ax3.grid(True)
    ax4.plot(step, data4, color=c4, label=l4)
    ax4.grid(True)
    ax1.legend(loc = 'upper right') #凡例
    ax2.legend(loc = 'upper right') #凡例
    ax3.legend(loc = 'upper right') #凡例
    ax4.legend(loc = 'upper right') #凡例
    # fig.tight_layout()              #レイアウトの設定
    plt.show()
    # fig.savefig(file_name)

# 各移動平均の評価を保存するためのcsvファイルのラベル関数
##################################################################################################################################################
##################################################################################################################################################
def write_csv_title():
    for i in range(4):
        what_component = component[i]
        if what_component == "x":
            with open("csv_data/x_average.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["file", "sma", "wma", "ewa"])

        elif what_component == "y":
            with open("csv_data/y_average.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["file", "sma", "wma", "ewa"])

        elif what_component == "z":
            with open("csv_data/z_average.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["file", "sma", "wma", "ewa"])

        elif what_component == "abs":
            with open("csv_data/abs_average.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["file", "sma", "wma", "ewa"])




# 各移動平均の評価を追加する関数
##################################################################################################################################################
##################################################################################################################################################
def write_csv():
    for i in range(4):
        what_component = component[i]
        if what_component == "x":
            with open("csv_data/x_average.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([file_name, 1 - r2_score(df_1, sma_2), 1 - r2_score(df_1, wma_2), 1 - r2_score(df_1, ewa_2)])

        elif what_component == "y":
            with open("csv_data/y_average.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([file_name, 1 - r2_score(df_1, sma_2), 1 - r2_score(df_1, wma_2), 1 - r2_score(df_1, ewa_2)])

        elif what_component == "z":
            with open("csv_data/z_average.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([file_name, 1 - r2_score(df_1, sma_2), 1 - r2_score(df_1, wma_2), 1 - r2_score(df_1, ewa_2)])

        elif what_component == "abs":
            with open("csv_data/abs_average.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([file_name, 1 - r2_score(df_1, sma_2), 1 - r2_score(df_1, wma_2), 1 - r2_score(df_1, ewa_2)])

# 定義
##################################################################################################################################################
file_name = "hiromu1"

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
label_number = 1

average_count = 5
window = 3

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

# 一致させたデータを出力
##################################################################################################################################################
# print("sma_2")
# sma_2 = roll(sma_1)
# print("\n")
# print("wma_2")
# wma_2 = roll(wma_1)
# print("\n")
# print("ewa_2")
# ewa_2 = roll(ewa_1)
# print("\n")

# 個々のグラフを出力
##################################################################################################################################################
# individual_graph(step_1, df_1, sma_2, wma_2, ewa_2)
graph(step_1, df_1, sma_1, wma_1, ewa_1)

# originalとの誤差を出力
##################################################################################################################################################
# print(1 - r2_score(df_1, sma_2))
# print(1 - r2_score(df_1, wma_2))
# print(1 - r2_score(df_1, ewa_2))

#csvのラベルかっこみ
##################################################################################################################################################
# write_csv_title()

# csvに追加
##################################################################################################################################################
# write_csv()