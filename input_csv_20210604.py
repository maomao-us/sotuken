import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

label = ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
lx = ["2x", "3x", "4x", "5x"]
ly = ["2y", "3y", "4y", "5y"]
lz = ["2z", "3z", "4z", "5z"]
labs = ["2abs", "3abs", "4abs", "5abs"]
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
window = 5

sampling_number1 = 30
sampling_number2 = sampling_number1 + 1
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
def MIN_EV(d, e, f):
    ev = []
    list = []
    step_list1 = []
    step_list2 = []


    # 前後20個のデータを格納
    for i in range(200, len(data) - sampling_number2):
        for j in range(i - sampling_number1, i + sampling_number2):
            list.append(data[j])

        # バブルソート
        for j in range(len(list)):
            for k in range(len(list) - 1, j, -1):
                if list[k] < list[k - 1]:
                    list[k], list[k - 1] =  list[k - 1], list[k]

        if list[0] == data[i] and -d > data[i] and len(ev) % 2 == 0:
            ev.append(data[i])
            step_list1.append(step[i])

        elif (list[len(list) - 1] == data[i] and e < data[i]) and len(ev) % 2 == 1:
            ev.append(data[i])
            step_list1.append(step[i])

        list.clear()
        if len(ev) == 2 * f:
            break

    for i in range(len(step_list1) - 1):
        step_list2.append(step_list1[i + 1] - step_list1[i])

    ev = np.array(ev)
    if len(ev) > 1:
        print(len(ev), "個")
        print(ev)
        print(step_list2)
    return ev, step_list2

##################################################################################################################################################
for w in range(len(name)):
    print(name[w])
    for z in range(4):
        print(z + 2, "スイング")
        for i in range(10, 30):
            file_name = name[w] + "_" + str(i)
            print(file_name)

            df = pd.read_csv("oltana/" + name[w] + "_" + str(z + 2) + "/" + file_name + ".csv")
            data = df[label[0]].rolling(window, min_periods=1).apply(WMA)
            for h in range(5 - 1):
                data = data.rolling(window, min_periods=1).apply(WMA)
            data = np.array(data)

            step = []
            for h in range(len(data)):
                step.append(h + 1)
            step = np.array(step)

            ev, ev_step = MIN_EV(6, 15, z + 2)

            # if len(ev) <= 1:
            #     ev, ev_step = MIN_EV(2, 6)

            if csv_counter == 0 and len(ev) > 1:
                with open("sotuken_data/" + name[w] + "/" + name[w] + "_ev" + lx[z] + ".csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(ev)
                with open("step/" + name[w] + "/" + name[w] + "_step" + lx[z] + ".csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(ev_step)
            elif csv_counter >= 1 and len(ev) > 1:
                with open("sotuken_data/" + name[w] + "/" + name[w] + "_ev" + lx[z] + ".csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(ev)
                with open("step/" + name[w] + "/" + name[w] + "_step" + lx[z] + ".csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(ev_step)

            csv_counter += 1
        csv_counter = 0

# print("\n")
# col_names = ['c{0:02d}'.format(i) for i in range(20)]
# for w in range(len(name)):
#     print(name[w])
#     for c in range(2, 6):
#         print(c, "スイング")
#         for z in range(4):
#             df = pd.read_csv("sotuken_data/" + name[w] + "/" + name[w] + "_ev" + lx[z] + ".csv", header=None, names = col_names, engine = "python")
#             print(len(df))
