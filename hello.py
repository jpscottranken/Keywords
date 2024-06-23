# This is the original program created
# in the video. Later, I broke each
# individual "piece" into its own program.

import numpy as np

# Create two variables. Each is a 
# random number between 1 and 100.
number1 = np.random.randint(1,100)
number2 = np.random.randint(1,100)

x = 5

def test():
  x = 100
  print(x)

test()
print(x)    # 5

y = 5

def test():
  global y 
  y = 100
  print(y)

test()
print(y)    # 100

# Structured Programming
# Sequence
# Selection - if, if elif, if elif else, if else
# Iteration - for while

#for i in range(6):
#  print(i)

#n = 0

#while n < 5:
#  n += 1
#  if (n == 2):
#    continue
#  print(n)

#size = 'medium'

#match size:
#  case 'small':
#    print('match size small')
#  case 'medium':
#    print('match size medium')
#  case 'large':
#    print('match size large')

#if(size =='small'):
#    print('if size small')
#elif (size == 'medium'):
##    print('if size medium')
#elif (size == 'large'):
#    print('if size large')

first = 1
second = 'Hello'
third = 3.1416
fourth = True

#print (type(first))
#print (type(second))
#print (type(third))
#print (type(fourth))

#isMarried = True
#isDivorced = False

#if (isMarried):
#  print('The individual is married')
#else:
#  print('The individual is not married')

#firstNumber = 12
#secondNumber = 25

#thirdNumber = np.random.randint(0,100)
#if(thirdNumber == 0):
#  print('0 is neither odd nor even')
#elif (thirdNumber % 2 == 0):
#  print('The number ' + str(thirdNumber) + ' is even')
#else:
#  print('The number ' + str(thirdNumber) + ' is odd')


#if (firstNumber > 10 and secondNumber < 100):
#  print('Both Conditions Met')
#else:
#  print('One Or Both Conditions NOT Met')

#if (firstNumber < 10 or secondNumber > 100):
#  print('Both Conditions Met')
#else:
#  print('One Or Both Conditions NOT Met')

def add2(n1, n2):
  return n1 + n2

def subtract2(n1, n2):
  return n1 - n2

def multiply2(n1, n2):
  return n1 * n2

def divide2(n1, n2):
  return n1 / n2

#def intDivide(n1, n2):
  #return n1 \ n2

def mod2(n1, n2):
  return n1 % n2

def expo2(n1, n2):
  return n1 ** n2

#def hello():
#  print('hello')

#x = hello()  # hello

#print(x)     # None


# calling (using) the function hello
#print('The first  number is: ' + str(number1))
#print('The second number is: ' + str(number2))
#print(add2(number1, number2))
#print(subtract2(number1, number2))
#print(multiply2(number1, number2))
#print(divide2(number1, number2))
#print(mod2(number1, number2))
#print(expo2(number1, number2))
