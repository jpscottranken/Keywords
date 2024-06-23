"""
The global.py program demonstrates:
1.  import
2.  as
3.  global
4.  multiline Python comments (""" """)
"""

import numpy as np

x = 5

def test1():
  x = 100
  print(x)

test1()
print(x)    # 5

y = 5

def test2():
  global y 
  y = 100
  print(y)

test2()
print(y)    # 100
