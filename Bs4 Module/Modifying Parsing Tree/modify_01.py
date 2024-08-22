import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/Modifying%20Parsing%20Tree/practice.html"

def modify_tag_attributes(url: str) -> None:
    """
    Modify image alt text
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    images = soup.find_all('img')
    for img in images:
        if not img.has_attr('alt'):
            img['alt'] = 'Default set text'
        else:
            img['alt'] = img['alt'] + " - Updated"
    print(soup.prettify())

modify_tag_attributes(url)