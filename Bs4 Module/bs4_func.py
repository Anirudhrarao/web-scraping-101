from bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/home.html"
def first_element(url: str) -> None:
    """
        Finds the first element that matches the given criteria
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    first_article = soup.find(class_='article')
    print(first_article.get_text())

# first_element(url)


def find_all_elements(url: str) -> None:
    """
        Finds all elements that match the given criteria.
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    articles = soup.find_all(class_="additional-info")
    for info in articles:
        print(info.get_text())

# find_all_elements(url)

def select_element(url: str) -> None:
    """
        Select all element using css selector
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    content_articles = soup.select('.content .article')
    for element in content_articles:
        print(element.h2.get_text())

# select_element(url)

def select_one_element(url: str) -> None:
    """
        Select one element using css selector
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    header = soup.select_one('#main-header')
    print(header.get_text())

# select_one_element(url)

def access_attributes(url: str) -> None:
    """
        Access attributes of element
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    header_attrs = soup.find(class_='header').attrs
    print(header_attrs)

# access_attributes(url)

def get_children_list(url: str) -> None:
    """
        Return a list of an element's children
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    body_content = soup.footer.contents
    for child in body_content:
        print(child)

# get_children_list(url)

def get_children(url: str) -> None:
    """
        Returns a generator of an element’s children.
        :params url of str type
        :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    section_childrens = list(soup.find('section').children)
    for child in section_childrens:
        print(child)

get_children(url)