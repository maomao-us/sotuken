import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score

#CSVファイルを読み込む
csv_x = pd.read_csv('Nx.csv')
print(len(csv_x))
# len(csv_x) = 600

plot_x = []
# plot_y1 = []
# plot_y2 = []
# plot_y3 = []

# time
for i in range(len(csv_x)):
    plot_x += [csv_x.iloc[i,0]]

# acc x1
# for i in range(len(csv_x)):
#     plot_y1 += [csv_x.iloc[i,1]]

# acc x2
# for i in range(len(csv_x)):
#     plot_y2 += [csv_x.iloc[i,2]]

# acc x3
# for i in range(len(csv_x)):
#     plot_y3 += [csv_x.iloc[i,3]]



window = 10
plot_z1 = csv_x['Linear Acceleration x1 (m/s^2)'].rolling(window).mean()
plot_z2 = csv_x['Linear Acceleration x2 (m/s^2)'].rolling(window).mean()
plot_z3 = csv_x['Linear Acceleration x3 (m/s^2)'].rolling(window).mean()

for i in range(0,window - 1):
    plot_z1[i] = 0
    plot_z2[i] = 0
    plot_z3[i] = 0

plot_roll = np.roll(plot_z1,-10)

print(r2_score(plot_roll, plot_z2))

# plt.plot(plot_x,plot_y1)
# plt.plot(plot_x,plot_y2)
# plt.plot(plot_x,plot_y3)

# plt.plot(plot_x,plot_z1)
plt.plot(plot_x, plot_roll)
plt.plot(plot_x,plot_z2)
# plt.plot(plot_x,plot_z3)

plt.show()


