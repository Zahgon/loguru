import datetime
import re
from typing import Optional, Tuple


class Frequencies:
    """Provide static methods to compute the next occurrence of various time frequencies.

    Includes hourly, daily, weekly, monthly, and yearly frequencies
    based on a given datetime object.
    """

    @staticmethod
    def hourly(t: datetime.datetime) -> datetime.datetime:
        """Compute the next hour occurrence.

        Parameters
        ----------
        t : datetime.datetime
            The reference datetime.

        Returns
        -------
        datetime.datetime
            Next hour with minutes, seconds, microseconds set to zero.
        """
        pass

    @staticmethod
    def daily(t: datetime.datetime) -> datetime.datetime:
        """Compute the next day occurrence.

        Parameters
        ----------
        t : datetime.datetime
            The reference datetime.

        Returns
        -------
        datetime.datetime
            Next day with hour, minutes, seconds, microseconds set to zero.
        """
        pass

    @staticmethod
    def weekly(t: datetime.datetime) -> datetime.datetime:
        """Compute the next week occurrence.

        Parameters
        ----------
        t : datetime.datetime
            The reference datetime.

        Returns
        -------
        datetime.datetime
            Next Monday with hour, minutes, seconds, microseconds set to zero.
        """
        pass

    @staticmethod
    def monthly(t: datetime.datetime) -> datetime.datetime:
        """Compute the next month occurrence.

        Parameters
        ----------
        t : datetime.datetime
            The reference datetime.

        Returns
        -------
        datetime.datetime
            First day of next month with hour, minutes, seconds, microseconds set to zero.
        """
        pass

    @staticmethod
    def yearly(t: datetime.datetime) -> datetime.datetime:
        """Compute the next year occurrence.

        Parameters
        ----------
        t : datetime.datetime
            The reference datetime.

        Returns
        -------
        datetime.datetime
            First day of next year with hour, minutes, seconds, microseconds set to zero.
        """
        pass


def parse_size(size: str) -> Optional[float]:
    """Parse a size string with optional units into bits.

    Supports formats like '100MB', '2GiB', '1.5TB'. Case insensitive.

    Parameters
    ----------
    size : str
        Size string to parse (e.g., '100MB', '2GiB').

    Returns
    -------
    float | None
        Size in bits or None if invalid format.

    Raises
    ------
    ValueError
        If numeric value or unit is invalid.
    """
    pass


def parse_duration(duration: str) -> Optional[datetime.timedelta]:
    """Parse a duration string and return a corresponding timedelta object.

    The string can include multiple units (years, months, weeks, days, hours, minutes, seconds).
    Example: "1h 30min", "2 days, 3h", "1.5y 2months".

    Parameters
    ----------
    duration : str
        The duration string to parse.

    Returns
    -------
    datetime.timedelta | None
        The parsed duration or None if input is invalid.

    Raises
    ------
    ValueError
        If a value cannot be converted to float or if an invalid unit is encountered.
    """
    pass


def parse_frequency(frequency: str):
    """Parse a frequency string and return the corresponding Frequencies method.

    Supported frequencies: hourly, daily, weekly, monthly, yearly.

    Parameters
    ----------
    frequency : str
        The frequency string.

    Returns
    -------
    Callable | None
        Corresponding Frequencies method or None if unrecognized.
    """
    pass


def parse_day(day: str) -> Optional[int]:
    """Parse a weekday string and return its integer value.

    Accepts full day names or "w0" to "w6".

    Parameters
    ----------
    day : str
        The day to parse.

    Returns
    -------
    int | None
        Integer value (Monday=0 ... Sunday=6), or None if invalid.

    Raises
    ------
    ValueError
        If the digit in 'wX' is not in range [0-6].
    """
    pass


def parse_time(time: str) -> datetime.time:
    """Parse a time string and return a `datetime.time` object.

    Supports formats: HH, HH:MM, HH:MM:SS, HH AM/PM, etc.

    Parameters
    ----------
    time : str
        The time string.

    Returns
    -------
    datetime.time
        The parsed time.

    Raises
    ------
    ValueError
        If input doesn't match any supported format.
    """
    pass


def parse_daytime(daytime: str) -> Optional[Tuple[int, datetime.time]]:
    """Parse a string representing a day and time separated by 'at'.

    Parameters
    ----------
    daytime : str
        The day and time string.

    Returns
    -------
    tuple[int, datetime.time] | None
        Parsed (day, time) or None.

    Raises
    ------
    ValueError
        If the day or time cannot be parsed.
    """
    pass
