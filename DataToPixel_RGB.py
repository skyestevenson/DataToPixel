# TODO add feature to include original filename in file, use filename to reconstruct original file without user input
# TODO make this work in RGB colorspace, reduce number of pixels needed

# we need to encode ASCII data as an image!
# each ASCII character takes up a 0-127 space, meaning we can fit at least 1 ASCII character into each channel of a given pixel in an image!
# we need to assign the numeric value of a series of ASCII characters to each of the channels of each pixel of an image!

# ensure proper division
from __future__ import division
import os

# make list from string
fileName = raw_input("Give me a file to pixelize:\n")
#fileName = ""
data = open(fileName,"r")
dataString = data.read()
#dataString = raw_input("Please give me text:")
dataList = list(dataString)
listLength = len(dataList)

#print "list length: " + str(listLength)

import math
width = int(math.ceil(math.sqrt(listLength/3)))
#width = int(math.ceil(listLength/3))+1

#print "width: " + str(width)

# make the image
from PIL import Image
image = Image.new('RGB',(width,width),color=0)
#image = Image.new('RGB',(width,1),color=0)

# load the temp image and store the ASCII value in one of its pixels
px = image.load()
# px[1,1] = (ascValue)
#image.show()

# we have to loop through the coordinates 1,1 2,1 3,1 1,2 2,2 3,2 with 3 being the width of the image - maybe we raise the x coordinate until it hits the width count, then raise the y coordinate until it hits the secnd width count, then do the same operation - can we use modulo to determine if a scanline width count has been reached?
# then we need to assign the ASCII numeric value to the pixel at each of those locations

index = 0

for q in range(0,width):
    for i in range(0,width):
        if index < listLength: #prevents an error when trying to access data at indices higher than what's in the list
            # evaluate RGB values
            rVal = ord(dataList[index])
            if (index+1) < listLength:
                gVal = ord(dataList[index+1])
            else:
                gVal = 0
            if (index+2) < listLength:
                bVal = ord(dataList[index+2])
            else:
                bVal = 0
            
            px[i,q] = (rVal,gVal,bVal)
            
            #print rVal
            #print gVal
            #print bVal
            
            #print str(index+1) + "/" + str(listLength) + " done"
            currentProgress = 100 * ((index + 1) / listLength)
            print("{:.4f}%".format(currentProgress))
            index += 3

print("Finished!")

#image.show()
image.save("CONVERTED.png")

oldFileSize = os.path.getsize(fileName)
newFileSize = os.path.getsize("CONVERTED.png")
fileSizeReduction = 100 * (1 - (newFileSize / oldFileSize))

print("File size reduced by {:.2f}%".format(fileSizeReduction))