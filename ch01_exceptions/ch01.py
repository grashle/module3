# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:40:13 2019

@author: 612383423
"""

#try: 
#    f=open('testfile')
#except Exception:
#    print ('sorry, this file doesn\'t exist, or the file name is wrong. please double check.')
#    
#    
#try:
#    f=open('testfile.txt')
#    s1= not_exists
#except FileNotFoundError: 
#    print ('sorry this file name is wrong, or the file doesn\'t exist.')
#
#
## the exception key word is used for general exceptions, and FileNotFoundError is one of the built in exceptions.
#
### Multiple Exceptions
#    
#try:
#    f=open('testfile.txt')
#    s1 = not_exists
#except FileNotFoundError:
#    print ('Sorry, this file does not exist, or the file name is wrong.')
#except Exception:
#    print ('Sorry. something is wrong after opening function.')     
#
#### Task 1
#    
#try: 
#    f=open('testfile.txt')
#    s1=not_exists
#except Exception as e:
#    print(e)  #here, the system prints the actual error if there is anything wrong with the try block
#
#### Task 2
#
#try: 
#    f=open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()    
#    
### Task 3

try:
    f=open('testfile.txt')
    s1= not_exist
except Exception as e:
    print(e)
    
# here, e is a variable that represents anything wrong
    
### Task 4 
    
try: 
    f=open('testfile')
except Exception as e:
    print (e)
else: 
    print(f.read())
    f.close()
    
### Task 5
finally: 
    print ('executing finally..')


try:
    f=open('testfile.txt')
except Exception as e:
    print(e)
else: 
    print (f.read())
    
### Task 6 - manually raising an exception
    
try:
    with open('test.txt', 'r') as f:
        f_text = f.read()
        if f.name == 'test.txt':
            # it's better to raise specific errors than generic
            raise Exception('that is the wrong file!')
except Exception as e:
    print(e)
else:
    print(f_text)
finally:
    print('this is the end!')
    
    