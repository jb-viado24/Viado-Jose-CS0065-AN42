import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('squads.csv')

df.head()

print(df.shape)

text_cols = [c for c in df.columns if c.endswith('/question') or c.endswith('/context')]
text_list = df[text_cols].stack().dropna().astype(str).tolist()
print(len(text_list))

clean_desc = []
for w in range(len(text_list)):
    desc = text_list[w].lower()

    #remove punctuation
    desc = re.sub('[^a-zA-Z]', ' ', desc)

    #remove tags
    desc=re.sub("</?.*?>"," <> ",desc)

    #remove digits and special chars
    desc=re.sub("(\\d|\\W)+"," ",desc)

    clean_desc.append(desc)

stop_words = ['is','you','your','and', 'the', 'to', 'from', 'or',
'I', 'for', 'do', 'get', 'not', 'here', 'in', 'im', 'have', 'on',
're', 'new', 'subject']

wordcloud = WordCloud(width = 800, height = 800, background_color =
'black', stopwords = stop_words, max_words = 1000
                      , min_font_size =
20).generate(' '.join(clean_desc))

fig = plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('cloud_text_csv.png')
plt.show()