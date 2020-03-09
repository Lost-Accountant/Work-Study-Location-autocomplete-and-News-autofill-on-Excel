import html2text
from bs4 import BeautifulSoup
import newspaper
from newspaper import Article

html = r"C:\Users\gxsgt\Desktop\Violent Land\Hong Kong Protest\Factiva.html"

with open(html, encoding='utf8') as f:
    html_string = f.read()

#print(html_string)

text = html2text.html2text(html_string)

#print(text)

soup = BeautifulSoup(html_string, 'html.parser')

# extract each article
main_article = soup.find_all('div', id =lambda x: x and x.startswith('article'))
#print(main_article[0])

# extract headline
#print(main_article[0].find_all('div', id='hd'))
#headlines = main_article[0].find_all('span', {'class' : "enHeadline"})
#headline = [span.get_text() for headline in headlines]
#print(headline[0])

# find author
#authors = main_article[0].find_all('div', {'class':"author"})
#author = [author.get_text() for author in authors]
#print(author[0])


#print(main_article[0].find_all('div'))
divtag = main_article[2].find_all('div', {'class':"article enArticle"})
#print(divtag)

#for tag in divtag:
#    each_tag = tag.find_all('div')
#print(each_tag)

# find author
#print(each_tag[2].get_text())

# find date
#print(each_tag[4].get_text())

# find main body
for tag in divtag:
    each_tag = tag.find_all('p')
print(each_tag)

for each in each_tag:
    print(each.get_text())

# find article id
print(each_tag[-1].get_text())





