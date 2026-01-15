from ._base import BaseResource
from ..models import *

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

    def get_discord(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserDiscordResponse:
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

    def get_education(self: "SyncTorn", **kwargs) -> UserEducationResponse:
        """
        Get your education information.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """
        url = self._build_url("user", "education")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserEducationResponse(**data)

    def get_enlisted_cars(self: "SyncTorn", **kwargs) -> UserEnlistedCarsResponse:
        """
        Get your enlisted cars.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """
        url = self._build_url("user", "enlistedcars")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserEnlistedCarsResponse(**data)

    def get_equipment(self: "SyncTorn", **kwargs) -> UserEquipmentResponse:
        """
        Get your equipment & clothing.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """
        url = self._build_url("user", "equipment")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserEquipmentResponse(**data)

    def get_events(self: "SyncTorn", **kwargs) -> UserEventsResponse:
        """
        Get your events.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **striptags** (bool): Determines if fields include HTML or not.
            * **limit** (int): Default Value: 20
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """
        url = self._build_url("user", "events")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserEventsResponse(**data)

    def get_faction(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserFactionResponse:
        """
        Get your faction information.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "faction")
        else:
            url = self._build_url("user", "faction")

        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserFactionResponse(**data)

    def get_forum_feed(self: "SyncTorn", **kwargs) -> UserForumFeedResponse:
        """
        Get updates on your threads and posts.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "forumfeed")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserForumFeedResponse(**data)

    def get_forum_friends(self: "SyncTorn", **kwargs) -> UserForumFriendsResponse:
        """
        Get updates on your friends' activity.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "forumfriends")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserForumFriendsResponse(**data)

    def get_forum_posts(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserForumPostsResponse:
        """
        Get your posts.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **striptags** (bool): Determines if fields include HTML or not.
            * **limit** (int): Default Value: 20
            * **sort** (str): Sorted by the greatest timestamps. Available values: DESC, ASC.
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "forumposts")
        else:
            url = self._build_url("user", "forumposts")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserForumPostsResponse(**data)

    def get_forum_subscribed_threads(self: "SyncTorn", **kwargs) -> UserForumSubscribedThreadsResponse:
        """
        Get updates on threads you subscribed to.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "forumsubscribedthreads")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserForumSubscribedThreadsResponse(**data)
    
    def get_forum_threads(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserForumPostsResponse:
        """
        Get your threads.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **limit** (int): Default Value: 20
            * **sort** (str): Sorted by the greatest timestamps. Available values: DESC, ASC.
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "forumposts")
        else:
            url = self._build_url("user", "forumposts")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserForumPostsResponse(**data)

    def get_hof(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserHofResponse:
        """
        Get your Hall of Fame rankings.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "hof")
        else:
            url = self._build_url("user", "hof")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserHofResponse(**data)

    def get_honors(self: "SyncTorn", **kwargs) -> UserHonorsResponse:
        """
        Get your achieved honors.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "honors")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserHonorsResponse(**data)

    def get_icons(self: "SyncTorn", user_id: int | None = None, **kwargs) -> UserIconsResponse:
        """
        Get your icons information.

        **Access Level:** Public Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        if user_id:
            url = self._build_url("user", user_id, "icons")
        else:
            url = self._build_url("user", "icons")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserIconsResponse(**data)

    def get_job_points(self: "SyncTorn", **kwargs) -> UserJobPointsResponse:
        """
        Get your job points.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "jobpoints")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserJobPointsResponse(**data)

    def get_job_ranks(self: "SyncTorn", **kwargs) -> UserJobRanksResponse:
        """
        Get your starter job positions.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "jobranks")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserJobRanksResponse(**data)

    def get_log(self: "SyncTorn", **kwargs) -> UserLogsResponse:
        """
        Get your log.

        **Access Level:** Full Access

        :param kwargs: Optional API parameters:
            * **log** (List[int]): Log Ids
            * **cat** (int): Log Category ID
            * **target** (int): Get logs where you interacted with a specific player by passing their player ID.
            * **limit** (int): Default Value: 20
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "log")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserLogsResponse(**data)

    def get_medals(self: "SyncTorn", **kwargs) -> UserMedalsResponse:
        """
        Get your medals.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "medals")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserMedalsResponse(**data)

    def get_merits(self: "SyncTorn", **kwargs) -> UserMeritsResponse:
        """
        Get your merits.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "merits")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserMeritsResponse(**data)

    def get_messages(self: "SyncTorn", **kwargs) -> UserMessagesResponse:
        """
        Get your messages.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **limit** (int): Default Value: 20
            * **sort** (str): Sorted by the greatest timestamps. Available values: DESC, ASC.
            * **to** (int): Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
            * **from** (int): Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "messages")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserMessagesResponse(**data)

    def get_missions(self: "SyncTorn", **kwargs) -> UserMissionsResponse:
        """
        Get your missions.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "missions")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserMissionsResponse(**data)

    def get_money(self: "SyncTorn", **kwargs) -> UserMoneyResponse:
        """
        Get your current wealth.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "money")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserMoneyResponse(**data)

    def get_new_events(self: "SyncTorn", **kwargs) -> UserNewEventsResponse:
        """
        Get your unseen events.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **striptags** (bool): Determines if fields include HTML or not.
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "newevents")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserNewEventsResponse(**data)

    def get_new_messages(self: "SyncTorn", **kwargs) -> UserNewMessagesResponse:
        """
        Get your unseen messages.

        **Access Level:** Limited Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "newmessages")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserNewMessagesResponse(**data)
    
    def get_notifications(self: "SyncTorn", **kwargs) -> UserNotificationsResponse:
        """
        Get your notifications.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "notifications")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserNotificationsResponse(**data)

    def get_organized_crime(self: "SyncTorn", **kwargs) -> UserOrganizedCrimeResponse:
        """
        Get your current ongoing organized crime.

        **Access Level:** Minimal Access

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("user", "organizedcrime")
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)
        
        return UserOrganizedCrimeResponse(**data)

    def get_personal_stats(
        self: "SyncTorn",
        user_id: int | None = None,
        cat: Optional[PersonalStatsCategoryEnum | str] = PersonalStatsCategoryEnum.ALL,
        stat: Optional[List[PersonalStatsStatName | str]] = None,
        **kwargs) -> UserPersonalStatsResponse:
        """
        Get your personal stats.

        **Access Level:** Public Access, Limited Access

        :param user_id: User id or user discord id
        :param kwargs: Optional API parameters:
            * **cat**: Stats Category.
            * **stat**: Stat Name (Max 10)
            * **timestamp** (int): Return stats until this timestamp.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """



        if user_id:
            url = self._build_url("user", user_id, "personalstats")
        else:
            url = self._build_url("user", "personalstats")

        if stat:
            kwargs["stat"] = stat
        else: 
            kwargs["cat"] = cat
        
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return UserPersonalStatsResponse(**data)