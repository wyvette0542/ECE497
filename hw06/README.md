# hw06

Plug in and Turn on

The LCD is connected and when I ran on.sh, error messages were shown on the LCD. 

Display Images

Both boris.png and tux.png are successfully displayed. By changing the rotate degree to 180, I was able to rotate the image. 

Play Movies

A movie was successfully played and rotated with the same method as rotating images. 

Generate Text

I was able to put my name and other texts on the LCD display. 

Etch-A-Sketch

It allows the player to put 4 arguments when running the game. The first argument is the width of the line which the player desires and the rest 3 arguments are the RGB numbers the player wants. All input arguments are optional and the default width is 1 and the default color is black (r = 0, g = 0, b = 0). Then the game will draw lines with the width and color chosen by the player. 

All the Makefile and framebuffer files are in the folder "ili9341". I only copied etch-a-sketch.c, where I made modifications, out to the main directory. 
