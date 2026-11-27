import logging
import time

from app.commons import configure_logging
from app.llm import create_response

configure_logging()

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    start_time = time.time()
    logger.info(f"Start: {start_time}")

    response = create_response('What is the capital of England?')
    logger.info(f"Response: {response}")

    end_time = time.time()
    logger.info(f"End: {end_time}, elapsed time: {end_time - start_time}")
