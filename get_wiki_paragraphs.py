import bs4
import requests


def get_paragraphs(link):
    response = requests.get(link)
    paragraphs = []

    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
        raw_paragraphs = html.select("p")
        raw_paragraphs = [current.text for current in raw_paragraphs if len(current.text) > 1]

        for current in raw_paragraphs:
            paragraphs.append(current.strip())
    return paragraphs
