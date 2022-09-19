# Vid 10

# local vs. global scopes
# code in a global scope can't access local variables but code in a local scope can access global variables
# code in one function's local scope cannot use variables in another local scope so could use same name 

spam = 42 # global variable 
def eggs():
    spam = 42 #local variable 

# global statements NEED CLARIFICATION

def spam():
    global eggs
    eggs='Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)

# Vid 11

# can do try and except to avoid one error to stop your whole code from running 

def div42by(divideBy):
    try:
        return 42/ divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(0))
print(div42by(11))

# could have general except statements for all types of errors

print('How many cats do you have?')
numCats = input()
if int(numCats) >= 4:
    print('That is a lot of cats')
else:
    print('That is not that many cats')
# potential error cause people could type in anything maybe nums in letters, so solve by:

print('How many cats do you have?')
numCats = input()
try: 
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number')

# Vid 12

# This is a guess the number game 

import random 

print('Hello, what is your name?')
name = input()

print('well' + name + 'I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess< secretNumber:
        print('Your guess is too low')
    if guess> secretNumber:
        print('Your guess is too high')
    else:
        break # It means they guessed it 

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else: 
    print('Nope! the number I was thinking of was' + str(secretNumber))


# Vid 13
# lists and list items 

['cat','bat','rat','elephant']
spam = ['cat','bat','rat','elephant']
spam [0]
'cat'
spam[1]
'bat'

spam=[['cat','bat'],[10,20,30,40,50]]
spam [0]
['cat','bat']
spam[0][1]
'bat'
spam[1][4]
50

spam = ['cat','bat','rat','elephant']
spam[-1]
'elephant'
spam[-2]
'rat'


'The' + spam[-1] + ' is afraid of the' + spam[-3] + "."
'The elephant is afraid of the bat.'

spam[1:3]
['bat','rat'] # goes up to but does not include the last number

spam='Hello'
spam = [10,20,30]
spam[1] = 'Hello' # can assign new values to list items 
spam
[10,'Hello',30]

spam[1:3] = ['CAT','DOG','MOUSE']
spam
['10','CAT','DOG','MOUSE']

spam = ['cat','bat','rat','elephant ']
spam[:2]
['cat','bat']
spam[1:]
['bat','rat','elephant ']

spam = ['cat','bat','rat','elephant ']
del spam[2]
['cat','bat','elephant']
del spam[2]
['cat','bat']

len([1,2,3])
3

[1,2,3] + [4,5,6]
[1,2,3,4,5,6]

[1,2,3] * 3
[1,2,3,1,2,3,1,2,3]

list('hello')
['h','e','l','l','o']

'howdy' in ['hello','hi','howdy','heyas']
True #cause can be found in it 

