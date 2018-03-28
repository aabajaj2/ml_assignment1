from logger import logger
import sys
class file_logger(logger):

    """
    Constructor
    """
    def __init__(self, log_level, filename):
        logger.__init__(self, log_level)
        self.__log_level__ = log_level
        self.__filename__ = filename


    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """
    def log(self, log_level, message):
        if self.__log_level__ >= log_level:
            f = open(self.__filename__, 'a')
            fmessage = str(log_level)+": "+message
            f.write(fmessage)
            f.write("\n")


