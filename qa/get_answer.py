import numpy as np
from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer

checkpoint = 'distilbert-base-uncased-distilled-squad'
model = TFAutoModelForQuestionAnswering.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


def get_answer(context, question):
    inputs = tokenizer([context], [question], return_tensors="np")
    outputs = model(inputs)

    start_position = np.argmax(outputs.start_logits[0])
    end_position = np.argmax(outputs.end_logits[0])
    answer = inputs["input_ids"][0, start_position: end_position + 1]
    answer = tokenizer.decode(answer)
    if '[SEP]' in answer:
        answer = answer[:answer.index("SEP") - 1]
    return answer
