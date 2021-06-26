import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]

for a in range(8):
    print(name[a])
    min_ev = []
    min_step = []
    min_Euclid = []
    mean_ev = []
    mean_step = []
    mean_Euclid = []

    file_ev = "Euclid/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[3] + ".csv"
    file_step = "Euclid/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[3] + ".csv"
    file_Euclid = "Euclid/" + name[a] + "/" + name[a] + "_Euclid_" + lx[3] + ".csv"

    ev = pd.read_csv(file_ev, header=None, engine = "python")
    step = pd.read_csv(file_step, header=None, engine = "python")
    Euclid = pd.read_csv(file_Euclid, header=None, engine = "python")

    for b in range(len(ev)):
        mean_ev.append(int(np.mean(ev.values[b])))
        mean_step.append(int(np.mean(step.values[b])))
        mean_Euclid.append(int(np.mean(Euclid.values[b])))
        min_ev.append(int(min(ev.values[b])))
        min_step.append(int(min(step.values[b])))
        min_Euclid.append(int(min(Euclid.values[b])))


    # print(min_ev)
    # print(mean_ev)
    # print(min_step)
    # print(mean_step)
    # print(min_Euclid)
    # print(mean_Euclid)
