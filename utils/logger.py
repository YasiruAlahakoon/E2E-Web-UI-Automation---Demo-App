# File: utils/logger.py
import logging
import os

def get_logger(name=__name__):
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.mkdir('logs')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate handlers if logger already configured
    if logger.hasHandlers():
        return logger

    # File Handler with mode 'a' to append
    file_handler = logging.FileHandler('logs/automation.log', mode='a')
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console Handler (so you see it in terminal too)
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger