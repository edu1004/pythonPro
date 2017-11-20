#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

import RPi.GPIO as GPIO
import time

print("GPIO")

GPIO.setmode(GPIO.BCM)
print("GPIO setup pins as outps")
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		inputValue = GPIO.input(24)
		
		if(inputValue == False):
			print("Pressed Button 24")
			time.sleep(0.3)
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()


