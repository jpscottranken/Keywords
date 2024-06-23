"""
The iteration.py program demonstrates:
1.  import
2.  as
3.  def
4.  print
5.  for
6.  while
7.  multiline Python comments (""" """)
"""

import numpy as np

def forTest():
  print('for test. Should print 0 - 4')
  for i in range(5):
    print(i)

def whileTest():
  print('while test. Should print 1 3 4 5')
  n = 0

  while n < 5:
    n += 1
    if (n == 2):
      continue
    print(n)

forTest()
whileTest()