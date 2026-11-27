import hashlib
import logging
import time

from app.commons import configure_logging
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

cache = {}

if __name__ == '__main__':
    start_time = time.perf_counter()
    logger.info(f"Start with local LLM")
    elapsed_times = []

    for q in questions:
        logger.info(f"\tQuestion: {q}")
        start_question_time = time.perf_counter()

        hashed_question = hashlib.sha256(q.encode()).hexdigest()
        if hashed_question in cache:
            response = cache[hashed_question]
            logger.info(f"\tHashed answer: {response}")
        else:
            response = create_response(q)
            cache[hashed_question] = response

        elapsed_times.append(time.perf_counter() - start_question_time)
        logger.info(f"\tResponse: {response} \n")

    logger.info(f"Elapsed times: {elapsed_times}")
    logger.info(f"Elapsed time: {time.perf_counter() - start_time}")

    # Elapsed times: [1.8235748000006424, 3.460000152699649e-05, 2.6091941999911796, 1.945741799994721, 0.13996340001176577, 0.15947130000859033]
    # 2nd value is: 35 microseconds (0.000035 s), it's roughly 44,0* faster than the first LLM call (1.53 s)
    # Elapsed time: 6.678642200000468
