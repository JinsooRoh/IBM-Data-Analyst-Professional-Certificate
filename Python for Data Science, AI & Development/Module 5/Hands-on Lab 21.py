# API Examples
# Example 1: RandomUser API

# Bellow are Get Methods parameters that we can generate. 
# Get Methods
# get_cell()
# get_city()
# get_dob()
# get_email()
# get_first_name()
# get_full_name()
# get_gender()
# get_id()
# get_id_number()
# get_id_type()
# get_info()
# get_last_name()
# get_login_md5()
# get_login_salt()
# get_login_sha1()
# get_login_sha256()
# get_nat()
# get_password()
# get_phone()
# get_picture()
# get_postcode()
# get_registered()
# get_state()
# get_street()
# get_username()
# get_zipcode()

# To start using the API you can install the randomuser library running the pip install command.
# pip install randomuser
# pip install pandas

# Then, we will load the necessary libraries.
from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
print(some_list)

# The "Get Methods" functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset.
# For example, to get full name, we call get_full_name() function.
name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
for user in some_list:
    print(user.get_full_name(),"",user.get_email())

# Exercise 1
# In this Exercise, generate photos of the random 10 users.
for user in some_list:
    print(user.get_picture())

# To generate a table with information about the users, we can write a function containing all desirable parameters.
# For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed.
# We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
from randomuser import RandomUser
import pandas as pd

def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({
            "Name": user.get_full_name(),
            "Gender": user.get_gender(),
            "City": user.get_city(),
            "State": user.get_state(),
            "Email": user.get_email(),
            "DOB": user.get_dob(),
            "Picture": user.get_picture()
        })
    return pd.DataFrame(users)

get_users()

df1 = pd.DataFrame(get_users())

# Example 2: Fruityvice API
# Another, more common way to use APIs, is through requests library. The next lab, Requests and HTTP, will contain more information about requests.
# We will start by importing all required libraries.

import requests
import json

# We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format.
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function.
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
print(df2)

# Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

# Exercise 2
# In this Exercise, find out how many calories are contained in a banana.
banana = df2.loc[df2["name"] == 'Banana']
cal_banana = banana.iloc[0]['nutritions.calories']
print(cal_banana)

# Exercise 3
# This page contains a list of free public APIs for you to practice. Let us deal with the following example.
import requests
import json
import pandas as pd

# Fetch data from the Official Joke API
url = 'https://official-joke-api.appspot.com/jokes/ten'
data2 = requests.get(url)
results2 = json.loads(data2.text)

# Convert JSON data into a pandas DataFrame and drop unnecessary columns
df3 = pd.DataFrame(results2)
df3.drop(columns=["type", "id"], inplace=True)

# Remove line breaks and extra whitespace from setup and punchline columns
df3['setup'] = df3['setup'].str.replace(r'\n|\r', ' ', regex=True).str.strip()
df3['punchline'] = df3['punchline'].str.replace(r'\n|\r', ' ', regex=True).str.strip()

# Configure pandas display options for better output formatting
pd.set_option('display.max_colwidth', None)  # Remove column width limit
pd.set_option('display.expand_frame_repr', False)  # Prevent frame expansion
pd.set_option('display.colheader_justify', 'left')  # Align column headers to the left

# Print the DataFrame in a clean format with adjusted column spacing
print(df3.to_string(index=False, justify='left', col_space=60))