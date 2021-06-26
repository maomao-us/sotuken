import csv
import math
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["5x", "5y", "5z"]
top = ["E1", "E2", "E3", "E4", "S5", "E6", "E7", "E8", "E9", "E10", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S"]


##################################################################################################################################################
##################################################################################################################################################
def Authentication():
    for a in range(8):
        print(name[a])
        print("\n")
        for b in range(8):
            print(name[b])
            for c in range(3):
                print(lx[c])
                train_ev = "train_data/data/" + name[a] + "/" + name[a] + "_train_" + lx[c] + ".csv"
                train_step = "train_data/step/" + name[a] + "/" + name[a] + "_train_" + lx[c] + ".csv"
                test_ev = "sotuken_data_test/data/" + name[b] + "/" + name[b] + "_test_" + lx[c] + ".csv"
                test_step = "sotuken_data_test/step/" + name[b] + "/" + name[b] + "_test_" + lx[c] + ".csv"

                df_train_ev = pd.read_csv(train_ev, header=None, engine = "python")
                df_train_step = pd.read_csv(train_step, header=None, engine = "python")
                df_test_ev = pd.read_csv(test_ev, header=None, engine = "python")
                df_test_step = pd.read_csv(test_step, header=None, engine = "python")

                data = []

                for d in range(len(df_test_ev)):
                    for e in range(0, 201):
                        for f in range(len(df_test_ev.columns)):
                            if df_train_ev.values[0, f] - (e*0.01) * math.sqrt(df_train_ev.values[1, f]) < df_test_ev.values[d, f] <  df_train_ev.values[0, f] + (e*0.01) * math.sqrt(df_train_ev.values[1, f]):
                                data.append(1)
                            else:
                                data.append(0)
                        
                        for f in range(len(df_test_step.columns)):
                            if df_train_step.values[0, f] - (e*0.01) * math.sqrt(df_train_step.values[1, f]) < df_test_step.values[d, f] <  df_train_step.values[0, f] + (e*0.01) * math.sqrt(df_train_step.values[1, f]):
                                data.append(1)
                            else:
                                data.append(0)

                        if 0.5 <= np.mean(data):
                            data.append(1)
                        else:
                            data.append(0)

                        if e == 0:
                            with open("Authentication/" + name[a] + "/" + name[b] + "/" + str(d + 1) + "_" + lx[c] + ".csv", "w", newline = "") as f:
                                writer = csv.writer(f)
                                writer.writerow(top)
                                writer.writerow(data)
                        else:
                            with open("Authentication/" + name[a] + "/" + name[b] + "/" + str(d + 1) + "_" + lx[c] + ".csv", "a", newline = "") as f:
                                writer = csv.writer(f)
                                writer.writerow(data)

                        data.clear()

Authentication()