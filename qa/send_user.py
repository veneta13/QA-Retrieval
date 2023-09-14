from .get_answer import get_answer
from .get_wiki_paragraphs import get_paragraphs
from .rank_paragraphs import get_top_paragraph
from .retrieve_wiki import google_search
from .wrap_answer import format_answer


def send_user(query):
    try:
        wiki_link = google_search(query)
        paragraphs = get_paragraphs(wiki_link)
        top_paragraph = get_top_paragraph(paragraphs, query)
        answer = get_answer(top_paragraph, query)
        if len(answer) < 1:
            return "Sorry, I can't find an answer.", ""
        answer = format_answer(query, answer)
        return answer, top_paragraph
    except:
        return "Sorry, I can't find an answer.", ""
