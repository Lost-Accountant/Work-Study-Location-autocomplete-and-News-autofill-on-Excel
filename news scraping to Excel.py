from bs4 import BeautifulSoup

def load_html():
    file_name = input('what is the html name')
    html = r"C:\Users\gxsgt\Desktop\Violent Land\Hong Kong Protest\{}.html".format(file_name)

#html = r"C:\Users\gxsgt\Desktop\Violent Land\Hong Kong Protest\Factiva.html"

    with open(html, encoding='utf8') as f:
        html_string = f.read()

    soup = BeautifulSoup(html_string, 'html.parser')
    return soup


if __name__ == "__main__":

    #load_html()
    main_article = load_html().find_all('div', id =lambda x: x and x.startswith('article'))
    print(main_article[0])
