#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import os

print("os pipe")
#precess
fd_receive,fd_transmit = os.pipe()

print("fd_receive:",fd_receive)
print("fd_transmit:",fd_transmit)

data = "yangssem"
data_length = os.write(fd_transmit, data.encode())
print("data_length:",data_length)

print("The pipe os.read():", os.read(fd_receive,1024))




