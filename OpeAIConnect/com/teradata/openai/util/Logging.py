import logging
from logging import Logger

logging.basicConfig(filename='poc.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)


class Logging:
    @property
    def log(self) -> Logger:
        """Return a logger."""
        return logger
