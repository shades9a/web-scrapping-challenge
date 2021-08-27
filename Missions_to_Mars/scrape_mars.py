
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():

    ExecutablePath = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome',headless=False)

def scrape_info():
    browser = init_browser()

    UrlNews = "https://mars.nasa.gov/news/"
    browser.visit(UrlNews)

    html = browser.html
    NewsMars = BeautifulSoup(html, 'lxml')

    NewsTitle = NewsMars.find('div','content_title').text
    
    NewsParagraph = NewsMars.find('div','rollover_description_inner').text

    browser.quit()

    browser = init_browser()
 
    UrlJplImages = 'https://www.jpl.nasa.gov/spaceimages/?search=planet&category=Mars'
    browser.visit(UrlJplImages)
    
    html = browser.html
    JplSoup = BeautifulSoup(html, 'lxml')

    UrlJpl = 'https://www.jpl.nasa.gov'
    image = JplSoup.find_all('img', class_='thumb')[30]['src']
    ImageUrl = UrlJpl + image

    browser.quit()

    browser = init_browser()

    UrlTWTR = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(UrlTWTR)

    html = browser.html

    browser.quit()

    browser = init_browser()

    UrlFacts = 'https://space-facts.com/mars/'
    browser.visit(UrlJpl)

    html = browser.html

    browser.quit()

    UrlHemispheres = "https://astrogeology.usgs.gov"
    UrlHemispheresImages = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    
    browser.quit()

