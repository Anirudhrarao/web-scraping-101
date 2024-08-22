import requests
from bs4 import BeautifulSoup

def parse_html(url: str) -> None:
    html = requests.get(url)
    html_parse = BeautifulSoup(html.text, 'lxml')
    for para in html_parse.find_all('p'):
        print(para.get_text())
# parse_html("https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed")

def parse_xml(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    
    soup = BeautifulSoup(xml_content, 'lxml-xml')
    print('Library Books: ')
    for book in soup.find_all('book'):
        book_id = book['id']
        title = book.find('title').get_text()
        author = book.find('author').get_text()
        year = book.find('year').get_text()
        print(f'ID: {book_id}')
        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f'Year: {year}')
        print()

parse_xml('info.xml')