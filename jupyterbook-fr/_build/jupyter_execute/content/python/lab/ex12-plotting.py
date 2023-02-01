#!/usr/bin/env python
# coding: utf-8

# # Exercise 12 - Plotting
# 
# 'A picture paints a thousand words' - and a good figure can be the difference between understanding or not understanding a dataset. In this exercise, we will begin to learn how to make figures in Python.
# 
# Python's main plotting library is called `matplotlib`, and it is conventional to `import matplotlib.pyplot as plt`. This provides access to core plotting functionality.
# 
# The starting point for any figure is to call `plt.figure()`. This creates a blank canvas, onto which you will subsequently draw whatever you wish to display. Most commonly, you will probably wish to plot some set of data, contained within an array (or list). This can be achieved by calling `plt.plot()`:
# ```python
# x = np.linspace(0, 2*np.pi, 100) # 100 equally-spaced points
# y = np.sin(x)
# plt.figure()
# plt.plot(x, y)
# plt.show()
# ```
# Note that `plt.show()` is the final command here, to 'finalise' the figure. This is not strictly necessary when entering plot commands into the Jupyter browser window, but it is needed if your plotting commands are in a separate function.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# We can control the properties of the line by specifying various additional arguments:
# - Color: specify `color=colorinfo`. `colorinfo` can be specficied in [a variety of different ways](https://matplotlib.org/users/colors.html), but most often you will probably want to use a color name. You can use any of the names from [this list](https://en.wikipedia.org/wiki/X11_color_names) (ignoring any spaces or capitalisation), and any name from [this list](https://xkcd.com/color/rgb/) (including spaces) prefaced by `xkcd:`. There are also single-letter shorthands for red (`'r'`), green (`'g'`), blue (`'b'`), cyan (`'c'`), yellow (`'y'`), magenta (`'m'`), black (`'k'`) and white(`'w'`). Some examples:
#     - `color='lightcoral'`
#     - `color='xkcd:boring green'`
#     - `color='r'`
# 
# - Line width: specify `linewidth=width`, where width is measured in '[points](https://en.wikipedia.org/wiki/Point_%28typography%29)', for example `linewidth=3`.
# 
# - Line style: specify `linestyle=styleinfo`, where styleinfo is one of [various strings](https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html) such as `'solid'`, `'dashed'`, `'dotted'`, and so on. Again, there are shorthands for the most common cases: `'-'`, `':'`, `'--'` and `'-.'`.
# 
# For the simplest cases, where the shorthand forms for color and/or line style are appropriate, these can be combined and provided as a third, unlabelled argument to plot, e.g. `plt.plot(x, y, 'r:')` to plot a dotted red line.
# 
# **&#10148; Try the various options out, and ensure that you understand what they do.**

# In[ ]:


# Try it here!


# Often, one wishes to plot two or more lines on a single figure. The simplest way to achieve this is often to call `plt.plot(...)` multiple times:
# ```python
# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.figure()
# plt.plot(x,y1)
# plt.plot(x,y2)
# ```
# However, you can also combine multiple `(x, y, fmt)` triplets into a single plot command:
# ```python
# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.figure()
# plt.plot(x, y1, 'r:', x, y2, 'b--')
# ```
# When plotting multiple lines on a single plot, it is often desirable to label them. This can be achieved by passing `label=textstring` to each `plt.plot(...)` call, and then calling `plt.legend()`.
# ```python
# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.figure()
# plt.plot(x, y1, label='sin(x)')
# plt.plot(x, y2, label='cos(x)')
# plt.legend()
# plt.show()
# ```
# This only works if you are calling `plt.plot()` separately for each line. Many different options can be passed to `plt.legend()` to control the layout of the resulting legend.
# 
# **&#10148; Try them out.**

# In[ ]:


# Try it here!


# Sometimes, we may wish to plot individual data points with symbols, rather than a line joining them all together. This can be achieved by providing [a letter specifying which symbol to use](https://matplotlib.org/1.4.1/api/markers_api.html) as the third argument to `plt.plot()` (optionally preceded by a one-letter color shorthand). For example, `plt.plot(x, y, 'o')` plots data points as circles; `plt.plot(x, y, 'r^')` plots red triangles. For more control over colors, one can specify options `markerfacecolor=colorinfo` and `markeredgecolor=colorinfo`. If one wishes to have both markers *and* line, one can specify the selected symbol via `marker=markerletter`.
# 
# **&#10148; Try these out.**

