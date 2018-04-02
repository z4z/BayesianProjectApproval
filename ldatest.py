from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()

data = ['The programming model of KRL has identity as a core feature. KRL programs execute on behalf of a particular entity. The idea of entity is built into the underlying semantics of the language. The entity orientation of KRL is supported by the underlying KRE (Kynetx Rules Engine) and so is usable by any program running in the engine—even one not written in KRL. The next two features illustrate why identity is crucial to the programming model.','KRL has a class of variables called “persistent variables” or just “persistents”. There are two kinds of persistents: application variables and entity variables. Both are closed over the ruleset they are in, meaning that they are only visible to code executing within the ruleset. Application variables are stored for the ruleset and are available to any entity executing the ruleset. Entity variable values are only visible to the entity for whom they were stored. Application variables are roughly analogous to class variables. Entity variables are like instance variables.','Conditions are similar to the safety of a gun. If the conditional expression does not return true, the rule does not fire. Just as a gun either shoots or doesn\'t shoot based upon the safety, there is no else statement on conditionals. If you want a rule to fire in the opposite case, you can use the not fired postlude to trigger another event, or you can have a rule with a conditional which tests for the opposite case.', 'Collodi was born in Florence on 24 November 1826. He spent most of his childhood in the town of Collodi where his mother was born. His mother was a farmer\'s daughter and his father was a cook. He had 10 siblings but seven died at a young age.','During the Italian wars of Independence in 1848 and 1860 Collodi served as a volunteer with the Tuscan army. His active interest in political matters may be seen in his earliest literary works as well as in the founding of the satirical newspaper Il Lampione in 1853. This newspaper was censored by order of the Grand Duke of Tuscany.[2] In 1854 he published his second newspaper, Lo scaramuccia','Lorenzini became fascinated by the idea of using an amiable, rascally character as a means of expressing his own convictions through allegory. In 1880 he began writing Storia di un burattino ("The story of a marionette"), also called Le avventure di Pinocchio, which was published weekly in Il Giornale per i Bambini, the first Italian newspaper for children.[4] Pinocchio was adapted into a 1940 film by Disney that is considered to be one of Disney\'s greatest']

tf_vectorizer = CountVectorizer(max_features=200,stop_words='english')
tf = tf_vectorizer.fit_transform(data)
lda = LatentDirichletAllocation(n_components=2, learning_method='batch')
lda.fit_transform(tf)

tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, 5)