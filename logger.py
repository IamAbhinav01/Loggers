import logging
## used for debuggings and warning.


#configure base settings
# logging.basicConfig(filename='app.log',
#                     filemode='w',
#     level=logging.DEBUG,
#                     format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S'
#                     )
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


##Multiple Loggers

logger1 = logging.getLogger('logger1')
logger1.setLevel(logging.DEBUG)
logger2 = logging.getLogger('logger2')
logger2.setLevel(logging.WARNING)
logger3 = logging.getLogger('logger3')
logger3.setLevel(logging.ERROR)


logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


logger1.debug("This is a debug message from logger1")
logger1.info("This is an info message from logger1")
logger2.warning("This is a warning message from logger2")
logger3.error("This is an error message from logger3")