import httpx
import time
from urllib.parse import urlencode
from enum import Enum
from typing import Any, Dict

from .exceptions import *

class BaseClient:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: float = 10.0
    ):
        self._base_url = base_url.rstrip("/")
        self._headers = {
            "Authorization": f"ApiKey {api_key}",
            "Accept": "application/json",
            "User-Agent": "TornPy/0.1.0"
        }
        self._timeout = timeout

    def _build_url(self, *args: Any) -> str:
        path = "/".join(str(arg).strip("/") for arg in args)
        url = f"{self._base_url}/{path}"
        return url

    def _prepare_params(
        self, 
        key: str | None = None, 
        bypass_cache: bool = False, 
        comment: str | None = None,
        **extra_params: Any
    ) -> Dict[str, Any]:
        """Centralized parameter handling for shared and specific query params."""
        # 1. Base parameters found in all images
        params = {}

        if key:
            params["key"] = key
        
        if comment:
            params["comment"] = comment
        
        if bypass_cache:
            params["timestamp"] = int(time.time())

        for k, v in extra_params.items():
            if v is None:
                continue
                
            # Handle lists like filters=["incoming", ApiFiltersAttacksRevivesEnum.OUTGOING]
            if isinstance(v, list):
                # map(str, v) turns the Enum member into its value ("incoming")
                # and leaves normal strings exactly as they are.
                extra_params[k] = ",".join(map(str, v))
                
            # Handle single values (like sort="DESC" or an Enum member)
            elif isinstance(v, Enum):
                extra_params[k] = v.value
            
        params.update({k: v for k, v in extra_params.items() if v is not None})
            
        return params

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise TornAPIError(
                f"API Request failed: {exc.response.status_code} - {exc.response.text}"
            ) from exc
        data = response.json()

        if "error" in data:
            error_info = data["error"]
            code = error_info.get("code")
            msg = error_info.get("error", "Unknown Error")

            match code:
                case 0:
                    raise UnknownError(code, msg)
                case 1:
                    raise NoKeyError(code, msg)
                case 2:
                    raise IncorrectKeyError(code, msg)
                case 3:
                    raise WrongTypeError(code, msg)
                case 4:
                    raise WrongFieldsError(code, msg)
                case 5:
                    raise TooManyRequestsError(code, msg)
                case 6:
                    raise IncorrectIDError(code, msg)
                case 7:
                    raise IncorredIDEntityRelationError(code, msg)
                case 8:
                    raise IPBlockError(code, msg)
                case 9:
                    raise APIDisabledError(code, msg)
                case 10:
                    raise KeyOwnerInFederalJailError(code, msg)
                case 11:
                    raise KeyChangeError(code, msg)
                case 12:
                    raise KeyReadError(code, msg)
                case 13:
                    raise KeyDisabledDueToInactivityError(code, msg)
                case 14:
                    raise DailyLimitReachedError(code, msg)
                case 15:
                    raise TemporaryError(code, msg)
                case 16:
                    raise AccessLevelError(code, msg)

        return response.json()