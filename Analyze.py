#this will analyze the array that has all the coords for the vision blocking

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from process import ProcessImage

coords = ProcessImage("samples/dungeon.png",5)
#anywhere there is a 1, its a "hit"
# print(coords)
#what I need to do is find the first hit, and search all adjacent pixels
#until there are no more hits to be found
testArray = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]]
def lookAtNeighbors(array,coords):
  foundHit = False
  x, y = coords
    #coords = (x,y)
  for dx in range(-1,2):
    for dy in range(-1,2):
      X = x + dx if x + dx > 0 else 0
      Y = y + dy if y + dy > 0 else 0
      try:
        value = array[X][Y]
        if value == 1:
          foundHit = True
      except IndexError:
        pass
  return foundHit


def findGroups(inputArray):
  coordArray = []
  groups = {}
  for xindex, xs in enumerate(inputArray):
    for yindex, ys in enumerate(xs):
      if lookAtNeighbors(testArray, (xindex, yindex)):
        coordArray.append((xindex,yindex))
  coordArray.sort(key=lambda tup: tup[0])
  print(coordArray)
  for coords in coordArray:
    try:
      groups[coords[0]].append(coords[1]) 
    except Exception as e:
      groups[coords[0]] = []
  print(groups)
  #now have an array of coords sorted by their X coords
print(findGroups(testArray))
