# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:28:02 2019

@author: 612383423
"""
### Task 1 
#print ('what\'s your age?')
#age = input()

### Task 2 
print ("what's your age?")
age = int(input())
type(age)

### Task 3 
#option=input('please input yes or no: ').lower()


### Task 4
#option=input('please input yes or no: ').lower()
#if len(option)<=1:
#    print('try again')

### Task 5 
print('***choice***')
print ('1. display my name')
print ('2. display my age')
print ('3. display my city')
choice = 0
choice= int(input('what is your choice? '))

    
#while choice <1 or choice >3:
#   choice=int(input('what is your choice? '))

### Task 6

while True:
    try:
        while choice<1 or choice>3:
            choice=int(input('what is your choice? '))
        break
    except ValueError:
        print('please type a number')

if choice==1:
    print ('ms wu')
elif choice ==2: 
    print ('5 years old')
elif choice == 3:
    print ('london')
    
### Task 7 
    
#class Spam(object):
#    def __init__(self, description, value):
#        if not description or value <=0:
#            raise ValueError
#        self.description = description
#        self.value=value
#
#s= Spam ('', -1)
#print(s.value)
    
class Spam(object):
    def __init__(self, description, value):
        assert description != ""
        assert value > 0
        self.description = description
        self.value=value

s= Spam ('gracy', 8)
print(s.value)