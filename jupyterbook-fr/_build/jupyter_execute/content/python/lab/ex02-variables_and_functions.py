#!/usr/bin/env python
# coding: utf-8

# # Exercise 2 - Variables and functions
# 
# *Andrew Valentine - andrew.valentine@anu.edu.au*

# We saw in the last exercise that Python can do simple calculations, such as
# ```python
# 3 + 5
# 4 * 2.1
# 8 / 3
# 2 - 15.3
# 3**7
# ```
# On its own, this isn't terribly useful. However, we can store the results of calculations, by 'assigning' them to a 'variable'. To do this, we just need to type
# ```python
# nameForThisQuantity = 3 + 5
# ```
# We can use any name we want, provided it:
# 
# - Starts with a letter, and
# - Contains only the alphanumeric characters (a-z, A-Z, 0-9) and (if you wish) the underscore character, '_'. ***Note that variable names are case-sensitive, so `variablename`, `variableName` and `VariableName` are all treated as being distinct!***
# 
# Strictly, your variable names can also *begin* with an underscore. However, there is a convention among Python programmers that this is only done in special circumstances, which we won't encounter in this course.
# 
# The computer doesn't care what name you use. However, humans who have to look at your program will be much happier if you use names that describe what the quantity 'means'. The computer will treat these two examples identically: 
# 
# ```python
# azqg = 17.3
# bppe = 12.5
# cdoq = azqg * (1 + bppe/100)
# ```
# 
# ```python
# cost_before_tax = 17.3
# tax_rate = 12.5
# cost_after_tax = cost_before_tax * (1 + tax_rate / 100)
# ```
# 
# Which one do you find easier to understand? 
# 
# You may encounter code that looks more like (1) than (2). This is because early programming languages placed strict limits on the length of variable names. However, there is no longer any need for this!
# 
# ## Using variables 
# 
# As you may have noticed from the above example, once we have set the value of a variable, we can use it in calculations. Thus, 
# ```python
# x = 3
# y = 2
# print(x * y)
# ```
# will perform the calculation $(3\times 2) = 6$, and display the answer on the screen. If we wish, we can choose to assign the result to another variable, e.g.
# ```python
# x = 3
# y = 2
# z = x*y - y
# ```
# Now, `z` contains the value 4. We can also *reassign* the value of a variable, 
# ```python
# x = 3
# y = 2
# x = x + y
# ```
# Notice that `x` appears on both sides of the equals sign here. This should be read as 'do the calculation `x + y` and then store the result in `x` (over-writing whatever was there before)'. We end up with `x` containing the value $3 + 2 = 5$.
# 
# **&#10148; Try creating some variables, and using them in simple calculations.** Check that the results match what you expect.

# In[ ]:


# Try it here!


# In fact, constructs such as `x = x + y` are so common that Python has a special shorthand notation for this. We can express the same equation by entering `x += y`. There are similar versions for other operators: `-=`, `*=` and `/=`. 
# 
# **&#10148; Try out these shorthand operators.** Is `x += 3` the same as `3 += x`? Why?

# In[ ]:


# Try it here!


