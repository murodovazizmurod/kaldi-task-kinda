import requests
# from pydub import AudioSegment

host = 'https://www.kitobook.com/'


urls = []

# Open the text file in read mode
with open('audio_urls.txt', 'r') as file:
    # Read each line from the file and add it to the list
    for line in file:
        # Optionally, you can strip whitespace characters (like newline) from each line
        # and add it to the list
        urls.append([line.strip().split('/')[-1], line.strip()] )

for i in urls:
	response = requests.get(host+i[1])
	with open('./audios/'+i[0],'wb') as mp3:
		mp3.write(response.content)