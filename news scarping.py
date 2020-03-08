import newspaper
from newspaper import Article


#url = 'https://news.mingpao.com/ins/%E6%B8%AF%E8%81%9E/section/20200302/s00001'
url = 'https://www.scmp.com/'
#url = 'http://thestandnews.com/archive/20190505/'

news = newspaper.build(url) #, language= 'zh')

#for category in news.category_urls():
   # print(category)

for article in news.articles:
    print(article.url)

#url2 = 'https://www.thestandnews.com/politics/%E9%80%83%E7%8A%AF%E6%A2%9D%E4%BE%8B-%E9%99%B3%E6%96%87%E6%95%8F%E5%80%A1%E6%9C%AA%E7%B0%BD-%E5%85%AC%E6%B0%91%E6%AC%8A%E5%88%A9%E5%85%AC%E7%B4%84-%E5%9C%8B%E4%B8%8D%E4%BD%9C%E7%A7%BB%E4%BA%A4-%E7%94%B0%E5%8C%97%E4%BF%8A%E6%8C%87%E6%9E%97%E9%84%AD%E6%87%89%E8%AC%99%E5%8D%91-%E4%BF%83%E6%93%B1%E7%BD%AE%E4%BF%AE%E4%BE%8B/'
url2 = 'https://news.mingpao.com/ins/%e6%b8%af%e8%81%9e/article/20190505/s00001/1557069733412/%e3%80%8c%e9%ba%a5%e9%ba%a5%e9%80%81%e3%80%8d%e5%93%a1%e5%b7%a5%e9%81%ad%e5%ae%a2%e9%a8%99%e6%ac%be%e6%a1%88-25%e6%ad%b2%e7%84%a1%e6%a5%ad%e7%94%b7%e8%a2%ab%e6%8d%95'

example = Article(url2, language= 'zh')
example.download()
example.parse()
print(example.title)
print(example.authors)
print(example.publish_date)

print(example.text)


