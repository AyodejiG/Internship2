#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[134]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[135]:


page= requests.get('https://www.cnbc.com/world/?region=world')


# In[136]:


page


# In[137]:


soup= BeautifulSoup(page.content)
soup


# In[168]:


Headline_title= soup.find('div',class_="LatestNews-headlineWrapper")


# In[169]:


Headline_title


# In[171]:


Headline_title.text


# In[173]:


News_time=soup.find('span',class_="LatestNews-wrapper")


# In[174]:


News_time


# In[175]:


News_time.text


# In[190]:


News_link=soup.find('a',class_="LatestNews-headline")


# In[191]:


News_link


# In[192]:


News_link.text


# In[194]:


Headlines=[]
for i in soup.find_all('div',class_="LatestNews-headlineWrapper"):
    Headlines.append(i.text)


# In[195]:


Headlines


# In[200]:


updatetime=[]
for i in soup.find_all('span',class_="LatestNews-wrapper"):
    updatetime.append(i.text.split('|')[0])
    
updatetime


# In[199]:


link=[]
for i in soup.find_all('a',class_="LatestNews-headline"):
    link.append(i.text.split('|')[0])
    
link


# In[203]:


df=pd. DataFrame({'HEADLINE':Headlines,'TIME':updatetime,'NEWSLINK URL':link})
df


# In[204]:


#6) Write a python program to scrape the details of most downloaded articles from AI in last 90 DAYS


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# In[235]:


page1= requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")

page1


# In[251]:


soup1= BeautifulSoup(page.content)
soup1

