import csv
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import itertools

name_1 = "csv_data/kouhai1.csv"
label = "Linear Acceleration x (m/s^2)"
# label = "Linear Acceleration y (m/s^2)"
# label = "Linear Acceleration z (m/s^2)"
# label = "Absolute acceleration (m/s^2)"
match_p = 0.95
rolling_count = 30


# csvのほしい列データと単純移動平均と総ステップ数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def csv_sma_step(name, label):
    # csv から抽出
    csv = pd.read_csv(name)
    df = csv[label]
    df = np.array(df)

    # 総ステップ数
    list = []
    for i in range(len(csv)):
        list.append(i + 1)
    list = np.array(list)

    # 移動平均と一致率
    print("sma")
    for i in range(100):
        count = i + 1
        sma = csv[label].rolling(i + 1, center =True, min_periods=1).mean()
        sma = np.array(sma)

        max_roll = np.roll(sma, 0)

        for j in range(rolling_count):
            roll = np.roll(sma,-j)
            if r2_score(df, roll) > r2_score(df, max_roll):
                max_roll = roll

        if r2_score(df , max_roll) < match_p:
            print("一致率 : ", r2_score(df , max_roll))
            print("window : ", count)
            print("\n")
            break

    
    return csv, df, max_roll, list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
csv_1, data_1, sma_1, step_1 = csv_sma_step(name_1, label)


# 加重移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 加重移動平均と一致率
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def rolling_wma(name, label):
    print("wma")
    for i in range(100):
        count = i + 1
        wma = csv_1[label].rolling(i + 1, min_periods=1).apply(WMA)
        wma = np.array(wma)

        max_roll = np.roll(wma, 0)

        for j in range(rolling_count):
            roll = np.roll(wma,-j)
            if r2_score(data_1, roll) > r2_score(data_1, max_roll):
                max_roll = roll

        if r2_score(data_1 , max_roll) < match_p:
            print("一致率 : ", r2_score(data_1 , max_roll))
            print("window : ", count)
            print("\n")
            break
    return max_roll
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
wma_1 = rolling_wma(name_1, label)


# 加重移動平均と一致率
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def rolling_ewm(name, label):
    print("ewm")
    for i in range(100):
        count = i + 1
        ewm = csv_1[label].ewm(span = i + 1, adjust=False).mean()
        ewm = np.array(ewm)

        max_roll = np.roll(ewm, 0)

        for j in range(100):
            roll = np.roll(ewm,-j)
            if r2_score(data_1, roll) > r2_score(data_1, max_roll):
                max_roll = roll

        if r2_score(data_1 , max_roll) < match_p:
            print("一致率 : ", r2_score(data_1 , max_roll))
            print("window : ", count)
            print("\n")
            break
    return max_roll
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------      
ewm_1 = rolling_ewm(name_1, label)



# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph_4(step, data1, data2, data3, data4):
    #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
    fig = plt.figure()

    #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    c1,c2,c3,c4 = "blue","green","red","black"      # 各プロットの色
    l1,l2,l3,l4 = "original","sma","wma","ewm"      # 各ラベル

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
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
plot_graph_4(step_1, data_1, sma_1, wma_1, ewm_1)


# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph_2(step, data1, data2):
    #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
    fig = plt.figure()

    c1,c2 = "r","b"
    l1,l2 = "original","sma : n = 50"

    plt.plot(step, data1, color=c1, label=l1)
    plt.plot(step, data2, color=c2, label=l2)
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig("graph/2KP_20210415_n(60).eps")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
x = csv_1[label].rolling(50, min_periods=1).mean()
x = np.array(x)
# plot_graph_2(step_1, data_1, x)

# グラフにして保存する関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def plot_graph_3(step, data1, data2):
    fig = plt.figure()
    plt.subplot(2,1,1)
    plt.plot(step, data1, color="r", label = "original")
    plt.legend(loc = 'lower right')
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot(step, data2, color="b", label="sma : n = 6")
    plt.legend(loc = 'lower right')
    plt.grid()
    plt.show()
    fig.savefig("graph/2KP_20210415_n(6).eps")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# plot_graph_3(step_1, data_1, sma_1)