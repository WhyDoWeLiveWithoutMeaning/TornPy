from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .._sync_client import SyncTorn

from ..models import (
    UserBasicResponse,
    UserAmmoResponse,
    ApiFiltersAttacksRevivesEnum,
    AttacksResponse
)

class UserMixin:
    def get_user_ammo(self: "SyncTorn", **kwargs) -> UserAmmoResponse:
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
        response = self.client.get(url, params=params)
        data = self._handle_response(response)

        return UserAmmoResponse(**data)

    def get_user_attacks(self: "SyncTorn", **kwargs):
        """
        Get your detailed attacks.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **filters** (List[ApiFiltersAttacksRevivesEnum]): It's possible to use this query parameter to only get incoming or outgoing attacks, It's also possible to combine this with 'idFilter'. This filter allows using from/to to filter by ids instead of timestamps.
            * **limit** (int): Default Value: 100
            * **sort** (str): Sorted by the greatest timestamps. Available values: DESC, ASC.
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "attacks")
        params = self._prepare_params(**kwargs)
        response = self.client.get(url, params=params)
        data = self._handle_response(response)

        return AttacksResponse(**data)



    def get_user_basic(self: "SyncTorn", user_id: int | None = None, *, striptags: bool = True, **kwargs) -> UserBasicResponse:
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
        response = self.client.get(url, params=params)
        data = self._handle_response(response)

        return UserBasicResponse(**data)
