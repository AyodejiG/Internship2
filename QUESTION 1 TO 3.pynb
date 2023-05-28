#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a python program to display all the header tags from wikipedia.org and make data frame.

get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


# importing the required libraries 
from bs4 import BeautifulSoup
import requests


# In[4]:


# Send request to webpage server to get the source code of the page
page= requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[9]:


page


# In[80]:


soup= BeautifulSoup(page.content, "html.parser")
soup


# In[83]:


header_tags = soup.find(["h1", "h2", "h3", "h4", "h5", "h6"])


# In[84]:


header_texts = [tag.get_text() for tag in header_tags]


# In[85]:


headers= []
for i in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    headers.append(i.text)
    
headers
    


# In[86]:


print(len(headers))


# In[87]:


import pandas as pd
df = pd.DataFrame({'HeadersTags': headers})
df


# In[39]:


# 2. Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)

from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[40]:


page= requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[41]:


page


# In[45]:


soup= BeautifulSoup(page.content)
soup


# In[59]:


name = soup.find('div', class_="presidentListing")
name


# In[60]:


name.text


# In[62]:


term= soup.find('span',class_="terms")
term


# In[63]:


term.text


# In[66]:


names=[]
for i in soup.find_all('div',class_="presidentListing"):
    names.append(i.text)
    
    
names


# In[69]:


term_in_office=[]
for i in soup.find_all('span',class_="terms"):
    term_in_office.append(i.text)
    
    
term_in_office


# In[70]:


print(len(names),len(term_in_office))


# In[73]:


df1=pd.DataFrame({'Name':names,'Term-In-Office':term_in_office})
df1


# In[ ]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.


# In[141]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# In[142]:


page1= requests.get("https://icc-cricket.com")
page1


# In[152]:


soup=BeautifulSoup(page1.content)
soup


# In[161]:


matches_team1 = soup.find('span',class_="u-hide-mobile")

matches_team1


# In[162]:


matches_team1.text


# In[ ]:


# Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
make data frame


# In[147]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[149]:


page2=requests.get('https://www.cnbc.com/world/?region=world')


# In[150]:


page2


# In[151]:


soup=BeautifulSoup(page2.content)
soup

