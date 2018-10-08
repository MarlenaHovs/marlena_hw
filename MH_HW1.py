
# coding: utf-8

# # Variables

# In[ ]:


project = 'cake'
difficulty = 3


# In[2]:


ingredients = ["flour", "butter", "sugar", "eggs", "cocoa powder", "baking powder"]
print (ingredients)


# In[3]:


print ('apples' in ingredients)


# In[4]:


print ('butter' in ingredients)


# In[6]:


print ('eggs' or 'margarine' in ingredients)


# In[8]:


print ('eggs' and 'margarine' in ingredients)


# In[11]:


flour, butter,sugar, eggs, cocoa_powder, baking_powder = 175, 175, '100g', 2, '1ts', 0.5
print (flour, butter, sugar, eggs, cocoa_powder, baking_powder)


# In[12]:


print (flour)


# In[2]:


flour, butter,sugar, eggs, cocoa_powder, baking_powder = 175, 175, "100g", 2, "1ts", 0.5


# In[6]:


print("Flour - ",flour)
print("Butter - ",butter)
print("Sugar - ",sugar)
print("Eggs - ",eggs)
print("Cocoa_powder -",cocoa_powder)
print("Baking_powder - ",baking_powder)


# # Operators

# In[15]:


a = 15
b = 8
c = 2

5*a**2 - a*b -a%2 - a/5


# In[16]:


b**3 +3*a*b - 10*c


# # Date and Time
# 

# In[10]:


import datetime
import time
import calendar


# In[11]:


birthday = datetime.date (1991, 5, 21)


# In[16]:


print ("my bday is on:", birthday)
print ("year:", birthday.year)
print ("month:", birthday.month)
print ("day:", birthday.day)
print ("weekday:", birthday.weekday())


# In[18]:


nextbirthday = datetime.date(2019,5,21)
today = datetime.date.today()
print("Rest days till my next birthday:", nextbirthday - today)


# In[19]:


may_calendar = calendar.month(2007, 5)
print (cal)


# In[27]:


yesterday = today - datetime.timedelta(days=1)
print (yesterday)


# In[31]:


print ("current time:", datetime.datetime.now())


# In[34]:


print ("2 days from yesterday:", yesterday + datetime.timedelta (days=2))
print ("3 days before yesterday:", yesterday - datetime.timedelta(days=3))


# # Extra
# 

# In[41]:


List = [3,5,6,8]
for n in List:
    if n % 2==0:
        print ("even number:", n)
    else:
        print ("odd number:", n)

