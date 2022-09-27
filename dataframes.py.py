#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydataset import data
import pandas as pd


# In[2]:


import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

grades_df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)


# In[ ]:


grades_df


# In[ ]:


#passing english


# In[ ]:


df.english >= 70
grades_df['passing_english'] = df.english >= 70
mpg['mpg_difference'] = mpg.city


# In[ ]:


grades_df


# In[ ]:


grades_df.sort_values(by='passing_english') #duplicates are kept


# In[ ]:


grades_df.sort_values(['passing_english', 'name'],ascending=True) 
#duplicates are kept


# In[ ]:





# In[ ]:


#sort by passing english then grade in english


# In[ ]:


grades_df.sort_values(['passing_english', 'english',])


# In[ ]:


df.english >= 70
grades_df['passing_english'] = df.english >= 70


# In[ ]:


#Overall grades


# In[ ]:


grades_df['overall'] = (df.english + df.english + df.reading)/3


# In[ ]:


grades_df


# In[3]:


mpg = data('mpg')


# In[4]:


#how many rows and columns
mpg.shape


# In[5]:


#what are the data types
mpg.dtypes


# In[6]:


mpg.info


# In[7]:


mpg.describe


# In[77]:


#RENAMEs


# In[78]:


mpg = mpg.rename(columns = {'cty':'city','hwy':'highway', 'class':'class_type'})


# In[84]:


mpg = mpg.sort_values(by='highway', ascending=False)
mpg


# In[85]:


#City vs highway
mpg.city[1]


# In[86]:


mpg_highway = mpg.highway
mpg_highway


# In[87]:


mpg_city = mpg.city
mpg_city


# In[ ]:





# In[97]:


mpg_difference = (mpg.city - mpg.highway)


# In[98]:


mpg_difference.sort_values()


# In[99]:


#NO CARS HAVE HIGHER CITY THAN HIGHWAY, just my accord hybrid


# In[101]:


mpg.iloc[152] #toyota tacoma 4x4
mpg.iloc[177] #jeep grand cherokee 4x4


# In[102]:


models = mpg.model


# In[103]:


models = list(models)


# In[104]:


#which compact car has the worst and best highway mileage
car_class = mpg.class_type


# In[105]:


car_class = list(car_class)


# In[106]:


#car_class


# In[146]:


car_class[0]


# In[108]:


hwy_miles = mpg.highway


# In[109]:


hwy_miles = list(hwy_miles)


# In[147]:


#hwy_miles
hwy_miles[0]


# # checking if compact and adding to dict
# 

# In[159]:


car_dict = {'id_number':[],'class':[],'miles':[],'model':[]}
x=0
for i in car_class:
    #print(i)
    if i == 'compact':
    #car_dict.update({'id_number':x,'class':car_class[x],'miles':hwy_miles[x]})
        car_dict['id_number'].append(x)
        car_dict['class'].append(car_class[x])
        car_dict['miles'].append(hwy_miles[x])
        car_dict['model'].append(models[x])
        x += 1
    else:
           x+=1
    if x > 300:
        break
        
#car_dict
print(car_dict['model'][0] + ' ' + str(car_dict['id_number'][0]))
print(car_dict['model'][1] + ' ' + str(car_dict['id_number'][1]))
print(car_dict['model'][-1] + ' ' + str(car_dict['id_number'][-1])) 
print(car_dict['model'][-2] + ' ' + str(car_dict['id_number'][-2]))


# In[145]:


#now add mileage
#x=1
#for i in car_dict:
#    print(i)
#    car_dict[keys(x)] = hwy_miles[x]
#    x += 1
#    if x > 10:
#        break
        
#car_dict


# In[144]:


#compact_cars = {}
#x=1
#while x < 3:    
#    if car_class[x] == 'compact':
#        compact_cars.append(car_class[x])
#        print(compact_cars)
#        x+=1
#        if x > 10:
#            break


# In[163]:


average_mileage = (mpg.city + mpg.highway)/2


# In[164]:


average_mileage


# In[173]:


average_mileage[222]


# In[170]:


average_mileage[70]


# In[174]:


average_mileage[127]


# In[192]:


mpg.manufacturer[1]


# In[ ]:





# In[196]:


average_mileage[1]


# In[ ]:





# In[244]:


q = 0
high_miler = ''
highest_mpg = 0
while q < 234:
    
    
    #print('q = ' + str(q))
    #print(mpg.manufacturer[q+1])
    checksum = str(mpg.manufacturer[q+1])
    if checksum == 'dodge':
        if average_mileage[q+1] > highest_mpg:
            highest_mpg = average_mileage[q+1]
            high_miler = str(mpg.manufacturer[q+1])
            indy = mpg.index[q+1]
            q +=1
          #  print('one added')
        else:
     #       print('nope')
            q+=1
    else:
        q += 1
   # print('nothing at all')
    if q > 300:
        break

print(mpg.iloc[indy])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




