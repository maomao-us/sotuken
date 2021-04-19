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
file_name = ["output_kentei/kentei_x.csv", "output_kentei/kentei_y.csv", "output_kentei/kentei_z.csv", "output_kentei/kentei_abs.csv", ]
output_name = ["evaluation_x.csv", "evaluation_y.csv", "evaluation_z.csv", "evaluation_abs.csv"]
file_number = 1


# csv のヘッダー
##################################################################################################################################################
with open("evaluation_kentei/" + output_name[file_number], "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "T", "0.05", "0.05_True(1)_False(0)?", "0.01", "0.01_True(1)_False(0)?", "F", "F_OK_NO?"])

# 検定
##################################################################################################################################################
##################################################################################################################################################
def evaluation_kentei():
    df = pd.read_csv(file_name[file_number])

    kentei = []
    z = 1
    for i in range(len(df)):
        for j in range(len(df.columns)):
            kentei += [df.iloc[i, j]]
        print(z, "回目")
        z += 1
        print(kentei)
        if kentei[0] + kentei[1] - 2 == 6:
            if kentei[2] > 2.447 or kentei[2] < -2.447:
                kentei.append(1)
            else:
                kentei.append(0)

            if kentei[2] > 3.707 or kentei[2] < -3.707:
                kentei.append(1)
            else:
                kentei.append(0)

            if 1/10.649 < kentei[3] < 10.649:
                kentei.append(1)
            else:
                kentei.append(0)

            with open("evaluation_kentei/" + output_name[file_number], "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([kentei[0] + kentei[1] - 2, kentei[2], 2.447, kentei[4], 3.07, kentei[5], kentei[3], kentei[6]])
        
        if kentei[0] + kentei[1] - 2 == 4:
            if kentei[2] > 2.776 or kentei[2] < -2.776:
                kentei.append(1)
            else:
                kentei.append(0)
        
            if kentei[2] > 4.604 or kentei[2] < -4.604:
                kentei.append(1)
            else:
                kentei.append(0)

            if 1/39 < kentei[3] < 39:
                kentei.append(1)
            else:
                kentei.append(0)

            with open("evaluation_kentei/" + output_name[file_number], "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([kentei[0] + kentei[1] - 2, kentei[2], 2.776, kentei[4], 4.604, kentei[5], kentei[3], kentei[6]])
        kentei.clear()
        print("\n")

evaluation_kentei()