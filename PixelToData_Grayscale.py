#fileName = raw_input("Give me a file to pixelize:\n")

from PIL import Image
image = Image.open("asciiConverted.png")

# get image width
width, height = image.size

# load up pixels
px = image.load()

stringOutput = ""

index = 0

for q in range(0,width):
    for i in range(0,width):
            stringOutput += chr(px[i,q])
            print str(index) + "/" + str(width^2) + " done"
            index += 1
            
#print stringOutput

# save to file
outFile = open("TESTCONVERT.jpg","w")
outFile.write(stringOutput)
outFile.close()