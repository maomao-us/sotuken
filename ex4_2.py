import pandas as pd
from urllib.request import urlretrieve

urlretrieve("http://nagamune.com/rb2/data4-1.csv","data4-1.csv")
csv=pd.read_csv("data4-1.csv",encoding="shift-jis")
print(csv.iloc[0:365,0:2])