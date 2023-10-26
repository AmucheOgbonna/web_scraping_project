import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the HTML.
start_url = 'https://en.wikipedia.org/wiki/Amazon_(company)'

# Download the HTML from start_url
download_html = requests.get(start_url)

# Parse the HTML with BeautifulSoup and create a soup objecttext)
beautiful_soup = BeautifulSoup(download_html.text)

# To open file, and  transforms a complex HTML document into a complex tree of Python objects.
with open('download_html', 'w')as file:
  file.write(beautiful_soup.prettify())
# Get the column headers
table_heads = full_table.select('[scope*="col"]')
table_columns = []

for element in table_heads:
  column_label = element.get_text(strip=True)
  table_columns.append(column_label)

table_head = full_table.select('th')[5]
table_head =table_head.get_text(strip=True)
table_columns.append(table_head)

print(table_columns)

regex = re.compile('\[\d{2}\]')

table_rows = full_table.find_all(['tr','class*="rh heading table-rh"'])
table_data = []

for index, element in enumerate(table_rows):
  val = element.select('th')
  values = element.select('td')
  if index > 0:
    if index == 1:
      Africa = ['Africa']
      values =element.select('td')
      for value in values:
        Africa.append(value.text.strip())
      table_data.append(Africa)


    elif index > 1 and index <=5:
      Americas = ['Americas']
      values =element.select('td')
      for value in values:
        column_label = value.get_text(strip = True)
        column_label = regex.sub(' ',column_label)
        Americas.append(column_label)
      table_data.append(Americas)


    elif index > 5 and index <=12:
      Asia = ['Asia']
      values =element.select('td')
      for value in values:
        Asia.append(value.text.strip())
      table_data.append(Asia)

    elif index > 12 and index <=21:
      Europe = ['Europe']
      values =element.select('td')
      for value in values:
        column_label = value.get_text(strip = True)
        column_label = regex.sub(' ',column_label)
        Europe.append(column_label)
      table_data.append(Europe)

    else:
      Oceania = []
      values =element.select('td')
      for value in values:
        Oceania.append(value.text.strip())
      table_data.append(Oceania)

print(table_data)
df = pd.DataFrame(table_data, columns=table_columns)
df
