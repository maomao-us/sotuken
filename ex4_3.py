import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

urlretrieve("http://nagamune.com/rb2/data4-1.csv","data4-1.csv")
csv=pd.read_csv("data4-1.csv",encoding="shift-jis")
x=[]
for i in range(0,365):
  x+=[csv.iloc[i,0]]
y=[]
for i in range(0,365):
  y+=[csv.iloc[i,1]]
plt.plot(x,y)
plt.show()