#!/usr/bin/env python
# coding: utf-8

# # Exercise 6 - More loops
# 
# We have already encountered one way of repeating calculations - the `while` loop. Python also provides a second kind of loop, the `for` loop. This allows us to do a calculation for each of the entries in a list, tuple or dictionary.
# 
# Typically, a `for` loop takes the form:
# ```python
# for <variable> in <collection>:
#     [calculations using <variable>]
# ```
# As with the `while` loop, everything within the indented block is executed multiple times, with the `<variable>` getting set equal to a different element of `<collection>` on each pass. `<collection>` may be any 'iterable', such as a list. For example, the following code would calculate the sum of all the entries in `a`:
# ```python
# a = [1, 5, 9]
# s = 0
# for x in a:
#     s += x
#     print(x, s)
# print("Total is:", s)
# ```
# It is possible to use `continue` and `break` statements within a `for` loop, just as in a `while` loop.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Often, we simply want to perform a calculation $n$ times, counting off as we go. To allow this, Python provides the `range` function, which is a special kind of iterable. It can be used as follows:
# ```python
# n = 20
# for i in range(n):
#     print(i)
# ```
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# You should have seen that by default, the counting starts from 0, and continues up to $n-1$ (so that there are a total of $n$ passes through the loop). If you want to start from a different number, you can provide this:
# ```python
# istart = 3
# istop = 15
# for i in range(istart, istop):
#     print(i)
# ```
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Notice that the counting starts with `istart`, and finishes with `istop-1`. We can also count in increments of `istep`:
# ```python
# istart = 3
# istop = 15
# istep = 4
# for i in range(istart, istop, istep):
#     print(i)
# ```
# This will print `istart`, `istart + istep`, `istart + 2*istep` etc, but not any value equal to or greater than `istep`.
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# The value of $\pi$ can be found via an infinite sum
# $\pi = 2 \sum_{k=0}^\infty 2^k (k!)^2 / (2k+1)!$, 
# where $n!$ denotes the factorial of $n$, i.e., $n! = n(n-1)(n-2)\ldots 1$. This can be computed by initialising a variable to contain the value `1`, and then looping through the integers up to `n` multiplying the variable by each.
# 
# **&#10148; By summing the first $N$ terms in the series, compute an approximation to $\pi$ and explore how the accuracy of the approximation changes with $N$.** A good starting point is $N = 20$.

# In[ ]:


# Try it here!


# Often, we may need to iterate through a collection of objects (such as a list), but also keep a count of how many objects we have dealt with. There are various ways this could be done - one might be:
# ```python
# a = [3, 5, 7]
# for i in range(len(a)):
#     print("Object number", i, " is ", a[i])
# ```
# However, Python provides the `enumerate` function for precisely this purpose:
# ```python
# a = [3, 5, 7]
# for i, ai in enumerate(a):
#     print("Object number", i, " is ", ai)
# ```
# The iterable created by `enumerate` returns a tuple of `(index, object)` pairs, which can be assigned to a pair of variables (here, `i` and `ai`).
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Another common circumstance is that we have two (or more) collections, and we want to access the $i$-th element of each simultaneously. Again, this could be achieved using something like:
# ```python
# a = [3, 5, 7]
# b = ['a', 'b', 'c']
# for i in range(len(a)):
#     print("The letter associated with ", a[i], " is ", b[i])
# ```
# but Python also provides the `zip` function for this purpose: 
# ```python
# a = [3, 5, 7]
# b = ['a', 'b', 'c']
# for ai, bi in zip(a, b):
#     print("The letter associated with ", ai, " is ", bi)
# ```
# This creates an iterator which returns a tuple on each iteration, containing the $i$-th element of each of the collections passed to `zip`. The elements of this tuple can be assigned to variables (here, `ai` and `bi`).
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Finally, a `for` loop can be used to build a list using the following shorthand:
# ```python
# <list> = [ <expression involving variable> for <variable> in <collection> ]
# ```
# e.g.
# ```python
# a = [i**2 for i in range(3, 13, 2)]
# ```
# This is sometimes known as a `list comprehension`. A tuple can be built similarly
# ```python
# a = tuple(i**2 for i in range(3, 13, 2))
# ```
# and
# ```python
# a = {x:y for x, y in zip(['a', 'b', 'c'], [1, 2, 3])}
# ```
# can be used to construct a dictionary.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Another infinite series generating $\pi$ is given by Madhava of Sangamagrama:
# $\pi = \sqrt{12}\sum_{k=0}^\infty (-3)^{-k} / (2k+1)$.
# 
# **&#10148; By computing the first $N$ terms of this expression, and comparing them to the first $N$ terms of the expression given earlier, determine which series converges faster (i.e., which gives better results for small $N$?).**

# In[ ]:


# Try it here!


# ## Prime numbers
# 
# The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is a method for finding prime numbers (i.e., integers which are not divisible by any other integers except themselves and one).  Suppose you want to find all the prime numbers less than or equal to 25. First, you write down a list of all the numbers from 2 up to 25:
# ```text
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# ```
# Now, you start crossing out numbers. First, we consider the first entry in the list, 2. We keep this, but cross out every second number thereafter:
# ```text
# 2 3 X 5 X 7 X 9 X 11 X 13 X 15 X 17 X 19 X 21 X 23 X 25
# ^Start here
# ```
# We move our pointer to the next not-crossed-out number, 3. We then cross out every 3rd entry (counting ones that are already crossed out):
# ```text
# 2 3 X 5 X 7 X X X 11 X 13 X X X 17 X 19 X X X 23 X 25
#   ^Start here
# ```
# The next not-crossed out number is 5, so we remove every 5th entry:
# ```text
# 2 3 X 5 X 7 X X X 11 X 13 X X X 17 X 19 X X X 23 X X
#       ^Start here
# ```
# If we continue this procedure, we will find that we do not cross out any more numbers. The remaining numbers - 2, 3, 5, 7, 11, 13, 17, 19 and 23 - are all the primes less than (or equal to) 25.
# 
# **&#10148; Write a function that takes a single input, $N$, and returns the list of all prime numbers less than $N$.**

# In[ ]:


# Try it here!
