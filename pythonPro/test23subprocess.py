#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import subprocess

print("subprocess")

#subprocess.call("ls -al | more",shell=True)
#subprocess.call("sh ./test23.sh",shell=True)

result = subprocess.check_output("sh ./test23.sh",shell=True)
print(result)


print("\n")
#=========================

lst = [11,22,33]
val = "echo {}".format(lst[0])
subprocess.call(val,shell=True)

print("\n")
#=========================

