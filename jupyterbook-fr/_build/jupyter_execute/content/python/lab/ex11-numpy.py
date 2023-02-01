#!/usr/bin/env python
# coding: utf-8

# # Exercise 11 - NumPy
# 
# An important module (or, really, collection of modules) for scientists is NumPy ('Numerical Python'). This provides a wide range of tools and data structures for working with numerical data, and for implementing matrix-vector calculations.
# 
# It is conventional to use `import numpy as np` when importing NumPy. NumPy then provides a fairly comprehensive set of mathematical functions, including:
# - `np.sin()`, `np.cos()`, `np.tan()` - Trigonometric functions,
# - `np.arcsin()`, `np.arccos()`, `np.arctan()` - Inverse trigonometric functions,
# - `np.arctan2()` - [Two-argument version of the inverse tangent function](https://en.wikipedia.org/wiki/Atan2) that returns value in the correct quadrant,
# - `np.sinh()`, `np.cosh()`, `np.tanh()`, `np.arcsinh()`, `np.arccosh()`, `np.arctanh()` - Hyperbolic functions and their inverses,
# - `np.exp()`, `np.log()` - Exponentiation and its inverse, the natural logarithm,
# - `np.log10()` - Logarithm to base-10,
# - and many more.
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
# - `np.ones(dims)` - Array filled with elements equal to `1`.
# - `np.zeros(dims)` - Array filled with elements equal to `0`.
# - `np.eye(N)` - $N \times N$ identity matrix (ones on diagonal, zero otherwise).
# - `np.arange(start, stop, step)` - Create ascending sequence of numbers from `start`, in intervals of `step`, finishing before `stop`. If only two (unlabelled) arguments are given, it is assumed that `step=1`. If only one argument is given, it is additionally assumed that `start=0`.
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


# Arrays can be useful for storing almost any sort of structured data. However, one important use is to represent vectors and matrices for linear algebra. Python does not provide special data types for these, but instead a 1-D array may be regarded as a vector, and a 2-D array as a matrix.
# 
# In standard Cartesian coordinates $(x, y, z)$, an anti-clockwise rotation by an angle $\theta$ about the $z$-axis can be represented by the rotation matrix
# 
# $$ \mathbf{R}_{z}(\theta) = \left(\begin{array}{ccc}\cos\theta & -\sin \theta & 0\\\sin\theta & \cos\theta & 0\\0 & 0 & 1\end{array}\right)$$
# 
# **&#10148; Write a function that returns this rotation matrix for any given angle.** You may find the function `np.deg2rad()` useful for converting angles between degrees and radians (its inverse is `np.rad2deg()`).

# In[ ]:


# Try it here


# We can now rotate any vector by multiplying it by this rotation matrix. However, you will notice that simply using the `*` operator does not work (can you work out what it does do?). Instead, you need to use the `.dot()` method provided by NumPy arrays, which does matrix multiplication:
# ```python
# def rotation_about_z(theta):
#     ...
#     return R
# 
# v = np.array([1, 0.1, 3]) # Vector
# R = rotation_about_z(20)
# rotated_v = R.dot(v)
# ```

# In[ ]:


# Try it here


# Rotations about the $x$ and $y$ axes may be represented by the rotation matrices
# 
# $$\mathbf{R}_{x} = \left(\begin{array}{ccc}1 & 0 & 0\\0 & \cos\theta & -\sin\theta\\0 & \sin\theta & \cos\theta\end{array}\right) \hspace{2cm}\mathbf{R}_{y} = \left(\begin{array}{ccc}\cos\theta & 0 & -\sin\theta\\0 & 1 & 0\\\sin\theta&0&\cos\theta\end{array}\right)$$
# 
# respectively. 
# 
# **&#10148; Write functions to generate these rotation matrices.**

# In[ ]:


# Try it here


# If an object is rotated several times, we simply need to multiply the appropriate rotation matrices together to get a 'compound' rotation matrix describing the overall transformation. However, it is important to do the rotation in the correct order, since matrix multiplication is not commutative (i.e., $\mathbf{AB}\ne\mathbf{BA}$). If the *first* rotation is by an angle $\alpha$ about axis $i$, and then the next rotation is by angle $\beta$ about axis $j$, the compound rotation matrix is $\mathbf{R}_j(\beta)\,\mathbf{R}_i(\alpha)$, and we should call `Rj.dot(Ri)` - that is, the first rotation is at the right. If we then rotate the object again, by an angle $\gamma$ about axis $k$, we would need $\mathbf{R}_k(\gamma)\,\mathbf{R}_j(\beta)\,\mathbf{R}_i(\alpha)$ or `Rk.dot(Rj.dot(Ri))`.
# 
# **&#10148; Write a function that takes a list of (axis, angle) tuples, and computes the appropriate compound rotation.** The rotations should be applied in the order that they appear in the list, so that the first entry in the list is the *right-most* rotation matrix in the product. Rotation axes will be specified as letters, `'x'`, `'y'` or `'z'`.

# In[ ]:


# Try it here!


# A triangle has corners at the origin, point $(2,1,0)$ and point (-1,-1,0). It undergoes several rotations. First, it is rotated about the $x$-axis by $30^\circ$, then about the $z$-axis by $15^\circ$. It is then rotated again by $5^\circ$ about the $x$-axis, then by $120^\circ$ about the $y$-axis. Finally, it is rotated by $-25^\circ$ about the $x$-axis once more. Demonstrate that after all the rotations, its corners are now at approximately $(0,0,0)$, $(-1.34,1.68,0.51)$ and $(0.88,-1.10,0.13)$.
# 

# In[ ]:


# Try it here!


# We will return to this exercise once we have learned how to plot figures.
# 
# Numpy also provides some useful routines for reading and writing files. In particular, `np.loadtxt()` provides an easy way to read simple plain-text data files such as those we encountered in Exercise 8. 
# 
# **&#10148; Try using `np.loadtxt()` to read and process the data file from Exercise 8.** Compare your solution to that from the earlier exercise. Which is simpler?
# 
# 

# In[ ]:


# Try it here!


# For saving plain-text files, Numpy provides a `np.savetxt()` routine. If you do not need your file to be human-readable, you can also use `np.save()` and `np.load()` to store and re-load arrays:
# ```python
# a = np.array([3, 4, 5])
# np.save('test.npy', a)
# b = np.load('test.npy')
# print(b)
# ```
# This is a fast and convenient way to retain data for use within your program. 

# In[ ]:


# Try it here!


# ## Test your mastery of numpy !
# 
# This exercise might be interesting as it tests your ability to understand loops and arrays. It is a little more challenging than many of the ones we have encountered so far, and you can skip it if you feel your time would be better spent elsewhere. However, if you have been finding the course easy it should be a fun challenge.
# 
# Can you write a [**Sudoku Solver**](Ex11a-Sudoku.ipynb) ?

# In[ ]:




