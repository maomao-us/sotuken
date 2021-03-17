import csv 
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score


#CSVファイルを読み込む
csv_hiromu = pd.read_csv('hiromu1.csv')
csv_kouhai = pd.read_csv('kouhai1.csv')
csv_nakajima = pd.read_csv('nakajima1.csv')


# 時間とcsv ファイルの各列要素を入れるための空リスト
# -------------------------------------------------------------------------------------------------
plot_time = []

plot_x_hiromu = []
plot_x_kouhai = []
plot_x_nakajima = []

plot_y_hiromu = []
plot_y_kouhai = []
plot_y_nakajima = []

plot_z_hiromu = []
plot_z_kouhai = []
plot_z_nakajima = []

plot_abs_hiromu = []
plot_abs_kouhai = []
plot_abs_nakajima = []
# -------------------------------------------------------------------------------------------------


# 6秒間を約0.005秒間隔で測定しているので1200個の要素を抽出


# 要素を代入
# -------------------------------------------------------------------------------------------------
for i in range(1200):
    plot_time.append((i + 1) * 0.005)

    plot_x_hiromu += [csv_hiromu.iloc[i,1]]
    plot_x_kouhai += [csv_kouhai.iloc[i,1]]
    plot_x_nakajima += [csv_nakajima.iloc[i,1]]

    plot_y_hiromu += [csv_hiromu.iloc[i,2]]
    plot_y_kouhai += [csv_kouhai.iloc[i,2]]
    plot_y_nakajima += [csv_nakajima.iloc[i,2]]

    plot_z_hiromu += [csv_hiromu.iloc[i,3]]
    plot_z_kouhai += [csv_kouhai.iloc[i,3]]
    plot_z_nakajima += [csv_nakajima.iloc[i,3]]

    plot_abs_hiromu += [csv_hiromu.iloc[i,4]]
    plot_abs_kouhai += [csv_kouhai.iloc[i,4]]
    plot_abs_nakajima += [csv_nakajima.iloc[i,4]]
# -------------------------------------------------------------------------------------------------


# hiromu1.csvをもとに修正


# kouhai1.csv を修正
# -------------------------------------------------------------------------------------------------
# ｘ成分を修正
# count_x_kouhai = 0
# plot_x_kouhai_roll = 0
# plot_x_kouhai_maxroll = np.roll(plot_x_hiromu, 0)

# for i in range(1200):
#     plot_x_kouhai_roll = np.roll(plot_x_hiromu,i)
#     if r2_score(plot_x_kouhai_roll, plot_x_kouhai) > r2_score(plot_x_kouhai_maxroll, plot_x_kouhai):
#         plot_x_kouhai_maxroll = plot_x_kouhai_roll
#         count_x_kouhai = i

# print("kouhai1.csv のｘ成分の修正前後の比較")
# print(r2_score(plot_x_hiromu, plot_x_kouhai))
# print(r2_score(plot_x_kouhai_maxroll, plot_x_kouhai))
# print("何回動いた？")
# print(count_x_kouhai)
# print("\n")

# # ｙ成分を修正
# count_y_kouhai = 0
# plot_y_kouhai_roll = 0
# plot_y_kouhai_maxroll = np.roll(plot_y_hiromu, 0)

# for i in range(1200 ):
#     plot_y_kouhai_roll = np.roll(plot_y_hiromu,i)
#     if r2_score(plot_y_kouhai_roll, plot_y_kouhai) > r2_score(plot_y_kouhai_maxroll, plot_y_kouhai):
#         plot_y_kouhai_maxroll = plot_y_kouhai_roll
#         count_y_kouhai = i

# print("kouhai1.csv のy成分の修正前後の比較")
# print(r2_score(plot_y_hiromu, plot_y_kouhai))
# print(r2_score(plot_y_kouhai_maxroll, plot_y_kouhai))
# print("何回動いた？")
# print(count_y_kouhai)
# print("\n")

# # ｚ成分を修正
# count_z_kouhai = 0
# plot_z_kouhai_roll = 0
# plot_z_kouhai_maxroll = np.roll(plot_z_hiromu, 0)

# for i in range(1200 ):
#     plot_z_kouhai_roll = np.roll(plot_z_hiromu,i)
#     if r2_score(plot_z_kouhai_roll, plot_z_kouhai) > r2_score(plot_z_kouhai_maxroll, plot_z_kouhai):
#         plot_z_kouhai_maxroll = plot_z_kouhai_roll
#         count_z_kouhai = i

# print("kouhai1.csv のz成分の修正前後の比較")
# print(r2_score(plot_z_hiromu, plot_z_kouhai))
# print(r2_score(plot_z_kouhai_maxroll, plot_z_kouhai))
# print("何回動いた？")
# print(count_z_kouhai)
# print("\n")
# # -------------------------------------------------------------------------------------------------

# # 成分

# # hiromu3.csv を修正
# # -------------------------------------------------------------------------------------------------
# # ｘ成分を修正
# count_x_nakajima = 0
# plot_x_nakajima_roll = 0
# plot_x_nakajima_maxroll = np.roll(plot_x_nakajima, 0)

# for i in range(1200 ):
#     plot_x_nakajima_roll = np.roll(plot_x_nakajima, i)
#     if r2_score(plot_x_nakajima_roll, plot_x_kouhai) > r2_score(plot_x_nakajima_maxroll, plot_x_kouhai):
#         plot_x_nakajima_maxroll = plot_x_nakajima_roll
#         count_x_nakajima = i

