import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd

# 定義
##################################################################################################################################################
file_1 = ["sma_x1", "sma_y1", "sma_z1", "sma_abs1", "wma_x1", "wma_y1", "wma_z1", "wma_abs1", "ewa_x1", "ewa_y1", "ewa_z1", "ewa_abs1"]
file_2 = ["sma_x2", "sma_y2", "sma_z2", "sma_abs2", "wma_x2", "wma_y2", "wma_z2", "wma_abs2", "ewa_x2", "ewa_y2", "ewa_z2", "ewa_abs2"]
file_number = 0

# 検定
##################################################################################################################################################
##################################################################################################################################################
def kentei():
    kentei = []
    for z in range(8,12):
        df_1 = pd.read_csv("output2/" + file_1[z] + ".csv", header=None)
        df_2 = pd.read_csv("output2/" + file_2[z] + ".csv", header=None)

        data_1 = []
        data_2 = []
        for i in range(len(df_1.columns)):
            data_1 += [df_1.iloc[0, i]]
        for i in range(len(df_2.columns)):
            data_2 += [df_2.iloc[0, i]]
        print(file_1[z])
        print(data_1)
        print(data_2)
        # print(len(data_1))

        mean_data_1 = np.mean(data_1)
        mean_data_2 = np.mean(data_2)
        std_data_1 = np.var(data_1, ddof = 1)
        std_data_2 = np.var(data_2, ddof = 1)
        print("data_1_mean : ", mean_data_1)
        print("data_2_mean : ", mean_data_2)
        print("data_1_std : ", std_data_1)
        print("data_2_std : ", std_data_2)

        std = ((len(data_1) - 1)*(std_data_1) + (len(data_2) - 1)*(std_data_2)) / (len(data_1) + len(data_2) - 2)
        print("Total_std : ", std)

        T = (mean_data_1 - mean_data_2) / (((1/len(data_1)) + (1/len(data_2)))*std)**(1/2)
        print("T 検定統計量 : ", T)
        print("\n")
        kentei.append(T)
        data_1.clear()
        data_2.clear()
    
    print(kentei)
    with open("output3/kentei.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(kentei)

kentei()
print()