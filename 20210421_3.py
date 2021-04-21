import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd

# 定義
##################################################################################################################################################
file_1 = ["sma_1", "wma_1", "ewa_1"]
file_2 = ["sma_2", "wma_2", "ewa_2"]
file_number = 2

# 検定
##################################################################################################################################################
##################################################################################################################################################
def kentei():
    df_1 = pd.read_csv("output/" + file_1[file_number] + ".csv", header=None)
    df_2 = pd.read_csv("output/" + file_2[file_number] + ".csv", header=None)

    data_1 = []
    data_2 = []
    for i in range(3):
        data_1 += [df_1.iloc[0, i]]
        data_2 += [df_2.iloc[0, i]]
    print(file_1[file_number])
    print(data_1)
    print(data_2)

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

kentei()