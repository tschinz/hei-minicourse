#!/usr/bin/env python
# coding: utf-8

# # Exercise 11 - Sudoku
# 
# This exercise is a little more challenging than many of the ones we have encountered so far, and you can skip it if you feel your time would be better spent elsewhere. However, if you have been finding the course easy it should be a fun challenge.
# 
# You are probably all familiar with Sudoku - the Japanese puzzle where you put numbers into a 9 x 9 grid. The rules are:
# - Each row must contain each of the numbers 1-9 exactly once
# - Each column must contain each of the numbers 1-9 exactly once
# - Each of the 9 3 x 3 sub-blocks of the grid must contain each of the numbers 1-9 exactly once.
# 
# Can you write a computer program to solve any Sudoku?
# 
# To get you started, here is an example Sudoku grid (using `0` to indicate a blank cell:
# ```python
# sudoku = np.array([[5,3,0,0,7,0,0,0,0],
#                    [6,0,0,1,9,5,0,0,0],
#                    [0,9,8,0,0,0,0,6,0],
#                    [8,0,0,0,6,0,0,0,3],
#                    [4,0,0,8,0,3,0,0,1],
#                    [7,0,0,0,2,0,0,0,6],
#                    [0,6,0,0,0,0,2,8,0],
#                    [0,0,0,4,1,9,0,0,5],
#                    [0,0,0,0,8,0,0,7,9]])
# ```
# You can find more grids online.
# 
# *Hint:* Break the task down into pieces. Start by writing a function that displays Sudoku grids nicely. Next, write one that checks whether a grid is complete, or contains errors. Then think about the various steps involved in solving the Sudoku, and implement these one-at-a-time.

# In[ ]:


import numpy as np

# Try it here!


# In[ ]:




