"""
The selection.py program demonstrates:
1.  import
2.  as
3.  if, elif, else
4.  print
5.  multiline Python comments (""" """)
"""

import numpy as np

def matchTest(size):
  match size:
    case 'small':
      print('match size small')
    case 'medium':
      print('match size medium')
    case 'large':
      print('match size large')

def ifTest(size):
  if(size =='small'):
      print('if size small')
  elif (size == 'medium'):
      print('if size medium')
  elif (size == 'large'):
      print('if size large')
  else:
    print('Unknown size')

matchTest('large')
ifTest('small')