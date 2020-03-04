import logging



from .https import RemoteHTTP
from dvc.scheme import Schemes



logger = logging.getLogger(__name__)

class RemoteSTRATUS(RemoteHTTP):
    scheme = Schemes.STRATUS
    def __init__(self, repo, config):
        super().__init__(repo,config)
        logger.info("initialized successfully")

    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        logger.info("stratus remote push")