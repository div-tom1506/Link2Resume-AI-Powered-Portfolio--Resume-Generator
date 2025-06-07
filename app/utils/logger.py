import logging

logger = logging.getLogger("Link2Resume")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s")
console_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(console_handler)