# There is no particular advantage to using these short forms, except convenience and readibility.
# 
# ## Naming Conventions 
# 
# You can call your variables anything you like. However, following a few conventions will improve the clarity of your code:
# 
# - If your variable name is made up of multiple words, either:
#     - Join them using underscores (e.g. `a_long_variable_name = 17`), or
#     - Capitalize the first letter of each word (e.g. `AnotherLongVariableName = 23.6`). This is sometimes referred to as 'camel case' (since it is lower case with extra humps!).
# - It is common to use UPPER CASE for constants that should never need to be changed within the program, e.g. `GRAVITATIONAL_ACCELERATION = 9.81`.
# - Traditionally, variables that contain integers have names beginning with the letters i, j, k, l, m, or n; variables containing real numbers start with any other letter. This comes from early programming languages (especially Fortran) where it was a requirement, and follows a similar convention in mathematics. Nowadays, this convention is often ignored for long variable names. However, if your name only contains one or two characters (e.g. `a` or `ix`), it is usual to choose the first letter appropriately. In particular, a bare `i`, `j`, `k`, `m` or `n` should only be used for a counting index (more on that later). If you ignore this rule, the program will work fine, but you can expect anyone who has to decipher your code in future to get very, very angry with you.
# 
# Some other tips:
# 
# - If your code is connected to another document (e.g. you are trying to plot some equation from a paper) then use clearly-related names in both. For example, if your paper has the equation $y = \alpha x +3\gamma$, then use the variable names `x`, `y`, `alpha` and `gamma` in your code. You can even use unicode.
# - Make your variable names long enough to be clearly understood, but not *too* long. At most, you probably want it to be based on two or three words.
# - Do not give your variable a name that has a special meaning in Python (e.g. `int` or `sum`). Doing so will not *always* cause problems, but it is a common source of grief. Fortunately, most text editors (including the one that is part of Jupyter) will highlight these 'reserved words' in a different colour, so you can avoid using them. For example:
# ```python
# x = 3   # x is in black; I can use it for a variable name.
# sum = 5 # sum is in green: it has a special meaning and would be a bad choice for a variable name
# ```
# 
# Above all, try and develop a consistent style, and name similar quantities in similar ways. For example, the following are individually all reasonable choices for variable names:
# ```python
# mass_of_helium = 4.003
# neon_mass = 20.180
# massArgon = 39.948
# mKrypton = 83.798
# mXe = 131.293
# ```
# However, mixing the different styles within one program is guaranteed to cause you confusion and lead to errors. Pick one format that makes sense to you, and stick with it.
# 
# ### Types 
# 
# As we have discussed, any variable has a **type**. We can ask Python to report on the type of a given variable by using the command `type(variable_name)`. For example,
# ```python
# a = 3
# type(a)
# ```
# will print `int` (shorthand for 'integer'), while
# ```python
# a = 3.0
# type(a)
# ```
# will print `float` (i.e., floating-point). We will encounter other types in due course.

# In[ ]:


# Try it here!


# ## Salary calculations
# 
# Let's try doing a realistic calculation. Suppose your annual salary is \$87,232, and the annual tax rate is 35%. How much money should be paid into your bank account every two weeks?
# 
# **&#10148; Calculate your fortnightly pay.** Remember, break the problem down into individual steps, and create variables for each of the quantities involved! You should find the answer is \$2,180.80.

# In[ ]:


# Try it here!


# Let's do something a bit more complicated. Suppose the tax rate is only 20% on the first \$30,000 that you earn, and 35% on the remainder. 
# 
# **&#10148; Copy your earlier code and adapt it for this case.** 

# In[ ]:


# Try it here!


# ## Functions
# 
# A **function** provides a convenient way to 'wrap up' code to accomplish a particular task. Once a function is written, it can (generally) be used without us needing to know anything about _how_ it works. This is a very powerful concept, and complex programs are often made by chaining many functions together.
# 
# In general, a function has a well-defined set of **inputs** (sometimes known as the function's 'arguments') and **outputs** (sometimes called the 'return value'). In Python, and most other modern programming languages, a 'function call' looks like
# ```python
# output1, output2 = function_name(input1, input2, input3)
# ```
# We have already encountered a couple of functions: we have used `print()` and `type()`. These are known as 'built-in functions', as they are a core piece of the Python programming language. For a full list of built-ins, see [this page](https://docs.python.org/3.4/library/functions.html) of the official Python documentation. Other functions can be accessed by 'importing' them from 'modules' - we will learn more about this shortly.
# 
# It is easy to write your own functions. This is done by using the `def` command, and writing something like:
# ```python
# def function_name(input1, input2, input3):
#     [code to compute outputs...]
#     return output1,output2
# ```
# Note that `function_name`, `input1`, `output1` etc can be any name you wish to use. In general, a function definition comprises:
# - The keyword `def`, followed by
# - The function name, followed by
# - An opening parenthesis `(`, followed by
# - Zero or more input variables, followed by
# - A closing parenthesis `)`, followed by
# - A colon, `:`
# 
# This is all followed by an indented block of code containing zero or more lines of the form
# - The keyword `return`, followed by
# - Zero or more variable names (or valid expressions)
# 
# For example
# ```python
# def addThreeNumbers(first, second, third):
#     return first + second + third
# ```
# We can then 'call' this function:
# ```python 
# a = 3
# b = 5
# result = addThreeNumbers(a, b, -1)
# ```
# The variable `result` should now contain the value `7` (= 3 + 5 - 1). 
# 
# **&#10148; Create the `addThreeNumbers` function and try it out.** 

