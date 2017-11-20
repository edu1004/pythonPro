#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("class")

#MemberVO
class MemberVO:
	userName = "yangssem"
	def __init__(self):
		print("__init__")
		
m = MemberVO()
print(m.userName)

print("\n")
#=====================
class ScoreVO:
	def __init__(self,name,kor,eng,math):
		print("__init__")
		self.name = name
		self.kor = kor
		self.eng = eng
		self.math = math
	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

s = ScoreVO("KIM",99,88,77)
s.setName("lee")
print(s.name)
print(s.getName())
print(vars(s))
print(type(vars(s)))
print("\n")
#=====================
class BoardVO:
	def __init__(self,title="bbbb"):
		print("__init__")
		self.title = title

b = BoardVO()
print(b.title)

b = BoardVO("aaaaa")
print(b.title)

print("\n")
#=====================
class Student:
	def __init__(self,num=0,name='hong'):
		print("__init__")
		#__ >> private  , _ >> protected
		self.__num = num
		self.__name = name
		
	def getNum(self):
		return self.__num
	def setNum(self,num):
		self.__num = num
	
st = Student()
#print(st.num) error
#print(st.name) error
#getters,setters
st.setNum(99)
print(st.getNum())




