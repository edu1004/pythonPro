#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("set")


#===================
s = set([1,2,3,1,2,3])
for item in s:
	print(item)

print("\n")
#===================
s = set((11,22,33,11,22,33))
for item in s:
	print(item)

print("\n")

#===================
s = set((11,22,33,11,22,33))
s.add(99)
s.add((222,333,444))
s.add(99)
for item in s:
	print(item)

print("\n")

#===================
s = set((11,22,33,11,22,33))
s.remove(22)
for item in s:
	print(item)

print("\n")


#===================
s = set((11,22,33,11,22,33))
s.update((77,88,99))
for item in s:
	print(item)

print("\n")

#===================
s1 = set([11,22,33])
s2 = set([22,33,44])
print("s1&s2:",s1&s2,type(s1&s2))
print("intersection:",s1.intersection(s2),type(s1&s2))


print("s1|s2:",s1|s2)
print("union:",s1.union(s2))


print("s1-s2:",s1-s2)
print("s2-s1:",s2-s1)
print("difference:",s2.difference(s1))
for item in s1:
	print(item)
for item in s2:
	print(item)
print("\n")



#===================
s = set([1,2,3])
lst = list(s)
print(lst[0])
print(lst[1])
print(lst[2])

tp = tuple(s)
print(tp[0])
print(tp[1])
print(tp[2])

for item in s:
	print(item)
print("\n")
