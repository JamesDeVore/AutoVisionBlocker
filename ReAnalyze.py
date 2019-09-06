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
  for x in range(0,widthPixels,squareSize):
    for y in range(0,heightPixels,squareSize):
      if processedImgArray[x][y] == 1:
        try:
          originMap[int(x)].append(y)
        except Exception as e:
          originMap[int(x)] = [y]
  #now I need to consolidate the boxes, so first I will create a sorted list of all x values
  xValues = list(originMap)
  xValues.sort()
  #now to ensure all y vals are sorted too
  
  longerThan1 = True
  largestXMap = {}
  while longerThan1:
    for xVal in xValues:
      yList = originMap[xVal]
      yList.sort()
      if len(yList) == 0:
        continue
      try:
        y0 = yList[0]
        y1 = y0
        for index,yVal in enumerate(yList):
          nextVal = yList[index + 1]
          if  nextVal - squareSize == yList[index]:
            y1 = yList[index]
            #adjacent
            continue
          else:
            #not adjacent
            y1 = yList[index]
            #now remove them
            originMap[xVal] = yList[index + 1:]
            break;
        try:
          largestXMap[xVal - squareSize].append((y0,y1))
        except Exception as e:
          largestXMap[xVal - squareSize] = [(y0,y1)]
        # print(y0,y1)
      except IndexError:
        if y1 == yList[index]:
          #last one, only one more left
          originMap[xVal] = []
        else:
          y1 = yList[index]
          originMap[xVal] = yList[index + 1:]
        try:
          largestXMap[xVal - squareSize].append((y0, y1))
        except Exception as e:
          largestXMap[xVal - squareSize] = [(y0, y1)]
        # print(xVal,y0, y1)
        continue
    for xs,lists in originMap.items():
      if len(lists) > 0:
        longerThan1 = True
        break
      else:
        longerThan1 = False



  #y values are sorted in originMap and I have sortex X values in the list
    #will need to loop over every x Value and start consolidating
  # print(largestXMap)
  for xVal,listOfTuples in largestXMap.items():
    for y0,y1 in listOfTuples:
      thisBox = {
                'originX':y0 -squareSize,
                'originY':xVal,
                'dX':y1,
                'dY':xVal + squareSize
              }
      boxArray.append(thisBox)
  return boxArray







  # for x, yArray in originMap.items():
  # #   #now I need to iterate and prep the data to be rendered easily
  #   for y in yArray:
  #     thisBox = {
  #       'originX':y,
  #       'originY':x,
  #       'dX':y + squareSize,
  #       'dY':x + squareSize
  #     }
  #     boxArray.append(thisBox)
  # return boxArray


# print(CreateSquares(ProcessImage("samples/dungeon.png", 5),5))

