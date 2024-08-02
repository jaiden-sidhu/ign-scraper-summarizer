import requests
from bs4 import BeautifulSoup

def extract_verdict_text(url):
    # Grabbing headers to IGN doesn't block the webscrape
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    # Checking to make sure the request worked
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Grabbing the text data by data-cy value
        verdict_element = soup.find(attrs={"data-cy": "verdict"})
        if verdict_element:
            return verdict_element.get_text(strip=True)[7:]
        else:
            return "Element with data-cy='verdict' not found."
    elif response.status_code == 403:
        # In case the access changes for some reason
        print("Access to the webpage is forbidden (403).")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")