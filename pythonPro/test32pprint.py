#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

from pprint import *

print("pprint")



lsts = [[1,2,3],[4,5],[6,7,8]]

print(lsts)
print(*lsts)
print(*lsts,sep='\n')

print('='*40)
print('** pprint **')

pp = PrettyPrinter(width=40,indent=5)

dic = {'name':'yangssem','subject':[1,2,3,4,5],'age':33}

pp.pprint(dic)
print(dic)
print(*dic)

data = dict(id='admin',pw='hi123456')
print(data)
print(*data)
print([ key for key in data])
print([ (key,data[key]) for key in data])
print(*[ (key,data[key]) for key in data],sep='\n')
