# Question-Answering Bot

**Question-answering bot build with DistilBERT and Django.**

![UI](img/bot_ui.JPG)

## Workflow Explanation

- User submits a question.
- The system selects the most relevant Wikipedia article.
- It ranks the paragraphs within the article using Okapi BM25.
- The top-ranked paragraph serves as the context for the DistilBERT model.
- The system receives the response from DistilBERT.
- Finally, it generates a coherent sentence using Chat GPT and sends it back to the user.
