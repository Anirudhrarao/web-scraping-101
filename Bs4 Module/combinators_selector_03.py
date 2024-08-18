import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/css_selector.html"


def descendant_selector(url: str) -> None:
    """
    Select all paragraphs from class ".main-content"
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    paragraphs = soup.select('.main-content p')
    for para in paragraphs:
        print(para.get_text())

# descendant_selector(URL)

def child_selector(url: str) -> None:
    """
    Select direct child <p> of class ".featured"
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    featured_paras = soup.select('.featured > p')
    for para in featured_paras:
        print(para.get_text(strip=True))

# child_selector(URL)

def adjacent_sibling_selector(url: str) -> None:
    """
    Select the element immediately following the .sidebar.
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    adjacent_sibling = soup.select_one('.sidebar + .main-content')
    if adjacent_sibling:
        print(adjacent_sibling.get_text())

# adjacent_sibling_selector(URL)

def general_sibling_select(url: str) -> None:
    """
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    general_sibling = soup.select('.sidebar ~ .main-content')
    for sibling in general_sibling:
        print(sibling.get_text())

# general_sibling_select(URL)