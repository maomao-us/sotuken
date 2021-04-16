import csv
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas as pd
from sklearn.metrics import r2_score

# 定義
##################################################################################################################################################
file_name = ["hiromu1", "hiromu2", "hiromu3", "kouhai1", "kouhai2", "kouhai3"]

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]

average_count = 5
window = 5

component = ["x", "y", "z", "abs"]

# 各移動平均の結果を保存するためのcsvファイルのラベル
##################################################################################################################################################
for z in range(4):
    what_component = component[z]
    if what_component == "x":
        with open("output_average/x_average.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["file", "sma", "wma", "ewm"])

    elif what_component == "y":
        with open("output_average/y_average.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["file", "sma", "wma", "ewm"])

    elif what_component == "z":
        with open("output_average/z_average.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["file", "sma", "wma", "ewm"])

    elif what_component == "abs":
        with open("output_average/abs_average.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["file", "sma", "wma", "ewm"])

# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma

# 評価の結果をcsvに書き込む関数
##################################################################################################################################################
##################################################################################################################################################
def input_result():
    for i in range(6):
        df = pd.read_csv("csv_data/" + file_name[i] + ".csv")

        for j in range(4):
            data = df[label[j]]
            data = np.array(data)

            # csvデータの総ステップ数
            step = []
            for k in range(len(df)):
                step.append(k + 1)
            step = np.array(step)

            # 各移動平均，n = 5，試行回数5回
            sma = df[label[j]].rolling(window, center =True, min_periods=1).mean()
            wma = df[label[j]].rolling(window, min_periods=1).apply(WMA)
            ewm = df[label[j]].ewm(span = window, adjust=False).mean()

            for l in range(average_count - 1):
                sma = sma.rolling(window, center = True, min_periods=1).mean()
                wma = wma.rolling(window, min_periods=1).apply(WMA)
                ewm = ewm.ewm(span = window, adjust=False).mean()

            sma = np.array(sma)
            wma = np.array(wma)
            ewm = np.array(ewm)

            max_roll_sma = np.roll(sma, 0)
            for m in range(30):
                roll = np.roll(sma, -m)
                if r2_score(data, roll) > r2_score(data, max_roll_sma):
                    max_roll_sma = roll

            max_roll_wma = np.roll(wma, 0)
            for n in range(30):
                roll = np.roll(wma, -n)
                if r2_score(data, roll) > r2_score(data, max_roll_wma):
                    max_roll_wma = roll

            max_roll_ewm = np.roll(wma, 0)
            for o in range(30):
                roll = np.roll(ewm, -o)
                if r2_score(data, roll) > r2_score(data, max_roll_ewm):
                    max_roll_ewm = roll

            print("sma")
            print(1 - r2_score(data, max_roll_sma))
            print("\n")
            print("wma")
            print(1 - r2_score(data, max_roll_wma))
            print("\n")
            print("ewm")
            print(1 - r2_score(data, max_roll_ewm))
            print("\n")

            what_component = component[j]
            if what_component == "x":
                with open("output_average/x_average.csv", "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([file_name[i], 1 - r2_score(data, max_roll_sma), 1 - r2_score(data, max_roll_wma), 1 - r2_score(data, max_roll_ewm)])

            elif what_component == "y":
                with open("output_average/y_average.csv", "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([file_name[i], 1 - r2_score(data, max_roll_sma), 1 - r2_score(data, max_roll_wma), 1 - r2_score(data, max_roll_ewm)])

            elif what_component == "z":
                with open("output_average/z_average.csv", "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([file_name[i], 1 - r2_score(data, max_roll_sma), 1 - r2_score(data, max_roll_wma), 1 - r2_score(data, max_roll_ewm)])

            elif what_component == "abs":
                with open("output_average/abs_average.csv", "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([file_name[i], 1 - r2_score(data, max_roll_sma), 1 - r2_score(data, max_roll_wma), 1 - r2_score(data, max_roll_ewm)])

input_result()