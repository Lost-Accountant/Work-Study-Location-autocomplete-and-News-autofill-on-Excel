import newspaper

#url = 'https://news.mingpao.com/ins/%e6%b8%af%e8%81%9e/section/20200308/s00001'
url = 'https://www.thestandnews.com/politics/'

news = newspaper.build(url)

#for category in scmp.category_urls():
#    print(category)

for article in news.articles:
    print(article.url)

