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
def T_sum():
    for a in range(8):
        print(name[a])
        for b in range(8):
            for c in range(10):
                for d in range(2):

                    file = "Authentication/" + name[a] + "/" + name[b] + "/" + str(c + 1) + "_" + lx[d] + ".csv"
                    df = pd.read_csv(file, engine = "python")
                    df = df.T

                    if d == 0:
                        with open("xyz_Authentication/"+ name[a] + "/" + name[b] + "/" + str(c + 1) + "_xyz.csv", "w", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df.values[len(df) - 1])
                    else:
                        with open("xyz_Authentication/"+ name[a] + "/" + name[b] + "/" + str(c + 1) + "_xyz.csv", "a", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df.values[len(df) - 1])

T_sum()

##################################################################################################################################################
##################################################################################################################################################
def result():
    for a in range(8):
        print(name[a])
        for b in range(8):
            for c in range(10):
                    file = "xyz_Authentication/"+ name[a] + "/" + name[b] + "/" + str(c + 1) + "_xyz.csv"
                    df = pd.read_csv(file, header=None, engine = "python")
                    df_T = df.T

                    data = []

                    for d in range(len(df_T)):
                        if np.mean(df_T.values[d]) == 1:
                            data.append(1)
                        else:
                            data.append(0)
                    
                    with open("xyz_Authentication/"+ name[a] + "/" + name[b] + "/" + str(c + 1) + "_xyz.csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data)

result()