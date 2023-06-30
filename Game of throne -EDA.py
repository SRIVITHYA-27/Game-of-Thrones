#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


battle = pd.read_csv('battles.csv') #load the data


# ***EXPLORATORY DATA ANALYSIS***

# In[4]:


battle.head()


# In[5]:


battle.tail()


# In[6]:


battle.shape #size of data


# In[8]:


#rename the column name attacker_1 to primary_attacker
battle.rename(columns={'attacker_1':'primary_attacker'},inplace = True)
battle.head()


# In[10]:


#renaming the column defender_1 to primary_defender
battle.rename(columns={'defender_1':'primary_defender'},inplace = True)
battle.head()


# In[13]:


#to know the counts of attacker_king
battle['attacker_king'].value_counts()


# In[14]:


#battled location
battle['location'].value_counts()


# ***DATA VISUALIZATION***

# In[15]:


sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='attacker_king',y='attacker_size',data=battle)
plt.show()


# Stannis Baretheon has the highest attacker, was attacked more than 27000 when compared to others.so he is the top attacker_king in the battle.

# In[18]:


sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='defender_king',y='defender_size',data=battle)
plt.show()


# Renly Baratheon is the top defender in the battle, he has the 20000 followed by joffrey Baratheon and Robb Stark

# In[17]:


sns.countplot(x=battle['attacker_king'],hue=battle['battle_type'])
plt.show()


# Joffrey tommen Barratheon is the top attacker_king in pitched battle and slege, 
# but Robb stark is topper in ambush and stronger than joffrey  tommen Barratheon

# In[21]:


#loading the character death data as dataframe:death
death = pd.read_csv('character-deaths.csv')
death.head()


# In[22]:


death.shape


# In[23]:


death['Gender'].value_counts()


# In[24]:


death['Nobility'].value_counts()


# In[25]:


sns.countplot(death['Death Year'])
plt.show()


# In[ ]:




