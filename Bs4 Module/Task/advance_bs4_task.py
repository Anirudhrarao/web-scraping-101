import streamlit as st
import json
import requests
from bs4 import BeautifulSoup
from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class WebScraper:
    url: str 
    soup: BeautifulSoup = field(init=False)

    def __post_init__(self):
        self.soup = self._get_soup()

    def _get_soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "lxml")
    
    def extract_titles_and_authors(self) -> List[Dict[str, str]]:
        articles_data: List[Dict[str, str]] = []
        articles = self.soup.select(".main-content .article")

        for article in articles:
            title_element = article.select_one(".title")
            author_element = article.select_one(".author")

            title_text = title_element.get_text(strip=True) if title_element else "Title missing"
            author_text = author_element.get_text(strip=True) if author_element else "Author missing"

            articles_data.append({
                "title": title_text,
                "author": author_text
            })
        
        return articles_data
    
    def extract_comments(self) -> List[Dict[str, str]]:
        comment_data: List[Dict[str, str]] = []
        comments = self.soup.select(".comments .comment")

        for comment in comments:
            user_element = comment.select_one(".username")
            text_element = comment.select_one(".text")

            user_text = user_element.get_text(strip=True) if user_element else "Username missing"
            comment_text = text_element.get_text(strip=True) if text_element else "Comment missing"

            comment_data.append({
                "username": user_text,
                "comment": comment_text
            })
        
        return comment_data
    
    def extract_sidebar_links(self) -> List[str]:
        links_data: List[str] = []
        links = self.soup.select(".sidebar ul li a")

        for link in links:
            links_data.append(link.get_text(strip=True))
        
        return links_data
    
    def modify_last_comment(self) -> Dict[str, str]:
        last_comment_element = self.soup.select(".comments .comment .text")[-1]
        original_comment = last_comment_element.get_text(strip=True)
        
        last_comment_element.string = f"{original_comment} - updated comment"
        updated_comment = last_comment_element.get_text(strip=True)

        return {
            "original_comment": original_comment,
            "updated_comment": updated_comment
        }

def main():
    st.title("Web Scraper Dashboard")

    url = st.text_input("Enter the URL:", "http://127.0.0.1:5500/web-scraping-101/Bs4%20Module/Task/index.html")

    if st.button("Scrape Data"):
        scraper = WebScraper(url)
        
        with st.spinner("Scraping data..."):
            articles = scraper.extract_titles_and_authors()
            comments = scraper.extract_comments()
            sidebar_links = scraper.extract_sidebar_links()
            modified_comment = scraper.modify_last_comment()
            
            st.subheader("Articles")
            st.write(articles)

            st.subheader("Comments")
            st.write(comments)

            st.subheader("Sidebar Links")
            st.write(sidebar_links)

            st.subheader("Modified Comment")
            st.write(modified_comment)

            data = {
                "articles": articles,
                "comments": comments,
                "sidebar_links": sidebar_links,
                "modified_comment": modified_comment
            }
            
            st.subheader("Download JSON")
            json_data = json.dumps(data, indent=4)
            st.download_button("Download JSON", json_data, "scraped_data.json", "application/json")
    
if __name__ == "__main__":
    main()
