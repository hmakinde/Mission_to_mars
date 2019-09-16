#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import re
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup


# In[4]:


executable_path = {'executable_path': '/Users/hmm794/Downloads/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


# NASA MARS NEWS
# Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text
# Assign the text to variables that you can reference later
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[6]:


news_html = browser.html
nsoup = bs(news_html,'lxml')


# In[26]:


news_title = nsoup.find('div', class_='content_title').text
news_p = nsoup.find('div', class_='article_teaser_body').text
print('The news title is: ', news_title)
print('------')
print('The news paragraph is: ', news_p )


# In[27]:


## JPL Mars Space Imgades - Featured Image
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(jpl_url)


# In[28]:


jpl_html = browser.html
jsoup = bs(jpl_html,'lxml')


# In[31]:


img_link = jsoup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']
base_link = jsoup.find('div', class_='jpl_logo').a['href'].rstrip('/')
featured_image_url = base_link + img_link
featured_image_title = jsoup.find('h1', class_="media_feature_title").text.strip()
print('The reatured image url is: ', featured_image_url )


# In[42]:


## Mars Weather
twitter_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(twitter_url)


# In[47]:


# Parse html file with BeautifulSoup
twitter_html = browser.html
twitter_soup = bs(twitter_html,'html.parser')


# In[48]:


# Find weather tweets with BeautifulSoup
mars_weather_tweets = twitter_soup.find_all('p', class_='TweetTextSize')
mars_weather_tweets


# In[90]:


mars_weathers = tweet.text
for tweet in mars_weather_tweets:
    if tweet.text.startswith('Sol'):
        mars_weathers = tweet.text
    print(mars_weathers)


# In[92]:


# Url to Mars facts website
facts_url = 'https://space-facts.com/mars/'


# In[93]:


fact_table = pd.read_html(fact_url)
mars_fact_table = fact_table[0]


# In[94]:


mars_fact_table_html = mars_fact_table.to_html(header=False, index=False)


# In[95]:


mars_fact_table_html = mars_fact_table_html.replace('\n', '')


# In[100]:


mars_fact_table_html


# In[96]:


## Mars Hemispheres
hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hem_url)


# In[97]:


urls = [(a.text, a['href']) for a in browser
         .find_by_css('div[class="description"] a')]


# In[98]:


hemisphere_image_urls = []


# In[99]:


for title,url in urls:
    product_dict = {}
    product_dict['title'] = title
    browser.visit(url)
    img_url = browser.find_by_css('img[class="wide-image"]')['src']
    product_dict['img_url'] = img_url
    hemisphere_image_urls.append(product_dict)


# In[ ]:





# In[ ]:





# In[ ]:




