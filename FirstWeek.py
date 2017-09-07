# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:51:31 2017

@author: Uri G Fernandez
"""

print('hello world')
print('no se porque se hacen tantos renglones')
x=int(input('Enter an Integer:  '))
if x%2==0:
    print('')
    print('Even')
else:
    print('Odd')
    print('Donde with conditional')
x=int(input('Enter an Integer:  '))
if x%2==0:
    if x%3==0:
        print('Divisible by 2 and 3')
    else:
        print('divisibleby 2 and not by 3')
elif x%3==0:
    print('Divisible by 3')
x=float(input('Enter a number for X  '))
y=float(input('Enter a number for Y  '))
if x==y:
     print('X and Y are equal')
     if y!= 0:
         print('therefore, x/y is  ', x/y)
elif x<y:
        print('X is smaller')
else:
        print('y is smaller')
print('Thanks')