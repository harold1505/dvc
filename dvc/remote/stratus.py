from .https import RemoteHTTPS
from dvc.scheme import Schemes


class RemoteSTRATUS(RemoteHTTPS):
    scheme = Schemes.STRATUS
    def _upload(self, from_file, to_info, name=None, no_progress_bar=False):
        logger.info("stratus remote push")
        with Tqdm(
            total=None if no_progress_bar else os.path.getsize(from_file),
            leave=False,
            bytes=True,
            desc=to_info.url if name is None else name,
            disable=no_progress_bar,
        ) as pbar:

            def chunks():
                with open(from_file, "rb") as fd:
                    while True:
                        chunk = fd.read(self.CHUNK_SIZE)
                        if not chunk:
                            break
                        pbar.update(len(chunk))
                        yield chunk

            response = self._request("POST", to_info.url, data=chunks())
            if response.status_code not in (200, 201):
                raise HTTPError(response.status_code, response.reason)