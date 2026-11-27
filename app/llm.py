from ollama import ChatResponse
from ollama import EmbedResponse
from ollama import chat
from ollama import embed

LLM_MODEL = 'mistral:7b'

EMBEDDING_MODEL = 'qwen3-embedding:4b'

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


def create_embedding(query_question):
    response: EmbedResponse = embed(
        model=EMBEDDING_MODEL,
        input=[query_question],
    )

    return response['embeddings'][0]
