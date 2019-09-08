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
  
  atLeastOneYListLeft = True
  largestXMap = {}
  while atLeastOneYListLeft:
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
        atLeastOneYListLeft = True
        break
      else:
        atLeastOneYListLeft = False



  #y values are sorted in originMap and I have sorted X values in the list
    #will need to loop over every x Value and start consolidating

  #now I should consolidate all the X boxes
  maximizedCoords = []
  allBoxesConsolidated = True
  xValues = list(largestXMap)
  xValues.sort()
  while allBoxesConsolidated:
    for index, xVal in enumerate(xValues):
      #first, get the nearest tuple off the top
      nextIndex = index + 1
      try:
        thisTuple = largestXMap[xVal][0]
        latestXValue = xVal
        largestXMap[xVal] = largestXMap[xVal][1:] #taken it out of the list
        nextXVal = xValues[nextIndex]
        nextList = largestXMap[nextXVal]
        # print(thisTuple)
        # print(nextList)
        foundTuple = [tup for tup in nextList if tup[0] == thisTuple[0] and tup[1] == thisTuple[1]]
        while len(foundTuple) > 0:
          #filter the list and move on
          # print(nextXVal)
          largestXMap[nextXVal] = [tups for tups in nextList if tups[0] != thisTuple[0] and tups[1] != thisTuple[1]]
          nextIndex = nextIndex + 1
          try:
            nextXVal = xValues[nextIndex]
            nextList = largestXMap[nextXVal]
          except KeyError as e:
            break
          foundTuple = [tup for tup in nextList if tup[0] == thisTuple[0] and tup[1] == thisTuple[1]]
        maximizedCoords.append((thisTuple[0],thisTuple[1],xVal,nextXVal))
        break
      except IndexError as e:
        #not sure what to do yet
        continue 
      except KeyError:
        break
    #now I have the most recent Tuple and it's xValue
    #next is to look at the next index and see if it is good
    for xs, lists in largestXMap.items():
      if len(lists) > 0:
        allBoxesConsolidated = True
        break
      else:
        allBoxesConsolidated = False
  print(maximizedCoords)
  for x0,x1,y0,y1 in maximizedCoords:
    thisBox = {
                'originX':x0 - (squareSize / 2),
                'originY':y0,
                'dX':x1 - (squareSize / 2),
                'dY':y1
              }
    boxArray.append(thisBox)
    




  # for xVal,listOfTuples in largestXMap.items():
  #   for y0,y1 in listOfTuples:
  #     thisBox = {
  #               'originX':y0 -squareSize,
  #               'originY':xVal,
  #               'dX':y1,
  #               'dY':xVal + squareSize
  #             }
  #     boxArray.append(thisBox)
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

