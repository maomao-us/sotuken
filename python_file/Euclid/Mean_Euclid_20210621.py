import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]
ly = ["2y", "3y", "4y", "5y"]
lz = ["2z", "3z", "4z", "5z"]

# Euclid(ユークリッド距離)
##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(8):
        min_Euclid = []
        for z in range(4):
            print(name[a])
            file_x = "Euclid/Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + lx[z] + ".csv"
            file_y = "Euclid/Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + ly[z] + ".csv"
            file_z = "Euclid/Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + lz[z] + ".csv"

            df_x = pd.read_csv(file_x, header=None, engine = "python")
            df_y = pd.read_csv(file_y, header=None, engine = "python")
            df_z = pd.read_csv(file_z, header=None, engine = "python")

            sum_data = []
            min_data = []

            for b in range(len(df_x) - 1):
                for c in range(len(df_x.columns)):
                    # print(c + 1, "回目")
                    # print(int((df_x.values[b, c])))
                    # print(int((df_y.values[b, c])))
                    # print(int((df_z.values[b, c])))
                    # print("\n")
                    sum_data.append(int((df_x.values[b, c] + df_y.values[b, c] + df_z.values[b, c]) / 3))
                
                min_data.append(min(sum_data))

                if b == 0:
                    with open("Euclid/mean_Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + str(z + 2) + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(sum_data)
                
                elif 0 < b:
                    with open("Euclid/mean_Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + str(z + 2) + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(sum_data)
                
                sum_data.clear()
            
            with open("Euclid/mean_Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + str(z + 2) + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(min_data)

Euclid()