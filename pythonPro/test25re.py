#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

import re


print("regEXP : regular Expressions")
#[] word
#. \n 제외 한문자
#(*) 반복 0~
#(+) 반 복 1~
#{m,n}
pattern = re.compile("(\d{6})[-]\d{7}")
data = "kim 123456-1234567 010-1111-1111 lee 222222-3333333"
print(pattern.sub("\g<1>-*******",data))
print(pattern.sub("\g<1>-1******",data))
