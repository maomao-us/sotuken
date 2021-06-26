import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def wma(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma

##################################################################################################################################################
label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)"]
window = 5
name = "kutukake"
number = 1
file = 2
counter = 10
df10 = pd.read_csv("oltana/" + name + "_" + str(file) + "/" + name + "_" + str(counter) + ".csv")
df11 = pd.read_csv("oltana/" + name + "_" + str(file) + "/" + name + "_" + str(counter+1) + ".csv")

data_10 = df10[label[number]]
data_11 = df11[label[number]]

step10 = []
step11 = []
for i in range(len(df10)):
    step10.append(i)

for i in range(len(df11)):
    step11.append(i)

wma10 = df10[label[number]].rolling(window, min_periods=1).apply(wma)
wma11 = df11[label[number]].rolling(window, min_periods=1).apply(wma)


for i in range(4):
    wma10 = wma10.rolling(window, min_periods=1).apply(wma)
    wma11 = wma11.rolling(window, min_periods=1).apply(wma)

# plt.plot(step, data_x, label = "x")
# plt.plot(step, data_y, label = "y")
# plt.plot(step, data_z, label = "z")
# fig = plt.figure()
# plt.plot(step10, data_10, label = "10")
# plt.plot(step11, data_11, label = "11")
# plt.legend()
# plt.grid()
# plt.show()

fig = plt.figure()
plt.plot(step10, wma10, label = str(counter))
# plt.plot(step11, wma11, label = str(counter+1))
plt.legend()
plt.grid()
plt.show()

a = df10.columns[0]
print(a)

# file_name1 = "nakajima/nakajima_11.csv"
# file_name2 = "takenaka/takenaka_11.csv"
# df1 = pd.read_csv(file_name1)
# df2 = pd.read_csv(file_name2)
# data_10 = df1[label[number]]
# data_11 = df2[label[number]]
# step10 = []
# step11 = []
# for i in range(len(df1)):
#     step10.append(i)

# for i in range(len(df2)):
#     step11.append(i)

# plt.plot(step10, data_10, label = "nakajima")
# plt.plot(step11, data_11, label = "t")
# plt.legend()
# plt.grid()
# plt.show()
