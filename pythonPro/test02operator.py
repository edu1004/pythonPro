#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
print('operator')

su = 100
result = su +1

print('result:',result)

re01 = 'result:'
re02 = '101'
re03 = re01+re02
print(re03)

#+,-,*,/,%
print('10+10=',10+10)
print('10-10=',10-10)
print('10*10=',10*10)
print('10/10=',10/10)
print('10%3=',10%3)
print("'a'*10",'a'*10)

#+=,-=,*=,/=,%=
x = 11
x += 10
print('x+=10',x)

x -= 10
print('x-=10',x)

x *= 10
print('x*=10',x)

x /= 10
print('x/=10',x)

x %= 10
print('x%=10',x)

#&=, |= ^=
z = 10

z &= 2
print('z&=2',z)

z |= 2
print('z|=2',z)

z ^= 2
print('z^=2',z)

#&, |, ^
y = 10
print('y&2',y&2)
print('y|2',y|2)
print('y^2',y^2)

#==,!=,>,<,>=,<=
print('y==10',y==10)
print('y!=10',y!=10)
print('y>=10',y>=10)
print('y<=10',y<=10)
print('y>10',y>10)
print('y<10',y<10)

#3hang
result = True and "KIM" or "LEE"
print("result:",result)
result = False and "KIM" or "LEE"
print("result:",result)


result = "yangssem" if True  else "Han"
print("result:",result)
result = "yangssem" if False  else "Han"
print("result:",result)







