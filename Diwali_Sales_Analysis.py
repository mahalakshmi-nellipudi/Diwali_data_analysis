#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 


# In[3]:


df = pd.read_csv('Diwali Sales Data.csv' , encoding = 'unicode_escape')
# We use encoding to handle special or non-ascii characters in the csv data preventing encoding errors while reading the data 


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


# Drop unrelated or blank coloumns
df.drop(['Status' , 'unnamed1'], axis = 1, inplace=True)


# In[8]:


# Check for null values
pd.isnull(df).sum()


# In[9]:


# Drop null values
df.dropna(inplace=True)


# In[11]:


# Change data type
df['Amount'] = df['Amount'].astype('int')


# In[12]:


df['Amount'].dtypes


# In[13]:


df.columns


# In[14]:


# Rename column
df.rename(columns= {'Marital_Status' : 'Shaadi'})


# In[15]:


# Describe() method returns the description of the data int the data frame
df.describe()


# In[16]:


# Using describe fro specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# In[18]:


# Plotting barchart for gender and it's count
ax = sns.countplot(x = 'Gender' , data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


# Plotting a bar chart for gender vs total amount
sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender', y= 'Amount', data = sales_gen)


# In[25]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


# Total amount vs age group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Age Group', y= 'Amount', data = sales_age)


# In[31]:


# Total no of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State', y= 'Orders')


# In[32]:


# Marital Status
ax = sns.countplot(data = df, x = 'Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status' , y = 'Amount', hue = 'Gender')


# In[35]:


# Occupation
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation', y  = 'Amount')


# In[38]:


# Product category
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data  =df, x = 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[39]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')


# In[40]:


# From the above graph we can see that most of the sold items are food, clothing, electronics
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID', y = 'Orders')


# In[43]:


# Top 10 most sold products
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby("Product_ID")['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# In[ ]:


# Married women age group 26-35 years from UP, Maharastra and karnataka working in IT, Healthcare and Aviation are more likely to buy products from food, clothing, Electronics category

