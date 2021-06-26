import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["5x", "5y", "5z"]
label_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
color_list =["r", "b", "g", "c", "m", "y", "k", '#f781bf']

##################################################################################################################################################
##################################################################################################################################################
def Authentication_graph():
    x = []
    for a in range(3):
        print(lx[a])
        for b in range(8):
            fig = plt.figure()
            for c in range(8):
                file_FRR = lx[a] + "_Authentication/" + name[b] + "/" + name[c] + "_FRR.csv"
                file_FAR = lx[a] + "_Authentication/" + name[b] + "/" + name[c] + "_FAR.csv"

                if b == c:
                    df_FRR = pd.read_csv(file_FRR, header=None, engine = "python")
                    for d in range(len(df_FRR.columns)):
                        x.append(d*0.01)
                    plt.plot(x, df_FRR.values[len(df_FRR) - 1], label = label_list[c], color = color_list[c])
                    x.clear()
                else:
                    df_FAR = pd.read_csv(file_FAR, header=None, engine = "python")
                    for d in range(len(df_FAR.columns)):
                        x.append(d*0.01)
                    plt.plot(x, df_FAR.values[len(df_FAR) - 1], label = label_list[c], color = color_list[c])
                    x.clear()
            plt.legend()
            plt.grid()
            # plt.show()
            fig.savefig("graph_Authentication/" + name[b] + "/" + label_list[b] + "_" + lx[a] + ".png")
            plt.close()

Authentication_graph()