import logging
from unittest import TestCase

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(
                    filename='logfile.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)


class Test_LOG(TestCase):
    def test_001(self):
        logger.info('Logged INFO message')
        logger.warning('Logged WARNING message')
        logger.error('Logged ERROR message')
        assert 1 == 1
