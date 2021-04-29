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

##################################################################################################################################################
label = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
window = 5

df = pd.read_csv("takenaka_4/takenaka_24.csv")

step = df[label[0]]
data_x = df[label[1]]
data_y = df[label[2]]
data_z = df[label[3]]
data_abs = df[label[4]]

sma = df[label[2]].rolling(window, min_periods=1).mean()
wma = df[label[2]].rolling(window, min_periods=1).apply(WMA)
ewa = df[label[2]].ewm(span = window, adjust=False).mean()

for i in range(4):
    sma = sma.rolling(window, min_periods=1).mean()
    wma = wma.rolling(window, min_periods=1).apply(WMA)
    ewa = ewa.ewm(span = window, adjust=False).mean()

# plt.plot(step, data_x, label = "x")
# plt.plot(step, data_y, label = "y")
# plt.plot(step, data_z, label = "z")
fig = plt.figure()
plt.plot(step, data_x, label = "x")
plt.plot(step, data_y, label = "y")
plt.plot(step, data_z, label = "z")
plt.legend()
plt.grid()
plt.show()
# fig.savefig("graph/KP1_graph.png")