# print("nakajima1.csv のｘ成分の修正前後の比較")
# print(r2_score(plot_x_nakajima, plot_x_kouhai))
# print(r2_score(plot_x_nakajima_maxroll, plot_x_kouhai))
# print("何回動いた？")
# print(count_x_nakajima)
# print("\n")

# # ｙ成分を修正
# count_y_nakajima = 0
# plot_y_nakajima_roll = 0
# plot_y_nakajima_maxroll = np.roll(plot_y_nakajima, 0)

# for i in range(1200 ):
#     plot_y_nakajima_roll = np.roll(plot_y_nakajima, i)
#     if r2_score(plot_y_nakajima_roll, plot_y_kouhai) > r2_score(plot_y_nakajima_maxroll, plot_y_kouhai):
#         plot_y_nakajima_maxroll = plot_y_nakajima_roll
#         count_y_nakajima = i

# print("nakajima1.csv のy成分の修正前後の比較")
# print(r2_score(plot_y_nakajima, plot_y_kouhai))
# print(r2_score(plot_y_nakajima_maxroll, plot_y_kouhai))
# print("何回動いた？")
# print(count_y_nakajima)
# print("\n")

# # ｚ成分を修正
# count_z_nakajima = 0
# plot_z_nakajima_roll = 0
# plot_z_nakajima_maxroll = np.roll(plot_z_nakajima, 0)

# for i in range(1200 ):
#     plot_z_nakajima_roll = np.roll(plot_z_nakajima, i)
#     if r2_score(plot_z_nakajima_roll, plot_z_kouhai) > r2_score(plot_z_nakajima_maxroll, plot_z_kouhai):
#         plot_z_nakajima_maxroll = plot_z_nakajima_roll
#         count_z_nakajima = i

# print("nakajima1.csv のz成分の修正前後の比較")
# print(r2_score(plot_z_nakajima, plot_z_kouhai))
# print(r2_score(plot_z_nakajima_maxroll, plot_z_kouhai))
# print("何回動いた？")
# print(count_z_nakajima)
# print("\n")
# -------------------------------------------------------------------------------------------------


fig = plt.figure(figsize=(5,5))

# x1 = fig.add_subplot(1, 6, 1)
# x2 = fig.add_subplot(1, 6, 3)
# x3 = fig.add_subplot(1, 6, 5)

# 修正前のグラフ
# -------------------------------------------------------------------------------------------------
# ひろむ先輩
# plt.plot(plot_time,plot_x_hiromu)
# plt.plot(plot_time,plot_y_hiromu)
# plt.plot(plot_time,plot_z_hiromu)

# 後輩
# plt.plot(plot_time,plot_x_kouhai)
# plt.plot(plot_time,plot_y_kouhai)
# plt.plot(plot_time,plot_z_nakajima)

# 中島
# plt.plot(plot_time,plot_x_nakajima)
# plt.plot(plot_time,plot_y_nakajima)
# plt.plot(plot_time,plot_z_nakajima)
# -------------------------------------------------------------------------------------------------


# 修正後のグラフ
# -------------------------------------------------------------------------------------------------
# 後輩
# plt.plot(plot_time, plot_x_kouhai_maxroll)
# plt.plot(plot_time, plot_y_kouhai_maxroll)
# plt.plot(plot_time, plot_z_kouhai_maxroll)

# 中島
# plt.plot(plot_time, plot_x_nakajima_maxroll)
# plt.plot(plot_time, plot_y_nakajima_maxroll)
# plt.plot(plot_time, plot_z_nakajima_maxroll)
# -------------------------------------------------------------------------------------------------


# 修正前のグラフと比較
# -------------------------------------------------------------------------------------------------
plt.plot(plot_time,plot_x_hiromu, label="hiromu")
plt.plot(plot_time,plot_x_kouhai, label = "kouhai")
plt.plot(plot_time,plot_x_nakajima, label = "nakajima")

# plt.plot(plot_time,plot_y_hiromu)
# plt.plot(plot_time,plot_y_kouhai)
# plt.plot(plot_time,plot_y_nakajima)

# plt.plot(plot_time,plot_z_hiromu)
# plt.plot(plot_time,plot_z_kouhai)
# plt.plot(plot_time,plot_z_nakajima)
# -------------------------------------------------------------------------------------------------


# 修正後のグラフと比較
# -------------------------------------------------------------------------------------------------
# ｘ成分
# plt.plot(plot_time, plot_x_hiromu)
# plt.plot(plot_time, plot_x_kouhai_maxroll)
# plt.plot(plot_time, plot_x_nakajima_maxroll)

# ｙ成分
# plt.plot(plot_time, plot_y_hiromu)
# plt.plot(plot_time, plot_y_kouhai_maxroll)
# plt.plot(plot_time, plot_y_nakajima_maxroll)

# ｚ成分
# plt.plot(plot_time, plot_z_hiromu)
# plt.plot(plot_time, plot_z_kouhai_maxroll)
# plt.plot(plot_time, plot_z_nakajima_maxroll)
# -------------------------------------------------------------------------------------------------

plt.title("dimension_x")
plt.legend()
plt.grid()
plt.xlim(1.5, 4.5)

fig.savefig("hiromu_kouhai_nakajima_x.png")
