import csv
import numpy as np
import pandas as pd
from pandas.core.generic import NDFrame

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
index_2 = ["2x", "2y", "2z", "2abs"]
l_22 = ["2xx", "2yy", "2zz", "2absabs"]

index_3 = ["3x", "3y", "3z", "3abs"]
l_33 = ["3xx", "3yy", "3zz", "3absabs"]

index_4 = ["4x", "4y", "4z", "4abs"]
l_44 = ["4xx", "4yy", "4zz", "4absabs"]

index_5 = ["5x", "5y", "5z", "5abs"]
l_55 = ["5xx", "5yy", "5zz", "5absabs"]

t = [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, \
        2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, \
            2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042]

count = 0
number = 1
size = 20
list = []
yuuisa_number = 0
label_number = 0

# 検定その1
##################################################################################################################################################
##################################################################################################################################################
def kentei_1(x, y, z):
    with open("kentei_data_2/"  + name[x] + "/" + name[x] + "_" + name[y] + "_" + index_3[z] + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["m", "n", "times", "F"])

    col_names = ['c{0:02d}'.format(i) for i in range(20)]
    file_name = name[x] + "_ev" + index_3[z]
    file_name2 = name[y] + "_ev" + index_3[z]
    df1 = pd.read_csv("sotuken_data/" + name[x] + "/" + file_name + ".csv", header=None, names = col_names, engine = "python")
    df2 = pd.read_csv("sotuken_data/" + name[y] + "/" + file_name2 + ".csv", header=None, names = col_names, engine = "python")

    data1 = []
    data2 = []

    range_size = len(df1)

    for i in range(len(df1)):
        for j in range(len(df1.columns)):
            data1 += [df1.iloc[i, j]]
        data1 = np.array(data1)
        data1 = [x for x in data1 if np.isnan(x) == False]

        for k in range(len(df2)):
            for l in range(len(df2.columns)):
                data2 += [df2.iloc[k, l]]
            data2 = np.array(data2)
            data2 = [x for x in data2 if np.isnan(x) == False]

            mean_data1 = np.mean(data1)
            # print(mean_data1)
            mean_data2 = np.mean(data2)
            # print(mean_data2)
            std_data1 = np.var(data1, ddof = 1)
            # print(std_data1)
            std_data2 = np.var(data2, ddof = 1)
            # print(std_data2)
            std = ((len(data1) - 1)*(std_data1) + (len(data2) - 1)*(std_data2)) / (len(data1) + len(data2) - 2)
            T = (mean_data1 - mean_data2) / (((1/len(data1)) + (1/len(data2)))*std)**(1/2)
            # print(T)
            with open("kentei_data_2/"  + name[x] + "/" + name[x] + "_" + name[y] + "_" + index_3[z] + ".csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([len(data1), len(data2), k + 1,T])

            data2.clear()
        data1.clear()

# 有意差
##################################################################################################################################################
##################################################################################################################################################
def yuuisa(x, y, z):
    global count
    global number
    global list

    file_name = name[x] + "_" + name[y] + "_" + index_3[z]
    df1 = pd.read_csv("kentei_data_2/" + name[x] + "/" + file_name + ".csv")
    file_name2 = name[y] + "_ev" + index_3[z]
    col_names = ['c{0:02d}'.format(i) for i in range(20)]
    df2 = pd.read_csv("sotuken_data/" + name[y] + "/" + file_name2 + ".csv", names = col_names, header=None, engine = "python")

    data_0 = df1["m"]
    data_0 = np.array(data_0)
    data_1 = df1["n"]
    data_1 = np.array(data_1)
    data_2 = df1["times"]
    data_2 = np.array(data_2)
    data_3 = df1["F"]
    data_3 = np.array(data_3)

    for i in range(len(df1)):
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

        if data_2[i] == len(df2):
            list.append(count)
            count = 0
    print(list)

    if y == 0:
        with open("yuuisa_data_2/" + name[x] + "/" + name[x] + "_" + index_3[z] + ".csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(list)
    elif y >= 1:
        with open("yuuisa_data_2/" + name[x] + "/" + name[x] + "_" + index_3[z] + ".csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(list)
    list.clear()

for a in range(4):
    for b in range(8):
        for c in range(8):
            kentei_1(b, c, a)

for a in range(4):
    for b in range(8):
        for c in range(8):
            yuuisa(b, c, a)