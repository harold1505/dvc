import logging



from .https import RemoteHTTP
from dvc.scheme import Schemes



logger = logging.getLogger(__name__)

class RemoteSTRATUS(RemoteHTTP):
    scheme = Schemes.STRATUS
    