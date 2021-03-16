import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import matplotlib.pyplot as plt

csv_x = pd.read_csv('Nx.csv')

plot_x = []
plot_y1 = []
plot_y2 = []
plot_y3 = []

window = 10
plot_x1 = csv_x['Linear Acceleration x1 (m/s^2)'].rolling(window).mean()
plot_x2 = csv_x['Linear Acceleration x2 (m/s^2)'].rolling(window).mean()
plot_x3 = csv_x['Linear Acceleration x3 (m/s^2)'].rolling(window).mean()

for i in range(0,window - 1):
    plot_x1[i] = 0
    plot_x2[i] = 0
    plot_x3[i] = 0

# DTWを計算
distance, path = fastdtw(plot_x1, plot_x2, dist=euclidean)

print("DTW距離:", distance)
plt.plot(plot_x1, label='plot_x1')
plt.plot(plot_x2, label='plot_x2')
# 各点がどのように対応しているかを図示する
for plot_x1_, plot_x2_ in path:
  plt.plot([plot_x1_, plot_x2_], [plot_x1[plot_x1_], plot_x2[plot_x2_]], color='gray', linestyle='dotted', linewidth=1)
plt.legend()
plt.title('Our two temporal sequences')
plt.show()