from .https import RemoteHTTPS
from dvc.scheme import Schemes


class RemoteSTRATUS(RemoteHTTPS):
    scheme = Schemes.STRATUS
