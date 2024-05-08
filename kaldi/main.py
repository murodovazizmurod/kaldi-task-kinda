from os import listdir


speakers = {
    '997': 'guvoh',
    '999': 'tony',
    '996': 'ruhiy'
}

books = {
    '996': [],
    '999': [],
    '997': []
}

transcripts = {
    '996': [],
    '997': [],
    '999': []
}


for t in listdir('transcripts'):
    if '997' in t:
        transcripts['997'].append(t)
    elif '996' in t:
        transcripts['996'].append(t)
    elif '999' in t:
        transcripts['999'].append(t)

for i in listdir('audios'):
    if 'Guvoh' in i:
        books['997'].append(i)
    elif 'Tony' in i:
        books['999'].append(i)
    elif 'Ruhiy' in i:
        books['996'].append(i)

for s in  speakers:
    transcripts[s] = sorted(transcripts[s], key=lambda x: int(x.split('_')[1].split('.')[0]))


# For wav.scp file
wavscp = ''

# for k, v in books.items():
#     for a in range(len(v)):
#         wavscp += f"{speakers[k]}_{transcripts[k][a].split('.')[0]}" + " " + './audios/'+str(v[a]) + '\n'


# with open('./kaldi/egs/digits/train/wav.scp', 'w', encoding="UTF-8") as file:
#     file.write(wavscp)


# for text file

text_file = ''
for k, v in books.items():
    for a in range(len(v)):
        text_file += f"{speakers[k]}_{transcripts[k][a].split('.')[0]}" + " " + f'./transcripts/{transcripts[k][a]}\n'

with open('./kaldi/egs/digits/train/text', 'w', encoding="UTF-8") as file:
    file.write(text_file)


# utt2spk file
utt2spk = ''
for k, v in books.items():
    for a in range(len(v)):
        utt2spk += f"{speakers[k]}_{transcripts[k][a].split('.')[0]}" + " " + f'{speakers[k]}\n'

with open('./kaldi/egs/digits/train/utt2spk', 'w', encoding="UTF-8") as file:
    file.write(utt2spk)