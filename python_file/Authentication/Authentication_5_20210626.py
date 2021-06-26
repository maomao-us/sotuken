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
    for a in range(3):
        print(lx[a])
        for b in range(8):
            for c in range(8):
                for d in range(10):
                    file = "Authentication/" + name[b] + "/" + name[c] + "/" + str(d + 1) + "_" + lx[a] + ".csv"
                    df = pd.read_csv(file, engine = "python")
                    df_T = df.T

                    file_FRR = lx[a] + "_Authentication/" + name[b] + "/" + name[c] + "_FRR.csv"
                    file_FAR = lx[a] + "_Authentication/" + name[b] + "/" + name[c] + "_FAR.csv"

                    if b == c:
                        if d == 0:
                            with open(file_FRR, "w", newline = "") as f:
                                writer = csv.writer(f)
                                writer.writerow(df_T.values[len(df_T) - 1])
                        else:
                            with open(file_FRR, "a", newline = "") as f:
                                writer = csv.writer(f)
                                writer.writerow(df_T.values[len(df_T) - 1])

                    else:
                        if d == 0:
                            with open(file_FAR, "w", newline = "") as f:
                                writer = csv.writer(f)
                                writer.writerow(df_T.values[len(df_T) - 1])
                        else:
                            with open(file_FAR, "a", newline = "") as f:
                                writer = csv.writer(f)
                                writer.writerow(df_T.values[len(df_T) - 1])
Authentication()

##################################################################################################################################################
##################################################################################################################################################
def rate():
    for a in range(3):
        print(lx[a])
        for b in range(8):
            for c in range(8):
                data_FRR = []
                data_FAR = []

                file_FRR = lx[a] + "_Authentication/" + name[b] + "/" + name[c] + "_FRR.csv"
                file_FAR = lx[a] + "_Authentication/" + name[b] + "/" + name[c] + "_FAR.csv"

                if b == c:
                    df_FRR = pd.read_csv(file_FRR, header=None, engine = "python")
                    df_FRR_T = df_FRR.T
                    for d in range(len(df_FRR_T)):
                        data_FRR.append(format(1 - np.mean(df_FRR_T.values[d]), ".1f"))
                    with open(file_FRR, "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_FRR)
                    data_FRR.clear()
                else:
                    df_FAR = pd.read_csv(file_FAR, header=None, engine = "python")
                    df_FAR_T = df_FAR.T
                    for d in range(len(df_FAR_T)):
                        data_FAR.append(format(np.mean(df_FAR_T.values[d]), ".1f"))
                    with open(file_FAR, "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_FAR)
                    data_FAR.clear()
rate()