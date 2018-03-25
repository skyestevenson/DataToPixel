# DataToPixel
DataToPixel is a Python script that can store files as PNG pixelmaps of ASCII values, as well as a script to convert the images back into their original format.

DataToPixel goes through every character in a file, and stores its numeric ASCII value as a pixel value in the converted image, which is automatically saved as a PNG. The grayscale script encodes one ASCII character per pixel, where the RGB script encodes three per pixel: one in each color channel of each pixel.

##Example
![Plato's Republic](skyestevenson.github.com/DataToPixel/img/Plato_Republic_PDF.png)

## Dependencies
Requires Python Imaging Library (PIL)
