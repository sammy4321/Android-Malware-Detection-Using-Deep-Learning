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


#api_index = dict((c,i+1) for i,c in enumerate(all_api_calls))



processed_and_indexed_training_examples = []
outputs = []
indexed_file = open('testing_file_index','r')

for row in indexed_file.readlines():
	#print(row)
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

#print(outputs)
#print(processed_and_indexed_training_examples)

processed_and_indexed_training_examples = np.array(processed_and_indexed_training_examples)
outputs = np.array(outputs)






json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


results = loaded_model.evaluate(x=processed_and_indexed_training_examples,y=outputs)

print(results)