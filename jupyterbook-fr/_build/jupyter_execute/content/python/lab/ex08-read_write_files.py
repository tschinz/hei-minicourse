#!/usr/bin/env python
# coding: utf-8

# # Exercise 8 - Reading and writing files
# 
# So far, we have typed all the data for our programs in 'by hand'. However, as you have no doubt noticed, this quickly gets tedious. It is useful to be able to read and write data files, allowing information to be stored and shared with other people.
# 
# In order to read a data file, we need to understand what information it contains, and how this has been encoded. This is generally referred to as the 'file format'. Different programs produce files in different formats - a photograph in `.jpeg` format cannot be read by a spreadsheet package, which might expect to receive files in `.xlsx` format.
# 
# The simplest file format for storing and transferring scientific data is a plain text file in 'ascii' ('American Standard Code for Information Exchange') format. This is the sort of file that can be read and produced using a simple text editor such as 'notepad' (on Windows) or 'TextEdit' (on a Mac). Commonly, such files will have an extension such as `.txt` or `.dat`.
# 
# Reading ascii files in Python is a four-step process:
# 1. Open the file;
# 2. Read each line from the file;
# 3. Parse each line (i.e., extract the required information from it);
# 4. Close the file.
# 
# We assume that the file is already saved on your computer, and you know the 'path' to the file. To open the file, we use the `open()` function, which returns a `file` object. It is important to assign this to a variable (here, `fp`) so that we can continue to access the open file.
# ```python
# filename = 'sample.dat'
# fp = open(filename, 'r')
# ```
# Here, `filename` is a variable holding the file name (or file path and name, if it is not in our current working directory), and the second argument, `'r'`, specifies that we want to open the file for reading only.
# 
# Once the file is open, we can read from it. There are various ways of doing this, but for small files the simplest method is generally to call the `readlines()` function, which returns the entire file in the form of a list:
# ```python
# lines = fp.readlines()
# ```
# Each element of the list `lines` is now a string, containing one of the lines from the file `sample.dat`. Since we have read all the information in the file, we can now close the file:
# ```python
# fp.close()
# ```
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Opening and closing files explicitly is useful to illustrate how Python handles reading and writing files. However, doing this in practice can get quite messy because these 'connections' to files stay open until you explicitly close them. With single files, this can lead to data corruption and data loss, with more complex scripts you might open 10,000 files and not close any of them, clogging up your computer!
# 
# Luckily, Python has a really handy construct for dealing with this automatically, called '[context managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)'. They have a number of uses, but in the case of reading/writing files, you create a 'context' that contains a connection to a file, which is automatically closed when the code within the context is finished. This sounds complex... so an example:
# 
# ```python
# filename = 'sample.dat'
# with open(filename, 'r') as fp:
#     lines = fp.readlines()
# ```
# 
# The `with` statement tells python that the file you're giving it is only used in the following indented code, and can be closed afterwards.
# 
# This performs exactly the same as manually opening and closing the file, as above, but automatically cleans up after you.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# Once you have a list of strings, you can use the list- and string-parsing tools we have already encountered to extract the necessary data and store it in appropriate data structures.
# 
# The file `sample.dat` contains records of the mass and volume of twenty samples of a given material.
# 
# **&#10148; Read the data from this file, compute the density of each sample and hence the average density of the material.**

# In[ ]:


# Try it here!


# To write data to file, we need to first open the file for writing. This can be done by using `'w'` instead of `'r'` when opening the file. Note that if a file already exists with the specified name, it will be immediately overwritten and lost. To avoid this, you can instead use `'x'` when opening the file. This will throw an error if there is an existing file, rather than overwrite it. Again, when opening the file it is important to assign the result of `open()` to a variable, so we can write to it.
# 
# ```python
# outputfile = 'processed_samples.dat'
# fp = open(outputfile, 'w')
# ```
# 
# Once the file is open, we can write any text strings to it by calling the `write()` function. Remember, to insert a new line, you use the symbol `'\n'`, otherwise everything will be on a single line:
# ```python
# fp.write("Hello!\n")
# fp.write("This is some text to store in a file... ")
# line = "The file has only two lines."
# fp.write(line)
# ```
# Once everything is written to the file, call `close()` to close it.
# ```python
# fp.close()
# ```
# **&#10148; Create a new file, based on the data you read earlier. It should contain three columns: mass, sample volume and sample density. All quantities should be in SI units.** 
# 
# Remember, you can use the string-formatting tools we encountered in the last exercise to control how your numbers are written out. You can open a text file by clicking its name in Jupyter's file browser. Verify that the file has been correctly written.

# In[ ]:


# Try it here!


# From the examples above, we just saw how to read and write data using Python built-in methods. These are good for simple files, but not for more complex information such as an Excel spreadsheet. Later in the course, we will encounter a number of more sophisticated tools that can help us with these kinds of files.