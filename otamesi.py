import csv
# from operator import le
import numpy as np
import matplotlib.pyplot as plt
# import pprint
import pandas as pd
from sklearn.metrics import r2_score
from scipy import signal
from sklearn import preprocessing
# from scipy.stats import zscore

name1 = "csv_data/N.csv"
x_label = "Linear Acceleration x (m/s^2)"

data = pd.read_csv(name1)

df = data[x_label]
df = np.array(df)

for i in range(100):
    s = i + 1
    rolling_list = data[x_label].rolling(i + 1, min_periods=1).mean()
    rolling_list = np.array(rolling_list)

    max_roll = np.roll(rolling_list, 0)

    for j in range(len(df)):
        roll = np.roll(rolling_list,j)
        if r2_score(roll, df) > r2_score(max_roll, df):
            max_roll = roll

    if r2_score(df, max_roll) < 0.99:
        print(r2_score(df, max_roll))
        print("window = ",i + 1)
        plt.plot(df)
        plt.plot(max_roll)
        plt.legend()
        plt.show()
        break

# plt.plot(rolling_list)
# plt.show()