import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/Task/index.html"

def extract_titles(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    titles = soup.select(".main-content .article .title")
    authors = soup.select(".main-content .article .author")
    for title, author in zip(titles, authors):
        title_text = title.get_text(strip=True)
        author_text = author.get_text(strip=True)
        print(f"Title: {title_text}, Author: {author_text}")

# extract_titles(url)

def extract_user_comment(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    users = soup.select(".comments .comment .username")
    comments = soup.select(".comments .comment .text")
    for user, comment in zip(users, comments):
        user_text = user.get_text(strip=True)
        comment_text = comment.get_text(strip=True)
        print(f"User Name: {user_text}, Comment: {comment_text}")

# extract_user_comment(url)


def extract_sidebar_links(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    links = soup.select(".sidebar ul li a")
    for link in links:
        print(f"Link Name: {link.get_text(strip=True)}")

# extract_sidebar_links(url)

def extract_title_using_css(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    articles_title = soup.select(".main-content .article .title")
    for title in articles_title:
        print(f"Title: {' '.join(title.get_text().split(' ')[:2])}")
    
# extract_title_using_css(url)


def extract_last_comment_and_modify(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    last_comment_element = soup.select(".comments .comment .text")[-1]

    original_comment = last_comment_element.get_text(strip=True)
    print(f"Original comment: {original_comment}")

    last_comment_element.string = f"{original_comment} - updated by developer"
    updated_comment = last_comment_element.get_text(strip=True)
    print(f"Updated comment: {updated_comment}")


extract_last_comment_and_modify(url)