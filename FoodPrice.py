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


# In[8]:


df=df.drop_duplicates(['ProductId'], keep='last')
df.head(3)


# In[9]:


df.drop_duplicates(['ProductId'],keep='last').reset_index(drop=True)


# In[10]:


df.head(3)


# In[21]:


df_pro=df.loc[:,['ProductId','ProductName','UmId','UmName']]


# In[23]:


df_pri =df.loc[:,['ProductId','Place','Month','Year','Price']]


# In[13]:


df.loc[10:20,['ProductId','Place','Month','Year','Price']]


# In[24]:


pd.merge(df_pro,df_pri, on='ProductId')

