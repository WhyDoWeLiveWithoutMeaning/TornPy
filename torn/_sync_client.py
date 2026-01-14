import httpx
import time
from ._base import BaseClient
from .resources.user import UserResource
from .resources.faction import FactionResource
from .models import UserBasicResponse

class SyncTorn(BaseClient):
    def __init__(self, api_key: str):
        super().__init__(base_url="https://api.torn.com/v2", api_key=api_key)
        self.client = httpx.Client()
        self.user = UserResource(self)
        self.faction = FactionResource(self)

    def _request(self, url: str, params: dict):
        """
        Internal wrapper to handle the conditional Authorization header.
        """
        # Copy headers to avoid permanently modifying the client's defaults
        request_headers = self._headers.copy()

        # If a key is passed in params, remove the Authorization header
        if "key" in params and params["key"] is not None:
            request_headers.pop("Authorization", None)

        return self.client.get(url, params=params, headers=request_headers)