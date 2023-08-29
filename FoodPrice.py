#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import re


# In[2]:


data_path = 'D:\\codegym3\\'
data_name = 'FoodPrice_in_Turkey.csv'

df = pd.read_csv(data_path+data_name, encoding= 'unicode_escape')

df.head(3)


# In[3]:


df.shape


# In[4]:


df.dtypes


# In[5]:


x = df.groupby(['ProductName'])['Price'].mean()
print(x)


# In[ ]:




