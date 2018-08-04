import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
#print train.head() , '\n\n',test.head()

#Show an random image
i = random.choice(train.index)
img_id = train.ID[i]
img = imread(os.path.join('Train',img_id))
print 'ID: ', os.path.join('Train',img_id), '\nAge: ', train.Class[i]
imshow(img)
#plt.show()
#print img.shape





#Resizing the images
temp = []
count =1 
for img_id in train.ID:
	print count
	count = count + 1
	img = imread(os.path.join('Train',img_id))
	#img = imresize(img, 32, 32)
	img = img.astype('float32')
	temp.append(img)	
train_x = np.stack(temp)
train_x = train_x / 255


for img_id in test.ID:
	img = imread(os.path.join('Test',img_id))
	#img = imresize(img, 32, 32)
	img = img.astype('float32')
	temp.append(img)
test_x = np.stack(temp)
test_x = test_x / 255



print train.Class.value_counts()
