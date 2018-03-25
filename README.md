# DataToPixel
DataToPixel is a Python script that can store files as PNG pixelmaps of ASCII values, as well as a script to convert the images back into their original format.

DataToPixel goes through every character in a file, and stores its numeric ASCII value as a pixel value in the converted image, which is automatically saved as a PNG. The grayscale script encodes one ASCII character per pixel, where the RGB script encodes three per pixel: one in each color channel of each pixel.

## Example
Here's a lossless conversion of a PDF of Plato's Republic into a PNG pixelmap.
![Plato's Republic](https://github.com/skyestevenson/DataToPixel/blob/master/Plato_Republic_PDF.png?raw=true)

## Dependencies
Requires Python Imaging Library (PIL)
