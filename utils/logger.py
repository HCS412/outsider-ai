# utils/logger.py

import os
import logging
from datetime import datetime

LOG_DIR = "logs"
ERROR_LOG_FILE = os.path.join(LOG_DIR, "errors.log")

# Ensure logs folder exists
os.makedirs(LOG_DIR, exist_ok=True)

# Setup basic error file logger
logging.basicConfig(
    filename=ERROR_LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def log_error(msg: str):
    logging.error(msg)

def print_section(title: str):
    print(f"\n\033[96m✦ {title}\033[0m")
    print("-" * (len(title) + 4))
