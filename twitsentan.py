#Display top 5 rows to check if everything looks good
df.head(5)

#To save it back as Excel
df.to_excel("path to save") #Write DateFrame back as Excel file
consumer_key='pxVtnqmxyRlORbO61He73OcjD'
consumer_secret='1uPdOXUtvRTN0ZmodbbUgYyOjs8U8IkGDOd3BMDtjXp4W566mD'
access_token='167750290-1P8C3JDRvoRS1eLa0b2zPRhnwJ9bDY4hOsz8Qb6H'
access_secret='OmFH0bmb1okjF5puI9IxcvxX0DWI4JUrBmNDJqMNR7T7O'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
fetched_tweets = api.search(q = 'india', count = 400, ln= 'en')
fetched_tweets
tweet_df=pd.DataFrame(columns=['text'])
tweet_df
tweets = []
for tweet in fetched_tweets:
    tweets_text= tweet.text
    tweets.append(tweets_text)
    
tweet_df['text']=tweets
tweet_df.head()	
tweet_df.iloc[1,0]
tweet_df['text'] =pd.DataFrame(tweet_df['text'].unique())
tweet_df.head()
tweet_df.isnull().sum()
#droping NAN valus
tweet_df1=tweet_df.dropna()
tweet_df1[:5]
stopwords=set(STOPWORDS)
stopwords
import matplotlib.pyplot as plt
all_words =' '.join([text for text in tweet_df1['text']])
wordcloud=WordCloud(width=800,height=500,random_state=21,background_color='pink',max_font_size=110).generate(all_words)
plt.figure(figsize=(10,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()