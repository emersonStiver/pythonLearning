import logging
#different log levels, configuraltions, lgo in multiple modules, how to use different log handlers, rotating file handler
import logging.config
import traceback
from logging.handlers import RotatingFileHandler

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %H:%M:%S')
#if i want to log in multiple modules, you gotta create your own logger in the modules

#import helper

#DICTS AND FILECONFIGS
#logging.config.fileConfig('logging.ini')
#logger = logging.getLogger()
#logger.debug('this is a debug message')

#we can log to different file levels
#by default, only logs above warnings are printed
#logging.debug("This is a debug message")
#logging.info("This is an info message")
#logging.warning("This is a warning message")
#logging.error("This is an error message")
#logging.critical("This is a critical message")


#log handlers are used to dispatch the appropiate log message to the hanlder
# specific destination, you can use different handlers to send messasges to send log
#mmessages to the standard output stream, to file or via email

#create handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create the handlers
streamH = logging.StreamHandler()
fileH = logging.FileHandler('file.log')

#level and the format
streamH.setLevel(logging.ERROR)
fileH.setLevel(logging.ERROR)

#we set the formatter to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamH.setFormatter(formatter)
fileH.setFormatter(formatter)

logger.addHandler(streamH)
logger.addHandler(fileH)

logger.debug('this is a debug message')
logger.info('this is info')
logger.warning('this is a warning')
logger.error('this is an error')




#CAPTURING STEP TRACES

try:
    list1 = [1,2,3]
    val = list1[2]
except IndexError as e:
    #logging.error(e, exc_info=True)
    logging.error("The error is %s", traceback.format_exc())





