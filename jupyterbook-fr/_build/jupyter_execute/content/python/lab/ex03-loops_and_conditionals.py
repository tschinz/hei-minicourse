#!/usr/bin/env python
# coding: utf-8

# # Exercise 3 - Loops and conditionals
# *Andrew Valentine - andrew.valentine@anu.edu.au*

# Much of the power in programming comes from being able to repeat calculations, and/or change how our program works depending on the values of certain variables. To achieve this, we need to employ 'loop expressions' and 'conditional expressions'.
# 
# ## Conditionals
# 
# Conditional expressions allow us to alter the behaviour of our program depending on the circumstances. To do this, we employ an `if...elif...else` construct, which takes the form:
# ```python
# if <condition>:
#     [...]
# elif <another condition>:
#     [...]
# else:
#     [...]
# ```
# Here, each `<condition>` is a 'logical' expression - something which is either 'true' or 'false'. Each `[...]` denotes a block of code that is only executed if the condition is met. We can have as many `elif` ('else if') blocks as we wish, and we can omit the `elif` and/or `else` blocks entirely. At most, one block will be executed: each is tried in the order they appear in the program, until one is found for which `<condition>` is `True`. Notice that the `else` block does not have a condition - this is executed if none of the other conditions are met.
# 
# To make this clearer, here's a real example, inside a function:
# ```python
# def condExample(x):
#     if x<0:
#         print("x is negative")
#     elif x<=1:
#         print("x is between 0 and 1 (inclusive)")
#     else:
#         print("x is greater than 1")
# ```
# **&#10148; Try it out!** Does everything behave as you would expect? Try deleting the `elif` and/or `else` clauses; how does this affect the output?

# In[ ]:


# Try it here!


# ### Logical expressions
# 
# Logical expressions are calculations that result in either `True` or `False`. As we have already seen, they often arise by comparing the value of two variables (or a variable and a constant), such as `x > 0`. The comparison operators are:
# 
# | Operator | Meaning |
# |---|---|
# |`>` | Greater than|
# |`<` | Less than|
# |`>=`| Greater than or equal to|
# |`<=`| Less than or equal to|
# |`==`| Equal to|
# |`!=`| Not equal to|
# 
# You can check you understand how these work by testing expressions in a Python cell: for example, entering
# ```python
# 3 > 5
# ```
# should evaluate to `False`.
# 
# **&#10148; Try all the operators above.**

# In[ ]:


# Try it here!


# Note: an important point is that the constants `True` or `False` are Booleans, and not text. So `"True"` (string) is very different of `True` (Boolean). A possible mistake is to confound them and use `"True"` instead of `True`. In general, as soon as you want to use something based on a true/false behavior, use Boolean constants in your program.
# 
# To build more complicated expressions, you can use the Boolean operators `and`, `or` and `not`. An expression of the form `A and B` is only `True` if both `A` and `B` are separately `True`. On the other hand, `A or B` is `True` if either (or both) of `A` and `B` are themselves `True`. The `not` operator flips `True` to `False`, and vice versa. You can use parentheses to group expressions if necessary.
# 
# For example:
# ```python
# x > 3 and (y == 2 or not (y > 3 and x+y ==4) )
# ```
# Many logical conditions can be expressed in multiple forms, for example `x > 3` is identical to `not x <= 3`. In general, you should use the simplest form that is appropriate to your circumstances. 
# 
# N.B. In some other languages, the symbols `&` and `|` are used for `and` and `or`. In Python, these symbols are 'bitwise' operators, and they will not give the results you expect. We will avoid using them in this course.
# 
# **&#10148; Try using the `and`, `or` and `not` operators.**

# In[ ]:


# Try it here!


# Another logical operator you may encounter is `is`. This is used to test whether two variable names refer to the same entity. This is stronger than simply testing for equality. For example:
# ```python
# a = 300
# b = 300
# a is b
# ```
# will return `False`, whereas ```a is a``` returns `True`. This may seem rather pointless, but it turns out to be useful when writing more advanced programs. It is also commonly encountered in conjunction with a null default value within a function:
# ```python
# def printHello(name=None):
#     if name is None:
#         print("Hello, what is your name?")
#     else:
#         print("Hello "+name)
# ```
# To some extent, this is a matter of idiom, rather than necessity.
# 
# **&#10148; In the previous exercise, you wrote a function to calculate someone's fortnightly pay, given an annual salary. Extend this to allow the user to choose to have weekly or monthly figures, instead.** 
# 

# In[ ]:


# Try it here!


# ## Loops
# 
# Loops allow you to repeat a series of calculations a number of times, or until certain conditions are met. In Python, there are two main loop formats. The first is a `while` loop:
# ```python
# while <condition>:
#     [...]
# ```
# Here, `<condition>` is a logical expression (just like those discussed above). If this evaluates to `True`, the block of code (`[...]`) is executed in its entirety. The condition is then evaluated again, and the entire process repeats until it becomes `False`. For example, here is a loop that keeps doubling a number until it exceeds some threshold:
# ```python
# x = 1
# while x<100:
#     x+=x
# print(x)
# ```
# Normally, the entire indented block of code below the `while` statement is executed before the condition is checked again. However, two commands can be used to alter this:
# - The `break` keyword terminates the loop, jumping to the first statement *after* the indented block
# - The `continue` keyword skips over any remaining code within the indented block, but returns to re-evaluate the `<condition>`, and if this is True will execute the indented block as before.
# These two commands are almost invariably used in conjunction with an `if` statement.
# 
# For example:
# ```python
# x = 1
# while x < 100:
#     x+=5
#     if x == 71: break
#     if x%2==0: continue # Skip even x
#     print("In loop: x=", x)
# print("After loop: x=", x)
# ```
# If you run this code, you will see that it never prints an even number (since the print statement is after the `continue` in this case, and so doesn't get executed); moreover, the loop terminates at `x=71`, due to the `break` statement.

# In[ ]:


# Try it here!


# Sometimes, it may be appropriate to use the following style:
# ```python
# while True:
#     [...]
#     if <condition>: break
#     [...]
# ```
# Here, the loop condition is *always* `True`, creating an infinite loop. However, the use of a `break` allows us to escape from the loop.
# 
# There is another form of loop, the `for` loop. We will meet this in a later practical.

# In[ ]:


# Try it here!


# **&#10148; Caution: [infinite loops](https://en.wikipedia.org/wiki/Infinite_loop)...** if you have no `break` statement, the program will execute the loop until you provide an explicit "stop" signal. In Jupyter notebooks, this is the stop button, and in a terminal the ctrl+c command (for all operating systems). Infinite loops will run endlessly if not manually stopped (by sending a termination signal), and are a well known problem since the dawn of computer programming. Nowaday, it is not such a big deal but old systems used to froze when running such loops... So be careful and always check that your loop is not infinite!

# Suppose you start with an empty basket and you want to pick apples on a tree. You will make 100 picking moves.
# 
# You start by picking 2 apples at a time, but after doing this 50 times you get bored. You then pick 5 apples each time, and after doing this a further 25 times, you start picking 10 apples.
# 
# **&#10148; Write a function containing a loop to return the number of apples in your basket.**

# In[ ]:


# Try it here!


# Suppose you take out a $\$$500,000 mortgage to buy a house. You make a repayment of \$2,000 each month. However, each month the bank charges interest at a rate of 0.3% of the outstanding balance. How many months will it take you to pay off the debt? How much does it cost you?
# 
# **&#10148; Write a function to calculate this information for any loan amount, interest rate and monthly repayment.** 
# 

# In[ ]:


# Try it here!
