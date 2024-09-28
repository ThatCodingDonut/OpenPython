import requests
from bs4 import BeautifulSoup
import re

# Returns HTML content from a given url
def fetch_html(url):
    try:
        response = requests.get(url)
        # To throw an error in case of failure
        response.raise_for_status() 
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
# Parses given HTML to return a BeautifulSoup object
def parse_html(html):
    return BeautifulSoup(html, 'html.parser')

# Returns all links (<a>) at the given url
def get_links(url):
    parsed_html = parse_html(fetch_html(url))
    if parsed_html:
        links = [link.get('href') for link in parsed_html.find_all('a', href=True)]
        if links:
            return links
        return None
    return None

# Returns all headings (<h1> to <h6>) at the given url
def get_headings(url):
    parsed_html = parse_html(fetch_html(url))
    if parsed_html:
        headings = [heading.get_text() for heading in parsed_html.find_all(re.compile('h[1-6]'))]
        if headings:
            return headings
        return None
    return None

# Return all ids (id attribute) at the given url
def get_ids(url):
    parsed_html = parse_html(fetch_html(url))
    if parsed_html:
        ids = [tag.get('id') for tag in parsed_html.find_all(None, id=True)]
        if ids:
            return ids
        return None
    return None
    
# Returns all classes (class attribute) at the given url
def get_classes(url):
    parsed_html = parse_html(fetch_html(url))
    if parsed_html:
        classes = []
        for tag in parsed_html.find_all(None, class_=True):
            for class_name in tag.get('class'):
                # To remove duplicate class names
                if class_name not in classes:
                    classes.append(class_name)
        if classes:
            return classes
        return None
    return None