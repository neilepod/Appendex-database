import pandas as pd
import os
import sys
import json
from pandas import DataFrame
import json

df=pd.read_excel("(final)appendixb.xlsx")
b=df.to_dict()
df = pd.DataFrame(b)
print df
Export = df.to_json (r'C:\codes\test.json')
with open('test.json') as f:
    d = json.load(f)
    print(d)