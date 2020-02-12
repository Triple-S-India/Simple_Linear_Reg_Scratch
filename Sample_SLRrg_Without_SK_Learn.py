#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[45]:


x = np.array([1,2,3,4,5,6])
y = np.array([2,2,4,6,4,6])


# In[46]:


x_bar = np.mean(x)
y_bar = np.mean(y)


# In[47]:


x_bar, y_bar


# In[48]:


numer = 0
denom = 0
for i in range(len(x)):
    numer+= (x[i]-x_bar)*(y[i]-y_bar)
    denom+= (x[i]-x_bar)**2
b1 = numer/denom       #b1 is slop
b0 = y_bar - b1*x_bar    #b0 is intercept
print(b0,b1)


# In[49]:


plt.scatter(x,y)
x2 = np.arange(0,6,0.1)
y1 = b0 + b1*x2
plt.plot(x2,y1,color ='red')
plt.show()


# In[50]:


# calculating RMSE
rmse = 0
for i in range(len(x)):
    y_pred = b0 + b1*x[i]
    rmse+= (y_pred - y[i])**2
rmse = np.sqrt(rmse/len(x))
print(rmse)


# In[51]:


ss_t = 0
ss_r = 0
for i in range(len(x)):
    y_pred = b0 + b1*x[i]
    ss_t+= (y[i]-y_bar)**2
    ss_r+= (y[i]-y_pred)**2
r2 = 1 - (ss_r/ss_t)
print(r2)


# In[ ]:




