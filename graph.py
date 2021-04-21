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


label = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
window = 5

df = pd.read_csv("csv_data/hiromu1.csv")

step = df[label[0]]
# data_x = df1[label[1]]
# data_y = df1[label[2]]
# data_z = df1[label[3]]
# data_abs = df1[label[4]]

sma = df[label[1]].rolling(window, center =True, min_periods=1).mean()

for i in range(4):
    sma = sma.rolling(window, min_periods=1).apply(WMA)

# plt.plot(step, data_x, label = "x")
# plt.plot(step, data_y, label = "y")
# plt.plot(step, data_z, label = "z")
fig = plt.figure()
plt.plot(step, sma, label = "x")
plt.legend()
plt.grid()
plt.show()
fig.savefig("graph/KP1_graph.png")
