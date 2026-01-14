from ._base import BaseResource
from ..models import (
    UserBasicResponse,
    UserAmmoResponse,
    Crimes,
    ApiFiltersAttacksRevivesEnum,
    AttacksResponse,
    AttacksFullResponse,
    UserBarsResponse,
    UserBattleStatsResponse,
    UserBountiesResponse,
    UserCalendarResponse,
    UserCompetitionResponse,
    UserCooldownsResponse,
    UserCrimesResponse,
    UserDiscordResponse
)

class UserResource(BaseResource):
    def get_ammo(self: "SyncTorn", **kwargs) -> UserAmmoResponse:
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
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return UserAmmoResponse(**data)

    def get_attacks(self: "SyncTorn", **kwargs) -> AttacksResponse:
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
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return AttacksResponse(**data)

    def get_attacks_full(self: "SyncTorn", **kwargs) -> AttacksFullResponse:
        """
        Get your simplified attacks.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **filters** (List[ApiFiltersAttacksRevivesEnum]): It's possible to use this query parameter to only get incoming or outgoing attacks, It's also possible to combine this with 'idFilter'. This filter allows using from/to to filter by ids instead of timestamps.
            * **limit** (int): Default Value: 1000
            * **sort** (str): Sorted by the greatest timestamps. Available values: DESC, ASC.
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "attacksfull")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return AttacksFullResponse(**data)

    def get_bars(self: "SyncTorn", **kwargs) -> UserBarsResponse:
        """
        Get your bars information.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "bars")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return UserBarsResponse(**data)


    def get_basic(self: "SyncTorn", user_id: int | None = None, *, striptags: bool = True, **kwargs) -> UserBasicResponse:
        """
        Get your basic profile information or for a specific user.

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
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return UserBasicResponse(**data)

    def get_battlestats(self: "SyncTorn", **kwargs) -> UserBattleStatsResponse:
        """
        Get bounties placed on you or a specific user.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "battlestats")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserBattleStatsResponse(**data)

    def get_bounties(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserBountiesResponse:
        """
        Get your battlestats.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "bounties")
        else:
            url = self._build_url("user", "bounties")

        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserBountiesResponse(**data)

    def get_calendar(self: "SyncTorn", **kwargs) -> UserCalendarResponse:
        """
        Get your calendar events start time.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "calendar")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserCalendarResponse(**data)

    def get_competition(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserCompetitionResponse:
        """
        Get your competition information or for a specific user.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "competition")
        else:
            url = self._build_url("user", "competition")

        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return UserCompetitionResponse(**data)

    def get_cooldowns(self: "SyncTorn", **kwargs) -> UserCooldownsResponse:
        """
        Get your cooldowns information.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """
        url = self._build_url("user", "cooldowns")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserCooldownsResponse(**data)


    def get_crimes(self: "SyncTorn", crime_id: int | CrimeEnum, **kwargs) -> UserCrimesResponse:
        """
        Get your crime statistics.

        **Access Level:** Minimal Access

        :param crime_id (int): Crime Id, use the Crimes Enum from torn.models
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", str(crime_id if not isinstance(crime_id, Crimes) else crime_id.value), "crimes")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserCrimesResponse(**data)

    def get_discord(self: "SyncTorn", user_id: int | None = None, **kwargs):
        """
        Get your discord or for a specific user.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """
        
        if user_id:
            url = self._build_url("user", user_id, "discord")
        else:
            url = self._build_url("user", "discord")

        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return UserDiscordResponse(**data)

