import httpx
from ._base import BaseClient
from .resources.user_async import UserAsyncMixin

class AsyncTorn(BaseClient, UserAsyncMixin):
    def __init__(self, api_key: str):
        super().__init__(base_url="https://api.torn.com/v2", api_key=api_key)
        self.client = httpx.AsyncClient(headers=self._headers)
