import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

label = "Linear Acceleration y (m/s^2)"
lx = ["2y", "3y", "4y", "5y"]
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
window = 5

# 加重移動平均法の関数
##################################################################################################################################################
##################################################################################################################################################
def WMA(csv):
    weights = np.arange(len(csv)) + 1
    wma = np.sum(weights * csv) / weights.sum()
    return wma

# 極小値を格納
##################################################################################################################################################
##################################################################################################################################################
def MIN_EV(f):
    ev = []
    Max_ev = []
    step_list1 = []
    step_list2 = []
    Max_step = []

    # 前後20個のデータを格納
    for i in range(160, len(data) - 10):
        a = data[i - 1]
        b = data[i]
        c = data[i + 1]

        if len(ev) == 0 and (b-a) < 0 and 0 < (c-b):
            ev.append(data[i])
            step_list1.append(step[i])

        elif len(ev) > 0:
            if len(ev) % 2 == 1 and (b-a) > 0 and 0 > (c-b) and (max(data) - min(data)) * 0.4 < (data[i] - ev[len(ev) - 1]):
                ev.append(data[i])
                step_list1.append(step[i])

            if len(ev) % 2 == 0 and (b-a) < 0 and 0 < (c-b) and (max(data) - min(data)) * 0.4 < (ev[len(ev) - 1] - data[i]):
                ev.append(data[i])
                step_list1.append(step[i])

            if len(ev) % 2 == 0 and (b-a) > 0 and 0 > (c-b) and ev[len(ev) - 1] < data[i]:
                ev.pop()
                step_list1.pop()
                ev.append(data[i])
                step_list1.append(step[i])

            if len(ev) % 2 == 1 and (b-a) < 0 and 0 < (c-b) and data[i] < ev[len(ev) - 1]:
                ev.pop()
                step_list1.pop()
                ev.append(data[i])
                step_list1.append(step[i])

        if len(ev) == 2 * f:
            break
    
    for i in range(len(ev)):
        if i % 2 == 1:
            Max_ev.append(ev[i])
            Max_step.append(step_list1[i])


    for i in range(len(Max_step) - 1):
        step_list2.append(Max_step[i + 1] - Max_step[i])

    Max_ev = np.array(Max_ev)
    if len(Max_ev) > 1:
        print(len(Max_ev), "個")
        print(Max_ev)
        print(Max_step)
        print(step_list2)
    return Max_ev, Max_step, step_list2

##################################################################################################################################################
for w in range(0, 8):
    print(name[w])
    for z in range(0, 4):
        print(z + 2, "スイング")
        for i in range(10, 30):
            file_name = name[w] + "_" + str(i)
            print(file_name)

            df = pd.read_csv("oltana/" + name[w] + "_" + str(z + 2) + "/" + file_name + ".csv")
            data = df[label].rolling(window, min_periods=1).apply(WMA)
            for h in range(5 - 1):
                data = data.rolling(window, min_periods=1).apply(WMA)
            data = np.array(data)

            step = []
            for h in range(len(data)):
                step.append(h)
            step = np.array(step)

            ev, ev_step1, ev_step2 = MIN_EV(z + 2)

            if len(ev) == (z + 2):
                if i % 2 == 0 and i == 10:
                    with open("sotuken_data_train/data/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev)
                    with open("sotuken_data_train/step/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev_step2)
                elif i % 2 == 0 and 10 < i:
                    with open("sotuken_data_train/data/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev)
                    with open("sotuken_data_train/step/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev_step2)
                elif i % 2 ==1 and i == 11:
                    with open("sotuken_data_test/data/" + name[w] + "/" + name[w] + "_test_Max_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev)
                    with open("sotuken_data_test/step/" + name[w] + "/" + name[w] + "_test_Max_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev_step2)
                elif i % 2 ==1 and 11 < i:
                    with open("sotuken_data_test/data/" + name[w] + "/" + name[w] + "_test_Max_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev)
                    with open("sotuken_data_test/step/" + name[w] + "/" + name[w] + "_test_Max_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(ev_step2)

        df_train_ev = pd.read_csv("sotuken_data_train/data/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", header=None, engine = "python")
        df_train_step = pd.read_csv("sotuken_data_train/step/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", header=None, engine = "python")
        # df_test_ev = pd.read_csv("sotuken_data_test/data/" + name[w] + "/" + name[w] + "_test_ev_" + lx[z] + ".csv", header=None, engine = "python")
        # df_test_step = pd.read_csv("sotuken_data_test/step/" + name[w] + "/" + name[w] + "_test_step_" + lx[z] + ".csv", header=None, engine = "python")

        df_train_ev = df_train_ev.T
        df_train_step = df_train_step.T
        # df_test_ev = df_test_ev.T
        # df_test_step = df_test_step.T

        df_train_ev.to_csv("sotuken_data_train/data/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", header=None, index = False)
        df_train_step.to_csv("sotuken_data_train/step/" + name[w] + "/" + name[w] + "_train_Max_" + lx[z] + ".csv", header=None, index = False)
        # df_test_ev.to_csv("sotuken_data_test/data/" + name[w] + "/" + name[w] + "_test_ev_" + lx[z] + ".csv", header=None, index = False)
        # df_test_step.to_csv("sotuken_data_test/step/" + name[w] + "/" + name[w] + "_test_step_" + lx[z] + ".csv", header=None, index = False)