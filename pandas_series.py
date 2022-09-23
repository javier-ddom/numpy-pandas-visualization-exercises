#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
)


# In[3]:


type(fruits)


# In[ ]:





# In[4]:


len(fruits)


# In[ ]:





# In[5]:


fruits.index


# In[6]:


print(fruits.index)


# In[ ]:





# In[7]:


for x in fruits:
    print(x)
    #print(fruits[x])


# In[8]:


for x in fruits:
    print(type(x))


# In[9]:


p = 0
while p < 5:
    print(fruits[p])
    p += 1


# In[14]:


p = (len(fruits)) -1
q = 3
while q > 0:
    print(fruits[p])
    p -= 1
    q -= 1


# In[17]:


import random
p = 2
while p > 0:
    r = random.randint(1, 16)
    print(fruits[r])
    p -= 1


# In[ ]:





# In[18]:


fruits.describe()


# In[22]:


fruits.drop_duplicates(keep = False)


# In[24]:


counts = fruits.nunique()
counts


# In[27]:


from collections import Counter
Counter(fruits.keys())
Counter(fruits).values()


# In[32]:


values, counts = np.unique(fruits, return_counts=True)
print(values)
print(counts)


# In[43]:





# # exercises pt 2

# In[50]:


for x in fruits:
    qp = len(fruits)
    x = 0
    capitalized = []
    while qp > 0:
        capitalized.append(str.capitalize(fruits[x]))
        x += 1
        qp -= 1


# In[51]:


capitalized


# In[59]:


fruits[1]


# In[68]:


one_string = ""
x = 0
for ip in fruits:
    one_string = one_string + fruits[x]
    x += 1
    if x >= len(fruits):
        break
countA = one_string.count('a')


# In[74]:


one_string


# In[75]:


countA


# In[70]:





# In[78]:


one_string_vows = ""
x = 0
for ip in fruits:
    one_string_vows = one_string_vows + fruits[x]
    x += 1
    if x >= len(fruits):
        break
count_vows = one_string_vows.count('a', 'e', 'i', 'o', 'u')


# In[77]:


count_vows


# In[ ]:




