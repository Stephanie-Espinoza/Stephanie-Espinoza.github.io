print('Hello World')

x = 2 // 3
y = x * 4
z = y + 5
print('z= ',z)

# python has 'truthiness' and 'falsiness' if it displays the if result, then truthy, if it displays the else result, then falsie, example:

x=1
y=1
z= x==1 and y==1
if 0:
    result=3*4
else:
    result=1
print('result= ', result)

# would print out if result (12) because it's a truthy 

# while loop example
i=0 
total = 0 
while i<5:
    total = total + i
    i=i+1
print('total', total)

# result would be print('total= ', total) keep track of variables, use updated total every time

# introduction to for loops, REVIEW 

total = 0
for i in range(5):
    total=total-1
print('tota= ', total)

