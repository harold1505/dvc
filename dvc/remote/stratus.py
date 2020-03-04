import logging



from .https import RemoteHTTP
from dvc.scheme import Schemes



logger = logging.getLogger(__name__)

class RemoteSTRATUS(RemoteHTTP):
    scheme = Schemes.STRATUS

    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        logger.info("stratus upload method")