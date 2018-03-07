# Mission to Mars

![mission_to_mars](Images/final_app_part2.png)

I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

I completed my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.  The code is housed in a Jupyter Notebook file called `mission_to_mars.ipynb` that scrapes multiple sites for data:

* Scrapes the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragragh Text. 
* Visits the url for Nasa's Jet Propulsion Laboratory Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
* Visits the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrapes the latest Mars weather tweet.
* Visits the Mars Facts webpage [here](http://space-facts.com/mars/) and scrapes the table for facts about Mars: Diameter, Mass, etc.
* Visits the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

Next I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped.  I did this by converting my Jupyter notebook into a Python script called `scrape_mars.py` with a `scrape` function that executes the scraping code and returns one Python dictionary containing all of the scraped data.  Then I created a route called `/scrape` that imports the `scrape_mars.py` and calls the scrape function.  There is also a root route (`/`) that queries the Mongo databse and passes the data into an HTML template for display it.
