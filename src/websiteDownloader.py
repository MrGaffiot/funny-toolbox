import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path
import os

def download_website(base_url: str, output_dir: str, searchSite: str = None, isParent: bool = True):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    #Checks is it's the first round or not
    if isParent:
        base_response = requests.get(base_url)
        base_soup = BeautifulSoup(base_response.text, 'html.parser')
    else:
        base_response = requests.get(searchSite)
        base_soup = BeautifulSoup(base_response.text, 'html.parser')
        
    foundLinks = []
    foundLinksS = set()

    # Find all links on the page
    for link in base_soup.find_all('a', href=True):
        href = link['href']
        
        # Convert relative paths to absolute paths
        abs_href = urljoin(base_url, href)
        
        # Skip external links
        if not abs_href.startswith(base_url):
            continue
        
        #Skips duplicates
        if abs_href in foundLinksS:
            continue
        
        foundLinks.append(abs_href)
        foundLinksS.add(abs_href)
        
        # Get the filename from the URL
        filename = os.path.basename(abs_href) + ".html"
        
        # Download the linked page
        try:
            response = requests.get(abs_href)
            content = response.content
            
            # Save the content to a file
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(content)
            
            print(f"Downloaded {abs_href}")
        except Exception as e:
            print(f"Error downloading {abs_href}: {str(e)}")
    
    for childLink in foundLinks:
        print("downloading")
        download_website(childLink, output_dir, searchSite=childLink, isParent=False)

# Usage
base_url = "http://158.180.40.246/"
output_dir = "./downloaded_site"
download_website(base_url=base_url, output_dir=output_dir)
