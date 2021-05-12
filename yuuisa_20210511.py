import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["horinouti", "kawamura", "horinouti", "kutukake", "takenaka", "horinouti", "horinouti", "yamanada"]
index_2 = ["2x", "2y", "2z", "2abs"]
index_22 = ["2xx", "2yy", "2zz", "2absabs"]

index_3 = ["3x", "3y", "3z", "3abs"]
index_33 = ["3xx", "3yy", "3zz", "3absabs"]

index_4 = ["4x", "4y", "4z", "4abs"]
index_44 = ["4xx", "4yy", "4zz", "4absabs"]

index_5 = ["5x", "5y", "5z", "5abs"]
index_22 = ["5xx", "5yy", "5zz", "5absabs"]

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
def kentei_1():
    global label_number
    with open("kentei_data/horinouti/horinouti_kentei" + index_2[label_number] + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["m", "n", "times", "F"])

    col_names = ['c{0:02d}'.format(i) for i in range(20)]
    file_name = "horinouti_ev" + index_2[label_number]
    df = pd.read_csv("sotuken_data/horinouti/" + file_name + ".csv", header=None, names = col_names, engine = "python")

    data1 = []
    data2 = []

    range_size = size

    for i in range(range_size):
        for j in range(len(df.columns)):
            data1 += [df.iloc[i, j]]
        data1 = np.array(data1)
        data1 = [x for x in data1 if np.isnan(x) == False]

        for k in range(range_size):
            for l in range(len(df.columns)):
                data2 += [df.iloc[k, l]]
            data2 = np.array(data2)
            data2 = [x for x in data2 if np.isnan(x) == False]

            mean_data1 = np.mean(data1)
            mean_data2 = np.mean(data2)
            std_data1 = np.var(data1, ddof = 1)
            std_data2 = np.var(data2, ddof = 1)
            std = ((len(data1) - 1)*(std_data1) + (len(data2) - 1)*(std_data2)) / (len(data1) + len(data2) - 2)
            T = (mean_data1 - mean_data2) / (((1/len(data1)) + (1/len(data2)))*std)**(1/2)

            with open("kentei_data/horinouti/horinouti_kentei"+ index_2[label_number] + ".csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([len(data1), len(data2), k + 1,T])

            data2.clear()
        data1.clear()

# 検定その2
##################################################################################################################################################
##################################################################################################################################################
def kentei_2(m):
    with open("kentei_data/horinouti/horinouti_kentei" + index_2[m] + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["m", "n", "times", "F"])

    col_names = ['c{0:02d}'.format(i) for i in range(20)]
    file_name = "horinouti_ev" + index_22[m]
    df = pd.read_csv("sotuken_data/horinouti/" + file_name + ".csv", header=None, names = col_names, engine = "python")

    data1 = []
    data2 = []

    range_size = size

    for i in range(range_size):
        for j in range(len(df.columns)):
            data1 += [df.iloc[i, j]]
        data1 = np.array(data1)
        data1 = [x for x in data1 if np.isnan(x) == False]

        for k in range(range_size):
            for l in range(len(df.columns)):
                data2 += [df.iloc[k, l]]
            data2 = np.array(data2)
            data2 = [x for x in data2 if np.isnan(x) == False]

            mean_data1 = np.mean(data1)
            mean_data2 = np.mean(data2)
            std_data1 = np.var(data1, ddof = 1)
            std_data2 = np.var(data2, ddof = 1)
            std = ((len(data1) - 1)*(std_data1) + (len(data2) - 1)*(std_data2)) / (len(data1) + len(data2) - 2)
            T = (mean_data1 - mean_data2) / (((1/len(data1)) + (1/len(data2)))*std)**(1/2)

            with open("kentei_data/horinouti/horinouti_kentei"+ index_2[m] + ".csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([len(data1), len(data2), k + 1,T])

            data2.clear()
        data1.clear()

# 有意差
##################################################################################################################################################
##################################################################################################################################################
def yuuisa():
    while(1):
        global count
        global number
        global size
        global list
        global yuuisa_number
        global label_number


        file_name = "horinouti_kentei" + index_2[label_number]
        df = pd.read_csv("kentei_data/horinouti/" + file_name + ".csv")

        data_0 = df["m"]
        data_0 = np.array(data_0)
        data_1 = df["n"]
        data_1 = np.array(data_1)
        data_2 = df["times"]
        data_2 = np.array(data_2)
        data_3 = df["F"]
        data_3 = np.array(data_3)

        for i in range(len(df)):
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
            if data_2[i] == size:
                list.append(count)
                count = 0
        print(list)

        if max(list) >= 1:
            if yuuisa_number == 0:
                with open("yuuisa_data/horinouti/horinouti_" + index_2[label_number] + ".csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(list)
            elif yuuisa_number >= 1:
                with open("yuuisa_data/horinouti/horinouti_" + index_2[label_number] + ".csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(list)
            size -= 1
            col_names = ['c{0:02d}'.format(i) for i in range(20)]
            df = pd.read_csv("sotuken_data/horinouti/horinouti_ev" + index_22[label_number] + ".csv", header=None, names = col_names, engine = "python")
            df = df.drop(list.index(max(list)), axis=0)
            df.to_csv("sotuken_data/horinouti/horinouti_ev" + index_22[label_number] + ".csv", header=None, index = False)

            df = pd.read_csv("step/horinouti/horinouti_step" + index_22[label_number] + ".csv", header=None, names = col_names, engine = "python")
            df = df.drop(list.index(max(list)), axis=0)
            df.to_csv("step/horinouti/horinouti_step" + index_22[label_number] + ".csv", header=None, index = False)
            yuuisa_number += 1
            list.clear()
            kentei_2(label_number)

        elif max(list) == 0:
            if yuuisa_number == 0:
                print(yuuisa_number)
                with open("yuuisa_data/horinouti/horinouti_" + index_2[label_number] + ".csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(list)
            elif yuuisa_number >= 1:
                print(yuuisa_number)
                with open("yuuisa_data/horinouti/horinouti_" + index_2[label_number] + ".csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(list)
            list.clear()
            yuuisa_number = 0
            size = 20
            break

for l in range(4):
    col_names = ['c{0:02d}'.format(i) for i in range(20)]
    df = pd.read_csv("sotuken_data/horinouti/horinouti_ev" + index_2[label_number] + ".csv", header=None, names = col_names, engine = "python")
    df.to_csv("sotuken_data/horinouti/horinouti_ev" + index_22[label_number] + ".csv", header=None, index = False)

    df = pd.read_csv("step/horinouti/horinouti_step" + index_2[label_number] + ".csv", header=None, names = col_names, engine = "python")
    df.to_csv("step/horinouti/horinouti_step" + index_22[label_number] + ".csv", header=None, index = False)
    kentei_1()
    yuuisa()
    label_number += 1
