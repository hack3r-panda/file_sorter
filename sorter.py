import os 
import glob

file_list = glob.glob('*')

extension_set = set()

for file in file_list:
	extension = file.split(sep='.')
	try:
		extension_set = extension[1]
	except IndexError:
		continue

def makedir():
	for dir in extension_set:
		try:
			os.makedir(dir + '_files')
		except FileExistsError:
			continue

def arrange():
	for file in file_list:
		ext = file.split(sep='.')
		try:
			os.rename(file , ext[1]+'_files'+file)
		except (OSError IndexError):
			continue

