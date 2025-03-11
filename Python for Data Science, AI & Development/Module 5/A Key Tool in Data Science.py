# Web Scraping: A Key Tool in Data Science

# Importance of Web Scraping in Data Science
# Data Collection: Web scraping is a primary method of collecting data from the internet. This data can be used for analysis, research, etc.
# Real-time Application: Web scraping is used for real-time applications like weather updates, price comparison, etc.
# Machine Learning: Web scraping provides the data needed to train machine learning models.

# Web Scraping with Python

# BeautifulSoup
# BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files.
# It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.
from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Scrapy
# Scrapy is an open-source and collaborative web crawling framework for Python.
# It is used to extract theimport scrapy
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}

# Selenium
# Selenium is a tool used for controlling web browsers through programs and automating browser tasks.
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.example.com")