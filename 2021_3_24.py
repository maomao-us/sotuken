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


#CSVファイルを読み込む
name1 = "csv_data/hiromu1.csv"
name2 = "csv_data/kouhai1.csv"
order_number = 30
window = 10
x_label = "Linear Acceleration x (m/s^2)"

csv_1 = pd.read_csv(name1)
csv_2 = pd.read_csv(name2)


# ステップ数と単純移動平均法
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
window = 10
x_label = "Linear Acceleration x (m/s^2)"

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
sma_1, step_1 = step_and_sma(csv_1)
sma_2, step_2 = step_and_sma(csv_2)


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
ev_1, ev_step1 = FEV_to_EEV(sma_1, 524, 665)
ev_2, ev_step2 = FEV_to_EEV(sma_2, 462, 734)


# 極限のステップ数を出す関数
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def max_min(list):
    max = signal.argrelmax(list, order=order_number)
    min = signal.argrelmin(list, order=order_number)
    return max, min
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
max_1, min_1 = max_min(ev_1)
max_2, min_2 = max_min(ev_2)

# 極値のステップを格納
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
def EV_STEP(data):
    step = []
    step.append(1)
    for i in range(5, len(data) - 6):
        if data[i] > data[i - 1] > data[i - 2] > data[i - 3] > data[i - 4] > data[i - 5]\
            and data[i] > data[i + 1] > data[i + 2] > data[i + 3] > data[i + 4] > data[i + 5]:
            step.append(i + 1)
        elif data[i] < data[i - 1] < data[i - 2] < data[i - 3] < data[i - 4] < data[i - 5]\
            and data[i] < data[i + 1] < data[i + 2] < data[i + 3] < data[i + 4] < data[i + 5]:
            step.append(i + 1)
    step.append(len(data))
    step = np.array(step)
    return step
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
EV_STEP1 = EV_STEP(ev_1)
EV_STEP2 = EV_STEP(ev_2)
# print(EV_STEP1)
# print(EV_STEP2)

# print("hiromu 極大値 : ", max_1[0])
# print("hiromu 極小値 : ", min_1[0])
# print("\n")
# print("kouhai 極大値 : ", max_2[0])
# print("kouhai 極小値 : ", min_2[0])

def match_sma(point, step_list, ev_data):
    step = []
    t = point - 1

    for i in range(1, point):
        for k in range(step_list[i - 1], step_list[i] + 1):
            # print(step_list[i - 1])
            if k > 1 and k == step_list[i - 1]:
                # print("continue")
                continue
            value = (i - 1)/t + (1/t)*((k - step_list[i - 1])/(step_list[i] - step_list[i - 1]))
            step.append(value)
            # print(value)
    
    step = np.array(step)
    return step

hiromu_step = match_sma(6, EV_STEP1, ev_1)
kouhai_step = match_sma(6, EV_STEP2, ev_2)
# print(hiromu_step)
# print(kouhai_step)
# print(len(hiromu_step))
# print(len(kouhai_step))

plt.plot(hiromu_step, ev_1, "r", label = name1)
plt.plot(kouhai_step, ev_2, "b", label = name2)
plt.legend()
plt.grid()
plt.show()