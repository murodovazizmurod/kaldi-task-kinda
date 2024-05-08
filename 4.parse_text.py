import requests
import json
from bs4 import BeautifulSoup

site = 'https://www.kitobook.com'

with open('transcriptions.json', 'r') as file:
    json_data = json.load(file)


for i in json_data:
    data = requests.get(site+i)
    soup = BeautifulSoup(data.text, 'html.parser')

    # Find the <ul> element using the CSS selector
    text = soup.select_one('div.text')

    filepath = "./transcripts/" + i.split('/')[-2] + '_' + i.split('/')[-1] + '.txt'
    
    # Open the file in write mode
    with open(filepath, "w", encoding="UTF-8") as file:
        # Write the data to the file
        file.write(text.text)
