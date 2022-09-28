#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os
import numpy as np
import pandas as pd


# In[21]:


os.listdir()
os.chdir('git_practice')
os.chdir('Hello_World')


# In[22]:


from env import password, host, user
url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# In[23]:


url


# In[24]:


pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


# In[25]:


#error test: pd.read_sql('SEECT * FROM employees LIMIT 5 OFFSET 50', url)


# In[26]:


# error test: pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url+'s')
#t.title as titles


# In[27]:


emp_df = pd.read_sql('SELECT * FROM employees', url)
titles_df = pd.read_sql('SELECT * from titles',url)


# In[28]:



#emp_df


# In[29]:


titles_df


# In[30]:


#300024 rows × 6 columns empls, 443308 rows × 4 columns titles


# In[31]:


titles_df.describe()


# In[32]:


emp_df.describe()


# In[33]:


titles_df.nunique() #7 unique titles


# In[39]:


titles_df['to_date'].min() #oldest date 1/3/1985


# In[40]:


trim_titles_df = pd.read_sql('SELECT * from titles',url)


# In[ ]:





# In[ ]:





# In[41]:


check_date = (['9999-01-01'])


# In[43]:


#for thing in trim_titles_df:
#    trimmed = trim_titles_df.query('SELECT title FROM titles WHERE to_date not in check_date')


# In[44]:


#def drop_nines():
x = 1
check_date = (['9999-01-01'])
shortlist = []
for thing in trim_titles_df:
    if trim_titles_df['to_date'][x] == (['9999-01-01']):
        x = (x+1)
        continue
    else:
        shortlist.append(trim_titles_df['to_date'][x])
        x+= 1
    if x > 300:
        break
#print(type(trim_titles_df['to_date'][x])            )

#print((trim_titles_df['to_date'][x]) == (['9999-01-01']))
print(trim_titles_df)


# In[45]:


trim_titles_df


# In[ ]:





# In[ ]:





# # PART 2

# In[46]:


# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[47]:


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[48]:


users = users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)


# In[49]:


users


# # left and outer join

# In[50]:


#using a right join keeps id_x, name_x, role_id, id_y, name_y, and merge INDICATOR
#it dropped 2 people though, hsa 4 people joined on both columns,1R


# In[51]:


#using an outer join keeps the same columns, but includes all 7 people
# has 4-2-1 for both, left, and right types of merge


# # number 4: dropping foreign keys

# In[52]:


#if you dropped the foreign keys, but kept the id and role_id, the tables
#should merge correctly, there wouldn't be much data in it


# In[ ]:


#pd.merge(user, roles,
 #remove > #left_on='id'
 #remove > #right_on='id',
         #how='outer',
         #indicator=True)


# In[3]:


#LOAD MPG DATA SET
from pydataset import data


# In[4]:


mpg_df = data('mpg')


# ## SHOW DOC NO S AT THE END, SHOW DOC SHOW DOC

# In[5]:


#data('mpg',show_doc=True) #****SHOW DOC NO S AT THE END, SHOW DOC SHOW DOC****


# In[6]:


mpg_df.shape


# In[7]:


mpg_df.columns


# In[8]:


mpg_df.rename(columns={'class':'size_class'}) #could also do something like change fuel to 
                                                #be more readable, put full word not 1 letter


# In[78]:


mpg_df.describe()


# In[86]:


mpg_df.manufacturer


# In[87]:


mpg_df.manufacturer.nunique()


# In[88]:


mpg_df.model.nunique()


# In[95]:


mpg_df['mileage_difference'] = ((mpg_df.hwy) - (mpg_df.cty))


# In[97]:


#mpg_df


# In[104]:


mpg_df.sort_values(by=['mileage_difference'])


# In[9]:


#df['passing_math'] = np.where(df.math >= 70, 'passing', 'failing')


# Average mileage:

# In[10]:


mpg_df['average_mileage'] = (((mpg_df.hwy) + (mpg_df.cty))/2)


# In[17]:


mpg_df['average_mileage'] = round(2 / ((1/mpg_df.hwy) +((1/mpg_df.cty)), 2))


# #mpt_df['average_mileage'] = round(2 / ((1/mpg_df.highway) +((1/mpg_df.city)), 2))

# Automatic or manual:

# In[22]:


#data('mpg', show_doc=True) #>> trying to figure out more for the 


# In[23]:


#mpg_df['is_automatic'] = np.where(mpg_df['trans'] 'auto',"Is auto", "Not auto")
mpg_df['transmission']= mpg_df['trans'].str.contains('auto',na=False)


# In[24]:


mpg_df['transmission']


# In[ ]:


#mpg['is_automatic'] = mpg.transmission.str.contains('auto')


# In[25]:


#the average mpg of all models for each manufacturer


# In[28]:


mpg_df.groupby('manufacturer').average_mileage.mean().sort_values(ascending=True)


# In[29]:


mpg_df.groupby('manufacturer').average_mileage.mean().nlargest(5)


# ## do automatic or manual have better mpg

# In[38]:


mpg_df['transmisson_category'] = np.where(mpg_df.trans.str.contains('auto'),'automatic', 'manual')


# In[40]:


#mpg_df


# In[41]:


#manuals seem to have better mileage in this dataset


# In[ ]:




