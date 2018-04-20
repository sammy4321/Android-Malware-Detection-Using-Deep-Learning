import glob
import os
files = glob.glob("samples_malware/*")


for i in files:
	command = "tar -zxf "+i+" /home/samarth/Desktop/IAS project/extracted_files"
	os.system(command)
	break

