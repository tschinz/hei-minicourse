#!/usr/bin/env python
# coding: utf-8

# # Exercise 19 - Differential equations
# 
# Many physical, chemical and biological systems can be modelled using differential equations. Often, these do not have analytical solutions, but they can be solved numerically. There are many techniques for achieving this, and in this practical we will look only at a couple of simple examples.
# 
# ## The simple pendulum
# 
# A simple pendulum of mass $m$, suspended from a string of length $l$, obeys the differential equation
# $$\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} + \frac{g}{l}\sin\theta = 0,$$
# where $\theta$ is the angle the string makes with a vertical line. 
# 
# In this exercise, we will use the function `scipy.integrate.odeint()`. This solves differential equations of the form
# $$\frac{\mathrm{d}\mathbf{y}(t)}{\mathrm{d}t} = f(\mathbf{y},t).$$
# We therefore first need to work out how to write the pendulum equation in this form. Fortunately, there is a standard approach we can follow. We define $$\mathbf{y}(t) = \left(\begin{array}{c}\theta(t)\\\dot\theta(t)\end{array}\right),$$
# where $$\dot{\theta}  = \frac{\mathrm{d}\theta}{\mathrm{d}t}$$
# Now,
# $$\frac{\mathrm{d}\mathbf{y}}{\mathrm{d}t} = \left(\begin{array}{c}\dot\theta\\\ddot\theta\end{array}\right) = \left(\begin{array}{c}y_2(t)\\-\frac{g}{l}\sin y_1(t)\end{array}\right).$$
# Thus, given any vector $\mathbf{y}$, we can compute its time derivative.
# 
# **&#10148; Write and test a function to compute $\mathrm{d}\mathbf{y}/\mathrm{d}t$.** Its call signature should be
# ```func(y,t,...)``` even though the variable `t` is not required within the calculation.

# In[ ]:


# Try it here!


# The function `scipy.integrate.odeint()` expects to be given an *initial condition* -- the vector $\mathbf{y}$ at time $t=0$. Let's suppose that the pendulum is initially at an angle of ${\pi}/{4}$ radians from vertical, and at rest, so that $\dot\theta(0)=0$.
# 
# **&#10148; Create a vector `y0` to represent this initial condition.**

# In[ ]:


# Try it here!

y0 = np.array([0.3,0])


# Finally, `scipy.integrate.odeint()` needs a sequence of time-points at which the pendulum's state should be evaluated. These need to be sufficiently closely-spaced for the integration to be accurate. A good starting point might be
# ```python
# timesteps = np.linspace(0,10,1000)
# ```
# 
# **&#10148; Use `scipy.integrate.odeint` to compute the motion of the pendulum.** The function returns an array of dimension $(2\times N)$, where $N$ is the number of timesteps. This represents the vector $\mathbf{y}(t)$ evaluated at each of these times.
# 
# **&#10148; Make an animation showing the motion of the pendulum over time.**

# In[ ]:


# Try it here!

timesteps = np.linspace(0,10,500)
y = integ.odeint(simplePendulum,y0,timesteps,args = (0.1,1.5))
plt.plot(timesteps,y[:,0],timesteps,0.1*y[:,1])


# At present, our differential equation doesn't include any attenuation, and so the pendulum continues oscillating with the same amplitude indefinitely. A more realistic system could be modelled as $$\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} + \frac{g}{l}\sin\theta +\alpha \frac{\mathrm{d}\theta}{\mathrm{d}t}= 0$$
# where $\alpha$ is a small, positive constant.
# 
# **&#10148; Incorporate this extra term into your modelling, and make a new animation.**

# In[ ]:


# Try it here!


# **&#10148; Experiment with different initial conditions, pendulum properties, and integration steps.**

# In[ ]:


# Try it here!


# A [double pendulum](https://en.wikipedia.org/wiki/Double_pendulum) is one pendulum suspended from another. Suppose we have a metal rod of mass $m$ and length $l$, suspended from a pivot so that it functions as a pendulum. We then hang a second, identical rod from the free end of the first rod. Together, these two function as a double pendulum.
# 
# It can be shown (via Lagrangian mechanics) that the system can be fully-represented by specifying the two angles ($\theta_1$ and $\theta_2$) that each rod makes with the vertical, and two momenta ($p_1$ and $p_2$). The time-derivatives of the system are given by:
# 
# $$\begin{align}
# {\dot \theta_1} &= \frac{6}{ml^2} \frac{ 2 p_{1} - 3 \cos(\theta_1-\theta_2) p_{2}}{16 - 9 \cos^2(\theta_1-\theta_2)} \\
# {\dot \theta_2} &= \frac{6}{ml^2} \frac{ 8 p_{2} - 3 \cos(\theta_1-\theta_2) p_{1}}{16 - 9 \cos^2(\theta_1-\theta_2)}\\
# {\dot p_{1}} &=  -\tfrac{1}{2} m l^2 \left ( {\dot \theta_1} {\dot \theta_2} \sin (\theta_1-\theta_2) + 3 \frac{g}{l} \sin \theta_1 \right ) \\
# {\dot p_{2}} &=  -\tfrac{1}{2} m l^2 \left ( -{\dot \theta_1} {\dot \theta_2} \sin (\theta_1-\theta_2) + \frac{g}{l} \sin \theta_2 \right ).
# \end{align}$$
# 
# **&#10148; Using `scipy.integrate.odeint`, create an animation of the double pendulum in motion.**

# In[ ]:


# Try it here!

