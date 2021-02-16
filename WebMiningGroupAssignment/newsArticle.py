import newspaper
url = "http://www.cnn.com"
cnn = newspaper.build(url)

articles = cnn.articles
print(len(cnn.articles))
print(articles)
for article in cnn.articles:
    try:
        print(article.url + " | " + article.title)
    except:
        print("err")


