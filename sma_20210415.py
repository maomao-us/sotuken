import csv
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import itertools

name_1 = "csv_data/kouhai1.csv"
# label = "Linear Acceleration x (m/s^2)"
label = "Linear Acceleration y (m/s^2)"
# label = "Linear Acceleration z (m/s^2)"
# label = "Absolute acceleration (m/s^2)"
match_p = 0.95
rolling_count = 30

csv_1 = pd.read_csv(name_1)
df_1 = csv_1[label]
df_1 = np.array(df_1)

step_1 = []
for i in range(len(df_1)):
    step_1.append(i + 1)
step_1 = np.array(step_1)

window = 5
def sma(count):
    sma = csv_1[label].rolling(window, center =True, min_periods=1).mean()
    for i in range(count - 1):
        sma = sma.rolling(window, center = True, min_periods=1).mean()
    return sma

sma_1 = sma(5)


def graph(step, data1, data2):
    fig = plt.figure()
    plt.plot(step, data1, label = "original")
    plt.plot(step, data2, label = "sma")
    plt.legend()
    plt.grid()
    plt.show()

graph(step_1, df_1, sma_1)

# fig_1 = plt.figure()
# plt.plot(step_1, df_1, label = "original")
# plt.legend()
# plt.grid()
# fig_2 = plt.figure()
# plt.plot(step_1, sma_1, label = "sma_1")
# plt.legend()
# plt.grid()
# plt.show()

print(r2_score(df_1, sma_1))