import logging
import time

import numpy as np

from app.commons import configure_logging
from app.llm import create_embedding
from app.llm import create_response

configure_logging()

logger = logging.getLogger(__name__)

questions = [
    'What is recursion?',
    'What is recursion?',
    'Can you explain recursion?',
    'Tell me what recursion is.',
    'What is the capital of England?',
    'What is the capital of France?',
]

cached_embeddings = []
cached_responses = []

SIMILARITY_THRESHOLD = 0.9

if __name__ == '__main__':
    start_time = time.perf_counter()
    logger.info(f"Start")

    elapsed_times = []

    for q in questions:
        logger.info(f"\tQuestion: {q}")
        start_question = time.perf_counter()

        embedding = create_embedding(q)
        similarity = 0.0
        if cached_embeddings:
            similarities = np.array(cached_embeddings) @ embedding
            best = similarities.argmax()
            similarity = similarities[best]

        if similarity > SIMILARITY_THRESHOLD:
            response = cached_responses[best]
        else:
            response = create_response(q)
            cached_embeddings.append(embedding)
            cached_responses.append(response)

        elapsed_times.append(time.perf_counter() - start_question)
        logger.info(f"\tResponse: {response} \n")

    logger.info(f"Elapsed times: {elapsed_times}")
    logger.info(f"Elapsed time: {time.perf_counter() - start_time}")

    # Elapsed times: [1.392947100001038, 0.022014599991962314, 0.0472353000077419, 0.0323361000046134, 0.2007755999948131, 0.18097970000235364]
    # Elapsed time: 1.8770327000092948
