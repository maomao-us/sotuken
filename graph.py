import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score

#CSVファイルを読み込む
csv_x = pd.read_csv('Nx.csv')

# len(csv_x) = 600

plot_x = []
plot_x1 = []
plot_x2 = []
plot_x3 = []

# time
for i in range(len(csv_x)):
    plot_x += [csv_x.iloc[i,0]]

# acc x1
# for i in range(len(csv_x)):
#     plot_x1 += [csv_x.iloc[i,1]]

# acc x2
# for i in range(len(csv_x)):
#     plot_x2 += [csv_x.iloc[i,2]]

# acc x3
# for i in range(len(csv_x)):
#     plot_x3 += [csv_x.iloc[i,3]]



window = 10
plot_xm1 = csv_x['Linear Acceleration x1 (m/s^2)'].rolling(window).mean()
plot_xm2 = csv_x['Linear Acceleration x2 (m/s^2)'].rolling(window).mean()
plot_xm3 = csv_x['Linear Acceleration x3 (m/s^2)'].rolling(window).mean()

for i in range(0,window - 1):
    plot_xm1[i] = 0
    plot_xm2[i] = 0
    plot_xm3[i] = 0

count = 0
plot_roll = 0
plot_maxroll = np.roll(plot_xm1, 0)

for i in range(1,len(csv_x)):
    plot_roll = np.roll(plot_xm1,-i)
    if r2_score(plot_roll, plot_xm2) > r2_score(plot_maxroll, plot_xm2):
        plot_maxroll = plot_roll
        count = i

print("\n")
print(count)
print(r2_score(plot_maxroll, plot_xm2))

# plt.plot(plot_x,plot_x1)
# plt.plot(plot_x,plot_x2)
# plt.plot(plot_x,plot_x3)

# plt.plot(plot_x,plot_xm1)
plt.plot(plot_x, plot_maxroll)
plt.plot(plot_x,plot_xm2)
# plt.plot(plot_x,plot_xm3)

plt.show()


