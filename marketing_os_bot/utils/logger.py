import logging
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / 'analytics' / 'logs.txt'
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def setup_logger() -> logging.Logger:
    logger = logging.getLogger('bot')
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(LOG_PATH, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
