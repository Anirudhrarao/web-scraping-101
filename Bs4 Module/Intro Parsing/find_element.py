import requests
from bs4 import BeautifulSoup
url = 'http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/index.html'

def find_all_p(url) -> None:
    """
        Find elements bt tags
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.get_text())

# find_all_p(url)

def find_all_class(url) -> None:
    """
        Find elements by class
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    classes = soup.find_all(class_="section-text")
    for element in classes:
        print(element.get_text())

# find_all_class(url)

def find_all_ids(url) -> None:
    """
        Find elements by ids
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    ids = soup.find_all(id='home')
    for id in ids:
        print(id.get_text())

find_all_ids(url)

