import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def find_subdirectories(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        subdirectories = []
        base_url = urlparse(url).scheme + '://' + urlparse(url).netloc
        
        for link in soup.find_all('a', href=True):
            subdirectory_url = urljoin(base_url, link['href'])
            if subdirectory_url.startswith(base_url) and subdirectory_url != url:
                subdirectories.append(subdirectory_url)
        
        return subdirectories
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

link = input("Link: ")
subdirectories = find_subdirectories(link)

if subdirectories:
    print("Subdirectories:")
    for subdirectory in subdirectories:
        print(subdirectory)
else:
    print("No subdirectories found.")
