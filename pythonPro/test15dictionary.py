#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("dictionary")


#===================
dic = {'name':'yangssem','tel':'010'}
print(type(dic))
print("\n")

#===================
dic = {'name':'yangssem','tel':'010'}
print(dic['name'])
print(dic['tel'])
print(dic.get('name'))
print(dic.get('tel'))

print('name' in dic)
print("\n")

#===================
dic = {}

print('name' in dic)
print("\n")

#===================
dic = {1:'aaa',2:'bbb'}
dic[3] = 'yangssem'
dic[1] = 'kim'
dic['lst'] = [1,2,3]
dic['tp'] = (4,5,6)
dic['dt'] = {"id":"admin", "pw":"hi123456"}

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic['dt']['id'])

for key in dic:
	print(key,dic[key])

print("\n")

#===================
dic = {'aaa':'xxx','bbb':'yyy'}

for key in dic:
	print(key,dic[key])

print(dic.get('aaa'))
print(dic.get('ccc','zzz'))
print("\n")

#===================


dic.clear()

for key in dic:
	print(key,dic[key])

print("\n")
