import logging



from .https import RemoteHTTPS
from dvc.scheme import Schemes
from dvc.exceptions import HTTPError



logger = logging.getLogger(__name__)

class RemoteSTRATUS(RemoteHTTPS):
    
    def __init__(self, repo, config):
        super().__init__(repo, config)
    
    def checksum_to_path_info(self, checksum):
        return self.path_info / checksum

    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        logger.info("stratus upload method")
        logger.info("url:"+str(to_info.url))
        