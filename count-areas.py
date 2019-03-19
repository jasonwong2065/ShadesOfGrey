#!/usr/bin/env python3
import sys
import numpy as np
from Island import Island

np.set_printoptions(threshold=sys.maxsize)

def reader(inputFile,height,width):
    inputArray = np.fromfile(inputFile, dtype=np.uint8)
    inputArray = inputArray.reshape(height,width)
    return inputArray

if(len(sys.argv) != 4):
    print("Usage: python3 " + sys.argv[0] + " <input-filename> --shape <height>,<width>")
    sys.exit()

imageHeight = int(sys.argv[3].split(",")[0])
imageWidth = int(sys.argv[3].split(",")[1])
imageArray = reader(sys.argv[1],imageHeight,imageWidth)
Island.imageArray = imageArray
Island.imageHeight = imageHeight
Island.imageWidth = imageWidth
visitedArray = np.zeros((imageHeight,imageWidth))
outputArray = np.zeros(256)

while(len(np.where(visitedArray == 0)[0]) != 0):
    unVisitedPixelIndices = np.where(visitedArray == 0)
    nextPixelX = unVisitedPixelIndices[0][0]
    nextPixelY = unVisitedPixelIndices[1][0]
    nextPixelShade = imageArray[nextPixelX][nextPixelY]
    outputArray[nextPixelShade] += 1
    newIsland = Island(nextPixelShade,nextPixelX,nextPixelY)
    islandLocationArray = newIsland.searchIsland()
    visitedArray = np.add(visitedArray, islandLocationArray)
    #print(len(np.where(visitedArray == 0)[0]))
    #print(imageArray)
    #print("")
    #print(islandLocationArray)

print(outputArray)
