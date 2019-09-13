#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
df = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv", usecols=range(1, 5))


# In[ ]:


location_mask = (df["pair"] == 7) & (df["warning"] == 1)
before_mask = location_mask & (df["period"] == 1)
after_mask = location_mask & (df["period"] == 3)

before = df[before_mask]["speed"]
after = df[after_mask]["speed"]

print("average before sign: ", np.mean(before))
print("average after sign: ", np.mean(after))


# In[ ]:




