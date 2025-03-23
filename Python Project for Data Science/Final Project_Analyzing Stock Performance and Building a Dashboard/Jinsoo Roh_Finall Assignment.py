# Extracting and Visualizing Stock Data
import yfinance as yf
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import warnings
import os

# Set plot renderer (optional)
pio.renderers.default = "browser"

# Ignore future warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Define graphing function
def make_graph(stock_data, revenue_data, stock, output_file):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        subplot_titles=("Historical Share Price", "Historical Revenue"),
                        vertical_spacing=0.3)
    
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date),
                             y=stock_data_specific.Close.astype("float"),
                             name="Share Price"), row=1, col=1)

    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date),
                             y=revenue_data_specific.Revenue.astype("float"),
                             name="Revenue"), row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    
    # 🔥 HTML 파일로 저장
    fig.write_html(output_file)
    print(f"Saved {stock} graph to:\n{output_file}\n")



# ------------------------
# Question 1: Tesla stock
# ------------------------
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print("Tesla Data (head):")
print(tesla_data.head())

# ------------------------
# Question 2: Tesla revenue
# ------------------------
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url)
beautiful_soup = BeautifulSoup(html_data.text, "html5lib")

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
table = beautiful_soup.find_all("tbody")[1]
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()
        tesla_revenue = pd.concat(
            [tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])],
            ignore_index=True
        )

tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(',|\$', "", regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])

print("Tesla Revenue Data (tail):")
print(tesla_revenue.tail())

# ------------------------
# Question 3: GME stock
# ------------------------
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print("GameStop Data (head):")
print(gme_data.head())

# ------------------------
# Question 4: GME revenue
# ------------------------
url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url_2)
beautiful_soup_2 = BeautifulSoup(html_data_2.text, "html.parser")
tables = pd.read_html(url_2)
gme_revenue = tables[1]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$', "", regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])

print("GameStop Revenue Data (tail):")
print(gme_revenue.tail())

# ------------------------
# Question 5: Plot Tesla graph
# ------------------------
file_path = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python Project for Data Science\Final Project_Analyzing Stock Performance and Building a Dashboard"

tesla_file = os.path.join(file_path, "tesla_graph.html")
make_graph(tesla_data, tesla_revenue, 'Tesla', tesla_file)


# ------------------------
# Question 6: Plot GME graph
# ------------------------
gme_file = os.path.join(file_path, "gme_graph.html")
make_graph(gme_data, gme_revenue, 'GameStop', gme_file)