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
    for a in range(8):
        print(name[a])
        fig = plt.figure()
        for b in range(8):
            file_FRR = "5xyz_Authentication/" + name[a] + "/" + name[b] + "_FRR.csv"
            file_FAR = "5xyz_Authentication/" + name[a] + "/" + name[b] + "_FAR.csv"

            if a == b:
                df_FRR = pd.read_csv(file_FRR, header=None, engine = "python")
                for c in range(len(df_FRR.columns)):
                    x.append(c*0.01)
                plt.plot(x, df_FRR.values[len(df_FRR) - 1], label = label_list[b], color = color_list[b])
                x.clear()
            else:
                df_FAR = pd.read_csv(file_FAR, header=None, engine = "python")
                for c in range(len(df_FAR.columns)):
                    x.append(c*0.01)
                plt.plot(x, df_FAR.values[len(df_FAR) - 1], label = label_list[b], color = color_list[b])
                x.clear()
        plt.legend()
        plt.grid()
        # plt.show()
        fig.savefig("graph_Authentication/" + name[a] + "/" + label_list[a] + "_5xyz.png")
        plt.close()

Authentication_graph()