import time
import datetime

from ._base import BaseResource

class HelperResource(BaseResource):
    
    def datetime_from_timestamp(self, timestamp: int) -> datetime.datetime:
        """
        Converts a Torn API Unix timestamp into a UTC datetime object.
        """
        return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)

    def timestamp_from_datetime(self, dt: datetime.datetime) -> int:
        """
        Converts a Python datetime object back into a Torn-compatible Unix integer.
        """
        return int(dt.timestamp())

    def get_torn_time_now(self) -> int:
        """
        Returns the current Unix timestamp as an integer, exactly as Torn expects.
        """
        return int(time.time())