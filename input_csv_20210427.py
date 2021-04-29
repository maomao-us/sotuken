import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma


# 荷重移動平均法を行う関数
##################################################################################################################################################
##################################################################################################################################################
def sma(count):
    wma = df[label[label_number]].rolling(window, min_periods=1).apply(WMA)
    for i in range(count - 1):
        wma = wma.rolling(window, min_periods=1).apply(WMA)
    wma = np.array(wma)

    return wma

# グラフを出力する関数
##################################################################################################################################################
##################################################################################################################################################
def graph(step, data1, data2):
    fig = plt.figure()
    plt.plot(step, data1, label = "original")
    plt.plot(step, data2, label = "wma")
    plt.legend()
    plt.grid()
    plt.show()
    # fig.savefig("graph/KP2_20210416_average.png")
    # fig.savefig("graph/KP2_20210416_average.eps")

# 極小値を格納
##################################################################################################################################################
##################################################################################################################################################
def MIN_EV(data):
    min_ev = []
    list = []
    step_list = []
    count = 0

    # 前後20個のデータを格納
    for i in range(50, len(data) - 51):
        for j in range(i - 50, i + 51):
            list.append(data[j])

        # バブルソート
        for j in range(len(list)):
            for k in range(len(list) - 1, j, -1):
                if list[k] < list[k - 1]:
                    list[k], list[k - 1] =  list[k - 1], list[k]

        if (list[len(list) - 1] == data[i] and 30 < data[i]):
            min_ev.append(data[i])
            step_list.append(step[i])

        # if list[len(list) - 1] == data[i] and 5 < data[i]:
        #     count += 1
        #     print(count, "回目")
        #     print("count : ",step[i])
        #     min_ev.append(data[i])
        #     step_list.append(step[i])

        # if count == 5:
        #     break

        # 照合
        # if count >= 1:
        #     if list[0] == data[i]:
        #         min_ev.append(data[i])
        #         step_list.append(step[i])
        # elif list[0] == data[i] and -7 > data[i]:
        #     min_ev.append(data[i])
        #     step_list.append(step[i])

        # if list[0] == data[i] and -10 > data[i]:
        #     min_ev.append(data[i])
        #     step_list.append(step[i])

        # 格納したデータをリセット
        list.clear()

    # if len(min_ev) == 6:
    #     min_ev.pop(len(min_ev) - 1)
    #     step_list.pop(len(step_list) - 1)
    # min_ev.pop(len(min_ev) - 1)
    # step_list.pop(len(step_list) - 1)
    min_ev = np.array(min_ev)
    print(min_ev)
    print(step_list)
    return min_ev, step_list

# 極小値をcsvファイルに格納
##################################################################################################################################################
##################################################################################################################################################
def input_ev_csv(ev):
    with open("sotuken_data/takenaka_4/takenaka_ev4abs.csv", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(ev)

# 極小値のステップをcsvファイルに格納
##################################################################################################################################################
##################################################################################################################################################
def input_step_csv(step):
    with open("step/takenaka_4/takenaka_step4abs.csv", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(step)


# 定義
##################################################################################################################################################
# file_name = "takenaka_10"

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
label_number = 3

average_count = 5
window = 5

for i in range(10, 30):
    file_name = "takenaka_" + str(i)
    print(file_name)
    # csvの読み込みとリスト化
    ##################################################################################################################################################
    df = pd.read_csv("takenaka_4/" + file_name + ".csv")
    data = df[label[0]].rolling(window, min_periods=1).apply(WMA)
    for i in range(5 - 1):
        data = data.rolling(window, min_periods=1).apply(WMA)
    data = np.array(data)

    # csvデータの総ステップ数
    ##################################################################################################################################################
    step = []
    for i in range(len(data)):
        step.append(i + 1)
    step = np.array(step)

    # 移動平均のデータを出力
    ##################################################################################################################################################
    wma = sma(average_count)

    # 極小値を抽出
    ##################################################################################################################################################
    ev, ev_step = MIN_EV(wma)

    # グラフを出力
    ##################################################################################################################################################
    graph(step, data, wma)

    # 極小値とそのステップをcsvに出力
    ##################################################################################################################################################
    input_ev_csv(ev)
    input_step_csv(ev_step)