# In[ ]:


# Try it here!


# A few things to notice from this example:
# - When we 'call' (use) a function, we can give it both named variables (`a` and `b`), and values (`-1`).
# - The variable names we pass to the function don't need to match the variable names used when 'declaring' (defining) the function - so we can use `a` and `b` instead of `first` and `second`.
# - The `return` keyword specifies what the function result will be.
# 
# Here's a slightly more complicated example, which calculates the sign and absolute value of the input (unless it is zero):
# ```python
# def signAndValue(x):
#     if x == 0:
#         print("Unable to handle zero input")
#     elif x > 0:
#         return +1, x
#     else:
#         return -1, -x
#     print("Hope that helps!")
# ```
# **&#10148; Try creating this function and see how it behaves.** Some things to think about:
# - When is the message "Hope that helps!" printed? Why?
# - What form does the function result have? What is its type? What about if `x`=0?
# - What is the role of `if/elif/else`?
#           

# In[ ]:


# Try it here!


# You can call this function in two slightly different ways. The first is to write (for example)
# ```python
# result = signAndValue(x)
# ```
# and the second is to write
# ```python
# sgn, val = signAndValue(x)
# ```
# **&#10148; Try both forms.** What type does each result have? What happens if `x`=0? Look again at the function declaration: can you explain this behaviour?

# In[ ]:


# Try it here!


# The following function calculates the sum of the integers from `n0` to `N`, inclusive: $\sum_{n=n_0}^N n$.
# ```python
# def sumIntegers(N, n0):
#     result = 0
#     for i in range(n0, N+1):
#         result += i
#     return result
# ```
# Note that the function definition has the upper-limit, `N`, as the first input argument, contrary to what one might expect - the reason for this will soon become clear.
# 
# **&#10148; Create the function and test it.**

# In[ ]:


# Try it here!


# It might usually be the case that we want to start our sum at $n_0 = 1$. Python allows us to provide this as a 'default' value for the `n0` variable, by simply changing the function declaration:
# ```python
# def sumIntegers(N, n0=1):
#     result = 0
#     for i in range(n0, N+1):
#         result += i
#     return result
# ```
# Now, if we call `sumIntegers` with only _one_ argument, it is assumed that this is `N`, and `n0` receives its default value. However, if we provide _two_ arguments, these are interpreted as `N` and `n0` respectively.
# 
# **&#10148; Try it out!** Can you understand how the function works?

# In[ ]:


# Try it here!


# We can have multiple arguments with default values. For example, we can extend our function to compute $\sum_{n=n_0}^N n^{\,p}$ for some power $p$:
# ```python
# def sumIntegers(N, n0=1, p=1):
#     result = 0
#     for i in range(n0, N+1):
#         result += i**p
#     return result
# ```
# If we call this specifying one, two, or three arguments, they are assumed to occur in the same order as in the function declaration (i.e. `N`, `n0`, `p`). However, we can also explicitly specify which arguments we wish to set. For example
# ```python
# result = sumIntegers(10, p=2)
# ```
# would calculate the sum of squares, leaving `n0` set to its default value.
# 
# **&#10148; Try it out!** 

# In[ ]:


# Try it here!


# If inputs are not labelled, they are assumed to be provided in the same order as in the function definition. The following function displays the value of each argument: you can use it to check you understand the different ways to call a function.
# 
# ```python
# def printArgs(a, b, c=17, d=4.3):
#     print("a is: "+str(a))
#     print("b is: "+str(b))
#     print("c is: "+str(c))
#     print("d is: "+str(d))
# ```
#    
# 
# **&#10148; Check that you understand how arguments are passed to functions.**

