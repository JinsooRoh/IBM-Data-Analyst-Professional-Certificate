# Web Scraping with Python

# Python provides several libraries for web scraping. 
# 1. BeautifulSoup: BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files.
# It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# 2. Scrapy: Scrapy is an open-source and collaborative web crawling framework for Python.
# It is used to extract the data from the website.

import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}

# 3. Selenium: Selenium is a tool used for controlling web browsers through programs and automating browser tasks.

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.example.com")