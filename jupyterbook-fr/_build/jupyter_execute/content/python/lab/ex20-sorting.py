#!/usr/bin/env python
# coding: utf-8

# # Exercise N - Visualising sorting algorithms
# *Andrew Valentine - andrew.valentine@anu.edu.au*
# 
# We have already seen that Python provides various 'sorting' functions, as built-ins or within modules. But how do they work? In this practical we will look at a few different sorting algorithms, and visualise how they work.
# 
# ## Gnome sort 
# 
# Gnome sort is a very simple sorting algorithm. Imagine you have a line of objects that need to be sorted. If the object next to you and the one immediately in front of it are in the wrong order, you swap them and take one step backwards (unless you are at the start of the line). Otherwise, you take one step forward. You repeat this, starting from the first object, until all objects are sorted.
# 
# ## Bubble sort  
# 
# Bubble sort is rather similar. You start at the first object, and walk forwards down the line. If the object next to you is in the wrong order compared to the object _in front_ of it, you swap them. However, you do not take any backwards steps. Once you get to the end of the line, you go straight back to the start and repeat until you have all objects in the desired order.
# 
# ## Selection sort 
# 
# In selection sort, you guarantee that all objects behind you are sorted. As you walk forward down the line of objects, you look at the object next to you and everything in front of it. You identify which of these objects is the smallest, and swap it with the object next to you. You then take one step forward and repeat.
# 
# ## Shell sort 
# 
# In Shell sort, you use the bubble sort algorithm, except that you initially only compare every $N$-th object. You gradually reduce $N$ as sorting proceeds. For example, suppose you wish to sort objects labelled
# 
# `ABCDEFGHIJKLMNO`
# 
# Initially you sort every 5th object, using bubble sort. So, you ensure that the sequences
# `A    F    K    `, ` B    G    L   `, `  C    H    M  `, `   D    I    N ` and `    E    J    O` 
# are each correctly sorted individually (i.e., `A`, `F` and `K` are now in the correct order, but `A`, `B` and `C` may not be). Next, you might sort every 3rd object, looking at the sequences
# `A  D  G  J  M  `, ` B  E  H  K  N ` and `  C  F  I  L  O`.
# Finally, you do a third pass where you sort objects individually, i.e. you apply bubble sort to the entire list.
# 
# For more details, and a variety of other sorting algorithms, see [this Wikipedia page](https://en.wikipedia.org/wiki/Sorting_algorithm).
# 
# We can make a disordered array of integers:

# In[1]:


import numpy as np
data = np.arange(100)
np.random.shuffle(data)
data


# Write your own implementations of the four sorting algorithms, and make an animation like this showing how the array changes as sorting proceeds.

# Gnome sort is a very simple sorting algorithm. Imagine you have a line of objects that need to be sorted. If the object next to you and the one immediately in front of it are in the wrong order, you swap them and take one step backwards (unless you are at the start of the line). Otherwise, you take one step forward. You repeat this, starting from the first object, until all objects are sorted.

# In[2]:


def sort_gnome(x):
    """gnome sorting
    
    Parameters
    ----------
    x : 1d array
        the array to sort
    """
    
    length = len(x)
    
    i = 0
    while i < len(x)-1:
        n2 = x[i+1]
        n1 = x[i]
        
        if n2 < n1:
            x[i+1] = n1
            x[i] = n2
            i = i-1
            if i < 0:
                i = 0
        else:
            i += 1
            
    return x
        


# In[3]:


x2 = sort_gnome(data)


# In[4]:


x2


# In[5]:


from IPython.display import HTML
fp = open('sortingalgorithms.html','r')
html = fp.read()
fp.close()
HTML(html)


# In[ ]:




