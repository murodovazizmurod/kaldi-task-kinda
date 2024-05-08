from selenium import webdriver
import chromedriver_autoinstaller
import re
import json

# Read the JSON data from data.json
with open('data.json', 'r') as file:
    json_data = json.load(file)

# Initialize an empty list to store the URLs
urls = []

# Extract URLs from the JSON data
for item in json_data:
    if item:
        urls.append(item)



chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path



for url in urls[:5]:
    driver = webdriver.Chrome()



    # Initialize a headless browser (e.g., Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    # Load the webpage
    driver.get(url)

    # Get the HTML content of the page
    html_text = driver.page_source

    # Close the browser
    driver.quit()
    try:
        html_text = html_text.split('var myPlaylist = [')[1].split("$('#audioplayer').ttwMusicPlayer(myPlaylist")[0]
    except:
        print(url)
        continue
    # print(html_text)
    text_without_spaces = re.sub(r'\s+', ' ', html_text)
    text_without_spaces = text_without_spaces.replace('];', '')
    with open('mp3s.json','a',encoding="UTF-8") as file:
        file.writelines(text_without_spaces+'\n')