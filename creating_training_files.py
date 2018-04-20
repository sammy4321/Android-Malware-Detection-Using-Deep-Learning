from __future__ import print_function

import numpy as np
import re
import glob

from keras.utils.data_utils import get_file
from keras.layers.embeddings import Embedding
from keras import layers
from keras.layers import recurrent
from keras.models import Model
from keras.preprocessing.sequence import pad_sequences
import os
from keras.models import model_from_json

EMBED_HIDDEN_SIZE = 64
NO_OF_CONV_FILTERS = 256
NO_OF_CONV_SIZE = 3
API_SEQUENCE_MAX_LEN = 600
NUMBER_OF_API_CALLS = 6
NUMBER_OF_TRAINING_EXAMPLES_PER_BATCH = 4

all_api_calls_file = open('mixed_dataset/all_api_calls.txt')

all_api_calls = []
for lines in all_api_calls_file.readlines():
	all_api_calls.append(lines[:-1])


api_index = dict((c,i+1) for i,c in enumerate(all_api_calls))

training_file_calls = open('training_file_calls','w')
training_file_index = open('training_file_index','w')

print('API Index')
#print(api_index)

all_training_samples = glob.glob('mixed_dataset/*.out')

file_names = []
'''
for i in all_training_samples:
	#print(i)
	components = i.split('/')
	name = components[1].split('.')[0]
	#print(name)
	file_names.append()
'''

processed_training_examples = []
processing_count = 0


for i in all_training_samples:
	command = 'find '+i+' -name "*.smali" -exec cat {} \; | grep /*Manager | grep ";->" | grep \(.*\) | grep -v "Layout" | sort | uniq > feature_extractor.txt'
	os.system(command)
	components = i.split('/')
	name = components[1].split('.')[0]
	file_names.append(name)
	xlist = []
	calls_str = name + '-'
	index_str = name + '-'
	processed_training_examples_files = open('feature_extractor.txt','r')
	for lines in processed_training_examples_files.readlines():
		#xlist.append(lines[:-1])
		if lines[:-1] in all_api_calls:
			xlist.append(api_index[lines[:-1]])
		else:
			xlist.append(0)
		calls_str = calls_str + lines[:-1]+','
	#print(xlist)
	if len(xlist) >= API_SEQUENCE_MAX_LEN:
		xlist = xlist[:API_SEQUENCE_MAX_LEN]
	else:
		for i in range(API_SEQUENCE_MAX_LEN-len(xlist)):
			xlist.append(0)
	for m in xlist:
		index_str = index_str + str(m) + ','
	index_str = index_str + '\n'
	calls_str = calls_str + '\n'
	#for j in xlist:
	training_file_calls.write(calls_str)
	training_file_index.write(index_str)
	#processed_training_examples.append(xlist)
	processed_training_examples_files.close()
	print('processing count'+str(processing_count))
	processing_count = processing_count + 1
	#if processing_count == 3:
	#	break

training_file_calls.close()
training_file_index.close()

'''

#print('Processed Training Examples')
#print(processed_training_examples)
#print(len(processed_training_examples))
processing_count = 0





processed_and_indexed_training_examples = []
for i in processed_training_examples:
	xlist = []
	name = file_names[processing_count]
	index_str = name + '-'
	for j in i :
		if j in all_api_calls:
			xlist.append(api_index[j])
		else:
			xlist.append(0)
	#print(len(xlist))
	if len(xlist) >= API_SEQUENCE_MAX_LEN:
		xlist = xlist[:API_SEQUENCE_MAX_LEN]
	else:
		for i in range(API_SEQUENCE_MAX_LEN-len(xlist)):
			xlist.append(0)
	#processed_and_indexed_training_examples.append(xlist)
	for m in xlist:
		index_str = index_str + str(m) + ','
	index_str = index_str + '\n'
	training_file_index.write(index_str)
	print('Indexing Count'+str(processing_count))
	processing_count = processing_count + 1
	#if processing_count == 3:
	#	break

'''