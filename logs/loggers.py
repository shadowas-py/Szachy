import logging


def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    # l.addHandler(streamHandler)


# LOGGERS LIST
logger = setup_logger('logger', 'main.log')
debug_pins = setup_logger('debug_pins', 'debug_pins.log')

logger = logging.getLogger('logger')
debug_pins = logging.getLogger('debug_pins')
