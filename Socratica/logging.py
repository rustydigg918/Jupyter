Don't proceed there are certain issues with the file



# Logging modules gives everything we need to report
# progress and problems in your code.It would be nice if developer and machine
# were 100% reliable but that's not the case. Like Expecting an integer,
# someone hands a float. You call a cloud api- the server is down for maintainance
# A wide range of problems can happen that are out of our control. With logging,
# We can leave a breadcrumb, so something goes wrong, you can determine the cause

"""
With Logging hope for the best but
plan for the worst.
"""

# Logging allows us to write status messages to a file
# or other output streams. These messages information on
# which part of our code have executed, and what problems
# my have arisen.

# Each Log message has a level, The five
# built-in levels are, (debug, info,warning,
# error,critical). we may create an additional levels as well.


import logging

"""
['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'F
ileHandler', 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord',
'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', '
PlaceHolder', 'RootLogger', 'StrFormatStyle', 'StreamHandler', 'StringTemplateSt
yle', 'Template', 'WARN', 'WARNING', '_STYLES', '_StderrHandler', '__all__', '__
author__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__l
oader__', '__name__', '__package__', '__path__', '__spec__', '__status__', '__ve
rsion__', '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter',
'_defaultLastResort', '_handlerList', '_handlers', '_levelToName', '_lock', '_lo
gRecordFactory', '_loggerClass', '_nameToLevel', '_register_at_fork_reinit_lock'
, '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime',
 '_str_formatter', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConf
ig', 'captureWarnings', 'collections', 'critical', 'currentframe', 'debug', 'dis
able', 'error', 'exception', 'fatal', 'getLevelName', 'getLogRecordFactory', 'ge
tLogger', 'getLoggerClass', 'info', 'io', 'lastResort', 'log', 'logMultiprocessi
ng', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 're
', 'root', 'setLogRecordFactory', 'setLoggerClass', 'shutdown', 'sys', 'threadin
g', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
>>>
"""

# dir(logging)
# Here Capitalized items are Classes
# Items starts with lowercase lettes
# are methods.




# Create and configure logger
"""logging.basicConfig(filename = "E:\\PYTHON\\Log_files\\socratica.Log")
logger = logging.getLogger()

#Test the logger

logger.info("Our first message.")
print(logger.level) # >>>>>>>>>>>>>>>>>>>> throws 30"""





'''
What does that 30 means

Logger has 6 levels.

Level                   Numeric Value
NOTSET                      0
DEBUG                       10
INFO                        20
WARNING                     30
ERROR                       40
CRITICAL                    50

*** Logger will only write messages with a levels
greater than or equal to the set level.
Our test log message was an info message which has
a value of 20, but basic config sets the level of
root logger to warning by default.
To fix this, update the basic config call and
set the config level to debug.
This will guarantee that we will see all log
messages.
'''

logging.basicConfig(filename = "E:\\PYTHON\\Log_files\\socratica.Log",
                    level = DEBUG)
logger = logging.getLogger()

#Test the logger

logger.info("Our first message.")
