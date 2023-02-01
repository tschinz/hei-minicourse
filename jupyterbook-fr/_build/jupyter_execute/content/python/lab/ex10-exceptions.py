#!/usr/bin/env python
# coding: utf-8

# # Exercise 10 - Exception handling
# 
# By now, you will almost certainly have encountered 'exceptions' - the error messages that appear when you ask Python to do something that it doesn't like. For example, the following code will raise an exception:
# ```python
# a = [1, 2, 3]
# print(a[4])
# ```
# Attempting to execute this code results in some text similar to this:
# ```text
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-1-ba5ce40e4136> in <module>()
#       1 a = [1, 2, 3]
# ----> 2 print(a[4])
# 
# IndexError: list index out of range
# 
# ```
# The error here is that we have tried to access the 5th element of `a` (remember, counting starts from zero!), but `a` only contains three entries.
# 
# Another example might be
# ```python
# a = 1 + 'hello'
# ```
# which generates
# ```text
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-2-41d1b959c123> in <module>()
# ----> 1 1 + 'hello'
# 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ```
# Notice that these two error messages have different headlines: the first is an `IndexError`, whereas the second is a `TypeError`. You will notice that a variety of other kinds of error exist.
# 
# If these errors are simply coding mistakes, it is useful to have the program terminate immediately, so we can fix it. However, in 'real' code these sorts of problem may arise for reasons beyond the programmer's control - perhaps the user has provided an incorrect set of inputs, for example. It is therefore often useful to be able to 'catch' and 'handle' exceptions in a graceful manner.
# 
# To do this, Python provides the `try... except...` construct. This looks like:
# ```python
# try:
#     [code that may fail]
# except:
#     [code to handle the error]
# ```
# When a `try...except...` construct is encountered, Python first attempts to execute all the code within the indented `try` block. If this is successful, the code within the `except` block is never executed. However, as soon as an error is encountered, Python stops attempting to execute the `try` block, and jumps immediately to the first line in the `except` block. It executes everything in the `except` block, and then (assuming no more errors arise) continues with the first line *after* the `try...except...` construct.
# 
# So, for example:
# ```python
# try:
#     x = float(input('Please enter a number: '))
#     print("The next number is: ", x+1)
# except:
#     print("Sorry, that is not a valid number")
# ```
# will gracefully handle cases where the user types text into the input field.
# 
# **&#10148; Try it out!** Compare how Python behaves with, and without, the `try...except...` construct.

# In[ ]:


# Try it here!


# This kind of error handling is sometimes referred to as the 'EAFP' model: "easier to ask forgiveness than permission". Rather than attempting to verify that everything is correct *before* carrying out an operation - a process which can be tedious and computationally inefficient - we start by assuming everything will work, and then deal with any mess that we create.
# 
# Our `try... except...` statement above will handle *any* kind of error that might arise. This may seem superficially attractive, but it can lead to confusion. For example, suppose we had made a typo in our code, referring to a variable `z` (which doesn't exist):
# ```python
# try:
#     x = float(input('Please enter a number: '))
#     print("The next number is: ", z+1)
# except:
#     print("Sorry, that is not a valid number")
# ```
# Now, this will always complain that we have entered an invalid number - even though this is not the real problem. If we remove the `try... except...` we see that this code is triggerring a `NameError`, rather than the `ValueError` that we intended to avoid. If this were 'real' code, we might waste a lot of time trying to understand why Python thought we were entering invalid numbers.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# To avoid this, we can specify what sort of error(s) the `except` block is intended to handle:
# ```python
# try:
#     x = float(input('Please enter a number: '))
#     print("The next number is: ", z+1)
# except ValueError:
#     print("Sorry, that is not a valid number")
# ```
# Now, our typo will be obvious when we try and run the code, but once it is fixed everything will work as expected. If necessary, we can have one `except` that catches multiple types of exception
# ```python
# try:
#     [code]
# except ValueError, TypeError:
#     [code]
# ```
# and we can have multiple `except` blocks to handle different errors in different ways:
# ```python
# try:
#     [code]
# except ValueError:
#     [code]
# except TypeError:
#     [code]
# except:
#     [code]
# ```
# In the above example, the 'bare' `except` at the end is optional, and will catch all errors that do not match one of the 'named' exception handlers. For example
# ```python
# try:
#     x = float(input('Please enter a number: '))
#     print("The next number is: ", z+1)
# except ValueError:
#     print("Sorry, that is not a valid number")
# except:
#     print("Something unexpected happened")
# ```
# will catch the error arising from our typo.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Exception handling can sometimes be a central part of your code design. Suppose you need to write a piece of code to sum up the entries in a list (and you have forgotten that Python's `sum()` function exists to do this). One solution (the cleanest, and so the best) would be to loop over the entries in the array:
# ```python
# a = [1, 3, 6]
# s = 0
# for x in a:
#     s += x
# print(s)
# ```
# However, you could also write something like:
# ```python
# a = [1, 3, 6]
# i = 0
# s = 0
# while True:
#     try:
#         s += a[i]
#     except IndexError:
#         break
#     i+=1
# print(s)
# ```
# While this is unnecessarily complicated for such a straightfoward example, it illustrates how exception-handling can be used to control the flow of a program.

