import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
file_name = "yamanada_ev5abs"

# csv のヘッダー
##################################################################################################################################################
with open("kentei_data/yamanada_5/yamanada_kentei5abs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["m", "n", "times", "F"])

# 検定
##################################################################################################################################################
##################################################################################################################################################
def kentei():
    col_names = ['c{0:02d}'.format(i) for i in range(100)]
    df = pd.read_csv("sotuken_data/yamanada_5/" + file_name + ".csv", header=None, names = col_names)

    data1 = []
    data2 = []

    for i in range(20):
        with open("kentei_data/yamanada_5/yamanada_kentei5abs.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([i + 1, "行", "目"])
        for j in range(len(df.columns)):
            data1 += [df.iloc[i, j]]
        data1 = np.array(data1)
        data1 = [x for x in data1 if np.isnan(x) == False]
        print(i + 1, "行目")
        print(data1)
        print("\n")

        for k in range(20):
            for l in range(len(df.columns)):
                data2 += [df.iloc[k, l]]
            data2 = np.array(data2)
            data2 = [x for x in data2 if np.isnan(x) == False]
            print(data2)

            mean_data1 = np.mean(data1)
            mean_data2 = np.mean(data2)
            std_data1 = np.var(data1, ddof = 1)
            std_data2 = np.var(data2, ddof = 1)

            print("data1_mean : ", mean_data1)
            print("data2_mean : ", mean_data2)
            print("data1_std : ", std_data1)
            print("data2_std : ", std_data2)

            std = ((len(data1) - 1)*(std_data1) + (len(data2) - 1)*(std_data2)) / (len(data1) + len(data2) - 2)
            print("Total_std : ", std)

            T = (mean_data1 - mean_data2) / (((1/len(data1)) + (1/len(data2)))*std)**(1/2)
            print("T 検定統計量 : ", T)

            with open("kentei_data/yamanada_5/yamanada_kentei5abs.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([len(data1), len(data2), k + 1,T])

            # data2 = data2.tolist()
            data2.clear()
            print("\n")
        # data1 = data1.tolist()
        data1.clear()

kentei()