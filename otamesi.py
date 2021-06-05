import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
lx = ["2x", "3x", "4x", "5x"]
# ly = ["2y", "3y", "4y", "5y"]
# lz = ["2z", "3z", "4z", "5z"]
# labs = ["2abs", "3abs", "4abs", "5abs"]
name = ["takenaka", "nakajima"]
window = 5

csv_counter = 0

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
    step_list1 = []
    step_list2 = []

    # 前後20個のデータを格納
    for i in range(180, len(data) - 10):
        a = data[i - 1]
        b = data[i]
        c = data[i + 1]

        if (b-a) < 0 and 0 < (c-b) and b < min(data)/3 and len(ev) % 2 == 0:
            ev.append(data[i])
            step_list1.append(step[i])

        if (b-a) > 0 and 0 > (c-b) and b > max(data)/3 and len(ev) % 2 == 1:
            ev.append(data[i])
            step_list1.append(step[i])

        if len(ev) == 2 * f:
            break

    for i in range(len(step_list1) - 1):
        step_list2.append(step_list1[i + 1] - step_list1[i])

    ev = np.array(ev)
    if len(ev) > 1:
        print(len(ev), "個")
        print(ev)
        print(step_list1)
        print(step_list2)
    return ev, step_list1, step_list2

##################################################################################################################################################
label_number = 0
for w in range(2):
    print(name[w])
    for i in range(10, 15):
        file_name = name[w] + "_" + str(i)
        print(file_name)
        df = pd.read_csv(name[w]  + "/" + file_name + ".csv")
        data = df[label[label_number]].rolling(window, min_periods=1).apply(WMA)
        for h in range(5 - 1):
            data = data.rolling(window, min_periods=1).apply(WMA)
        data = np.array(data)
        step = []
        for h in range(len(data)):
            step.append(h)
        step = np.array(step)
        ev, ev_step1, ev_step2 = MIN_EV(5)

        if csv_counter == 0 and len(ev) == 2 * (5):
            with open(name[w] + "/" + name[w] + ".csv", "w", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(ev)
            with open(name[w] + "/" + name[w] + "_step"".csv", "w", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(ev_step2)
            csv_counter += 1

        elif csv_counter >= 1 and len(ev) == 2 * (5):
            with open(name[w] + "/" + name[w] + ".csv", "a", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(ev)
            with open(name[w] + "/" + name[w] + "_step"".csv", "a", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(ev_step2)

    df1 = pd.read_csv(name[w] + "/" + name[w] + ".csv", header=None, engine = "python")
    df2 = pd.read_csv(name[w] + "/" + name[w] + "_step"".csv", header=None, engine = "python")
    df1 = df1.T
    df2 = df2.T
    df1.to_csv(name[w] + "/" + name[w] + ".csv", header=None, index = False)
    df2.to_csv(name[w] + "/" + name[w] + "_step"".csv", header=None, index = False)
    csv_counter = 0