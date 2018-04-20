import numpy as np
import pandas as pd




all_api_calls_file = open('mixed_dataset/all_api_calls.txt')
all_api_calls = []
#column_names = []
for lines in all_api_calls_file.readlines():
	all_api_calls.append(lines[:-1])


api_index = dict((c,i+1) for i,c in enumerate(all_api_calls))

#print(api_index)

#print(len(api_index))

#total = len(api_index)



processed_and_indexed_training_examples = []
outputs = []
indexed_file = open('training_file_index','r')
count = 0
for row in indexed_file.readlines():
	#print(row)
	count = count + 1
	#print(count)
	components = row.split('-')
	name = components[0]
	indexes = components[1]
	indexes = indexes.split(',')[:-1]
	if name[-1] == 'e':
		outputs.append([0,1])
	else:
		outputs.append([1,0])
	#print(name)
	#print(indexes)
	xlist = []
	for i in indexes:
		xlist.append(int(i))
	processed_and_indexed_training_examples.append(xlist)
	#break

indexed_file.close()
#print(processed_and_indexed_training_examples)
list_for_all = []
column_names = [str(j+1) for j in range(len(api_index))]
#list_for_all.append(xlist)

total = len(processed_and_indexed_training_examples)

for c,i in enumerate(processed_and_indexed_training_examples):
	#print(i)
	print(str(c)+'/'+str(total))
	xlist = [0 for j in range(len(api_index))]
	for x in i:
		if x == 0:
			continue
		xlist[x] = 1
	#print(xlist)
	list_for_all.append(xlist)
	#break

#print(list_for_all[2])


df = pd.DataFrame(np.array(list_for_all),columns = all_api_calls)

#print(df.head())
df.to_csv('features.csv')

'''
#VarianceThreshold
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
x = pd.DataFrame(sel.fit_transform(df))


print (sel.get_support(indices=True))
selected_features = sel.get_support(indices=True)

for a in selected_features:
	print(all_api_calls[a])
'''	