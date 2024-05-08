from bs4 import BeautifulSoup, element
import requests
import re
import json

# URL of the webpage to scrape
url = 'https://www.kitobook.com/kitoblar/category/book/kutubxona/{0}/1/'

ids = []

with open('data.json', 'r') as file:
    json_data = json.load(file)

for i in json_data:
    ids.append(i.split('/')[-2])

text_url = []

for id in ids:
    # Send a GET request to the URL
    response = requests.get(url.format(id))

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <ul> element using the CSS selector
    ul_element = soup.select_one('ul.pagination')

    ul_element = ul_element.find_all('li')
    for i in ul_element:
        data: element.Tag = i.find('a')
        u = str(data).split('href="')[-1].split('/">')[0]
        current = i.find('span')
        current = str(current).replace('<span class="page-numbers current">', '').replace('</span>', '')
        text_url.append(u if u != "None" else f'/kitoblar/category/book/kutubxona/{id}/{current}')



with open('transcriptions.json', 'w') as json_file:
    json.dump(text_url, json_file, indent=4)