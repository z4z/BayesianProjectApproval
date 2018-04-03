import pickle
import numpy as np
import matplotlib.pyplot as plt

features = pickle.load(open("features4","rb"))
dates = pickle.load(open("dates","rb"))
features = np.hstack((dates,features))
length = dates.max()+1
avg_features = np.zeros((length,features.shape[1]))
for i in range(0,length):
    indices = np.nonzero(dates[:,0]==i)
    avg_features[i,:]=(sum(features[indices],0)/len(indices[0]))
         
pickle.dump(avg_features,open("avg_features","wb"))

days = avg_features[:,0]
num_days = len(days)
num_features = len(avg_features[0,:])

# stacked bar graph
# plt.bar(days, avg_features[:,1])

# for i in range(2,num_features):
# 	b = sum([avg_features[:,j] for j in range(1,i)])
# 	plt.bar(days, avg_features[:,i], bottom=b, width=1)

w = 7
days_w = days[w::w] - w

titles = ['Days','North Korea','Congress','Administration','Russia','Healthcare','News','Court','Miscellaneous','Trade','Taxes']

for i in range(1, num_features):
	plt.figure()
	new = [np.mean(avg_features[j-w:j,i]) for j in range(w,num_days,w)]
	plt.bar(days_w,new,width=w)
	plt.title(titles[i])
	plt.xlabel("Days Since Inauguration")
	plt.ylabel("Relative Frequncy of Topic")
	plt.savefig("LDA_plots/" + titles[i])

# for i in range(1,num_features):
# 	avg = np.mean(avg_features[])
# 	plt.bar(width=w)

# north_korea = avg_features[:,1]
# administration = avg_features[:,2]
# russia = avg_features[:,3]
# healthcare = avg_features[:,4]

# plt.bar(days,north_korea,width=1)
# plt.bar(days,administration,width=1)
# plt.bar(days,russia,width=1)
# plt.bar(days,healthcare,width=1)

plt.show()

