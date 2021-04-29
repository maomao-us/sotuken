import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
from sklearn import preprocessing
from sklearn.metrics import r2_score


# csvをリスト化
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def input_csv(csv, column):
    csv_data = []
    step = []
    for i in range(len(csv)):
        csv_data.append(csv.iloc[i, column])
        step.append(i + 1)
    csv_data = np.array(csv_data)
    step = np.array(step)
    return csv_data, step
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

#極値を抽出
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def input_ev(data, threshold):
    list = []
    for i in range(5, len(data) - 6):
        # if data[i] > data[i - 1] > data[i - 2] > data[i - 3] > data[i - 4] > data[i - 5]\
        #     and data[i] > data[i + 1] > data[i + 2] > data[i + 3] > data[i + 4] > data[i + 5]\
        #     and data[i] > threshold:
        #     list.append(data[i])

        if data[i] < data[i - 1] < data[i - 2] < data[i - 3] < data[i - 4] < data[i - 5]\
            and data[i] < data[i + 1] < data[i + 2] < data[i + 3] < data[i + 4] < data[i + 5]\
            and data[i] < threshold:
            list.append(-data[i])
    list = np.array(list)
    print(list)
    return list
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 序章
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
name1 = "csv_data/hiromu1.csv"
name2 = "csv_data/kouhai1.csv"
x_label = "Linear Acceleration x (m/s^2)"

csv_1 = pd.read_csv(name1)
csv_2 = pd.read_csv(name2)

data_1, step_1= input_csv(csv_1, 1)
data_2, step_2= input_csv(csv_2, 1)
# ev_list_1 = input_ev(data_1, -20)
# ev_list_2 = input_ev(data_2, -15)

# ステップ数と単純移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def step_and_sma(csv, window):
    sma = []
    rolling_list = csv[x_label].rolling(window, min_periods=1).mean()
    for i in range(len(rolling_list)):
        sma.append(rolling_list[i])
    sma = np.array(sma)
    # sma = zscore(sma)
    return sma
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

sma_1 = step_and_sma(csv_2, 5)
sma_2 = step_and_sma(csv_2, 10)
sma_3 = step_and_sma(csv_2, 15)
sma_4 = step_and_sma(csv_2, 20)
sma_5 = step_and_sma(csv_2, 25)


# 極限のステップ数を出す関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def max_min(list, order_number):
    # max = signal.argrelmax(list, order=order_number)
    min = signal.argrelmin(list, order=order_number)
    # return max, min
    # return max
    return min
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


min_1 = max_min(sma_1, 30)
min_2 = max_min(sma_2, 30)
min_3 = max_min(sma_3, 30)
min_4 = max_min(sma_4, 30)
min_5 = max_min(sma_5, 30)

def graph():
    fig = plt.figure()
    plt.plot(step_2, data_2)
    plt.plot(step_2, sma_1)
    # plt.plot(step_2, sma_2)
    # plt.plot(step_2, sma_3)
    # plt.plot(step_2, sma_4)
    # plt.plot(step_2, sma_5)
    # plt.plot(step_2, data_2, "b", label = "nakajima")
    # plt.plot(step_1[min_1], sma_1[min_1], "o")
    # plt.plot(step_1[min_1], sma_2[min_2], "o")
    # plt.plot(step_1[min_1], sma_3[min_3], "o")
    # plt.plot(step_1[min_1], sma_4[min_4], "o")
    # plt.plot(step_1[min_1], sma_5[min_5], "o")
    plt.legend()
    plt.grid()
    plt.show()
    # fig.savefig("graph/sample_6.png")

graph()


print(r2_score(data_2, sma_1))
print(r2_score(data_2, sma_2))
print(r2_score(data_2, sma_3))
print(r2_score(data_2, sma_4))
print(r2_score(data_2, sma_5))



# 終章
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 極値の合計
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def ev_mean_std(list_ev1, list_ev2):
    mean1 = np.mean(list_ev1)
    std1 = np.var(list_ev1, ddof = 1)
    mean2 = np.mean(list_ev2)
    std2 = np.var(list_ev2, ddof = 1)

    print("hiromu_mean : ", mean1)
    print("hiromu_std : ", std1)
    print("kouhai_mean : ", mean2)
    print("kouhai_std : ", std2)

    std = (len(list_ev1 - 1)*(std1) + len(list_ev2 - 1)*(std2)) / (len(list_ev1) + len(list_ev2) - 2)
    print("final std : ", std)

    T = (mean1 - mean2) / ((1/len(list_ev1) + 1/len(list_ev2))*std)**(1/2)
    print("検定統計量 : ", T)
    # 有意水準0.05%
    # 両側検定, m=3, n=3
    if T > 2.776 or T < -2.776:
        print("有意差あり！！！")
    else:
        print("残念　(*´Д｀)　")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# ev_mean_std(ev_list_1, ev_list_2)