import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]

# 検定_極値
##################################################################################################################################################
##################################################################################################################################################
def kentei_train():
    for a in range(8):
        print(name[a])
        file1 = "5_row/data/" + name[a] + "/" + name[a] + "_5_row.csv"
        file2 = "5_row/step/" + name[a] + "/" + name[a] + "_5_row.csv"
        df1 = pd.read_csv(file1, header=None, engine = "python")
        df2 = pd.read_csv(file2, header=None, engine = "python")

        mean_ev = []
        mean_step = []
        var_ev = []
        var_step = []

        for i in range(len(df1)):
            mean_ev.append(np.mean(df1.values[i]))
            var_ev.append(np.var(df1.values[i], ddof = 1))
        for i in range(len(df2)):
            mean_step.append(np.mean(df2.values[i]))
            var_step.append(np.var(df2.values[i], ddof = 1))

        # print(mean_ev)
        # print(var_ev)
        # print(mean_step)
        # print(var_step)
        # print("\n")

        with open("train_data_5/data/" + name[a] + "/" + name[a] + "_train_5.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(mean_ev)
            writer.writerow(var_ev)
        with open("train_data_5/step/" + name[a] + "/" + name[a] + "_train_5.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(mean_step)
            writer.writerow(var_step)

        mean_ev.clear()
        var_ev.clear()
        mean_step.clear()
        var_step.clear()

kentei_train()