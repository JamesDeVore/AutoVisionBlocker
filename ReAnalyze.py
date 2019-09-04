import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from process import ProcessImage

# processedImgArray = ProcessImage("samples/dungeon.png", 5)

def CreateSquares(processedImgArray, squareSize):
  #takes in the product of Process Image
  widthPixels, heightPixels = processedImgArray.shape
  result = np.where(processedImgArray == 1.0)
  allBoxOrigins = list(zip(result[0],result[1]))
        #go back to one pixel at a time
  originMap = {}
  boxArray = []
  for x in range(1,widthPixels,squareSize):
    for y in range(1,heightPixels,squareSize):
      if processedImgArray[x][y] == 1:
        try:
          originMap[x].append(y)
        except Exception as e:
          originMap[x] = [y]
  for x, yArray in originMap.items():
    #now I need to iterate and prep the data to be rendered easily
    for y in yArray:
      thisBox = {
        'originX':y,
        'originY':x,
        'dX':y + squareSize,
        'dY':x + squareSize
      }
      boxArray.append(thisBox)
  return boxArray


# print(CreateSquares(ProcessImage("samples/dungeon.png", 5),5))

