# 🕸️ Python Web Scraping Learning Checklist

## 1. Requests 📡
- [X] **Introduction to Requests**
  - [X] Installing Requests
  - [X] Making HTTP requests (GET, POST, PUT, DELETE)
  - [X] Handling responses (status codes, headers)
  - [X] Query parameters
- [X] **Advanced Requests**
  - [X] Handling cookies
  - [X] Sessions
  - [X] File uploads
  - [X] Timeout and retries
  - [X] Error handling

## 2. BeautifulSoup 🍲
- [X] **Introduction to BeautifulSoup**
  - [X] Installing BeautifulSoup
  - [X] Parsing HTML and XML documents
- [X] **Navigating the Parse Tree**
  - [X] Finding elements by tag, class, id
  - [] Functions in bs4
       # Essential BeautifulSoup Functions

| Function                | Purpose                                                                                       | Usage Example                                                                                                            |
|-------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `BeautifulSoup()`       | Creates a BeautifulSoup object, representing the document as a nested data structure.         | ```python\nsoup = BeautifulSoup(html_content, 'html.parser')\n```                                                       |
| `find()`                | Finds the first element that matches the given criteria.                                       | ```python\nh1_tag = soup.find('h1')\nprint(h1_tag.get_text())\n```                                                      |
| `find_all()`            | Finds all elements that match the given criteria.                                              | ```python\nparagraphs = soup.find_all('p')\nfor p in paragraphs:\n    print(p.get_text())\n```                           |
| `select()`              | Finds all elements that match the CSS selector.                                                | ```python\ncontent_elements = soup.select('.content')\nfor element in content_elements:\n    print(element.get_text())\n``` |
| `select_one()`          | Finds the first element that matches the CSS selector.                                         | ```python\nheader = soup.select_one('#main-header')\nprint(header.get_text())\n```                                       |
| `get_text()`            | Extracts all the text from an element, stripping out the HTML tags.                            | ```python\ntext = h1_tag.get_text()\nprint(text)\n```                                                                   |
| `attrs`                 | Accesses the attributes of an element.                                                         | ```python\ndiv = soup.find('div')\nattrs = div.attrs\nprint(attrs)\n```                                                  |
| `contents`              | Returns a list of an element’s children.                                                       | ```python\nbody_contents = soup.body.contents\nfor child in body_contents:\n    print(child)\n```                        |
| `children`              | Returns a generator of an element’s children.                                                  | ```python\nchildren = list(soup.body.children)\nfor child in children:\n    print(child)\n```                            |
| `parent`                | Accesses the parent element.                                                                   | ```python\nparent = h1_tag.parent\nprint(parent.name)\n```                                                              |
| `parents`               | Accesses a list of all parent elements.                                                        | ```python\nall_parents = list(h1_tag.parents)\nfor parent in all_parents:\n    print(parent.name)\n```                   |
| `previous_sibling`      | Accesses the previous sibling of an element.                                                   | ```python\nprev_sibling = h1_tag.previous_sibling\nprint(prev_sibling)\n```                                              |
| `next_sibling`          | Accesses the next sibling of an element.                                                       | ```python\nnext_sibling = h1_tag.next_sibling\nprint(next_sibling)\n```                                                  |
| `find_parent()`         | Finds the first parent element that matches the given criteria.                                | ```python\nparent_div = p_tag.find_parent('div')\nprint(parent_div)\n```                                                 |
| `find_next_sibling()`   | Finds the next sibling element that matches the given criteria.                                | ```python\nnext_p = p_tag.find_next_sibling('p')\nprint(next_p)\n```                                                     |
| `find_previous_sibling()` | Finds the previous sibling element that matches the given criteria.                          | ```python\nprev_p = p_tag.find_previous_sibling('p')\nprint(prev_p)\n```                                                 |

  - [ ] Using CSS selectors
  - [ ] Navigating using `.find()`, `.find_all()`, `.select()`
- [ ] **Modifying the Parse Tree**
  - [ ] Modifying tag attributes
  - [ ] Extracting and changing tag content
  - [ ] Decomposing tags
- [ ] **Advanced BeautifulSoup**
  - [ ] Handling nested structures
  - [ ] Working with encodings
  - [ ] Parsing complex HTML (handling bad HTML)
  - [ ] Integrating with Requests

## 3. Selenium 🕵️‍♂️
- [ ] **Introduction to Selenium**
  - [ ] Installing Selenium
  - [ ] Setting up WebDriver (Chrome, Firefox, etc.)
- [ ] **Basic Operations**
  - [ ] Opening a web page
  - [ ] Finding elements (by id, name, class, CSS selector, XPath)
  - [ ] Interacting with elements (click, send keys)
  - [ ] Handling alerts, pop-ups, and frames
- [ ] **Advanced Selenium**
  - [ ] Waiting for elements (implicit and explicit waits)
  - [ ] Executing JavaScript
  - [ ] Handling multiple windows and tabs
  - [ ] Capturing screenshots
  - [ ] Handling cookies and sessions
- [ ] **Selenium for Web Scraping**
  - [ ] Scraping JavaScript-rendered content
  - [ ] Handling infinite scrolling
  - [ ] Bypassing bot detection
  - [ ] Best practices for efficient scraping

## 4. Data Storage 💾
- [ ] **Storing Data in Files**
  - [ ] Saving data to CSV
  - [ ] Saving data to JSON
- [ ] **Storing Data in Databases**
  - [ ] Introduction to SQLite
  - [ ] Storing data in SQLite
  - [ ] Storing data in PostgreSQL

## 5. Best Practices and Ethical Considerations
- [ ] Understanding robots.txt
- [ ] Respecting website terms of service
- [ ] Avoiding IP blocks
- [ ] Legal considerations in web scraping
- [ ] Writing polite scrapers (rate limiting, user-agent strings)
