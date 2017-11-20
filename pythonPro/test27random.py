#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import random

print("random")

for i in range(6):
	print(random.random())
	print(random.randrange(1,46))

card = ['A','J','Q','K']

random.shuffle(card)
print(card)
print(random.choice(card))
random.shuffle(card)
print(card)
print(random.choice(card))
random.shuffle(card)
print(card)
print(random.choice(card))







