import logging
import os
import threading


from funcy import cached_property, memoize, wrap_prop, wrap_with

from .https import RemoteHTTPS
from dvc.scheme import Schemes
from dvc.exceptions import HTTPError, DvcException
from dvc.progress import Tqdm
import dvc.prompt as prompt



logger = logging.getLogger(__name__)

@wrap_with(threading.Lock())
@memoize
def get_input(message):
    return prompt.ask(message)

class RemoteSTRATUS(RemoteHTTPS):

    
    def __init__(self, repo, config):
        super().__init__(repo, config)
        self.bucket_name = get_input('Enter bucket name:')
        self.headers = {'Authorization' : 'Zoho-oauthtoken ' + get_input("Enter OAuth:")}
    
    def checksum_to_path_info(self, checksum):
        self.headers['Content-MD5'] = checksum
        return self.path_info / 'b' / self.bucket_name / 'k' / checksum

    @wrap_prop(threading.Lock())
    @cached_property
    def _session(self):
        import requests
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry

        session = requests.Session()

        retries = Retry(
            total=self.SESSION_RETRIES,
            backoff_factor=self.SESSION_BACKOFF_FACTOR,
        )

        session.mount("https://", HTTPAdapter(max_retries=retries))

        return session

    def _request(self, method, url, **kwargs):
        import requests
        logger.info('reached stratus request')

        try:
            res = self._session.request(
                method,
                url,
                headers=self.headers,
                **kwargs,
            )

            return res

        except requests.exceptions.RequestException:
            raise DvcException("could not perform a {} request".format(method))

    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        logger.info("stratus upload method")
        logger.info("url:"+str(to_info.url)+' from_file:'+str(from_file))
        
        response = self._request("PUT", to_info.url, data=open(from_file, "rb").read())
        _upload_response_handler(response)
            

    def _upload_response_handler(self,response) :
        if response.status_code == 200 :
            logger.info("Successfully uploaded")
    
        
        