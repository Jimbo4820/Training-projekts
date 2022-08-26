#!/usr/bin/env python
# coding: utf-8

# In[96]:


import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split


# In[97]:


import random
random.randint(1, 19)


# In[106]:


słownik = {'Kol1':[-0.3, 0.5, -0.8, np.nan, 0.7],
          'Kol2':[1.2, 1.2, np.nan, 1.4, np.nan],
          'Kol3':['sobaka', 'mysz', 'kot uczenyj', 'sobaka', 'pjos'],
          'Kol4':['dobrze', 'choroszo', 'well', 'gut', 'czudowo'],
          'Kol5':['a', 'a', 'b', 'b', 'a'],
          'Kol6':[13,np.nan, 57, 0.1, np.nan],}


# In[107]:


df = pd.DataFrame(słownik)
df.head()


# In[108]:


dane_1 = df[['Kol1','Kol2']]
dane_1


# In[109]:


dane_2 = df[['Kol3', 'Kol4']]
dane_2


# In[110]:


dane_3 = df[['Kol5']]
dane_3


# In[111]:


dane_2_kod = pd.get_dummies(dane_2)
dane_2_kod


# In[112]:


dane_2_kod.shape


# In[113]:


le = LabelEncoder()


# In[114]:


dane_3_kod = pd.DataFrame(le.fit_transform(dane_3), columns = ['Kol5'])


# In[115]:


dane_3_kod


# In[116]:


si = SimpleImputer(strategy = 'most_frequent')
dane_1_kod = pd.DataFrame(si.fit_transform(dane_1),
                         columns = ['Kol1', 'Kol2'])


# In[117]:


dane_1_kod


# In[118]:


dane = pd.concat([dane_1_kod, dane_2_kod, dane_3_kod], axis = 1)


# In[119]:


dane ['Kol5']


# In[120]:


X,y = dane.drop(['Kol5'], axis = 1), dane[['Kol5']]


# In[121]:


X


# In[122]:


y


# In[123]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4)
X_train.shape, X_test.shape
mnsc = MinMaxScaler()
X_train1 = mnsc.fit_transform(X_train)
X_test1 = mnsc.transform(X_test)
X_train1.shape, type (X_train1)
rfc = RandomForestClassifier()
rfc.fit(X_train1, y_train)


# In[124]:


y_pred = rfc.predict(X_test)
y_pred


# In[125]:


dane_6 = df[:]
dane_6


# In[ ]:





# In[126]:


dane_6_kod = pd.DataFrame(si.fit_transform(dane_6),
                         columns = [df[:]])
dane_6_kod


# In[ ]:




