import numpy as np
import pandas as pd

df = pd.read_csv('features.csv')

all_api_calls_file = open('mixed_dataset/all_api_calls.txt')
all_api_calls = []
#column_names = []
for lines in all_api_calls_file.readlines():
	all_api_calls.append(lines[:-1])


f = open('varthresh.txt','w')
#VarianceThreshold
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
x = pd.DataFrame(sel.fit_transform(df))


print (sel.get_support(indices=True))
selected_features = sel.get_support(indices=True)

for a in selected_features:
	f.write(all_api_calls[a]+"\n")
f.close()	
