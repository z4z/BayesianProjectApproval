from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import pickle


num_features = 1000
num_components = 10

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()
    
    
print("Loading Data...")
articles = pickle.load(open("articles","rb"))
articles = np.array(articles)
data = articles[:,1]

print("Vectorizing...")
tf_vectorizer = CountVectorizer(max_df=0.8, min_df=2,max_features=num_features,stop_words='english')
tf = tf_vectorizer.fit_transform(data)

print("Learning LDA...")
lda = LatentDirichletAllocation(n_components=num_components,learning_method='online',random_state=17)
features = lda.fit_transform(tf)


print("Saving Features...")
pickle.dump(features,open("features4","wb"))

tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, 10)