import logging
import threading


from funcy import cached_property, memoize, wrap_prop, wrap_with

from .https import RemoteHTTPS
from dvc.scheme import Schemes
from dvc.exceptions import HTTPError
import dvc.prompt as prompt



logger = logging.getLogger(__name__)

@wrap_with(threading.Lock())
@memoize
def get_input(message):
    return prompt.password(message)

class RemoteSTRATUS(RemoteHTTPS):

    
    def __init__(self, repo, config):
        super().__init__(repo, config)
        self.bucket_name = ask_bucket('Enter bucket name:')
    
    def checksum_to_path_info(self, checksum):
        return str(self.path_info)+'/b/'+str(self.bucket_name) + '/k/'+str(checksum)

    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        logger.info("stratus upload method")
        logger.info("url:"+str(to_info.url))
        
        