from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI


if __name__ == '__main__':
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
    messages = [
        SystemMessage(content="You format answers to questions"),
        HumanMessage(content="Question: what i sthe temperature outside? answer: 20 DEGREES")
    ]
    response = chat(messages)

    print(response.content, end='\n')
