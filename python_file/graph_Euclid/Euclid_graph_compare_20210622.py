import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
label_list = ["x", "y", "z", "xy", "xz", "yz", "xyz"]
color_list =["r", "b", "g", "c", "m", "y", "k"]
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x = [x1, x2, x3, x4, x5, x6, x7]

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y = [y1, y2, y3, y4, y5, y6, y7]

# Euclid(ユークリッド距離)_graph
##################################################################################################################################################
##################################################################################################################################################
def Euclid_graph():
    for a in range(8):
        print(name[a])

        fig = plt.figure()

        file = "compare/" + name[a] + "/" + name[a] + "_compare.csv"
        df = pd.read_csv(file, header=None, engine = "python")

        for b in range(len(df)):
            df_row = min(df.values[b])
            x[b].append(df_row)
            y[b].append(1)
            plt.bar(x[b], y[b], label = label_list[b], width = 1, color = color_list[b])
        
        plt.yticks([])
        plt.xlim(0, 200)
        plt.legend()
        plt.show()
        # fig.savefig("graph_Euclid/compare/" + name[a] + "/"  + name[a] + "_compare.png")
        plt.close()

        for b in range(len(x)):
            x[b].clear()
            y[b].clear()

Euclid_graph()