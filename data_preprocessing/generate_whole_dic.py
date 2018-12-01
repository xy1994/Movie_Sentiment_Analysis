import json

result = {}
stop_word = []
emotion_word = []

with open('stop_words.txt') as stopword:
    for line in stopword:
        word = line[:-1]
        word = filter(str.isalpha, word)
        word = word.lower()
        stop_word.append(word)

with open('emotion_dict.txt') as emoword:
    for line in emoword:
        word = line[:-1]
        word = filter(str.isalpha, word)
        word = word.lower()
        emotion_word.append(word)



#print stop_word

with open('Movies_and_TV_5.json') as json_data:
    for line in json_data:
        d = json.loads(line)
        #print(d)
        text = d['reviewText']
        text = str(text)
        #text = filter(str.isalpha, text)
        text = text.split()
        #text = filter(str.isalpha, text)
        for word in text:
            word = filter(str.isalpha, word)
            word = word.lower()
            if word not in stop_word:
                if word in emotion_word:
                    if word not in result:
                        result[word] = 0
                    result[word] += 1


finallist = sorted(result.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
#print result
file = open('whole_emotion_dic.txt', 'w')
for item in finallist:
  print>>file,item
