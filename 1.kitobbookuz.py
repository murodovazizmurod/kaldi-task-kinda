from bs4 import BeautifulSoup
import requests
import re
import json

# URL of the webpage to scrape
url = 'https://www.kitobook.com/kitoblar/audio'
site = 'https://www.kitobook.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find the <ul> element using the CSS selector
ul_element = soup.select_one('#content > div > div:nth-child(2) > div:nth-child(2) > ul')
urls = []
# If the <ul> element is found
if ul_element:
    # Find all <li> elements inside the <ul> element
    li_elements = ul_element.find_all('li')
    
    # If there are <li> elements found
    if li_elements:
        for a in li_elements:
            a_elements = a.select_one('a')
            text_without_spaces = re.sub(r'\s+', ' ', a.text)

            urls.append(site+a_elements.get('href'))
    else:
        print("No <li> elements found inside the <ul> element.")
else:
    print("No <ul> element found on the webpage with the specified CSS selector.")


with open('data.json', 'w') as json_file:
    json.dump(urls, json_file, indent=4)