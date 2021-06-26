import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]
label_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
color_list =["r", "b", "g", "c", "m", "y", "k", '#f781bf']
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x = [x1, x2, x3, x4, x5, x6, x7, x8]

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y = [y1, y2, y3, y4, y5, y6, y7, y8]

# Euclid(ユークリッド距離)_graph
##################################################################################################################################################
##################################################################################################################################################
def Euclid_graph():
    for a in range(8):
        for z in range(4):
            print(name[a])

            fig = plt.figure()

            # file_sum = "Euclid/sum_Euclid/" + name[a] + "/" + name[a] + "_Euclid_" +str(z + 2) + ".csv"
            file_mean = "Euclid/y_z_Euclid/" + name[a] + "/" + name[a] + "_Euclid_" +str(z + 2) + ".csv"

            # df_sum = pd .read_csv(file_sum, header=None, engine = "python")
            df_mean = pd.read_csv(file_mean, header=None, engine = "python")

            df_mean_row = sorted(df_mean.values[a])
            df_mean_row = [x for x in df_mean_row if math.isnan(x) == False]

            for b in range(len(df_mean_row)):
                if b == 0:
                    x[a].append(df_mean_row[b])
                    y[a].append(1)
                elif 1 <= b and df_mean_row[b] != x[a][len(x[a]) - 1]:
                    x[a].append(df_mean_row[b])
                    y[a].append(1)

            plt.bar(x[a], y[a], label = label_list[a], width = 1, color = color_list[a])
            
            df_mean_row = df_mean.values[8]
            df_mean_row = [x for x in df_mean_row if math.isnan(x) == False]

            for b in range(len(df_mean_row)):
                if b != a:
                    x[b].append(df_mean_row[b])
                    y[b].append(1)
                    plt.bar(x[b], y[b], label = label_list[b], width = 1, color = color_list[b])

            plt.yticks([])
            plt.xlim(0, 200)
            plt.legend()
            # plt.show()
            fig.savefig("graph_Euclid/y_z_Euclid/" + name[a] + "/" + label_list[a] + "_" +  name[a] + "_yz_" + str(z + 2) + ".png")
            plt.close()

            for b in range(8):
                x[b].clear()
                y[b].clear()

Euclid_graph()