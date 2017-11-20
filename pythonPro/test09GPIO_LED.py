#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

import RPi.GPIO as GPIO
import time

print("GPIO")

GPIO.setmode(GPIO.BCM)

print("GPIO setup pins as outps")

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,False)

GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)

for i in range(10):
	print(i,"ON")
	GPIO.output(17,True)
	GPIO.output(4,True)
	
	time.sleep(1)
	
	GPIO.output(17,False)
	GPIO.output(4,False)
	print(i,"OFF")
	time.sleep(1)
	
input("press enter to exit program")
GPIO.cleanup()


