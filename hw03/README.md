# hw02

TMP101
One of the TMP101 is at 0x48 and the other one is at 0x49. For #2, the shell commands print only the temperature at 0x48. For 3&4, I set the Thigh and Tlow in the python code with write_byte_data. When the temperature exceed the limits, a warning is printed. The temperature from both TMP101 will be printed when the button connected to GP1_4 is pressed. 

Etch-a-sketch
The four buttons connected to GP0 is used to control the movement. A seperate button connected to GP1_4 is used to clean the frame. Also, if the temperature of 0x48 TMP101 exceeds 28C/82.4F, the frame will clean up. 