# In[ ]:


# Try it here!


# Python automatically sets the limits of your axes. If you wish to change this, you can call `plt.xlim(lo,up)` and `plt.ylim(lo, up)`, with `lo` and `up` set to the lower and upper values of the axis, respectively. Note that if you call `plt.xlim()` or `plt.ylim()` without any arguments, they will return a tuple `(lo, up)` containing the current axis limits - this can be useful if you want to know the values that Python has determined automatically.
# 
# To label your axes, you can call `plt.xlabel(textstring)` and `plt.ylabel(textstring)`, where `textstring` is the text you want in the label. Similarly, to put a title on the plot, you can call `plt.title(textstring)`. Axes labels can be set by calling `plt.xticks(locations, labels)` where `locations` is a list of the x (or y) values you wish to annotate, and `labels` is the corresponding list of labels. Note that one can use LaTeX symbols within these labels. You can omit the `labels` argument if you just want to use the numerical value of each point. For example:
# ```python
# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.figure()
# plt.plot(x, y1, label='sin(x)', color='firebrick', linewidth=3)
# plt.plot(x, y2, label='cos(x)', color='royalblue', linestyle='dotted', linewidth=3)
# plt.legend()
# plt.xlim(0, 2*np.pi)
# plt.ylim(-1.25, 1.25)
# plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
# plt.yticks([-1, 0, 1])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title("Sine and cosine")
# plt.show()
# ```   
# All the text-producing commands (like `plt.xlabel()`) take [a variety of optional arguments](https://matplotlib.org/users/text_props.html) that control the appearance of their output. Useful ones include `fontsize=size` and `fontname=name`.
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# When you've finished setting up your figure, it is usually a good idea to call `plt.tight_layout()`. This adjusts various layout parameters to make sure everything is spaced correctly, and looks nice. Once you have a figure you're happy with, you can call `plt.savefig(filename)` to save the figure into a file. Here, `filename` is a text string, and it should end with a three-letter 'file extension' (`.***`) which determines the 'type' of graphics file to save. For most purposes, you will probably want to use `.pdf`, `.png` or `.jpg`.
# 
# Note that you can create several figures within one piece of code, by calling `plt.figure()` to get a 'fresh' canvas. 
# 
# **&#10148; Try it out!**

# In[ ]:


# Try it here!


# The file `cetml1659on.dat` contains a dataset of monthly average temperature measurements recorded in central England, from the year 1659 onwards. 
# 
# **&#10148; Open the file within your browser, and work out what the file format is; then read it in using `np.loadtxt`.** You will need to use the `skiprows` option of `loadtxt` to skip over the 'header' information. 
# 
# Create:
# - a plot showing the annual average temperature varying over time;
# - a plot showing the minimum, maximum, mean and median monthly temperatures across the 12 months of a year.

# In[ ]:


# Try it here!


# When you have data in a 2-D array - as with the dataset read by `np.loadtxt` - it can be useful to visualise it. This can be done using `plt.imshow()`. 
# 
# **&#10148;Try it out!**

# In[ ]:


# Try it here!


# To add a colorscale to your plot, you can call `plt.colorbar()`. You can adjust the values corresponding to the upper- and lower- limits of the color scale with `plt.clim(lo, up)`, just as for the x- and y-axis ranges. If you want to change the 'color map' (the colors used), you can pass the argument `cmap=colormapname` to `imshow()`, where `colormapname` is one of the names from [this list](https://matplotlib.org/users/colormaps.html).

# In[ ]:


# Try it here! 


# We can use this to reproduce Ed Hawkin's ['climate stripes' visualisation](https://www.climate-lab-book.ac.uk/2018/warming-stripes/) which has recently attracted media attention. Extract only the annual average temperature from the dataset, and use `imshow` and a Red-Blue colour scale.
# 

# In[ ]:


# Try it here!

