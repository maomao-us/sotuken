import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score


#CSVファイルを読み込む
csv_1 = pd.read_csv('kouhai1.csv')
csv_2 = pd.read_csv('kouhai2.csv')
csv_3 = pd.read_csv('kouhai3.csv')

x_label = "Linear Acceleration x (m/s^2)"
y_label = "Linear Acceleration y (m/s^2)"
z_label = "Linear Acceleration z (m/s^2)"
abs_label = "Absolute acceleration (m/s^2)"


# 移動平均線にしてノイズを除去するための関数
# -------------------------------------------------------------------------------------------------
def average_line(csv, label, window):
    plot_mean = []
    list = csv[label].rolling(window).mean()
    for i in range(1200):
        plot_mean.append(list[i])
    
    for i in range(window - 1):
        plot_mean[i] = 0
    
    return plot_mean
# -------------------------------------------------------------------------------------------------

# 時間とcsv ファイルの各列要素を入れるための空リスト
# -------------------------------------------------------------------------------------------------
# plot_x_csv1_mean = []
# plot_x_csv2_mean = []
# plot_x_csv3_mean = []

# plot_y_csv1_mean = []
# plot_y_csv2_mean = []
# plot_y_csv3_mean = []

# plot_z_csv1_mean = []
# plot_z_csv2_mean = []
# plot_z_csv3_mean = []

# plot_abs_csv1_mean = []
# plot_abs_csv2_mean = []
# plot_abs_csv3_mean = []
# -------------------------------------------------------------------------------------------------

plot_x_csv1_mean = average_line(csv_1, x_label, 5)

print(len(plot_x_csv1_mean))