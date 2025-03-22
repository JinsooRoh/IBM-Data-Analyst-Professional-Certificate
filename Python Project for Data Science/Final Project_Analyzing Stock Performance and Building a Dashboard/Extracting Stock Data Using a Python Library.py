
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import requests
import os

# Using the yfinance Library to Extract Stock Data
# Using the Ticker module we can create an object that will allow us to access functions to extract data.
# To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.
apple = yf.Ticker("AAPL")

# Now we can access functions and variables to extract the type of data we need.
# You can view them and what they represent here https://aroussi.com/post/python-yahoo-finance.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
response = requests.get(url)

save_dir = "C:/Users/js090/Desktop/IBM Data Analyst Professional Certificate/Python Project for Data Science/Final Project_Analyzing Stock Performance and Building a Dashboard"
save_path = f"{save_dir}/apple.json"

os.makedirs(save_dir, exist_ok=True)

with open(save_path, "wb") as file:
    file.write(response.content)

print("apple.json file is downloaded.")


# Stock Info
# Usig the attribute info we can extract information about the stock as a Python dictionary.
import json

file_path = "C:/Users/js090/Desktop/IBM Data Analyst Professional Certificate/Python Project for Data Science/Final Project_Analyzing Stock Performance and Building a Dashboard/apple.json"

with open(file_path) as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable
    # Print("Type:", type(apple_info))

print(apple_info)
print(apple_info["country"])

# Extracting Share Price
# A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time.
# Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data.
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
print("\nExtracting Share Price Data: ")
apple = yf.Ticker("AAPL")
apple_share_price_data = apple.history(period="max")
# print(apple_share_price_data) # All data

# The format that the data is returned in is a Pandas DataFrame. With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
print(apple_share_price_data.head())

# We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.
apple_share_price_data.reset_index(inplace=True)

# We can plot the Open price against the Date:
apple_share_price_data.plot(x="Date", y="Open")
print(apple_share_price_data.head())

# Extracting Dividends
# Dividends are the distribution of a companys profits to shareholders.
# In this case they are defined as an amount of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data.
# The period of the data is given by the period defined in the 'history` function.
print(apple.dividends)

# We can plot the dividends overtime:
apple.dividends.plot()



# Exercise
# Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd.
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import requests
import os

amd = yf.Ticker("AMD")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
response = requests.get(url)

save_dir = "C:/Users/js090/Desktop/IBM Data Analyst Professional Certificate/Python Project for Data Science/Final Project_Analyzing Stock Performance and Building a Dashboard"
save_path = f"{save_dir}/amd.json"

os.makedirs(save_dir, exist_ok=True)

with open(save_path, "wb") as file:
    file.write(response.content)

print("amd.json file is downloaded.")

import json

file_path = "C:/Users/js090/Desktop/IBM Data Analyst Professional Certificate/Python Project for Data Science/Final Project_Analyzing Stock Performance and Building a Dashboard/amd.json"

with open(file_path) as json_file:
    amd_info = json.load(json_file)

print(amd_info)

# Question 1
# Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.
print(amd_info["country"])

# Question 2
# Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.
print(amd_info["sector"])

# Question 3
# Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).
print("\nExtracting Volume Data: ")

amd_share_price_data = amd.history(period="max")
print(f"Volume traded on the first day: {amd_share_price_data['Volume'][0]}")
