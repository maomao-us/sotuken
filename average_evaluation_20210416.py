import csv
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score

# 定義
##################################################################################################################################################
file_name = ["x_average", "y_average", "z_average", "abs_average"]

label = ["sma", "wma", "ewm"]

# 各移動平均の評価を保存するためのcsvファイルのラベル
##################################################################################################################################################
with open("output_average/average_evaluation.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["sma", "wma", "ewm"])

# 本番
##################################################################################################################################################
for i in range(4):
    df = pd.read_csv("output_average/" + file_name[i] + ".csv")
    # print(i + 1, "回目")

    data1 = df[label[0]]
    data1 = np.array(data1)
    print(data1)
    # print("\n")

    data2 = df[label[1]]
    data2 = np.array(data2)
    print(data2)
    # print("\n")

    data3 = df[label[2]]
    data3 = np.array(data3)
    print(data3)
    print("\n")

    for j in range(len(df)):
        if data1[j] < data2[j] and data1[j] < data3[j]:
            with open("output_average/average_evaluation.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([1, 0, 0])

        elif data2[j] < data1[j] and data2[j] < data3[j]:
            with open("output_average/average_evaluation.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([0, 1, 0])

        elif data3[j] < data1[j] and data3[j] < data2[j]:
            with open("output_average/average_evaluation.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([0, 0, 1])