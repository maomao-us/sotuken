import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]
file_number = 1

# 検定
##################################################################################################################################################
##################################################################################################################################################
def kentei():
    count = 0
    for a in range(8):
        print(name[a])
        print("\n")
        for b in range(4):
            print(lx[b])
            for c in range(8):
                # print(name[c])
                file_name1 = "step2/" + name[a] + "/" + name[a] + "_step" + lx[b] + ".csv"
                file_name2 = "step2/" + name[c] + "/" + name[c] + "_step" + lx[b] + ".csv"
                df1 = pd.read_csv(file_name1, header=None, engine = "python")
                df2 = pd.read_csv(file_name2, header=None, engine = "python")
                # print(len(df1))

                result_T = []
                yuuisa_T_0025 = []
                yuuisa_T_0005 = []

                for i in range(len(df1)):
                    data1 = df1.values[i]
                    data2 = df2.values[i]

                    mean1 = np.mean(data1)
                    mean2 = np.mean(data2)
                    std1 = np.var(data1, ddof = 1)
                    std2 = np.var(data2, ddof = 1)
                    # print("data1_mean : ", mean1)
                    # print("data2_mean : ", mean2)
                    # print("data1_std : ", std1)
                    # print("data2_std : ", std2)

                    std = ((len(data1) - 1)*(std1) + (len(data2) - 1)*(std2)) / (len(data1) + len(data2) - 2)
                    # print("Total_std : ", std)

                    T = (mean1 - mean2) / (((1/len(data1)) + (1/len(data2)))*std)**(1/2)
                    # print("T 検定統計量 : ", T)

                    result_T.append(T)

                    if T < -2.021 or 2.021 < T:
                        yuuisa_T_0025.append(1)
                    else:
                        yuuisa_T_0025.append(0)

                    if T < -2.704 or 2.704 < T:
                        yuuisa_T_0005.append(1)
                    else:
                        yuuisa_T_0005.append(0)
                # print(result_T)
                # print(yuuisa_T_0025)
                # print(yuuisa_T_0005)

                if count == 0:
                    with open("kentei_T_step/" + name[a] + "/" + name[a] + "_kentei_step_" + lx[b] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(result_T)
                    with open("yuuisa_T_0025_step/" + name[a] + "/" + name[a] + "_T0025_step_" + lx[b] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(yuuisa_T_0025)
                    with open("yuuisa_T_0005_step/" + name[a] + "/" + name[a] + "_T0005_step_" + lx[b] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(yuuisa_T_0005)
                    count += 1
                elif count >= 1:
                    with open("kentei_T_step/" + name[a] + "/" + name[a] + "_kentei_step_" + lx[b] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(result_T)
                    with open("yuuisa_T_0025_step/" + name[a] + "/" + name[a] + "_T0025_step_" + lx[b] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(yuuisa_T_0025)
                    with open("yuuisa_T_0005_step/" + name[a] + "/" + name[a] + "_T0005_step_" + lx[b] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(yuuisa_T_0005)
            count = 0

kentei()