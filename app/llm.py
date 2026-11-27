from ollama import ChatResponse
from ollama import chat

LLM_MODEL = 'mistral:7b'

SYSTEM_PROMPT = """
  You are a helpful assistant that answers questions strictly based on the provided context. 
"""


def create_response(query_question):
    response: ChatResponse = chat(
        model=LLM_MODEL,
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': query_question + '\n/no_think'},
        ],
        options={"temperature": 0.2},
    )

    return response['message']['content']
