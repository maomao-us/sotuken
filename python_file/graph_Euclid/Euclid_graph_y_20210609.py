import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2y", "3y", "4y", "5y"]
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
# Euclid(ユークリッド距離)_graph_ev
##################################################################################################################################################
##################################################################################################################################################
def Euclid_graph_ev():
    for a in range(8):
        for z in range(4):
            fig = plt.figure()
            file = "Euclid/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv"
            df = pd .read_csv(file, header=None, engine = "python")

            for b in range(len(df)):
                print(name[b])
                df_row = sorted(df.values[b])
                print(df_row)
                count = 0
                for c in range(len(df.columns)):
                    if c == 0:
                        x[b].append(df_row[c])
                        count += 1
                    elif 1 <= c and df_row[c] == x[b][len(x[b]) - 1]:
                        count += 1
                    elif 1 <= c and df_row[c] != x[b][len(x[b]) - 1]:
                        x[b].append(df_row[c])
                        y[b].append(count)
                        count = 1
                y[b].append(count)
                print(x[b])
                print(y[b])
                plt.bar(x[b], y[b], label = label_list[b], width = 1, color = color_list[b])
            plt.legend()
            plt.show()
            # fig.savefig("graph_Euclid/ev/" + label_list[a] + "_" +  name[a] + "_Euclid_ev.png")

            for b in range(8):
                x[b].clear()
                y[b].clear()

# Euclid(ユークリッド距離)_graph_step
##################################################################################################################################################
##################################################################################################################################################
def Euclid_graph_step():
    for a in range(8):
        for z in range(4):
            fig = plt.figure()
            file = "Euclid/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv"
            df = pd .read_csv(file, header=None, engine = "python")

            for b in range(len(df)):
                print(name[b])
                df_row = sorted(df.values[b])
                print(df_row)
                count = 0
                for c in range(len(df.columns)):
                    if c == 0:
                        x[b].append(df_row[c])
                        count += 1
                    elif 1 <= c and df_row[c] == x[b][len(x[b]) - 1]:
                        count += 1
                    elif 1 <= c and df_row[c] != x[b][len(x[b]) - 1]:
                        x[b].append(df_row[c])
                        y[b].append(count)
                        count = 1
                y[b].append(count)
                print(x[b])
                print(y[b])
                plt.bar(x[b], y[b], label = label_list[b], width = 1, color = color_list[b])
            plt.legend()
            plt.show()
            # fig.savefig("graph_Euclid/step/" + label_list[a] + "_" +  name[a] + "_Euclid_step.png")

            for b in range(8):
                x[b].clear()
                y[b].clear()

# Euclid(ユークリッド距離)_graph
##################################################################################################################################################
##################################################################################################################################################
def Euclid_graph():
    for a in range(8):
        for z in range(4):
            print(name[a])
            fig = plt.figure()
            file = "Euclid/Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + lx[z] + ".csv"
            df = pd.read_csv(file, header=None, engine = "python")

            df_row = sorted(df.values[a])
            df_row = [x for x in df_row if math.isnan(x) == False]
            for b in range(len(df_row)):
                if b == 0:
                    x[a].append(df_row[b])
                    y[a].append(1)
                elif 1 <= b and df_row[b] != x[a][len(x[a]) - 1]:
                    x[a].append(df_row[b])
                    y[a].append(1)
            plt.bar(x[a], y[a], label = label_list[a], width = 1, color = color_list[a])
            
            df_row = df.values[8]
            df_row = [x for x in df_row if math.isnan(x) == False]
            # print(df_row)
            for b in range(len(df_row)):
                if b != a:
                    x[b].append(df_row[b])
                    y[b].append(1)
                    plt.bar(x[b], y[b], label = label_list[b], width = 1, color = color_list[b])



            # for b in range(len(df)):
            #     print(name[b])
            #     df_row = sorted(df.values[b])
            #     print(df_row)
            #     count = 0
            #     for c in range(len(df.columns)):
            #         if c == 0:
            #             x[b].append(df_row[c])
            #             count += 1
            #         elif 1 <= c and df_row[c] == x[b][len(x[b]) - 1]:
            #             count += 1
            #         elif 1 <= c and df_row[c] != x[b][len(x[b]) - 1]:
            #             x[b].append(df_row[c])
            #             y[b].append(count)
            #             count = 1
            #     y[b].append(count)
            #     print(x[b])
            #     print(y[b])
            #     plt.bar(x[b], y[b], label = label_list[b], width = 1, color = color_list[b])
            plt.yticks([])
            plt.xlim(0, 200)
            plt.legend()
            # plt.show()
            fig.savefig("graph_Euclid/Euclid/" + name[a] + "/" + label_list[a] + "_" +  name[a] + "_" + lx[z] + ".png")
            plt.close()

            for b in range(8):
                x[b].clear()
                y[b].clear()

# Euclid_graph_ev()
# Euclid_graph_step()
Euclid_graph()
