import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PreProcess import PrepareImage

#Already done but just for posterity re-process

def ProcessImage(pathToImage,resolution):
  #may move this later
  PrepareImage(pathToImage)
  img = mpimg.imread('temp/processed.png')
  Npx, Npy = img.shape[0], img.shape[1]
  searchSqSize = resolution
  target_array = np.empty((Npx,Npy)) #will hold the values for the pixels
  for i in range(1,Npx,searchSqSize):
    x0, x1 = i, i + searchSqSize
    for j in range(1, Npy, searchSqSize):
      y0, y1 = j, j + searchSqSize
      avg = np.mean(img[x0:x1, y0:y1])
      if avg < 0.9:
        img[x0:x1,y0:y1] = 0
        target_array[x0:x1, y0:y1] = 1
  return target_array

