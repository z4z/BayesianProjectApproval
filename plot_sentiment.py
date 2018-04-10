import pickle
import numpy as np
import matplotlib.pyplot as plt
         
sentiments_by_day = pickle.load(open("sentiments_by_day","rb"))

num_days = sentiments_by_day.shape[0]
days = np.arange(num_days)

# plot by day

plt.figure()
plt.plot(days, sentiments_by_day)
plt.title("Average Sentiment of New York Times Articles About Trump per Day")
plt.xlabel("Days Since Inauguration")
plt.ylabel("Positive Sentiment")
plt.savefig("sentiment_plots/by_day")

# plot by week

w = 7
days_w = days[w::w] - w

plt.figure()
new = [np.mean(sentiments_by_day[j-w:j]) for j in range(w,num_days,w)]
plt.bar(days_w, new, width=w)
plt.title("Average Sentiment of New York Times Articles About Trump per Day")
plt.xlabel("Days Since Inauguration")
plt.ylabel("Positive Sentiment")
plt.savefig("sentiment_plots/by_week")

plt.show()