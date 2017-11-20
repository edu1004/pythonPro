#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import os,sys

print("os sys")

fd = os.open("test29.txt",os.O_RDWR | os.O_CREAT)
print(fd)
print(type(fd))

txt = "My name is Yangssem"
txt_length = os.write(fd,txt.encode())

print(type(txt_length))

os.close(fd)
print("end....test29.txt create or write")