# In[ ]:


# Try it here!


# It is tempting to overuse `try...except...` clauses, to supress Python's built-in errror messages. Generally this will be a mistake, as it will make it harder to identify the causes of bugs. It is best to only use `try...except...` when necessary to handle 'predictable' error cases, or in production code.
# 
# **&#10148; In Exercise 4, you made a guessing game. Using `try...except...`, adapt it so that if the user enters anything other than an integer, they are prompted to 'try again'.**

# In[ ]:


# Try it here!


# Sometimes, it is useful to be able to access more information about the exact error that occurred. This can be achieved by modifying the `except` statement:
# ```python
# try:
#     [code]
# except <ErrorType> as <variable>:
#     [code]
# ```
# As an example,
# ```python
# try:
#     x = 1 + 'hello'
# except TypeError as err:
#     print("There is an error")
#     print(err)
# ```
# Now, if a TypeError is raised, Python creates the variable `err` and sets it to contain some more detailed information about the error. We can then use this to give a more detailed report, or to help us handle the problem. Different types of error may store different information within the variable.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Sometimes, there may be code that you want to execute regardless of whether an error occurs or not. For example, you might wish to save some information about the stage your program has reached, or delete temporary files. To help with this, Python provides a variant of `try...except...`:
# ```python
# try:
#     [code]
# finally:
#     [code]
# ```
# The code within the `finally` block is *always* executed, either after everything in `try` has been successfully completed, or *before* an error is propagated. For example:
# ```python
# try:
#     s = 0
#     for x in [1, 2, 3, 'x']:
#         s += x
# finally:
#     print("This line is printed *before* the error is raised...")
#     print(s)
# ```
# If the `try...finally...` occurs in a function, and `finally` contains a `return `statement the error is never raised. Similarly, if `try...finally...` occurs in a loop, and `finally` contains a `break` statement, the error is discarded.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Python also allows you to `raise` errors within your code, triggering the error-handling mechanisms already described. This is achieved by the command
# ```python
# raise <ErrorType>
# ```
# or
# ```python
# raise <ErrorType>(<message>)
# ```
# For example,
# ```python
# raise IndexError
# ```
# or 
# ```python
# raise IndexError("This is just an example")
# ```
# 
# A file `some_data.txt` is present in this folder. Use the skills you acquired during the last exercises to build a function that loads this file and multiply the two columns together. Do the sum for each line. If the sum is different from 100, raise a ValueError with a message saying that the sum of columns should be 100.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# In conjunction with `try...except...`, `raise` can allow an effective mechanism for controlling program flow, since an exception raised within a function (within another function, within...) can be caught and handled at the top-most level. For example, one might write something like:
# ```python
# def check_consistency(datafile_lines):
#     # Checks whether datafile contents are self-consistent
#     [...]
#     if [...]:
#         # File is good
#         return True
#     else:
#         return False
#    
# def load_datafile(...):
#     # Load data from file
#     with open(datafile, 'r') as fp:
#         lines = fp.readlines()
#         [...]
#         if not check_consistency(lines): raise IOError("Datafile is not self-consistent")
#             
# def restart_calculation(...):
#     # Attempt to resume interrupted calculation
#     [...]
#     load_datafile(...)
#     [...]
# 
# def program_startup(...):
#     [...]
#     try:
#         restart_calcuation(...)
#     except IOError:
#         start_new_calculation(...)
# ```
# Here, the `program_startup` routine attempts to restart an existing, previous calculation based on information in a file, but if reading this file fails for any reason, it will simply start the calculation afresh. 
# 
# **➤ Earlier, you wrote some code to compute the sum of columns of a dataset. Using the structure described above, adapt this so that if the file doesn't exist, the dataset 
# `[[1.,99.],[2.,98.],[3.,97.]]` is processed instead.**

# In[ ]:


# Try it here!

