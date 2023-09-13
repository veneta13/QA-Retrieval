import string

from rank_bm25 import BM25Okapi


def tokenize_paragraphs(paragraphs):
    translator = str.maketrans('', '', string.punctuation)
    paragraphs = [current.translate(translator).lower()
                  for current
                  in paragraphs]
    paragraphs = [current.split(' ') for current in paragraphs]
    return paragraphs


def tokenize_query(query):
    translator = str.maketrans('', '', string.punctuation)
    query = query.translate(translator).lower().split()
    return query


def get_top_paragraph(paragraphs, query):
    tokenized_paragraphs = tokenize_paragraphs(paragraphs)
    tokenized_query = tokenize_query(query)

    bm25 = BM25Okapi(tokenized_paragraphs)

    return bm25.get_top_n(tokenized_query, paragraphs, n=1)[0]
