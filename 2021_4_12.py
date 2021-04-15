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
def max_min(list):
    max = signal.argrelmax(list, order=order_number)
    min = signal.argrelmin(list, order=order_number)
    return max, min
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
name1 = "csv_data/hiromu1.csv"
name2 = "csv_data/kouhai1.csv"
order_number = 30
window = 10
x_label = "Linear Acceleration x (m/s^2)"

csv_1 = pd.read_csv(name1)
csv_2 = pd.read_csv(name2)

sma_1, step_1 = step_and_sma(csv_1)
sma_2, step_2 = step_and_sma(csv_2)

max_1, min_1 = max_min(sma_1)
max_2, min_2 = max_min(sma_2)

print("hiromu 極大値 : ", max_1[0])
print("hiromu 極小値 : ", min_1[0])
print("\n")
print("kouhai 極大値 : ", max_2[0])
print("kouhai 極小値 : ", min_2[0])

plt.plot(step_1, sma_1, "r", label = name1)
plt.plot(step_1[max_1], sma_1[max_1], "ro")
plt.plot(step_1[min_1], sma_1[min_1], "ro")
plt.plot(step_2, sma_2, "b", label = name2)
plt.plot(step_2[min_2], sma_2[min_2], "bo")
plt.plot(step_2[max_2], sma_2[max_2], "bo")
plt.legend()
plt.grid()
plt.show()


# 終章
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ev_1, ev_step1 = FEV_to_EEV(sma_1, 524, 665)
ev_2, ev_step2 = FEV_to_EEV(sma_2, 462, 734)

ev_1_data, step_1_list = EV_STEP(ev_1)
ev_2_data, step_2_list = EV_STEP(ev_2)

print(ev_1_data)
print(ev_2_data)
print(step_1_list)
print(step_2_list)

# min_1 = max_min(ev_1)
# min_2 = max_min(ev_2)

# print(min_1[0])
# print(min_2[0])

# plt.plot(ev_step1, ev_1, "r", label = name1)
# plt.plot(ev_step1[min_1], ev_1[min_1], "ro")
# plt.plot(ev_step2, ev_2, "b", label = name1)
# plt.plot(ev_step2[min_2], ev_2[min_2], "bo")
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
# ev_mean_std(ev_1_data, ev_2_data)