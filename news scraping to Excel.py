from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def load_html():
    file_name = input('what is the html name')
    html = r"C:\Users\gxsgt\Desktop\Violent Land\Hong Kong Protest\{}.html".format(file_name)

#html = r"C:\Users\gxsgt\Desktop\Violent Land\Hong Kong Protest\Factiva.html"

    with open(html, encoding='utf8') as f:
        html_string = f.read()

    soup = BeautifulSoup(html_string, 'html.parser')
    return soup


def extract_headline(each_article):
    headlines = each_article.find_all('span', {'class':"enHeadline"})
    headline = [headline.get_text() for headline in headlines]
    return headline[0]


def extract_author(each_tag):
    return each_tag[2].get_text()


def extract_date(each_tag):
    return each_tag[4].get_text()


def extract_id(each_tag):
    return each_tag[-1].get_text()


def extract_body(divtag):
    for tag in divtag:
        paragraphs = tag.find_all('p')

    paragraph = ''
    for sentence in paragraphs:
        paragraph = paragraph + sentence.get_text() + ' '

    return paragraph


def get_divtag(each_article):
    divtag = each_article.find_all('div', {'class': "article enArticle"})
    return divtag


def get_articles(soup):
    articles = soup.find_all('div', id =lambda x: x and x.startswith('article'))
    return articles


def auto_fill():
    wb = Workbook()
    ws = wb.active

    # fill in column names
    col_names = ['ID','Headline','Author','Date','Text']
    for col_num in range(len(col_names)):
        ws.cell(row=1, column=col_num + 1).value = col_names[col_num]



    wb.save('C:\\Users\\gxsgt\\Desktop\\Violent Land\\Hong Kong Protest\\balance.xlsx')
    return


if __name__ == "__main__":

    #load_html()
    #main_article = load_html().find_all('div', id =lambda x: x and x.startswith('article'))
    #print(main_article[0])
    #print(len(main_article))
    auto_fill()
