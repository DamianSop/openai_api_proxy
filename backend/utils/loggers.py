import logging


def get_module_logger(mod_name):

    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"generations/logs.log")
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] -  (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)
    return logger
