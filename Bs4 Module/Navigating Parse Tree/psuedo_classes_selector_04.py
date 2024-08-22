import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/css_selector.html"

def psuedo_class_extractor(url: str) -> None:
    """
    Select element using psuedo class
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    last_image = soup.select_one('.gallery img:last-child')
    second_info_box = soup.select_one('.sidebar .info-box:nth-child(2)')
    print(last_image['alt'])
    print(second_info_box.get_text(strip=True))
    
# psuedo_class_extractor(URL)

def grouping_psuedo_selector(url: str) -> None:
    """
    Select element using multiple psuedo class
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    heading_and_paragraphs = soup.select('h2, h3, p')
    for element in heading_and_paragraphs:
        print(element.get_text(strip=True))

grouping_psuedo_selector(URL)