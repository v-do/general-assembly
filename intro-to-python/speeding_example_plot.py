#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd


# In[ ]:


df = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv", usecols=range(1, 5))


# In[ ]:


location_mask = (df["pair"] == 7) & (df["warning"] == 1)
boxplot = df[location_mask].boxplot(column="speed", by=["period"], figsize=(8, 6))


# In[ ]:


plt.show(block=True)


# In[ ]:




