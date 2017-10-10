# hw05

Short Answers: 

1. After "matrix" is sent to the bone, boneSever.js is running and opens the i2c connection. Then boneSever.js opens MatrixLED. In matrixLED.js, when connect() is called, "matrix" will be called and reads the 8-bit i2c data and puts the data into variable "data". Then the function uses the received data to update matrixLED. At the same time, it also update the LED matrix on the browser. 

2. When an LED is clicked, function "LEDclick" is called and updates both disp[2*i] for the green LED and disp[2*i+1] for the red LED. Then the function sends data to the LED matrix using "socket.emit" and also update the corresponding color on the browser. 

3. "on", which corresponds to a green color. 

4. When function "LEDclick" is called, it checks if either disp[2*i] or disp[2*i+1] is an one to determine what color LED is on at that position and what "class" is the position at. Then update the position for the next "class" following a pattern of green -> red -> orange -> blank -> green and so on. After determining the current "class", toggle the corresponding bit and send the data to the bone. 

5. I added my name in the browser by editing matrixLED.html. 

All the files related to bone demo is in the folder "realtime", I only copied the three files about matrixLED, where I made modifications, out. The matrixLED files in the realtime folder and out of that folder are the same version. 

# Comments from Prof. Yoder
# Found your answers to the questions.  They look good.
# Thanks for the demo.
# Grade:  10/10