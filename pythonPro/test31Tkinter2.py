#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
from tkinter import *
#from Tkinter import * python 2.x

print("tkinter")

top = Tk()
nameLabel = Label(top,text="name")
nameLabel.pack()

nameEntry = Entry(top,text="kim")
nameEntry.pack()

okButton = Button(top,text="OK")
okButton.pack()


top.mainloop()


