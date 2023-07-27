import nltk 
import re 
from nltk.corpus import stopwords 
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

with open('miracle_in_the_andes.txt', 'r') as file:
    book = file.read()

import re 
pattern = re.compile('[a-zA-Z]+')
findings = re.findall(pattern, book.lower())
findings[:5]

dict = {}
for word in findings:
    if word in dict.keys():
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1

d_list = [(value, key) for (key, value) in dict.items()]
d_list = sorted(d_list, reverse=True)
#print(d_list[:5])

#remove stop words 
english_stopwords = stopwords.words('english')
filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))
#print(filtered_words[:10])

#SENTIMENT ANALYSIS: What is the most positive and negative chapters?

analyzer = SentimentIntensityAnalyzer()
#print(analyzer)

#expects a string
scores = analyzer.polarity_scores(book)
if scores['pos'] > scores['neg']:
    print('It is a positive text')
else:
    print('It is a negative text.')

######Chapter sentiment analysis#######

#get the chapter
pattern = re.compile('Chapter [0-9]+')
#split them by the pattern
chapters = re.split(pattern, book)
#exclude the first one that's a tite to get the actual chapters 
chapters = chapters[1:]

for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    print(scores)
