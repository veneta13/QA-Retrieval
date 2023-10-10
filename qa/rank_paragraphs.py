from hyperdb import HyperDB

def get_top_paragraph(paragraphs, query):
    database = HyperDB(paragraphs)
    result = database.query(query, top_k=1)[0][0]
    return result
