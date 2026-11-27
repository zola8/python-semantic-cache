import logging


def configure_logging():
    logging.basicConfig(
        level="DEBUG",
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    for name in ("httpcore", "httpx", "urllib3", "chromadb", "chromadb.telemetry"):
        logging.getLogger(name).setLevel(logging.WARNING)
