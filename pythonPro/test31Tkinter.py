#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
from tkinter import *
#from Tkinter import * python 2.x

print("tkinter")

top = Tk()
lst = ['yangssem','python','android','linux']

lstBox = Listbox(top)

for item in lst:
	lstBox.insert(0,item)

lstBox.pack()
top.mainloop()


