import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/Modifying%20Parsing%20Tree/practice.html"


def decompose_tag_from_tree(url: str) -> None:
    """
    Decompose or remove tags from tree to free up the memory
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    ads = soup.find_all('div', class_='ad')
    for ad in ads:
        ad.decompose()
    
    print(soup.prettify())

decompose_tag_from_tree(url)