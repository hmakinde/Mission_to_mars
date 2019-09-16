#!/usr/bin/env python
# coding: utf-8



# Dependencies
import pandas as pd
import re
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup



def init_browser():
    executable_path = {'executable_path': '/Users/hmm794/Downloads/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    mars_facts_data = {}
    # NASA MARS NEWS
    # Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text
    # Assign the text to variables that you can reference later
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    news_html = browser.html
    nsoup = bs(news_html,'lxml')


    news_title = nsoup.find('div', class_='content_title').text
    news_p = nsoup.find('div', class_='article_teaser_body').text
    print('The news title is: ', news_title)
    print('------')
    print('The news paragraph is: ', news_p )
    mmars_facts_data['news_title'] = news_title
    mars_facts_data['news_paragraph'] = news_p 


    ## JPL Mars Space Imgades - Featured Image
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)


    jpl_html = browser.html
    jsoup = bs(jpl_html,'lxml')


    img_link = jsoup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']
    base_link = jsoup.find('div', class_='jpl_logo').a['href'].rstrip('/')
    featured_image_url = base_link + img_link
    featured_image_title = jsoup.find('h1', class_="media_feature_title").text.strip()
    print('The reatured image url is: ', featured_image_url )
    mars_facts_data["featured_image"] = featured_img_url



    ## Mars Weather
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    # Parse html file with BeautifulSoup
    twitter_html = browser.html
    twitter_soup = bs(twitter_html,'html.parser')

    # Find weather tweets with BeautifulSoup
    mars_weather_tweets = twitter_soup.find_all('p', class_='TweetTextSize')
    mars_weather_tweets

    mars_weathers = tweet.text
    for tweet in mars_weather_tweets:
        if tweet.text.startswith('Sol'):
            mars_weathers = tweet.text
        print(mars_weathers)
    mars_facts_data["mars_weather"] = mars_weathers


    # Url to Mars facts website
    
    facts_url = 'https://space-facts.com/mars/'

    fact_table = pd.read_html(fact_url)
    
    mars_fact_table = fact_table[0]

    mars_fact_table_html = mars_fact_table.to_html(header=False, index=False)

    mars_fact_table_html = mars_fact_table_html.replace('\n', '')

    mars_fact_table_html

    mars_facts_data["mars_facts_table"] = mars_fact_table_html
    

    ## Mars Hemispheres
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)


    urls = [(a.text, a['href']) for a in browser
             .find_by_css('div[class="description"] a')]


    hemisphere_image_urls = []


    for title,url in urls:
        product_dict = {}
        product_dict['title'] = title
        browser.visit(url)
        img_url = browser.find_by_css('img[class="wide-image"]')['src']
        product_dict['img_url'] = img_url
        hemisphere_image_urls.append(product_dict)
        
    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls
    
    return mars_facts_data




