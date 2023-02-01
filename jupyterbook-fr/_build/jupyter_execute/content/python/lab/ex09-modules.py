#!/usr/bin/env python
# coding: utf-8

# # Exercise 9 - Modules
# 
# So far, almost everything we have used or encountered has been a core element of the Python language. By now, we know enough to be able to accomplish almost any computational task. However, writing all the code from scratch can be a time-consuming affair. One of the great attractions of Python as a programming language for scientific development is the ready availability of a large number of 'modules' - ready-to-use collections of functions - which provide good-quality code for most common tasks.
# 
# To use code from a module, you need to import it. This is conventionally done at the start of your Python file, although in principle it can be done at any point before you need to use functions from the module. There are several variant forms of import statement, but the simplest is
# ```python
# import <modulename> 
# ```
# where `<modulename>` is the name of the module you wish to use. Once you have done this, you can access functions within the module by typing `<modulename>.<function>()`. For example, the `datetime` module provides a range of functions to work with date and/or time information. To calculate the amount of time elapsed between 10am on 24 September 2018 (when this course started) and its conclusion at 4pm on 5 October, we can do the following:
# ```python
# import datetime
# a = datetime.datetime(2018, 9, 24, 10, 0, 0) # Year/Month/Day/Hour/Min/Sec
# b = datetime.datetime(2018, 10, 5, 16, 0, 0)
# print(b - a)
# ```
# Here, we are using a `datetime()` function within the `datetime` module. 

# In[ ]:


# Try it here!


# Sometimes, modules have long names and we expect to make heavy use of the module's functions. In this case, we might find having to preface each function name with the full module name rather tedious. Python therefore allows us to assign a shorthand name to any module when we import it, by adding `as <shortname>` after the `import` statement. For example, in a later exercise we will use the module `matplotlib.animation` to generate animations. We will import this as follows:
# ```python
# import matplotlib.animation as anim
# a = anim.FuncAnimation(...)
# ```
# If we did not use `as anim` when we imported the module, we would have to type `a = matplotlib.animation.FuncAnimation(...)` - which gets tedious rather quickly.
# 
# Sometimes, we know we only wish to use one or two functions from a module. In this case, we may prefer not to import the entire module, but instead use
# ```python
# from <module> import <function1>, <function2>
# ```
# This makes `<function1>` and `<function2>` available in our program, and we do not need to preface them by any module name. For example, the `math` module provides a number of functions for mathematical operations. If we just want to be able to compute exponentials and sines, we could do
# ```python
# from math import exp, sin
# a = exp(3) * sin(1.6)
# print(a)
# ```
# but we would not have access to anything else within the `math` library.
# 

# In[ ]:


# Try it here!


# The reason Python requires you to preface function calls with the module name, or import specific functions, is to avoid 'namespace clashes', where two functions with the same name are loaded. For example, many modules might provide a function called `save`, which does something appropriate to that module's purpose. By encouraging you to specify `<module>.save()`, or specifically import a `save` routine from one particular module, Python tries to avoid the bugs and confusion that could otherwise occur.
# 
# However, if you really want to expose all the functions in a module, Python allows you to use an import statement of the form
# ```python
# from <module> import *
# ```
# This works in exactly the same way as `from <module> import <function>`, except that it uses the 'wild-card' character `*` to indicate that *everything* in the module should be made available. A few modules are intended to be used in this way, but in general, it is best avoided unless you have a reason to need it.
# 
# ## Getting to grips with `datetime`
# 
# An important skill is to be able to work out what a particular module does, and how to use it, without being taught about it. 
# 
# **&#10148; Write a program that asks the user to enter their birth date, and then calculates how long it will be until their next birthday.**
# 
# You will need to use the [official documentation](https://docs.python.org/3.6/library/datetime.html) for the `datetime` module, as well as [other resources](http://www.google.com.au). You will find the `datetime.datetime.strptime()` and `datetime.datetime.now()` functions useful.

# In[ ]:


# Try it here!


# ## NumPy
# 
# An important module (or, really, collection of modules) for scientists is NumPy ('Numerical Python'). This provides a wide range of tools and data structures for working with numerical data, and for implementing matrix-vector calculations.
# 
# It is conventional to use `import numpy as np` when importing NumPy. NumPy then provides a fairly comprehensive set of mathematical functions, including
# - `np.sin()`, `np.cos()`, `np.tan()` - Trigonometric functions
# - `np.arcsin()`, `np.arccos()`, `np.arctan()` - Inverse trigonometric functions
# - `np.arctan2()` - [Two-argument version of the inverse tangent function](https://en.wikipedia.org/wiki/Atan2) that returns value in the correct quadrant
# - `np.sinh()`, `np.cosh()`, `np.tanh()`, `np.arcsinh()`, `np.arccosh()`, `np.arctanh()` - Hyperbolic functions and their inverses
# - `np.exp()`, `np.log()` - Exponentiation and its inverse, the natural logarithm
# - `np.log10()` - Logarithm to base-10
# 
# NumPy also provides some mathematical constants, including `np.pi` and `np.e`.

# In[ ]:


# Try it here!


