import logging

LOG_FORMAT = '%(levelname)-5s | %(message)s'
logging.basicConfig(filename= 'szachy.log', level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()