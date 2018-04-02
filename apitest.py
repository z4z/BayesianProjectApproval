import requests
from bs4 import BeautifulSoup
import pickle
articles = []
for page in range(0,201):
    r = requests.get(url = "https://api.nytimes.com/svc/search/v2/articlesearch.json",
                     params = {'api-key': "91c424e7544b4d2d9cf14dd03ee7693d",
                               'fq': "persons:(\"TRUMP, DONALD\") AND source:(\"The New York Times\") AND document_type:(\"article\")",
                               'begin_date': "20170123",
                               'end_date':"20170928",
                               'sort': "newest",
                               'fl': "web_url,pub_date,headline,abstract,news_desk",
                               'page':page})
    data = r.json()
    print(data["response"]["meta"])
    for document in data["response"]["docs"]:
        article = requests.get(url=document["web_url"])
        article = BeautifulSoup(article.text,"html.parser")
        paragraphs = article.find_all("p","story-body-text story-content");
        articletext = ""
        for p in paragraphs:
            articletext += p.text
        
        if len(articletext)>0:
            articles.append((document["pub_date"].split("T")[0],document["headline"]["main"] + " " + articletext))

pickle.dump( articles, open( "articles", "wb" ) )