# In[ ]:


# Try it here!


# Note that the `printArgs()` function above does not contain an explicit `return` statement. It is an example of a function that has 'side-effects': it does something that isn't apparent from knowledge of its outputs. Sometimes, it is necessary to write code with side-effects, especially for data input or output. However, they are a common source of problems, and they should be avoided where possible.
# 
# When you pass a variable to a function, you effectively create a copy of the information it contains (unless it is a 'list' or 'array' - more on those in a later exercise!). Changing the variable within the function does *not* change the value outside the function, *unless* you pass it back via an output. For example:
# 
# ```python
# def increment(x):
#     x += 1
#     print("Inside increment, x is now "+str(x))
#     return x
# 
# x = 0
# increment(x) # Notice that we don't do anything with the return value here
# print(x)      # x will therefore still be zero
# x = increment(x) # This time we are updating the value of x
# print(x)      # x will be one.
# ```
# **&#10148; Try this out, and check you understand what's going on.**

# In[ ]:


# Try it here!


# Earlier in this exercise, you wrote code to calculate someone's fortnightly salary after tax. 
# 
# **&#10148; Adapt your code to be a function and test it out.** The function should take the annual salary as a (required) argument, and the tax rate as an optional argument.

# In[ ]:


# Try it here!


# To allow one to use your function without knowing it, you need to document it. This is usually done just after the definition of the function. This step may seem unimportant at first, but is critical for re-using your code and distributing it to other people! In Jupyter notebooks, you can press shift+tab to bring the function help. 
# 
# **&#10148; Try this for the type() and print() functions.**

# In[ ]:


# Try it here!


# Another way is to just call `help(<functionname>)`. 
# 
# **&#10148; Try this below.**

# In[ ]:


# Try it here!


# Documentation is provided by writing 'docstrings' at the start of any function you create. These consist of blocks of text enclosed in triple inverted commas:
# ```python
# """[Documentation goes here...]"""
# ```
# In scientific Python, docstrings usually follow a certain style, e.g.:
# ```python
# def increment(x):
#     """increment x.
#     
#     Parameters
#     ----------
#     x : integer
#         the number you want to increament
#     
#     Returns
#     -------
#     x : integer
#         incremented x
#     """
#     x += 1
#     print("Inside increment, x is now "+str(x))
#     return x
# ```

# Writing this example will thus output

# In[ ]:


def increment(x):


# **&#10148; Document your function to calculate someone's fortnightly salary after tax and test it out.** 
# 

# In[ ]:


# Try it here!


# As we saw earlier, each variable we create has a type. Most variables come with certain functions and attributes 'attached' to them, to perform various operations that are commonly-required for that data type. These can be accessed using a 'dot':
# ```python
# a = <variablename>.<attributename>
# b = <variablename>.<functionname>()
# ```
# For example, if we create a complex number $z = 1+3i$ (where $i = \sqrt{-1}$)
# ```python
# z = 1 + 3j
# ```
# we can then access two attributes and a function,
# - `z.real` - The 'real part' of the complex number
# - `z.imag` - The 'imaginary part' of the complex number
# - `z.conjugate()` - Function returning the 'complex conjugate' of z
# 
# Similarly, any floating-point number, `v`, comes with a `v.as_integer_ratio()` function that reports $a$ and $b$ such that $v = a/b$. To see the full list of functions associated with any variable `v`, type `help(v)`. You can also type `v.` and then hit the <kbd>Tab</kbd> key.
# 
# You may notice that some variables have a lot of attached functions that are named with double-underscores, such as `x.__add__()`. These are used by Python internally, and are not intended to be called directly in programs. In fact, the `__add__()` function is called whenever you use `+`: internally, `x+y` gets translated to `x.__add__(y)`. We will discuss this in more detail later in the course, when we talk about 'object-oriented programming'.
