import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]

# 検定_極値
##################################################################################################################################################
##################################################################################################################################################


def kentei():
    T_list = []
    data = []
    count = 0
    i = 0
    for a in range(8):
        print(name[a])
        file_step = "step2/" + name[a] + "/" + name[a] + "_step5x.csv"
        file = "sotuken_data/" + name[a] + "/" + name[a] + "_ev5x.csv"
        df = pd.read_csv(file, header=None, engine = "python")

        for b in range(len(df)):
            for c in range(len(df)):
                for d in range(len(df.columns)):
                    data.append(df.values[b, d] - df.values[c, d])
                
                mean = np.mean(data)
                var = np.var(data, ddof = 1)

                T = mean / (var / len(data))**0.5

                if T < -1.812 or 1.812 < T:
                    count += 1
                data.clear()
            T_list.append(count)
            count = 0
        
        print(T_list)
        while(1):
            print(i + 1)
            file_step1 = "5_data/step/" + name[a] + "/" + name[a] + "_step5x.csv"
            file_step2 = "5_row/step/" + name[a] + "/" + name[a] + "_5_row.csv"
            file1 = "5_data/data/" + name[a] + "/" + name[a] + "_ev5x.csv"
            file2 = "5_row/data/" + name[a] + "/" + name[a] + "_5_row.csv"
            min_data = T_list.index(min(T_list))

            if i == 0:
                df1 = pd.read_csv(file, header=None, engine = "python")
                df1.to_csv(file1, header=None, index = False)
                df_step1 = pd.read_csv(file_step, header=None, engine="python")
                df_step1.to_csv(file_step1, header=None,  index = False)

                with open(file2, "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df1.values[min_data])
                with open(file_step2, "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df_step1.values[min_data])

            elif 0 < i:
                df1 = pd.read_csv(file1, header=None, engine = "python") 
                df_step1 = pd.read_csv(file_step1, header=None, engine="python")
                with open(file2, "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df1.values[min_data])
                with open(file_step2, "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(df_step1.values[min_data])
            
            if i == 4:
                df2 = pd.read_csv(file2, header=None, engine = "python")
                df2 = df2.T
                df2.to_csv(file2, header=None, index = False)
                df_step2 = pd.read_csv(file_step2, header=None, engine = "python")
                df_step2 = df_step2.T
                df_step2.to_csv(file_step2, header=None, index = False)

                df1 = df1.drop(min_data, axis = 0)
                df_step1 = df_step1.drop(min_data, axis = 0)
                df1.to_csv(file1, header=None, index = False)
                df_step1.to_csv(file_step1, header=None,  index = False)
                break
            
            df1 = df1.drop(min_data, axis = 0)
            df_step1 = df_step1.drop(min_data, axis = 0)
            df1.to_csv(file1, header=None, index = False)
            df_step1.to_csv(file_step1, header=None,  index = False)
            T_list.pop(min_data)
            print(T_list)
            i += 1
        
        i = 0
        T_list.clear()

kentei()