import csv
# from operator import le
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.nanfunctions import _nanprod_dispatcher
# import pprint
import pandas as pd
# from sklearn.metrics import r2_score
from scipy import signal
from sklearn import preprocessing
# from scipy.stats import zscore

# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma


file_hiromu = ["hiromu1", "kouhai1"]
label = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
window = 5

df1 = pd.read_csv("csv_data/" + file_hiromu[0] + ".csv")
df2 = pd.read_csv("csv_data/" + file_hiromu[1] + ".csv")

step1 = df1[label[0]]
step2 = df2[label[0]]
# data_x = df1[label[1]]
# data_y = df1[label[2]]
# data_z = df1[label[3]]
# data_abs1 = df1[label[4]]
# data_abs2 = df2[label[4]]

wma1 = df1[label[4]].rolling(window, min_periods=1).apply(WMA)
wma2 = df2[label[4]].rolling(window, min_periods=1).apply(WMA)

for i in range(4):
    wma1 = wma1.rolling(window, min_periods=1).apply(WMA)
    wma2 = wma2.rolling(window, min_periods=1).apply(WMA)

# plt.plot(step, data_x, label = "x")
# plt.plot(step, data_y, label = "y")
# plt.plot(step, data_z, label = "z")
plt.plot(step1, wma1, label = "hiromu")
plt.plot(step2, wma2, label = "kouhai")

plt.legend()
plt.grid()
plt.show()