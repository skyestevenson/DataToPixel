# TODO add feature to include original filename in file, use filename to reconstruct original file without user input
# TODO make this work in RGB colorspace, reduce number of pixels needed

# we need to encode ASCII data as an image!
# each ASCII character takes up a 0-127 space, meaning we can fit at least 1 ASCII character into each channel of a given pixel in an image!
# we need to assign the numeric value of a series of ASCII characters to each of the channels of each pixel of an image!

# make list from string
#fileName = raw_input("Give me a file to pixelize:\n")
fileName = "test.jpg"
data = open(fileName,"r")
dataString = data.read()
#dataString = raw_input("Please give me text:")
dataList = list(dataString)
listLength = len(dataList)

print "list length: " + str(listLength)

import math
width = int(math.ceil(math.sqrt(listLength)))

print "width: " + str(width)

# make the image
from PIL import Image
image = Image.new('L',(width,width),color=0)

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
            px[i,q] = (ord(dataList[index]))
            # print ord(dataList[index])
            print str(index) + "/" + str(listLength) + " done"
            index += 1


    
image.show()
image.save("asciiConverted.png")