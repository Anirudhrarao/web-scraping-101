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
  - [X] Functions in bs4
      # Essential BeautifulSoup Functions

  | Function                | Purpose                                                                                       |
  |-------------------------|-----------------------------------------------------------------------------------------------|
  | `BeautifulSoup()`       | Creates a BeautifulSoup object, representing the document as a nested data structure.         |
  | `find()`                | Finds the first element that matches the given criteria.                                       |
  | `find_all()`            | Finds all elements that match the given criteria.                                              |
  | `select()`              | Finds all elements that match the CSS selector.                                                |
  | `select_one()`          | Finds the first element that matches the CSS selector.                                         |
  | `get_text()`            | Extracts all the text from an element, stripping out the HTML tags.                            |
  | `attrs`                 | Accesses the attributes of an element.                                                         |
  | `contents`              | Returns a list of an element’s children.                                                       |
  | `children`              | Returns a generator of an element’s children.                                                  |
  | `parent`                | Accesses the parent element.                                                                   |
  | `parents`               | Accesses a list of all parent elements.                                                        |
  | `previous_sibling`      | Accesses the previous sibling of an element.                                                   |
  | `next_sibling`          | Accesses the next sibling of an element.                                                       |
  | `find_parent()`         | Finds the first parent element that matches the given criteria.                                |
  | `find_next_sibling()`   | Finds the next sibling element that matches the given criteria.                                |
  | `find_previous_sibling()` | Finds the previous sibling element that matches the given criteria.                          |

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
