#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

import test08AAA
import aaa.test08BBB as b
#from aaa.test08BBB import bbb
from aaa.test08BBB import *

print('import')

test08AAA.aaa()
b.bbb()
bbb()
