import numpy as np
import pandas as pd

df = pd.read_csv('features.csv')

all_api_calls_file = open('mixed_dataset/all_api_calls.txt')
all_api_calls = []
#column_names = []
for lines in all_api_calls_file.readlines():
	all_api_calls.append(lines[:-1])
target = []
count = 0
indexed_file = open('training_file_index','r')
for row in indexed_file.readlines():
	#print(row)
	count = count + 1
	print(count)
	components = row.split('-')
	name = components[0]
	if 'benign' in name:
		target.append(0)
	else :
		target.append(1)
print(target)
indexed_file.close()

f = open('selkbest.txt','w')
#SelectKbest
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif

selector = SelectKBest(chi2, k=500)
selector.fit(df, target)

print(selector.get_support(indices=True))

print (selector.get_support(indices=True))
selected_features = selector.get_support(indices=True)

for a in selected_features:
	f.write(all_api_calls[a]+"\n")
f.close()	

	