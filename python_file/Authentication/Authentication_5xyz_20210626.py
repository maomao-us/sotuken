import csv
import math
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["5x", "5y", "5z"]

##################################################################################################################################################
##################################################################################################################################################
def Authentication():
    for a in range(8):
        print(name[a])
        for b in range(8):
            for d in range(10):
                file = "xyz_Authentication/" + name[a] + "/" + name[b] + "/" + str(d + 1) + "_xyz.csv"
                df = pd.read_csv(file, engine = "python")

                file_FRR = "5xyz_Authentication" + "/" + name[a] + "/" + name[b] + "_FRR.csv"
                file_FAR = "5xyz_Authentication" + "/" + name[a] + "/" + name[b] + "_FAR.csv"

                if a == b:
                    if d == 0:
                        with open(file_FRR, "w", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df.values[len(df) - 1])
                    else:
                        with open(file_FRR, "a", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df.values[len(df) - 1])
                
                else:
                    if d == 0:
                        with open(file_FAR, "w", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df.values[len(df) - 1])
                    else:
                        with open(file_FAR, "a", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df.values[len(df) - 1])
Authentication()

##################################################################################################################################################
##################################################################################################################################################
def rate():
    for a in range(8):
        print(name[a])
        for b in range(8):
                data_FRR = []
                data_FAR = []

                file_FRR = "5xyz_Authentication" + "/" + name[a] + "/" + name[b] + "_FRR.csv"
                file_FAR = "5xyz_Authentication" + "/" + name[a] + "/" + name[b] + "_FAR.csv"

                if a == b:
                    df_FRR = pd.read_csv(file_FRR, header=None, engine = "python")
                    df_FRR_T = df_FRR.T
                    for c in range(len(df_FRR_T)):
                        data_FRR.append(format(1 - np.mean(df_FRR_T.values[c]), ".1f"))
                    with open(file_FRR, "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_FRR)
                    data_FRR.clear()
                else:
                    df_FAR = pd.read_csv(file_FAR, header=None, engine = "python")
                    df_FAR_T = df_FAR.T
                    for c in range(len(df_FAR_T)):
                        data_FAR.append(format(np.mean(df_FAR_T.values[c]), ".1f"))
                    with open(file_FAR, "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_FAR)
                    data_FAR.clear()

rate()