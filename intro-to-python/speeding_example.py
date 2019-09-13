#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data_frame = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv", usecols=range(1, 5))


# In[ ]:


before = []
after = []

for row in data_frame.values:
    if row[3] == 7:
        if row[2] == 1:
            if row[1] == 1:
                before.append(row[0])
            if row[1] == 3:
                after.append(row[0])

print("average before sign: ", sum(before)/len(before))
print("average after sign: ", sum(after)/len(after))


# In[ ]:




