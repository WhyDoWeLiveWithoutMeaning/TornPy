import httpx
import time
from ._base import BaseClient
from .resources.user import UserMixin
from .models import UserBasicResponse

class SyncTorn(BaseClient, UserMixin):
    def __init__(self, api_key: str):
        super().__init__(base_url="https://api.torn.com/v2", api_key=api_key)
        self.client = httpx.Client(headers=self._headers)
