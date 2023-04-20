#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(color_codes=True)


# In[25]:


weather = pd.read_csv("Test.csv")


# In[4]:


weather


# In[7]:


weather.info()


# In[16]:


sns.histplot(weather['humidity'])
plt.title("Element of Weather")
plt.show()


# In[14]:


sns.distplot(weather['humidity'])
plt.show()


# In[17]:


sns.histplot(weather['temperature'])
plt.title("Element of Weather")
plt.show()


# In[41]:


weather


# In[48]:


humidity = weather.humidity
temperature = weather.temperature
sns.jointplot(humidity)
sns.jointplot(temperature)


# In[38]:


plt.hist(weather.humidity)
plt.show()


# In[ ]:




