# -*- coding: utf-8 -*-
"""Data_Augmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J2TEEC66pRwlodgCBcBNCWv0vRB4JYB5

Credit for code: https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/

and 


https://www.geeksforgeeks.org/how-to-flip-an-image-horizontally-or-vertically-in-python/
"""

from numpy import expand_dims
import matplotlib.pyplot as plt
import os
from PIL import Image

#Problem -- could not run in colab with large data sets. It was not letting me upload the dataset
# for happy or sad, and I could not figure out what was going run when running in local

'''
IGNORE THIS, I WAS TESTING A FEW METHODS AND NEEDED TO EMPTY A FOLDER 
for folder, subfolders, file_list in os.walk("flipped_fear"): 
  for file_name in file_list:
    # Load image
    os.remove("flipped_fear/"+file_name)'''

## CHANGE THIS PATH VALUE TO BE THE PATH OF THE FOLDER WITH THE IMAGES YOU WANT TO FLIP 
path = "fear"

for folder, subfolders, file_list in os.walk(path):
  for file_name in file_list:
    print(file_name)

    file_name = "fear/"+file_name ## CHANGE THIS TO INCLUDE THE PROPER PATH NAME AT THE BEGINNING 
    original = Image.open(file_name)

    flipped = original.transpose(method=Image.FLIP_LEFT_RIGHT)
    new_name = "flipped_"+os.path.splitext(file_name)[0]+"_flipped.jpg"
    #print(new_name)  ## YOU CAN COMMENT OUT THE NEXT LINE AND UNCOMMENT THIS LINE IF YOU WANT TO CHECK THE NAME 
    flipped.save(new_name)

    original.close()
    flipped.close()

!zip -r /content/file.zip /content/flipped_fear

from google.colab import files
files.download("/content/file.zip")