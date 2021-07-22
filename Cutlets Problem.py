#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("cutlets.csv")


# In[3]:


df.head()


# In[8]:


df['Unit A'].mean()


# In[9]:


df['Unit B'].mean()


# In[10]:


df['Difference']=df['Unit A']-df['Unit B']


# In[11]:


df


# In[15]:


df['Difference'].mean()


# In[16]:


df['Difference'].std()


# In[ ]:





# In[12]:


df.shape


# In[13]:


cut_df=df.iloc[5:15,:]


# In[14]:


cut_df


# In[17]:


from scipy import stats


# In[18]:


cut_df['Difference'].mean()#sample mean


# In[22]:


import math


# In[23]:


math.sqrt(10)


# In[24]:


0.43011346378728066/3.1622776601683795


# In[25]:


(0.09405999999999999-0.05479428571428578)/0.13601381978721588 #Z-test


# In[26]:


stats.norm.sf(abs(0.288)) #P-value , since p-values>0.05 so Null hypothesis is accepted.


# In[ ]:




