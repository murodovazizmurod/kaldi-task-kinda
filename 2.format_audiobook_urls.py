

data = ''

with open('mp3s.json', 'r', encoding='UTF-8') as file:
    data = file.read()

data = data.split(' { mp3:\'/')

for i in data:
    with open('audio_urls.txt','a',encoding="UTF-8") as file:
        file.writelines(i.split('\', title:\'')[0]+'\n')