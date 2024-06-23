"""
The calculator01.py program demonstrates:
1.  import
2.  as
3.  if
4.  def
5.  return
6.  print
7.  str
8.  multiline Python comments (""" """)
"""

import numpy as np

# Create two variables. Each is a 
# random number between 1 and 100.
number1 = np.random.randint(1,100)
number2 = np.random.randint(1,100)

# Set two temporary variables
temp1 = number2
temp2 = number1

"""
If necessary (number1 < number2),
flip the values, i.e. put the
original value of number1 into
number2 and the original value
of number2 into number1
"""
if(number1 < number2):
  number1 = temp1
  number2 = temp2

# Add the 2 numbers together
def add2(n1, n2):
  return n1 + n2

# Subtract second number from first
def subtract2(n1, n2):
  return n1 - n2

# Multiply first number by second
def multiply2(n1, n2):
  return n1 * n2

# Divide first number by second
def divide2(n1, n2):
  return n1 / n2

# Divide first number by second
# "throw away" any remainder
def intDivide2(n1, n2):
  return n1 // n2

# Divide first number by second
# display remainder
def mod2(n1, n2):
  return n1 % n2

# Raise first number to second number
def expo2(n1, n2):
  return n1 ** n2

# Call the calculator functions above
print(str(number1) + ' + '  + str(number2) + ' = ' + str(add2(number1, number2)))
print(str(number1) + ' - '  + str(number2) + ' = ' + str(subtract2(number1, number2)))
print(str(number1) + ' * '  + str(number2) + ' = ' + str(multiply2(number1, number2)))
print(str(number1) + ' / '  + str(number2) + ' = ' + str(divide2(number1, number2)))
print(str(number1) + ' // ' + str(number2) + ' = ' + str(intDivide2(number1, number2)))
print(str(number1) + ' % '  + str(number2) + ' = ' + str(mod2(number1, number2)))
print(str(number1) + ' ** ' + str(number2) + ' = ' + str(expo2(number1, number2)))
