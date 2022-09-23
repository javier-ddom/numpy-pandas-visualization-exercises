#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import (python functions exercises)


# In[167]:


import os

os.getcwd()


# In[168]:


os.chdir('/Users/javierdominguez/codeup-data-science/python exercises')

location = os.getcwd()
print (location)


# # 3 functions exercise

# In[169]:


import python_functions_exercises

python_functions_exercises.is_vowel('a')


# In[10]:


python_functions_exercises.check_conson('a')


# In[11]:


from python_functions_exercises import calculate_tip

calculate_tip(110, .2)


# In[12]:


from python_functions_exercises import get_letter_grade as glg

glg()


# In[13]:


import itertools
#itertools.permutation(1,2,3,'a','b','c')


# In[14]:


list(itertools.combinations('abc123', 3)) #21 results?


# In[15]:


list(itertools.combinations('abcd', 2)) #6 combos


# In[181]:


list(itertools.permutations('abcd', 2)) #12 combos


# # profiles

# In[93]:


import json


# In[131]:


with open('profiles.json', 'r', encoding='utf-8') as pro:
    profs = json.load(pro)


# In[139]:


print(list(profs))


# In[137]:


def user_numbers():
    list_of_names = []
    i=0
    for nom in profs:
        if profs[i]['name'] not in list_of_names:
            list_of_names.append(profs[i]['name'])
            i+=1
               
        else:
            i += 1
            continue
    print(len(list_of_names))
    print(list_of_names)

#user_numbers()


# In[146]:


def active_users():
    list_active_users = []
    i=0
    for status in profs:
        if profs[i]['isActive'] == True:
            list_active_users.append(profs[i]['name'])
            i += 1
        else:
            i += 1
            continue
    print(len(list_active_users))
    print(list_active_users)
#active_users()


# In[148]:


def nonactive_users():
    list_nonactive_users = []
    i=0
    for status in profs:
        if profs[i]['isActive'] == False:
            list_nonactive_users.append(profs[i]['name'])
            i += 1
        else:
            i += 1
            continue
    print(len(list_nonactive_users))
    print(list_nonactive_users)
#nonactive_users()


# In[194]:


#can be made easier by defining a function to pull the balance
#and strip/convert, then just call the function in here

from re import sub
import decimal

def total_balances():
    balance_sum = 0
    i=0
    for status in profs:
        print(profs[i]["balance"])
        bal = float(profs[i]["balance"].strip('$').replace(',',""))
        print(bal)
        dec_bal = Decimal(bal)
        if bal != 0:
            balance_sum += bal
            i += 1
        else:
            i += 1
            continue
    print(balance_sum)
    return(balance_sum)


# In[195]:


balance_sum = total_balances()


# In[178]:


import decimal

Decimal(2/3)


# In[196]:


round(balance_sum / len(profs),2)


# In[197]:


#lowest balance
balance_ls = 0


# In[198]:


min(balance_ls)


# In[199]:


for profile in profiles:
    if profile['balance'].strip('$').replace(',','') == min(balance_ls)
    print(f'User {profile['name']} has the lowest amount of cash: {profile['balance']]'')


# In[ ]:





# In[200]:


for profile in profiles:
    if profilep['balance'].strip('$').replace(',','')


# In[229]:


fruits = []
i = 0
for thing in profs:
    print(profs[i]['favoriteFruit'])
    fruits.append(profs[i]['favoriteFruit'])
    i =+ 1


# In[206]:


set(fruits)


# In[230]:


fruits.count('strawberry')

#max(fruits, key=fruits.count)


# In[ ]:





# # least common fruit

# In[208]:


min(fruits, key=fruits.count)


# In[209]:


profs[0]


# In[217]:


message = profs[0]['greeting'].split(' ')


# In[218]:


message


# In[223]:


for word in message:
    if word.isdigit():
        print('This is a number', word)


# In[224]:


sum_messages = 0
for profile in profs:
    message = profile['greeting'].split(' ')
    for word in message:
        if word.isdigit():
            sum_messages = sum_messages + int(word)
            
sum_messages


# In[ ]:




