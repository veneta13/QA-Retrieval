from .get_answer import get_answer
from .get_wiki_paragraphs import get_paragraphs
from .rank_paragraphs import get_top_paragraph
from .retrieve_wiki import google_search


def send_user(query):
    wiki_link = google_search(query)
    paragraphs = get_paragraphs(wiki_link)
    top_paragraph = get_top_paragraph(paragraphs, query)
    answer = get_answer(top_paragraph, query)
    return answer, top_paragraph
