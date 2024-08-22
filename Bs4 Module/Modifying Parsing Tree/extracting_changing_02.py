import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/Modifying%20Parsing%20Tree/practice.html"

def extracting_changing_tag_content(url: str) -> None:
    """
    Extracting and changing tag content
    :params url of str
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    paras = soup.find_all('p')
    for i, p in enumerate(paras, start=1):
        print(f"Original content: {p.get_text()}")
        p.string = f"Updated para {i} content"

    print(soup.prettify())

extracting_changing_tag_content(url)