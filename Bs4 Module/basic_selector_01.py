"""
In Bs4 we can use select and select_one methods with css selector to target
HTML elements based one their attributes, classes, IDs, and more.
"""

import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/css_selector.html"

def extract_div(url: str) -> None:
    """
    Selects all elements of a given "type selector" (tag name).
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    divs = soup.select('div')
    print("length of div: ", len(divs))
    # for index,div in enumerate(divs):
    #     print(f"{index}'s div: {div}")

# extract_div(URL)

def extract_class(url: str):
    """
    Select all elements with class selector 'info-box'
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    info_boxes = soup.select('.info-box')
    for box in info_boxes:
        print(box.text)

# extract_class(URL)

def extract_id(url: str) -> None:
    """
    Select the main content area using its ID selector
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    main_contents = soup.select_one('#main-content')
    if main_contents:
        print(main_contents.get_text(strip=True))
    else:
        print('IDs not found!')

# extract_id(URL)
