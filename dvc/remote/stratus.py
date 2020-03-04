import logging



from .https import RemoteHTTPS
from dvc.scheme import Schemes
from dvc.exceptions import HTTPError



logger = logging.getLogger(__name__)

class RemoteSTRATUS(RemoteHTTPS):
    scheme = Schemes.STRATUS
