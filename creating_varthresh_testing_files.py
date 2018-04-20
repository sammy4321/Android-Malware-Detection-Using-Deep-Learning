import numpy as np

all_api_calls_file = open('mixed_dataset/all_api_calls.txt')
all_api_calls = []
#column_names = []
for lines in all_api_calls_file.readlines():
	all_api_calls.append(lines[:-1])

all_api_calls_file.close()
api_index = dict((c,i+1) for i,c in enumerate(all_api_calls))

l1_file = open('tree.txt','r')

features_selected_by_l1 = []
features_selected_by_l1_index = []

for line in l1_file.readlines():
	#print(line[:-1])
	features_selected_by_l1.append(line[:-1])
	features_selected_by_l1_index.append(int(api_index[line[:-1]]))
	#print(api_index[line[:-1]])






l1_file.close()

processed_and_indexed_training_examples = []
outputs = []
indexed_file = open('testing_file_index','r')
l1_indexed_files = open('testing_file_index_varthresh','w')
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
	xlist_str = name+'-'
	for i in indexes:
		if int(i) not in features_selected_by_l1_index:
			xlist.append(0)
			#print('Got zero')
			xlist_str = xlist_str + '0'+','
			continue
		#print('Got one')
		xlist_str = xlist_str + str(int(i))+','
		xlist.append(int(i))
	xlist_str = xlist_str+'\n'
	print(len(xlist))
	l1_indexed_files.write(xlist_str)
	processed_and_indexed_training_examples.append(xlist)
	print(count)
	#break

indexed_file.close()
l1_indexed_files.close()
#print(processed_and_indexed_training_examples)
#print(outputs)
#print(processed_and_indexed_training_examples)

processed_and_indexed_training_examples = np.array(processed_and_indexed_training_examples)
outputs = np.array(outputs)