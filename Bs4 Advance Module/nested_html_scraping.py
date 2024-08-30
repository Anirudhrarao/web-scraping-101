import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Advance%20Module/home.html"

def nested_scrapping(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    content_div = soup.find('div', class_='content')
    # Extract the article title
    title = content_div.find('h2').text
    # Extract the author name
    author = content_div.find('span', class_='author')
    # Extract the list items
    list_items = [li.text for li in content_div.find_all('li')]

    print("Title:", title)
    print("Author:", author)
    print("List Items:", list_items)

nested_scrapping(url)