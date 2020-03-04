import logging



from .https import RemoteHTTPS
from dvc.scheme import Schemes
from dvc.exceptions import HTTPError



logger = logging.getLogger(__name__)

class RemoteSTRATUS(RemoteHTTPS):
    scheme = Schemes.STRATUS
    def __init__(self, repo, config):
        super().__init__(repo,config)
        logger.info("initialized successfully")

    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        raise HTTPError(400, "stratus upload not implemented")
