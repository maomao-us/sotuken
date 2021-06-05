import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["takenaka", "nakajima"]

# 検定
##################################################################################################################################################
##################################################################################################################################################
def kentei():
    file_name1 = "nakajima/nakajima_step.csv"
    file_name2 = "takenaka/takenaka_step.csv"
    df1 = pd.read_csv(file_name1, header=None, engine = "python")
    df2 = pd.read_csv(file_name2, header=None, engine = "python")
    result_T = []
    yuuisa_T_0025 = []
    yuuisa_T_0005 = []
    for i in range(len(df1)):
        data1 = df1.values[i]
        data2 = df2.values[i]
        mean1 = np.mean(data1)
        mean2 = np.mean(data2)
        std1 = np.var(data1, ddof = 1)
        std2 = np.var(data2, ddof = 1)

        std = ((len(data1) - 1)*(std1) + (len(data2) - 1)*(std2)) / (len(data1) + len(data2) - 2)
        T = (mean1 - mean2) / (((1/len(data1)) + (1/len(data2)))*std)**(1/2)
        result_T.append(T)
        if T < -2.306 or 2.306 < T:
            yuuisa_T_0025.append(1)
        else:
            yuuisa_T_0025.append(0)
        if T < -3.355 or 3.355 < T:
            yuuisa_T_0005.append(1)
        else:
            yuuisa_T_0005.append(0)
    print(result_T)
    print(yuuisa_T_0025)
    print(yuuisa_T_0005)

kentei()