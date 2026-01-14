from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .._async_client import AsyncTorn

from ..models import UserBasicResponse, UserAmmoResponse

class UserAsyncMixin:
    async def get_user_ammo(self: "AsyncTorn", **kwargs):
        """
        Get your ammo information.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "ammo")
        params = self._prepare_params(**kwargs)
        response = await self.client.get(url, params=params)
        data = self._handle_response(response)

        return UserAmmoResponse(**data)

    async def get_user_basic(self: "AsyncTorn", user_id: int | None = None, *, striptags: bool = True, **kwargs):
        """
        Get your basic profile information.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **striptags** (bool): Determines if fields include HTML or not.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        # For looking up a Different User
        if user_id:
            url = self._build_url("user", user_id, "basic")
        else:
            url = self._build_url("user", "basic")

        if not striptags:
            kwargs["striptags"] = False

        params = self._prepare_params(**kwargs)
        response = await self.client.get(url, params=params)
        data = self._handle_response(response)

        return UserBasicResponse(**data)