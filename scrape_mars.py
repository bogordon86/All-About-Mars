
#Import Dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver

def init_browser():
# Create a path for Chrome Driver
	executable_path = {"executable_path": "./chromedriver.exe"}
	return Browser('chrome', **executable_path, headless=False)
	
def scrape():
	browser = init_browser()
	
    #Visit the Nasa Mars News Page
	nasa_url = 'https://mars.nasa.gov/news/'
	browser.visit(nasa_url)
	time.sleep(1)
	html = browser.html
	soup = bs(html, 'html.parser')

    #Get the news text and body
	news = soup.find("ul", class_="item_list")
    # Narrowing in on our Title\n,
	news_title = news.find("div", class_="content_title").text
	
    #Narrowing in on the News Text Body
	news_body = news.find("div", class_="article_teaser_body").text

    #Visit the Nasa Space Images of Mars Page
	spaceimg_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(spaceimg_url)
	time.sleep(1)
 
    # Retrieve the featured image from the page
    # Scrape the page
	spaceimg_html = browser.html
	spaceimg_soup = bs(spaceimg_html, 'html.parser')
 
    # Retrieving image link
	space_img = spaceimg_soup.find('a', class_="fancybox")
   
	featured_image_url = 'https://www.jpl.nasa.gov'+ space_img['data-fancybox-href']
 
    #Visit the Mars Weather Twitter Page 
	tweet_url = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(tweet_url)
	time.sleep(1)
  
	tweet_html = browser.html
	tweet_soup = bs(tweet_html, 'html.parser')
   
    #Retrieve the tweet
	mars_tweet = tweet_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
   
	mars_weather = mars_tweet.find('p', class_='tweet-text').text

 
    # Visit the Space Facts Page
	facts_url = "https://space-facts.com/mars/"
	browser.visit(facts_url)
	time.sleep(1)
 
	facts_html = browser.html
	facts_soup = bs(facts_html, 'html.parser')
	
    #Put the facts into a new table
	facts_table = facts_soup.find('table', class_='tablepress')

	frame_table = pd.DataFrame(columns=['description', 'value'], index = range(0,9))

	row_count = 0
	for row in facts_table.find_all('tr'):
		column_count = 0
		columns = row.find_all('td')
		for column in columns:
			frame_table.iat[row_count, column_count] = column.get_text()
			column_count += 1
		row_count += 1
	
	#Convert table to html
	table_html = frame_table.to_html(index=False)
   
	# Visit the USGS Astrogeology page
    #astro_url = ("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\")
    #browser.visit(astro_url)
    #time.sleep(1)
  
    # Scrape the page
    #astro_html = browser.html
    #astro_soup = bs(astro_html, 'html.parser')
  
    # Retrieving image link
    #image = astro_soup.find("div", class_="item")
  
    #image_url = image.find("img", class_="thumb")["src"]
    #featured_image_url = ("https://www.jpl.nasa.gov\" +image_url)
    #featured_image_url
  
	#Create a dictionary containing all scraped data from above
	mars_info = {
		"news_title" : news_title,
        "news_text" : news_body,
        "image" : featured_image_url,
        "weather" : mars_weather,
        "facts" : table_html
    }

	return(mars_info)