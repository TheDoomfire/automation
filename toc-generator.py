from bs4 import BeautifulSoup
from slugify import slugify


html = "every-money-investing-subreddits-on-reddit-com.md"

soup = BeautifulSoup(html)

toc = []
header_id = 1
current_list = toc
previous_tag = None

for header in soup.findAll(['h2', 'h3']):
    header['id'] = header_id
    if previous_tag == 'h2' and header.name == 'h3':
        current_list = []
    elif previous_tag == 'h3' and header.name == 'h2':
        toc.append(current_list)
        current_list = toc
        current_list.append((header_id, header.string))
        header_id += 1
        previous_tag = header.name

        if current_list != toc:
            toc.append(current_list)


def list_to_html(lst):
    result = ["<ul>"]
    for item in lst:
        if isinstance(item, list):
            result.append(list_to_html(item))
        else:
            result.append('<li><a href="#%s">%s</a></li>' % item)
            result.append("</ul>")
    return "\n".join(result)

# Table of contents
list_to_html(toc)

# Modified HTML
soup