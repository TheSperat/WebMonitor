import logging


class Logger:
    #Log format
    FORMAT = '%(asctime)-15s  %(message)s'

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.log_operator = logging.getLogger(__name__)
        self.log_operator.propagate = False
        self.handler = logging.FileHandler('log_file.log')
        self.log_setup()

    # Defines how logs would look like
    def log_setup(self):
        self.log_operator.setLevel(logging.INFO)
        self.handler.setFormatter(logging.Formatter(Logger.FORMAT))
        self.handler.setLevel(logging.INFO)
        self.log_operator.addHandler(self.handler)
