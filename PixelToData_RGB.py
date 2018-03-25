#fileName = raw_input("Give me a file to pixelize:\n")

from PIL import Image
image = Image.open("asciiConverted_RGB.png")

# get image width
width, height = image.size

# load up pixels
px = image.load()

stringOutput = ""

index = 0

for q in range(0,width):
    for i in range(0,width):
            # stringOutput += chr(px[i,q])
            
            pixelString = str(px[i,q])
            
            pixelString = pixelString.strip("()")
            
            pixelSplit = pixelString.split(", ")

            #print pixelString
            #print "---"
            
            for channel in pixelSplit:
                #print channel
                stringOutput += chr(int(channel))
                
            #print "-"
            
            print str(index) + "/" + str(width*width) + " done"
            index += 1
            
#print stringOutput

# save to file
outFile = open("TESTCONVERT.txt","w")
outFile.write(stringOutput)
outFile.close()