

import os
import argparse
import pandas as pd 
import numpy as np

example_dirname = os.path.abspath(os.path.dirname(__file__))

caffe_dirname = os.path.abspath(os.path.join(example_dirname,'../..'))
training_dirname = os.path.join(caffe_dirname,'data/101')
img_dirname = os.path.join(caffe_dirname,'data/101/101_ObjectCategories')

if __name__ == '__main__':
	parser =  argparse.ArgumentParser(
		description = 'Arrage the 101 data set')
	parser.add_argument(
		'train_percent',type = float, default = 0,
		help= "the percent of the training data")
	args = parser.parse_args()
	
	
	img_num = 0
	class_lable = 0
	img_class = open('image_class.txt','wb')
	img_list = open('img_list.txt','wb')
	# img_test = open('test.txt','w')
	dirs = os.listdir(img_dirname)
	for folder in dirs:
		name = os.path.join(img_dirname, folder)
		new_name = os.path.join(img_dirname, folder.lower())
		if new_name != name:
			os.rename(name,new_name)

	dirs.sort()
	for folder in dirs:
		img_class.write(folder + ' ' + str(class_lable) + os.linesep)
		temp = os.path.join(img_dirname,folder)
		for file in sorted(os.listdir(temp)):	
			# print file		
			img_list.write(os.path.join(temp,file)+' '+str(class_lable)+ os.linesep)
			img_num = img_num + 1
		class_lable = class_lable + 1

	
	print img_num
	img_class.close()
	img_list.close()

	df = pd.read_csv('img_list.txt',sep = " ",  header = None)
	print df.shape	

	# df.columns = ["img_path", "img_class"]
	df = df.iloc[np.random.permutation(img_num)]
	
	img_train = int(args.train_percent * img_num)
	print img_train
	df1 = df.iloc[:img_train]
	df2 = df.iloc[img_train:]
	df1.to_csv("train.txt", header=None, index=None, sep=' ', mode='w')
	df2.to_csv("test.txt", header=None, index=None, sep=' ', mode='w')
	
	




