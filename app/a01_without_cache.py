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

if __name__ == '__main__':
    start_time = time.perf_counter()
    logger.info(f"Start with local LLM")

    elapsed_times = []

    for q in questions:
        logger.info(f"\tQuestion: {q}")
        start_question = time.perf_counter()
        response = create_response(q)
        elapsed_times.append(time.perf_counter() - start_question)
        logger.info(f"\tResponse: {response} \n")

    logger.info(f"Elapsed times: {elapsed_times}")

    logger.info(f"End. Elapsed time: {time.perf_counter() - start_time}")
    # Elapsed times: [2.0180804999981774, 1.0547980999981519, 3.229536500002723, 1.519670399997267, 0.14955729999928735, 0.15434280000044964]
    # Elapsed time: 8.126698200008832
