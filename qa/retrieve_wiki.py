import requests
from bs4 import BeautifulSoup


def google_search(query):
    full_query = query

    url = 'https://www.google.com/search'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {
        'q': full_query,
        'site': 'wikipedia.com'
    }

    content = requests.get(url, headers=headers, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')
    search = soup.find(id='search')

    return search.find('a')['href']
