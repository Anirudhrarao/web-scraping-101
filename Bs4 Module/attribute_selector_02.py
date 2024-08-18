import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/css_selector.html"

def extract_links(url: str) -> None:
    """
    Select all <a> element in the <nav>
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    nav_links = soup.select("nav a")
    for link in nav_links:
        print(link.get_text(strip=True))

# extract_links(URL)

def get_elements_by_partial_class(url: str) -> None:
    """
    Select all element with class contains "side"
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    highlighted_elements = soup.select('[class*="side"]')
    for element in highlighted_elements:
        print(element.get_text())

# get_elements_by_partial_class(URL)