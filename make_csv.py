import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score


#CSVファイルを読み込む
csv_1 = pd.read_csv('hiromu1.csv')
csv_2 = pd.read_csv('hiromu2.csv')
csv_3 = pd.read_csv('hiromu3.csv')


# 時間とcsv ファイルの各列要素を入れるための空リスト
# -------------------------------------------------------------------------------------------------
plot_time = []

plot_x1 = []
plot_x2 = []
plot_x3 = []

plot_y1 = []
plot_y2 = []
plot_y3 = []

plot_z1 = []
plot_z2 = []
plot_z3 = []

plot_abs1 = []
plot_abs2 = []
plot_abs3 = []
# -------------------------------------------------------------------------------------------------


# 6秒間を約0.005秒間隔で測定しているので1200個の要素を抽出


# 要素を代入
# -------------------------------------------------------------------------------------------------
for i in range(1200):
    plot_time.append((i + 1) * 0.005)

    plot_x1 += [csv_1.iloc[i,1]]
    plot_x2 += [csv_2.iloc[i,1]]
    plot_x3 += [csv_3.iloc[i,1]]

    plot_y1 += [csv_1.iloc[i,2]]
    plot_y2 += [csv_2.iloc[i,2]]
    plot_y3 += [csv_3.iloc[i,2]]

    plot_z1 += [csv_1.iloc[i,3]]
    plot_z2 += [csv_2.iloc[i,3]]
    plot_z3 += [csv_3.iloc[i,3]]

    plot_abs1 += [csv_1.iloc[i,4]]
    plot_abs2 += [csv_2.iloc[i,4]]
    plot_abs3 += [csv_3.iloc[i,4]]
# -------------------------------------------------------------------------------------------------


# hiromu2.csvをもとに修正


# hiromu1.csv を修正
# -------------------------------------------------------------------------------------------------
# ｘ成分を修正
count_x1 = 0
plot_x1roll = 0
plot_x1maxroll = np.roll(plot_x1, 0)

for i in range(1200 ):
    plot_x1roll = np.roll(plot_x1,i)
    if r2_score(plot_x1roll, plot_x2) > r2_score(plot_x1maxroll, plot_x2):
        plot_x1maxroll = plot_x1roll
        count_x1 = i

print("hiromu1.csv のｘ成分の修正前後の比較")
print(r2_score(plot_x1, plot_x2))
print(r2_score(plot_x1maxroll, plot_x2))
print("何回動いた？")
print(count_x1)
print("\n")

# ｙ成分を修正
count_y1 = 0
plot_y1roll = 0
plot_y1maxroll = np.roll(plot_y1, 0)

for i in range(1200 ):
    plot_y1roll = np.roll(plot_y1,i)
    if r2_score(plot_y1roll, plot_y2) > r2_score(plot_y1maxroll, plot_y2):
        plot_y1maxroll = plot_y1roll
        count_y1 = i

print("hiromu1.csv のy成分の修正前後の比較")
print(r2_score(plot_y1, plot_y2))
print(r2_score(plot_y1maxroll, plot_y2))
print("何回動いた？")
print(count_y1)
print("\n")

# ｚ成分を修正
count_z1 = 0
plot_z1roll = 0
plot_z1maxroll = np.roll(plot_z1, 0)

for i in range(1200 ):
    plot_z1roll = np.roll(plot_z1,i)
    if r2_score(plot_z1roll, plot_z2) > r2_score(plot_z1maxroll, plot_z2):
        plot_z1maxroll = plot_z1roll
        count_z1 = i

print("hiromu1.csv のz成分の修正前後の比較")
print(r2_score(plot_z1, plot_z2))
print(r2_score(plot_z1maxroll, plot_z2))
print("何回動いた？")
print(count_z1)
print("\n")
# -------------------------------------------------------------------------------------------------

# 成分

# hiromu3.csv を修正
# -------------------------------------------------------------------------------------------------
# ｘ成分を修正
count_x3 = 0
plot_x3roll = 0
plot_x3maxroll = np.roll(plot_x3, 0)

for i in range(1200 ):
    plot_x3roll = np.roll(plot_x3, i)
    if r2_score(plot_x3roll, plot_x2) > r2_score(plot_x3maxroll, plot_x2):
        plot_x3maxroll = plot_x3roll
        count_x3 = i

print("hiromu3.csv のｘ成分の修正前後の比較")
print(r2_score(plot_x3, plot_x2))
print(r2_score(plot_x3maxroll, plot_x2))
print("何回動いた？")
print(count_x3)
print("\n")

# ｙ成分を修正
count_y3 = 0
plot_y3roll = 0
plot_y3maxroll = np.roll(plot_y3, 0)

for i in range(1200 ):
    plot_y3roll = np.roll(plot_y3, i)
    if r2_score(plot_y3roll, plot_y2) > r2_score(plot_y3maxroll, plot_y2):
        plot_y3maxroll = plot_y3roll
        count_y3 = i

print("hiromu3.csv のy成分の修正前後の比較")
print(r2_score(plot_y3, plot_y2))
print(r2_score(plot_y3maxroll, plot_y2))
print("何回動いた？")
print(count_y3)
print("\n")

# ｚ成分を修正
count_z3 = 0
plot_z3roll = 0
plot_z3maxroll = np.roll(plot_z3, 0)

for i in range(1200 ):
    plot_z3roll = np.roll(plot_z3, i)
    if r2_score(plot_z3roll, plot_z2) > r2_score(plot_z3maxroll, plot_z2):
        plot_z3maxroll = plot_z3roll
        count_z3 = i

print("hiromu3.csv のz成分の修正前後の比較")
print(r2_score(plot_z3, plot_z2))
print(r2_score(plot_z3maxroll, plot_z2))
print("何回動いた？")
print(count_z3)
print("\n")
# -------------------------------------------------------------------------------------------------


# 修正前のグラフ
plt.plot(plot_time,plot_x1)
plt.plot(plot_time,plot_x2)
plt.plot(plot_time,plot_x3)

# plt.plot(plot_time,plot_y1)
# plt.plot(plot_time,plot_y2)
# plt.plot(plot_time,plot_y3)

# plt.plot(plot_time,plot_z1)
# plt.plot(plot_time,plot_z2)
# plt.plot(plot_time,plot_z3)

# 修正後のグラフ
# plt.plot(plot_time, plot_x1maxroll)
# plt.plot(plot_time, plot_y1maxroll)
# plt.plot(plot_time, plot_z1maxroll)

# plt.plot(plot_time, plot_x3maxroll)
# plt.plot(plot_time, plot_y3maxroll)
# plt.plot(plot_time, plot_z3maxroll)

plt.show()

