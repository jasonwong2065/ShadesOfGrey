import numpy as np
class Island:
    """A grey area island
    Attributes:
        pixelX:
        pixelY:
        shade:
    """

    def __init__(self, shade, pixelX, pixelY):
        """Returns a GreyArea object"""
        self.shade = shade
        self.islandX = pixelX
        self.islandY = pixelY


    def floodCheck(self,pixelX, pixelY, shade):
        if(self.islandLocationArray[pixelX][pixelY] == 1):
            #Already visited
            return
        if(Island.imageArray[pixelX][pixelY] != shade):
            #Colour not equal
            return
        self.islandLocationArray[pixelX][pixelY] = 1
        if(pixelX != 0):
            #left
            # self.floodCheck(pixelX - 1, pixelY, shade)
            self.pixelQueue.append((pixelX - 1,pixelY))
        if(pixelX != self.imageWidth-1):
            #right
            # self.floodCheck(pixelX + 1, pixelY, shade)
            self.pixelQueue.append((pixelX + 1,pixelY))
        if(pixelY != 0):
            #up
            # self.floodCheck(pixelX, pixelY - 1, shade)
            self.pixelQueue.append((pixelX,pixelY-1))
        if(pixelY != self.imageHeight-1):
            #down
            # self.floodCheck(pixelX, pixelY + 1, shade)
            self.pixelQueue.append((pixelX,pixelY+1))
        return

    def searchIsland(self):
        self.islandLocationArray = np.zeros((Island.imageHeight,Island.imageWidth))
        self.pixelQueue = [(self.islandX, self.islandY)]
        while(len(self.pixelQueue) != 0):
            nextPixel = self.pixelQueue.pop()
            self.floodCheck(nextPixel[0], nextPixel[1], self.shade)

        return self.islandLocationArray

        # 1. If target-color is equal to replacement-color, return.
 #2. If the color of node is not equal to target-color, return.
 #3. Set the color of node to replacement-color.
 #4. Perform Flood-fill (one step to the south of node, target-color, replacement-color).
#    Perform Flood-fill (one step to the north of node, target-color, replacement-color).
#    Perform Flood-fill (one step to the west of node, target-color, replacement-color).
#    Perform Flood-fill (one step to the east of node, target-color, replacement-color).
# 5. Return.
