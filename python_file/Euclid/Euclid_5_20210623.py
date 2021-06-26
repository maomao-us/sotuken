import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]

# Euclid(ユークリッド距離)
##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(8):
        min_Euclid = []
        print(name[a])

        file_train_ev = "train_data_5/data/" + name[a] + "/" + name[a] + "_train_5.csv"
        file_train_step = "train_data_5/step/" + name[a] + "/" + name[a] + "_train_5.csv"
        df_train_ev = pd.read_csv(file_train_ev, header=None, engine = "python")
        df_train_step = pd.read_csv(file_train_step, header=None, engine = "python")

        for b in range(8):
            file_test_ev = "5_data/data/" + name[b] + "/" + name[b] + "_ev5x.csv"
            file_test_step = "5_data/step/" + name[b] + "/" + name[b] + "_step5x.csv"
            df_test_ev = pd.read_csv(file_test_ev, header=None, engine = "python")
            df_test_step = pd.read_csv(file_test_step, header=None, engine = "python")

            data_Euclid_ev = []
            data_Euclid_step = []
            data_Euclid = []
            sum = 0
            

            for c in range(len(df_test_ev)):
                for d in range(len(df_test_ev.columns)):
                    sum += (df_test_ev.values[c, d] - df_train_ev.values[0, d])**2 / df_train_ev.values[1, d]
                sum = int(sum)
                data_Euclid_ev.append(sum)
                sum = 0

            for c in range(len(df_test_step)):
                for d in range(len(df_test_step.columns)):
                    sum += (df_test_step.values[c, d] - df_train_step.values[0, d])**2 / (df_train_step.values[1, d] + 0.1)
                sum = int(sum)
                data_Euclid_step.append(sum)
                sum = 0

            for c in range(len(data_Euclid_ev)):
                data_Euclid.append(data_Euclid_ev[c] + data_Euclid_step[c])
            
            min_Euclid.append(min(data_Euclid))

            if b == 0:
                with open("Euclid/Euclid_5/" + name[a] + "/" + name[a] + "_Euclid_5.csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(data_Euclid)

            else:
                with open("Euclid/Euclid_5/" + name[a] + "/" + name[a] + "_Euclid_5.csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(data_Euclid)
    
        with open("Euclid/Euclid_5/" + name[a] + "/" + name[a] + "_Euclid_5.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(min_Euclid)
        
        min_Euclid.clear()
        data_Euclid_ev.clear()
        data_Euclid_step.clear()
        data_Euclid.clear()
Euclid()