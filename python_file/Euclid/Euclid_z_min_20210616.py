import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2z", "3z", "4z", "5z"]

# Euclid(ユークリッド距離)
##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(8):
        min_Euclid = []
        for z in range(0,4):
            print(name[a])
            file_train_ev = "train_data/data/" + name[a] + "/" + name[a] + "_train_min_" + lx[z] + ".csv"
            file_train_step = "train_data/step/" + name[a] + "/" + name[a] + "_train_min_" + lx[z] + ".csv"

            df_train_ev = pd.read_csv(file_train_ev, header=None, engine = "python")
            df_train_step = pd.read_csv(file_train_step, header=None, engine = "python")

            for b in range(8):
                file_test_ev = "sotuken_data_test/data/" + name[b] + "/" + name[b] + "_test_min_" + lx[z] + ".csv"
                file_test_step = "sotuken_data_test/step/" + name[b] + "/" + name[b] + "_test_min_" + lx[z] + ".csv"

                df_test_ev = pd.read_csv(file_test_ev, header=None, engine = "python")
                df_test_step = pd.read_csv(file_test_step, header=None, engine = "python")

                data_Euclid_ev = []
                data_Euclid_step = []
                data_Euclid = []
                sum = 0

                for c in range(len(df_test_ev)):
                    for d in range(len(df_test_ev.columns)):
                        sum += (df_test_ev.values[c, d] - df_train_ev.values[0, d])**2 / df_train_ev.values[1, d]
                    # sum = sum**(0.5)
                    sum = int(sum)
                    data_Euclid_ev.append(sum)
                    sum = 0

                for c in range(len(df_test_step)):
                    for d in range(len(df_test_step.columns)):
                        sum += (df_test_step.values[c, d] - df_train_step.values[0, d])**2 / df_train_step.values[1, d]
                    # sum = sum**(0.5)
                    sum = int(sum)
                    data_Euclid_step.append(sum)
                    sum = 0

                for c in range(len(data_Euclid_ev)):
                    data_Euclid.append(data_Euclid_ev[c] + data_Euclid_step[c])

                min_Euclid.append(min(data_Euclid))

                if b == 0:
                    with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid_ev)
                    with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid_step)
                    with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid)
                else:
                    with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid_ev)
                    with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid_step)
                    with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid)
            # df1 = pd.read_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv", header=None, engine = "python")
            # df2 = pd.read_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv", header=None, engine = "python")

            # df1 = df1.T
            # df2 = df2.T

            # df1.to_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv", header=None, index = False)
            # df2.to_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv", header=None, index = False)

            with open("Euclid/min/" + name[a] + "/" + name[a] + "_Euclid_" + lx[z] + ".csv", "a", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(min_Euclid)
            
            min_Euclid.clear()
Euclid()