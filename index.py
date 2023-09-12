# All imports here.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the HTML.
start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'

# Download the HTML from start_url
downloaded_html = requests.get(start_url)

# Parse the HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text)

# To open file, and  transforms a complex HTML document into a complex tree of Python objects.
with open('downloaded.html', 'w')as file:
  file.write(soup.prettify())

# Extract data to pandas
full_table = soup.select('table.wikitable')[1]
# print(full_table) 
table_head = full_table.select('tr th')

print('---------')
table_columns = []
for element in table_head:
  column_label = element.get_text(separator=' ', strip=True)
  table_columns.append(column_label)
  print(column_label)
print(table_columns)
print('------------------')

regex = re.compile('\[\d{3}\]')
table_rows = full_table.select('tr')
table_data = []

for index, element in enumerate(table_rows):
  if index > 0:
    row_list = []
    blank =[]
    values = element.select('td')
    for value in values:
      row_list.append(value.text.strip())
    table_data.append(row_list)
print(table_data)

df = pd.DataFrame(table_data, columns=table_columns)
regex = re.compile('\[\d{3}\]')
df.replace(regex, '', inplace=True)
df
