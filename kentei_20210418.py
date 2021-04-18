import csv
# from operator import le
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.nanfunctions import _nanprod_dispatcher
# import pprint
import pandas as pd
from scipy import signal
from sklearn import preprocessing

# 定義
##################################################################################################################################################
file_hiromu = ["hiromu_x", "hiromu_y", "hiromu_z", "hiromu_abs"]
file_kouhai = ["kouhai_x", "kouhai_y", "kouhai_z", "kouhai_abs"]
csv_name = ["kentei_x", "kentei_y", "kentei_z", "kentei_abs"]
file_number = 1


# csv のヘッダー
##################################################################################################################################################
with open("output_kentei/" + csv_name[file_number] + ".csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["hiromu_m", "kouhai_n", "T", "F"])

# 検定
##################################################################################################################################################
##################################################################################################################################################
def kentei():
    df_hiromu = pd.read_csv("output/" + file_hiromu[file_number] + ".csv", header=None)
    df_kouhai = pd.read_csv("output/" + file_kouhai[file_number] + ".csv", header=None)

    hiromu = []
    kouhai = []
    z = 1
    for i in range(len(df_hiromu)):
        for j in range(len(df_hiromu.columns)):
            hiromu += [df_hiromu.iloc[i, j]]
        hiromu = np.array(hiromu)
        hiromu = -hiromu
        hiromu = [x for x in hiromu if np.isnan(x) == False]

        for k in range(len(df_kouhai)):
            for l in range(len(df_kouhai.columns)):
                kouhai += [df_kouhai.iloc[k, l]]
            kouhai = np.array(kouhai)
            kouhai = -kouhai
            kouhai = [x for x in kouhai if np.isnan(x) == False]
            print(z, "回目")
            z += 1
            print(hiromu)
            print(kouhai)

            mean_hiromu = np.mean(hiromu)
            mean_kouhai = np.mean(kouhai)
            std_hiromu = np.var(hiromu, ddof = 1)
            std_kouhai = np.var(kouhai, ddof = 1)

            print("hiromu_mean : ", mean_hiromu)
            print("kouhai_mean : ", mean_kouhai)
            print("hiromu_std : ", std_hiromu)
            print("kouhai_std : ", std_kouhai)

            std = ((len(hiromu) - 1)*(std_hiromu) + (len(kouhai) - 1)*(std_kouhai)) / (len(hiromu) + len(kouhai) - 2)
            print("Total_std : ", std)

            T = (mean_hiromu - mean_kouhai) / (((1/len(hiromu)) + (1/len(kouhai)))*std)**(1/2)
            print("T 検定統計量 : ", T)

            F = std_hiromu / std_kouhai
            print("F 検定統計量 : ", F)

            with open("output_kentei/" + csv_name[file_number] + ".csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([len(hiromu), len(kouhai), T, F])

            # kouhai = kouhai.tolist()
            kouhai.clear()
            print("\n")
        
        # hiromu = hiromu.tolist()
        hiromu.clear()

kentei()