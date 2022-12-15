from bs4 import BeautifulSoup
from slugify import slugify


# https://splunktool.com/generate-a-table-of-contents-from-html-with-python

article = "every-money-investing-subreddits-on-reddit-com.md"


def list_to_html(lst):
    result = ["<ul>"]
    for item in lst:
        if isinstance(item, list):
            result.append(list_to_html(item))
        else:
            result.append('<li><a href="#{}">{}</a></li>'.format(item[0], item[1]))
    result.append("</ul>")
    return "\n".join(result)


soup = BeautifulSoup(article, 'html5lib')

toc = []
h2_prev = 0
h3_prev = 0
h4_prev = 0
h5_prev = 0

for header in soup.findAll(['h2', 'h3', 'h4', 'h5', 'h6']):
    data = [(slugify(header.string), header.string)]

    if header.name == "h2":
        toc.append(data)
        h3_prev = 0
        h4_prev = 0
        h5_prev = 0
        h2_prev = len(toc) - 1
    elif header.name == "h3":
        toc[int(h2_prev)].append(data)
        h3_prev = len(toc[int(h2_prev)]) - 1
    elif header.name == "h4":
        toc[int(h2_prev)][int(h3_prev)].append(data)
        h4_prev = len(toc[int(h2_prev)][int(h3_prev)]) - 1
    elif header.name == "h5":
        toc[int(h2_prev)][int(h3_prev)][int(h4_prev)].append(data)
        h5_prev = len(toc[int(h2_prev)][int(h3_prev)][int(h4_prev)]) - 1
    elif header.name == "h6":
        toc[int(h2_prev)][int(h3_prev)][int(h4_prev)][int(h5_prev)].append(data)

toc_html = list_to_html(toc)