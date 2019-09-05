#this will analyze the array that has all the coords for the vision blocking

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from process import ProcessImage


def analyzeImage(pathToImage, resolution):
  coords = ProcessImage(pathToImage,resolution)

  def minimum(a,b,c):
    l = min(a,b)
    return min(l,c)
  print(minimum(4,7,2))

  def maxSize(arr,startingCoord):
    result = np.zeros(arr.shape)
    maxVal = 0
    x = int(startingCoord[0])
    y = int(startingCoord[1])
    # arr = arr[x:,y:]
    try:
      startingVal = arr[startingCoord[0], startingCoord[1]]
    except Exception as e:
      return None
    for i in range(x,len(arr)):
      result[i][0] = arr[i][0]
      if result[i][0] == 1:
        maxVal = 1
    for i in range(y, len(arr[0])):
      result[0][i] = arr[0][i]
      if result[0][i] == 1:
        maxVal = 1
    
    for i in range(x,len(arr)):
      for j in range(y,len(arr[i])):
        if arr[i][j] == 0 or arr[i][j] == 0.5:
          break
        t = minimum(result[i-1][j], result[i-1][j-1], result[i][j-1])
        result[i][j] = t + 1
        if result[i][j] > maxVal:
          maxVal = result[i][j]

    x1 = int(x + maxVal)
    y1 = int(y + maxVal)
    if np.any(coords[x:x1,y:y1] == 0):
      return None
    coords[x:x1,y:y1] = 0.5
    # plt.imshow(coords, cmap='Greys_r')
    # plt.show()
    return (x,y,x1,y1)


  coordsArray = np.where(coords == 1.0)
  listOfCoordinates = list(zip(coordsArray[0], coordsArray[1]))
  # coords[0,:] = 1
  # coords[:, 0] = 1
  blackPixelsLeft = np.any(coords == 1.0)
  results = []
  while blackPixelsLeft:
    for val in listOfCoordinates:
      if coords[val[0],val[1]] != 1.0:
        continue
      res = maxSize(coords,val)
      # print(res)
      if res is not None:
        results.append(res)
        print(res)

    print(results,len(results))
    # plt.imshow(coords, cmap='Greys_r')
    # plt.show()
    blackPixelsLeft = np.any(coords == 1.0)


  returnData = []
  print(results)
  for x0,y0,x1,y1 in results:
    tempDict = {
        'dX': y1,
        'dY': x1,
        'originX': y0,
        'originY': x0
    }
    returnData.append(tempDict)
  return returnData

































#u
# ntil there are no more hits to be found
# testArray = [
#     [0, 1, 1, 0, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0]]



# def getDiagonalDown(arrayInput,currentCoordTuple):
#   return arrayInput[currentCoordTuple[0] + 1][currentCoordTuple[1] + 1]
  
# def checkUp(aI,cT):
#   sliceUp = aI[0:cT[0],cT[1]]
#   return np.any(aI == 0)

# def checkLeft(aI, cT):
#   sliceUp = aI[cT[0],0:cT[1]]
#   aI[cT[0], 0:cT[1]] = 0.5
#   return np.any(aI == 0)


# checkLeft(coords,(5,5))
# plt.imshow(coords, cmap='Greys_r')
# plt.show()

# for index(x,y) in enumerate(listOfCoordinates):
#   if checkUp(coords,(x,y)) and checkLeft(coords)























# while blackPixelsLeft:
  
#   for index,(x,y) in enumerate(listOfCoordinates):
#     if coords[x][y] == 1:
#       #havent marked this pixel as searched yet
#       x0 = x #mark starting point
#       y0 = y
#       x1 = x
#       y1 = x
#       for xPx in range(x,coords.shape[0]-1):
#         for yPx in range(y,coords.shape[1]-1):
#           if(coords[xPx][yPx] == 1):
#             #white space, mark it and keep moving forward
#             x1 = xPx
#             y1 = yPx
#             coords[xPx][yPx] = 0.5
#           else:
#             plt.imshow(coords, cmap='Greys_r')
#             plt.show()
          
          
#       print(x0,y0,x1,y1)
      
#       print(x1)
#       #now need to move west until the end

      


#   blackPixelsLeft = np.any(coords == 1.0)
  #now loop until I get to the end of each row to make the largest rect possible

  




# def lookAtNeighbors(array,coords):
#   foundHit = False
#   x, y = coords
#     #coords = (x,y)
#   for dx in range(-1,2):
#     for dy in range(-1,2):
#       X = x + dx if x + dx > 0 else 0
#       Y = y + dy if y + dy > 0 else 0
#       try:
#         value = array[X][Y]
#         if value == 1:
#           foundHit = True
#       except IndexError:
#         pass
#   return foundHit


# def findGroups(inputArray):
#   coordArray = []
#   groups = {}
#   for xindex, xs in enumerate(inputArray):
#     for yindex, ys in enumerate(xs):
#       if lookAtNeighbors(testArray, (xindex, yindex)):
#         coordArray.append((xindex,yindex))
#   coordArray.sort(key=lambda tup: tup[0])
#   print(coordArray)
#   for coords in coordArray:
#     try:
#       groups[coords[0]].append(coords[1]) 
#     except Exception as e:
#       groups[coords[0]] = []
#   print(groups)
#   #now have an array of coords sorted by their X coords
# print(findGroups(testArray))
