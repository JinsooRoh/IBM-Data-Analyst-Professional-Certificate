# Extracting and Visualizing Stock Data

import yfinance as yf
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import plotly.io as pio
pio.renderers.default = "iframe"

# In Python, you can ignore warnings using the warnings module.
# You can use the filterwarnings function to filter or ignore specific warning messages or categories.
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Define Graphing Function
# In this section, we define the function make_graph.
# You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

# Use the make_graph function the we've already defined.
# You'll need to invoke it in questions 5 and 6 to display the graphs and create the dashboard.
# Note: You don’t need to redefine the function for plotting graphs anywhere else in this notebook; just use the existing function.

# Question 1: Use yfinance to Extract Stock Data

# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object.
# The stock is Tesla and its ticker symbol is TSLA.
tesla = yf.Ticker("TSLA")

# Using the ticker object and the function history extract stock information and save it in a dataframe named tesla_data. Set the period parameter to "max" so we get information for the maximum amount of time.
tesla_data = tesla.history(period="max")

# Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

# Question 2: Use Webscraping to Extract Tesla Revenue Data

# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named html_data.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url)

# Parse the html data using beautiful_soup using parser i.e html5lib or html.parser.
beautiful_soup = BeautifulSoup(html_data.text,"html5lib")

# Using BeautifulSoup or the read_html function extract the table with Tesla Revenue and store it into a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue..
# 1. Create an Empty DataFrame
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# 2. Find the Relevant Table
table = beautiful_soup.find_all("tbody")[1]

# 3. Check for the Tesla Quarterly Revenue Table

# 4. Iterate Through Rows in the Table Body
rows = table.find_all("tr")
for row in rows:
    # 5. Extract Data from Columns
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()
        
        # 6. Append Data to the DataFrame
        tesla_revenue = pd.concat(
            [tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])],
            ignore_index=True
        )

# Execute the following line to remove the comma and dollar sign from the Revenue column.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")

# Execute the following lines to remove an null or empty strings in the Revenue column.
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.
tesla_revenue.tail()

# Question 3: Use yfinance to Extract Stock Data

# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object.
# The stock is GameStop and its ticker symbol is GME.
gme = yf.Ticker("GME")

# Using the ticker object and the function history extract stock information and save it in a dataframe named gme_data.
# Set the period parameter to "max" so we get information for the maximum amount of time.
gme_data = gme.history(period="max")


# Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display the first five rows of the gme_data dataframe using the head function.
# Take a screenshot of the results and code from the beginning of Question 3 to the results below.
gme_data.reset_index(inplace=True)
print(gme_data.head())

# Question 4: Use Webscraping to Extract GME Revenue Data
# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html.
# Save the text of the response as a variable named html_data_2.
url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url_2)

# Parse the html data using beautiful_soup using parser i.e html5lib or html.parser.
beautiful_soup_2 = BeautifulSoup(html_data_2.text,"html.parser")

# Using BeautifulSoup or the read_html function extract the table with GameStop Revenue and store it into a dataframe named gme_revenue.
# The dataframe should have columns Date and Revenue.
# Make sure the comma and dollar sign is removed from the Revenue column.
tables = pd.read_html(url_2)
gme_revenue = tables[1]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

# Question 5: Plot Tesla Stock Graph
# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])

tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",", "", regex=False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "", regex=False)

tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

make_graph(tesla_data, tesla_revenue, 'Tesla')

# Quesiton 6: Plot GameStop Stock Graph
gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])

gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",", "", regex=False)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$", "", regex=False)

gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

make_graph(gme_data, gme_revenue, 'GameStop')