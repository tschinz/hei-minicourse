#!/usr/bin/env python
# coding: utf-8

# # Exercise 4 - Guessing Games 
# 
# *Andrew Valentine - andrew.valentine@anu.edu.au*
# 

# **&#10148; Try playing this simple game.**

# In[ ]:


import numpy as np
import sys
import os
sys.path.append(os.getcwd()+'/.hidden/')
import guessingGames as gg
gg.guessingGame(nmax=10)


# **&#10148; Can you write your own version?**
# 
# A couple of hints to help you:
# - To read input from the keyboard, you can use 
# ```python
# x = input(message)
# ```
# 
# where `message` is the prompt shown to the user (e.g. 'Make a guess:' in `gg.guessingGame`). Whatever the user types in gets stored in the variable `x`. Note that `x` contains a string of characters, even if the user types in a number. You can use `int(x)` to convert the input to an integer (and `float(x)` if you want to convert it to a floating-point number).
# 
#   - To generate a random integer, you can call the function `np.random.randint(lo,hi)` where `lo` is the smallest integer you want to generate, and `hi` is **one greater than** the largest integer.

# In[ ]:


# Try it here!


# What happens if the user types something in that isn't an integer? Can you make your version robust?

# **&#10148; Here's another one to play:**

# In[ ]:


gg.higherOrLower(nmax=100)


# **&#10148; Try writing your own version.**
# 
# You should be able to use the code you wrote for `guessingGame` as a starting point.

# In[ ]:


# Try it here!


# **&#10148; Here's a final one to try.**

# In[ ]:


gg.montyHall(3)


# **&#10148; Can you make your own version?**

# In[ ]:


# Try it here!

