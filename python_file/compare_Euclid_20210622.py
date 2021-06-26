import csv
import numpy as np
import pandas as pd
import math

name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
label = ["5x", "5y", "5z"]

##############################################################################################################
##############################################################################################################
def Euclid_x_y_z():
    for a in range(8):
        for b in range(3):
            file_Euclid = "Euclid/Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + label[b] + ".csv"
            df = pd.read_csv(file_Euclid, header=None, engine = "python")

            df1 = df.values[8]
            df1 = [x for x in df1 if math.isnan(x) == False]

            df_1 = []
            for c in range(8):
                if c != a:
                    df_1.append(df1[c])

            df2 = df.values[a]
            df2 = [x for x in df2 if math.isnan(x) == False]

            

            if b == 0:
                with open("compare/" + name[a] + "/" + name[a] + "_compare.csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df_1)
                with open("compare_same_user/" + name[a] + "/" + name[a] + "_same.csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df2)
            if 0 < b:
                with open("compare/" + name[a] + "/" + name[a] + "_compare.csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df_1)
                with open("compare_same_user/" + name[a] + "/" + name[a] + "_same.csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df2)

##############################################################################################################
##############################################################################################################
def Euclid_xy_xz_yz():
    for a in range(8):
        file_xy = "Euclid/x_y_Euclid/" + name[a] + "/" + name[a] + "_Euclid_5.csv"
        file_xz = "Euclid/x_z_Euclid/" + name[a] + "/" + name[a] + "_Euclid_5.csv"
        file_yz = "Euclid/y_z_Euclid/" + name[a] + "/" + name[a] + "_Euclid_5.csv"

        df_xy = pd.read_csv(file_xy, header=None, engine = "python")
        df_xz = pd.read_csv(file_xz, header=None, engine = "python")
        df_yz = pd.read_csv(file_yz, header=None, engine = "python")

        df1 = df_xy.values[8]
        df1 = [x for x in df1 if math.isnan(x) == False]
        df2 = df_xz.values[8]
        df2 = [x for x in df2 if math.isnan(x) == False]
        df3 = df_yz.values[8]
        df3 = [x for x in df3 if math.isnan(x) == False]

        df_1 = []
        df_2 = []
        df_3 = []
        for b in range(8):
            if b != a:
                df_1.append(df1[b])
                df_2.append(df2[b])
                df_3.append(df3[b])

        df4 = df_xy.values[a]
        df4 = [x for x in df4 if math.isnan(x) == False]
        df5 = df_xz.values[a]
        df5 = [x for x in df5 if math.isnan(x) == False]
        df6 = df_yz.values[a]
        df6 = [x for x in df6 if math.isnan(x) == False]
        

        with open("compare/" + name[a] + "/" + name[a] + "_compare.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(df_1)
            writer.writerow(df_2)
            writer.writerow(df_3)
        with open("compare_same_user/" + name[a] + "/" + name[a] + "_same.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(df4)
            writer.writerow(df5)
            writer.writerow(df6)

##############################################################################################################
##############################################################################################################
def Euclid_xyz():
    for a in range(8):
        file_xyz = "Euclid/mean_Euclid/" + name[a] + "/" + name[a] + "_Euclid_5.csv"
        df_xyz = pd.read_csv(file_xyz, header=None, engine = "python")

        df1 = df_xyz.values[8]
        df1 = [x for x in df1 if math.isnan(x) == False]

        df_1 = []
        for b in range(8):
            if b != a:
                df_1.append(df1[b])

        df2 = df_xyz.values[a]
        df2 = [x for x in df2 if math.isnan(x) == False]

        with open("compare/" + name[a] + "/" + name[a] + "_compare.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(df_1)
        with open("compare_same_user/" + name[a] + "/" + name[a] + "_same.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(df2)

##############################################################################################################
##############################################################################################################
def Euclid_T():
    for a in range(8):
        # df_compare = pd.read_csv("compare/" + name[a] + "/" + name[a] + "_compare.csv", header=None, engine = "python")
        df_same = pd.read_csv("compare_same_user/" + name[a] + "/" + name[a] + "_same.csv", header=None, engine = "python")

        # df_compare = df_compare.T
        df_same = df_same.T

        # df_compare.to_csv("compare/" + name[a] + "/" + name[a] + "_compare.csv", header=None, index = False)
        df_same.to_csv("compare_same_user/" + name[a] + "/" + name[a] + "_same.csv", header=None, index = False)

Euclid_x_y_z()
Euclid_xy_xz_yz()
Euclid_xyz()
Euclid_T()