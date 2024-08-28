import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/Advanced%20bs4/nested.html'

def direct_navigation(url: str) -> None:
    """
    You can use find() and find_all() to navigate through nested structures by specifying the tags or classes of interest.
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    # Find the container 
    container = soup.find("div", class_="container")
    # Navigate to the first section within the content
    first_section = container.find("div", class_="content").find("div", class_="section")
    print(first_section.h2.get_text())
    print(first_section.p.get_text())

# direct_navigation(url)


def recursive_navigation(url: str) -> None:
    """
    Recursive navigating attributes using select() and select_all()
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    # Find all sections within the content
    container = soup.find("div", class_="container")
    sections = container.find("div", class_="content").find_all("div", class_="section")
    for section in sections:
        print(section.h2.get_text())
        print(section.p.get_text())

# recursive_navigation(url)

def navigation_using_css(url: str) -> None:
    """
    CSS selectors provide a powerful way to navigate nested structures without needing to explicitly call find() multiple times.
    :params url of str type
    :return None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    # Select the first section's title
    first_section_title = soup.select_one(".container .content .section h2").get_text()
    print(first_section_title)
    # Select all section contents
    section_contents = soup.select(".container .content .section p")
    for content in section_contents:
        print(content.get_text())

# navigation_using_css(url)

def handle_inconsistent_nesting() -> None:
    html_content = """
                    <div class="container">
                        <div class="header">
                            <h1>Title</h1>
                            <p>Subtitle</p>
                        </div>
                        <div class="content">
                            <div class="section">
                                <h2>Section 1</h2>
                                <p>Content for section 1</p>
                            </div>
                            <div class="section">
                                <p>Content for section 2</p>
                            </div>
                        </div>
                    </div>
                    """
    soup = BeautifulSoup(html_content, "lxml")
    #  Handle missing titles by checking if they exist
    sections = soup.select(".container .content .section")
    for section in sections:
        title = section.find("h4")
        content = section.find("p")

        if title:
            print("Title: ", title.get_text())
        else:
            print("No title found!")
        print(content.get_text())

# handle_inconsistent_nesting()
