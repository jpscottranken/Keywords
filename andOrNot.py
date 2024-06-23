"""
The andOrNot.py program demonstrates:
1.  import
2.  as
3.  print
4.  and or not
5.  multiline Python comments (""" """)
"""

firstNumber = 12
secondNumber = 25

if (firstNumber > 10 and secondNumber < 100):
  print('Both Conditions Met')
else:
  print('One Or Both Conditions NOT Met')

if (firstNumber < 10 or secondNumber > 100):
  print('Both Conditions Met')
else:
  print('One Or Both Conditions NOT Met')

if not(firstNumber > 10 and secondNumber < 100):
  print('Both Conditions Met')
else:
  print('One Or Both Conditions NOT Met')