# However, the core feature of NumPy is the array data type. This allows us to create structured grids containing data, which can then be accessed, transformed and used efficiently. Where numerical data is to be stored or processed, a NumPy array is likely to be the most effective mechanism to use. There are two main ways to create an array. First, we can use the `np.array()` function, to build an array from a list (or similar):
# ```python
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a)
# print(b)
# ```
# Second, we can use various functions that create 'standard' arrays:
# - `np.ones(dims)` - Array filled with elements equal to `1`
# - `np.zeros(dims)` - Array filled with elements equal to `0`
# - `np.eye(N)` - $N \times N$ identity matrix (ones on diagonal, zero otherwise)
# - `np.arange(start, stop, step)` - Create ascending sequence of numbers from `start`, in intervals of `step`, finishing before `stop`. If only two (unlabelled) arguments are given, it is assumed that `step=1`. If only one argument is given, it is additionally assumed that `start = 0`.
# - `np.linspace(start, stop, N)` - Create an array containing $N$ equally-spaced points, with the first one being at `start`, and the last being at `stop`.
# 
# Here, `dims` is a list or tuple specifying the number of elements in each dimension of the array: for example,
# `np.ones([3])` creates a one-dimensional array, identical to `np.array([1, 1, 1])`, whereas `np.zeros([3, 6, 2, 2, 3])` creates a five-dimensional array filled with zeros.
# 
# Many of the array-creation routines take an optional argument, `dtype=type`, where `type` is a string. This specifies the data type which can be stored in the array. For example, `np.ones([3, 3], dtype='int')` creates an array of integer type, while `np.zeros([3, 3], dtype='bool')` creates an array of Boolean (True/False) values, initialised to `False`.
# 
# **&#10148; Try each of these ways of building an array, and make sure you understand how they work.**

# In[ ]:


# Try it here! 


# Array elements can be accessed using `[...]` and a (zero-based) index for each dimension, or `:` to denote all elements within that dimension: we can thus obtain arrays that are a subset of a larger array.
# ```python
# a = np.array([3, 4, 5])
# print(a[2]) # Prints 5
# b = np.zeros([3, 4, 4, 2, 4])
# print(b[:, 3, 3, :, 0]) # Prints a 3 x 2 matrix of zeros
# b[:, 3, 3, :, 0] = np.ones([3, 2])
# print(b[:, :, 3, 0, 0]) # Prints 3 x 4 matrix with column of zeros
# ```
# As we have already seen with lists, it is possible to specify a limited range of any index by using syntax of the form `start:stop:step`.

# In[ ]:


# Try it here! 


# NumPy also provides tools for linear algebra - for example, if `a` and `b` are 1-D arrays that represent vectors, we can compute the dot product using `a.dot(b)`. We will not discuss linear algebra here; for more details, there are many resources [such as this one](http://people.duke.edu/~ccc14/pcfb/numpympl/LinearAlgebra.html) online.
# 
# One very useful feature of NumPy is that it has various functions to help read and write data from files without the hassle of doing it yourself. If you have a plain text file that contains a dataset as columns, you can call `np.loadtxt(filename)`. This will automatically open the file, read it, and return its contents in a NumPy array. If your file has a 'header' containing information in a different format from the main data table, you may need to tell NumPy to ignore some rows: this is done by passing the argument `skiprows = <number to skip>` to `np.loadtxt()`. Similarly, there is an `np.savetxt()` function which will write the contents of an array to a plain text file.
# 
# **&#10148; Use `np.loadtxt()` and `np.savetxt()` to repeat Exercise 8.** Notice how much easier it is!

# In[7]:


# Try it here!


# There are many other useful modules. Some key ones include:
# - `scipy` - a large collection of tools for accomplishing a wide range of mathematical and scientific tasks
# - `matplotlib` - Plotting figures
# - `stats` - statistical calculations
# - `pandas` - working with datasets
# 
# We will meet some of these in later exercises.

# ## Creating new modules
# 
# You can also create your own modules. This allows you to 'package up' functions that you use regularly, and re-use them in different programs. This is much better than routinely copying and pasting functions from one file to another, which usually ends up leading to confusion: one inevitably ends up with multiple versions of the function that all work in slightly different ways. By using a module, you guarantee that all programs that use it 'see' the same function. Note that Python's ability to have 'optional' function arguments, with default values (`def function(..., var1=default1,  var2=default2...)`) is often very useful for adding enhancements to a function without breaking any existing programs.
# 
# To create a module, you simply create a plain text file (using a text editor, or by selecting `New > Text File` within Jupyter's file browser window), and name it `<desired module name>.py`. Place whatever functions you wish to include within the module in this file, and save it. Then, you will be able to `import <module name>` and access the functions, as with any other module.
# 
# **&#10148; Package your birthday calculator into a module, and test it.**

# In[ ]:


# Try it here!


# Further information on Python modules is available in the [Python documentation](https://docs.python.org/3/tutorial/modules.html). At a later stage, if you create a significant module that is not available, you can contribute to the community by providing the module online through PyPi. Python is based on a free, open source framework with many libraries developped by people like you. So contributions are welcomed and important!
