from ._base import BaseResource
from ..models import *

class FactionResource(BaseResource):

    def get_applications(self: "SyncTorn", **kwargs) -> FactionApplicationsResponse:
        """
        Get your faction's applications.

        **Access Level:** Minimal Access (With Faction API Access)

        :param kwargs: Optional API parameters:
            * **bypass_cache** (bool): If True, adds a timestamp to force fresh data.
            * **comment** (str): A custom string to show in your API logs.
            * **key** (str): API key. It's not required to use this parameter when passing the API key via the Authorization header.
        """

        url = self._build_url("faction", "applications")
        params = self._prepare_params(**kwargs)
        response = self._request(url, params=params)
        data = self._handle_response(response)

        return FactionApplicationsResponse(**data)