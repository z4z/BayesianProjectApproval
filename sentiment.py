from textblob import TextBlob
import numpy as np
import pickle
import sys

# print("Loading Data...")
data = np.array(pickle.load(open("articles","rb")))
articles = data[:,1]

# num_articles = articles.shape[0]

# sentiments = np.zeros(num_articles)

# for i in range(num_articles):
# 	article = articles[i]
# 	analysis = TextBlob(article)
# 	sentiment = analysis.sentiment.polarity
# 	sentiments[i] = sentiment
# 	print(sentiment)

# print("Saving Sentiments...")
# pickle.dump(sentiments,open("sentiments","wb"))

dates = pickle.load(open("dates","rb"))
sentiments = pickle.load(open("sentiments", "rb"))

print(articles[np.nonzero(dates[:,0]==336)].shape)
sys.exit()

length = dates.max()+1
sentiments_by_day = np.zeros(length)

for i in range(0,length):
    indices = np.nonzero(dates[:,0]==i)
    sentiments_by_day[i]=(sum(sentiments[indices],0)/len(indices[0]))




print(sentiments_by_day)

print("Saving Sentiments by Day")
pickle.dump(sentiments_by_day,open("sentiments_by_day","wb"))
