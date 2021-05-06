import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
index_2 = ["2x", "2y", "2z", "2abs"]
index_3 = ["3x", "3y", "3z", "3abs"]
index_4 = ["4x", "4y", "4z", "4abs"]
index_5 = ["5x", "5y", "5z", "5abs"]

t = [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, \
        2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, \
            2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042]

count = 0
number = 1
list = []

for z in range(4):
    file_name = "takenaka_kentei" + index_4[z]
    df = pd.read_csv("kentei_data/takenaka_4/" + file_name + ".csv")

    data_0 = df["m"]
    data_0 = np.array(data_0)
    data_1 = df["n"]
    data_1 = np.array(data_1)
    data_2 = df["times"]
    data_2 = np.array(data_2)
    data_3 = df["F"]
    data_3 = np.array(data_3)

    print(z+1, "回目")
    for i in range(len(df)):
        # print("サイズ", data_0[i] + data_1[i] - 2)
        # print("T : ", data_3[i])
        # print(data_2[i])

        # number = 1
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 2
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 3
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 4
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 5
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 6
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 7
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 8
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 9
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 10
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 11
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 12
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 13
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 14
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 15
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 16
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 17
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 18
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 19
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 20
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 21
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 22
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 23
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 24
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 25
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 26
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 27
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 28
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 29
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1
        number += 1

        # number = 30
        if (data_0[i] + data_1[i] - 2) == number and (data_3[i] < -t[number - 1] or t[number - 1] < data_3[i]):
            count += 1

        number = 1
        # print(data_2[i])
        if data_2[i] == 20:
            list.append(count)
            count = 0
    print(list)
    with open("yuuisa_data/takenaka_4.csv", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(list)
    list.clear()