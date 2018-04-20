from __future__ import print_function
import re

all_api_calls = open("all_api_calls",'r')
all_apis_before_split = all_api_calls.read()
#print(all_apis_before_split)
#print(re.split(';',all_apis_before_split))
split_apis = re.split(';',all_apis_before_split)[:-1]
print(split_apis)
all_api_calls.close()



new_apis = ['Sammy','ujwal','there']

for apis in new_apis:
	apis = apis.lower()
	if apis not in split_apis:
		split_apis.append(apis)

print(split_apis)

all_api_calls = open("all_api_calls",'w')

string_to_write = ""

for apis in split_apis:
	string_to_write = string_to_write + apis + ';'

string_to_write = string_to_write + '\n'

all_api_calls.write(string_to_write)
all_api_calls.close()