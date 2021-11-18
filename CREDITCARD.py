#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
 
cc = pd.read_csv('C:/Users/Matia/Downloads/creditcard.csv', index_col = 0)
cc


# In[2]:


cc.info()


# In[3]:


cc.isna().sum()


# In[17]:


print(cc.shape)
print(cc.value_counts(cc['Class'], sort = True))


# In[6]:


cc.Class.value_counts().plot(kind = "bar", title = "Tipo de Caso")
plt.show()


# In[ ]:


cc.groupby(["Class", "Amount"]).size().unstack().plot(kind = "bar", title = "Monto por clase")
plt.show()

