from ._sync_client import SyncTorn
from ._async_client import AsyncTorn

def Torn(api_key: str = "", use_async: bool = False) -> SyncTorn | AsyncTorn:
    if use_async:
        return AsyncTorn(api_key)
    return SyncTorn(api_key)

__all__ = ["Torn", "SyncTorn", "AsyncTorn"]
