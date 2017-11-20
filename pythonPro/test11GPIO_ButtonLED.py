#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

import RPi.GPIO as GPIO
import time

print("GPIO")

GPIO.setmode(GPIO.BCM)
print("GPIO setup pins as outps")
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,False)

GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)

try:
	while True:
		inputValue = GPIO.input(24)
		GPIO.output(17,False)
		GPIO.output(4,False)
		print("OFF")
		if(inputValue == False):
			print("Pressed Button 24")
			print("ON")
			GPIO.output(17,True)
			GPIO.output(4,True)
			time.sleep(0.3)
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()


