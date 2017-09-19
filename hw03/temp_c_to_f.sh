#!/bin/bash

temp=`i2cget -y 1 0x48`
temp2=$(($temp *9/5+32))
echo "Temperature in F: "
echo $temp2


