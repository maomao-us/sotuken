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


# ステップ数と単純移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def step_and_sma(csv):
    sma = []
    step = []
    rolling_list = csv[x_label].rolling(window, min_periods=1).mean()
    for i in range(len(rolling_list)):
        sma.append(rolling_list[i])
        step.append(i + 1)
    sma = np.array(sma)
    sma = zscore(sma)
    step = np.array(step)
    return sma, step
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 極限のステップ数を出す関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def min_csv(list):
    min = signal.argrelmin(list, order=order_number)
    return min
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 最初の極値から最後の極値までをぶち込む
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def FEV_to_EEV(data, first, end):
    ev_to_ev = []
    step = []
    for i in range(first, end +1):
        ev_to_ev.append(data[i])
        step.append(i - (first - 1))
    ev_to_ev = np.array(ev_to_ev)
    step = np.array(step)
    return ev_to_ev, step
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# 極値とそのステップを格納
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def EV_STEP(data):
    ev = []
    ev.append(-data[0])
    step = []
    step.append(0)
    for i in range(5, len(data) - 6):
        # if data[i] > data[i - 1] > data[i - 2] > data[i - 3] > data[i - 4] > data[i - 5]\
        #     and data[i] > data[i + 1] > data[i + 2] > data[i + 3] > data[i + 4] > data[i + 5]:
        #     ev.append(data[i])
        #     step.append(i)
        if data[i] < data[i - 1] < data[i - 2] < data[i - 3] < data[i - 4] < data[i - 5]\
            and data[i] < data[i + 1] < data[i + 2] < data[i + 3] < data[i + 4] < data[i + 5]:
            ev.append(-data[i])
            step.append(i)
    ev.append(-data[len(data) - 1])
    step.append(len(data))
    ev = np.array(ev)
    step = np.array(step)
    return ev, step
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 序章
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
name1 = "hiromu1"
name2 = "kouhai1"
order_number = 30
window = 10
x_label = "Linear Acceleration x (m/s^2)"

hiromu_csv = pd.read_csv("csv_data/" + name1 + ".csv")
kouhai_csv = pd.read_csv("csv_data/" + name2 + ".csv")

hiromu_sma, hiromu_step = step_and_sma(hiromu_csv)
kouhai_sma, kouhai_step = step_and_sma(kouhai_csv)

# hiromu_min = min_csv(hiromu_sma)
# kouhai_min = min_csv(kouhai_sma)

# print("hiromu 極小値 : ", hiromu_min[0])
# print("\n")
# print("kouhai 極小値 : ", kouhai_min[0])

# plt.plot(hiromu_step, hiromu_sma, "r", label = name1)
# plt.plot(hiromu_step[hiromu_min], hiromu_sma[hiromu_min], "ro")
# plt.plot(kouhai_step, kouhai_sma, "b", label = name1)
# plt.plot(kouhai_step[kouhai_min], kouhai_sma[kouhai_min], "bo")
# plt.legend()
# plt.grid()
# plt.show()


# 終章
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


hiromu_ev, hiromu_evstep = FEV_to_EEV(hiromu_sma, 524, 640)
kouhai_ev, kouhai_evstep = FEV_to_EEV(kouhai_sma, 462, 689)

hiromu_ev_data, hiromu_step_list = EV_STEP(hiromu_ev)
kouhai_ev_data, kouhai_step_list = EV_STEP(kouhai_ev)

print(hiromu_ev_data)
print(kouhai_ev_data)
# print(hiromu_step_list)
# print(kouhai_step_list)

hiromu_min = min_csv(hiromu_ev)
kouhai_min = min_csv(kouhai_ev)

# print(hiromu_min[0])
# print(kouhai_min[0])

# plt.plot(hiromu_evstep, hiromu_ev, "r", label = name1)
# plt.plot(hiromu_evstep[hiromu_min], hiromu_ev[hiromu_min], "ro")
# plt.plot(kouhai_evstep, kouhai_ev, "b", label = name1)
# plt.plot(kouhai_evstep[kouhai_min], kouhai_ev[kouhai_min], "bo")
# plt.legend()
# plt.grid()
# plt.show()


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
ev_mean_std(hiromu_ev_data, kouhai_ev_data)