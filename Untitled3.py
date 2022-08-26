#!/usr/bin/env python
# coding: utf-8

# In[18]:


maxFib = 4000000
czet = 0
Fibanachi = [1,2]
for n in Fibanachi:
    if n >= 2:
        newFib = Fibanachi[-1] + Fibanachi[-2]
        if newFib < maxFib:
            Fibanachi.append(newFib)
        else:
            print(Fibanachi)
for i in Fibanachi:
    if i % 2 == 0:
            czet += i
print(czet)


# In[19]:


get_ipython().system('pwd')


# In[20]:


get_ipython().system('ls')


# In[21]:


def sum_of_lists(N):
           total = 0
           for i in range(5):
               L = [j ^ (j >> i) for j in range(N)]
               total += sum(L)
           return total


# In[22]:


sum_of_lists(10)


# In[28]:


import numpy as np
np.random.normal(0, 1, (3, 3))


# In[29]:


x3 = np.random.randint(10, size = (3,4,5))
x3


# In[34]:


y = np.array([99,99])
z = np.array([100, 200])
np.dstack((y,z))


# In[ ]:




