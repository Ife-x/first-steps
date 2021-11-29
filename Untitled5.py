#!/usr/bin/env python
# coding: utf-8

# In[5]:


import seaborn as sns


# In[23]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[14]:


df_used_cars = pd.read_csv("C:/Users/Kudi User/Downloads/bar_chart_data.csv")


# In[16]:


df_used_cars


# In[36]:


plt.figure(figsize = (15, 10))
plt.bar(x = df_used_cars["Brand"],
        height = df_used_cars["Cars Listings"],
       color = 'midnightblue')
plt.xticks(rotation = 45, fontsize =13)
plt.yticks(fontsize = 13)
plt.title("Cars Listings by Brand", fontsize = 16, fontweight ="bold")
plt.ylabel("Number of Listings", fontsize = 13)
plt.savefig("Used Cars Bar.png")
plt.show()


# In[39]:


df_fuel_engine_type = pd.read_csv("C:/Users/Kudi User/Downloads/pie_chart_data.csv")


# In[41]:


df_fuel_engine_type


# In[68]:


plt.figure(figsize = (10, 8))
plt.pie(df_fuel_engine_type['Number of Cars'],
        labels=df_fuel_engine_type['Engine Fuel Type'].values,
       autopct="%.2f%%",
       textprops={'size': 'x-large',
                  'fontweight': 'bold',
                  'rotation': '30',
                  'color': 'w'})
plt.legend()
plt.title('Cars by Engine Fuel Type', fontsize = 18, fontweight = 'bold')
plt.savefig("Cars by Engine Fuel Type.png")
plt.show()


# In[70]:


df_fuel_engine_types = pd.read_csv("C:/Users/Kudi User/Downloads/stacked_area_chart_data.csv")


# In[72]:


df_fuel_engine_types


# In[80]:


colors = ["#011638", "#7e2987", "ef2026"]
labels = ["Diesel", "Petrol", "Gas"]
sns.set_style("white")
plt.figure(figsize = (12, 6))
plt.stackplot(df_fuel_engine_types["Year"],
             df_fuel_engine_types["Diesel"],
             df_fuel_engine_types["Petrol"],
             df_fuel_engine_types["Gas"],
             colors= colors,
             edgecolor = 'none')
plt.xticks(df_fuel_engine_types["Year"], rotation = 45)
plt.legend(labels = labels, loc = "upper left")
plt.ylabel("Numbers of Cars", fontsize = 13)
plt.title("Popularity of Engine Fuel Types (1982-2016)", fontsize = 14, weight = "bold")
sns.despine()
plt.show()

