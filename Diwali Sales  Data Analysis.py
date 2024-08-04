#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv(r'C:\Users\saaubh\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df.drop(['Status','unnamed1'],axis = 1,inplace = True)


# In[11]:



pd.isnull(df)


# In[12]:


pd.isnull(df).sum()


# In[14]:


df.dropna(inplace = True)


# In[23]:


df['Amount'] = df['Amount'].astype('int')


# In[24]:


df['Amount'].dtypes


# In[25]:


df.columns


# In[28]:


df.rename(columns= {'Marital Status': 'Shadi'})


# In[29]:


df.describe()


# In[30]:


df[['Age', 'Orders', 'Amount']].describe()


# ## Exploratory Data Analytics

# ## Gender

# In[32]:


ax = sns.countplot(x = 'Gender' ,data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[39]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)                                                                 


# In[40]:


## From above graphs we can see that most of the buyers are female and even the purcheasing power of females are greater taan man


# # Age

# In[41]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[42]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)   


# From above graphs we can see that most of the buyers are of age group between 26_35 years female

# ## State

# In[45]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State', y = 'Orders')


# In[46]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State', y = 'Amount')


# From above graphs we can see that most of the orders and total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka

# ## Marital Status

# In[49]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
ax.bar_label(bars)


# In[52]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status', y = 'Amount', hue='Gender')


# From above graphs we can see that the most of the buyers are married (women) and they have high purchesing power

# ## Occupation

# In[55]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[58]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation', y = 'Amount')


# From the above graph we can see that most of the buyers are working in IT, Helthcare  and Aviation sector

# ## Product Categories

# In[59]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[60]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')


# From above graphs we can see that the most of the sold product are from food , clothing and Electromic Category

# In[63]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID' , y= 'Orders')


# Married Women age group 26_35 years from UP,Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to by products from Food, Clothing and Electronics category.

# In[ ]:




