# vid 2
'Hello' + '!' *10 
'Hello!!!!!!!!!!'

'Alice' + 'Bob'
'AliceBob'

'Alice' *3 
'AliceAliceAlice'

# assigning values 

spam = 'Hello'
spam + 'World'
'HelloWorld'

# overriding the value, spam assigned a new value 

spam = 'Goodbye' 
spam + 'World'
'GoodbyeWorld'

# statements

spam = 2*2
'4'

spam = 10 
spam = spam + 10
'spam = 20'

# vid 3

print('Hello World')

print('What is your name?')
myName = input ()
print ('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

# function examples 

len('AL') *10
20

int('1234')
1234

float('3.14')
3.14

float(1)
1.0

# Vid 4

'Boolean has two values True or False'

'Comparison Operators: ==, != (not equal to), <, >, <=, >='

42 == 42
True 

42 == 'Hello'
False

2!=3
True 

42 >= 100
False

myAge=26
myAge<30 
True 

42 == '42'
False 

42.0 == 42
True 

# and, or, and not boolean operators

True and True 
True 

True and False 
False 

False and False 
False 

True and False 
False 

# notice diff btween and and or 

True or True 
True 

True or False 
True 

False or True 
True 

False or False
False 


not True 
False 

not False 
True 

myAge = 26 
myPet = 'Cat'
myAge>20 and myPet == 'Cat'
True 


# Vid 5 

# flow control statements if and else 

name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')

password = 'swordfish'
if password == 'swordfish':
    print('Hi')
else:
    print('Bye')

if name != 'Alice':
    print('Hi Stranger')

# Vid 6

spam = 0 
while spam < 5:
    print('Hello World')
    spam = spam + 1

# ^while loop will itirate 5 times

while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank You!')

# break statements and continue statements for loops 

spam = 0 
while spam < 5:
    spam = spam+1 
    if spam ==3:
        continue 
    print('spam is' + str(spam))

'Would get spam is 1 spam is 2 spam is 4 spam is 4 (note: not spam is 3 becuase it never gets to the print statements it goes immediately to running the loop again'


# Vid 7

# for loops, ititrates a specific number of times 

print('My name is')
for i in range(5):
    print('Jimmy Five Times'+ str(i))

'Jimmy Five Times 0 Jimmy Five Times 1 Jimmy Five Times 2 Jimmy Five Times 3 Jimmy Five Times 4'

total = 0
for num in range(101):
    total = total + num
print(total)

i= 0
while i<5:
    print('Jimmy Five Times' + str(i))
    i=i=1

for i in range (12,16):
    print('Jimmy Five Times' + str(i))

for i in range (0,10,2):
    print('Jimmy Five Times' + str(i))

# ^ counting by 2

# Vid 8 

# standard library 

import random 
random.randint(1,10)
'Going to give a random integer in that range'

#this is an alternative way to do it but better to stick to previous one bc clearer
import random, sys, os, math 
from random import *
randint(1,10)

import sys 
sys.exit()

import sys 
print('Hello ')
sys.exit()
print('Goodbye')
# would never actually print out Goodbye bc it exits it beforehand 




