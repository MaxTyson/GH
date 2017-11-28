import os
import errno
import requests
import logging
from config import DATA

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    os.makedirs(DATA['dir_name'])
except FileExistsError as error:
    if error.errno != errno.EEXIST:
        raise

try:
    fh = logging.FileHandler \
        ('{}/{}'.format(DATA['dir_name'], DATA['log_file']))
except FileNotFoundError:
    logger.info('Directory {} not found!'.format('dir_name'))

formatter = logging.Formatter('%(asctime)s - %(name)s - \
    %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info('Start programm')

ids = requests.get(DATA['ids_url']).json()
try:
    for item_id in ids:
        item = DATA['item_url'].format(item_id)
        data = requests.get(item).json()
        logger.info('Request to {}'.format(item))
        print(data.get('title'))
except Exception:
    logger.info('Parsing failed')
else:
    logger.info('Done')
