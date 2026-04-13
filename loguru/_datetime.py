import re
from calendar import day_abbr, day_name, month_abbr, month_name
from datetime import datetime as datetime_
from datetime import timedelta, timezone
from functools import lru_cache, partial
from time import localtime, strftime

tokens = r"H{1,2}|h{1,2}|m{1,2}|s{1,2}|S+|YYYY|YY|M{1,4}|D{1,4}|Z{1,2}|zz|A|X|x|E|Q|dddd|ddd|d"

pattern = re.compile(r"(?:{0})|\[(?:{0}|!UTC|)\]".format(tokens))


def _builtin_datetime_formatter(is_utc, format_string, dt):
    pass


def _loguru_datetime_formatter(is_utc, format_string, formatters, dt):
    pass


def _default_datetime_formatter(dt):
    pass


def _format_timezone(dt, *, sep):
    pass


@lru_cache(maxsize=32)
def _compile_format(spec):
    pass


class datetime(datetime_):  # noqa: N801
    def __format__(self, fmt):
        return _compile_format(fmt)(self)


def _fallback_tzinfo(timestamp):
    utc_naive = datetime_.fromtimestamp(timestamp, tz=timezone.utc).replace(tzinfo=None)
    offset = datetime_.fromtimestamp(timestamp) - utc_naive
    seconds = offset.total_seconds()
    zone = strftime("%Z")
    return timezone(timedelta(seconds=seconds), zone)


def _get_tzinfo(timestamp):
    try:
        local = localtime(timestamp)
    except (OSError, OverflowError):
        # The "localtime()" can overflow on some platforms when the timestamp is too large.
        # Not sure the fallback won't also overflow, though.
        return _fallback_tzinfo(timestamp)

    try:
        seconds = local.tm_gmtoff
        zone = local.tm_zone
    except AttributeError:
        # The attributes were not availanble on all platforms before Python 3.6.
        return _fallback_tzinfo(timestamp)

    try:
        return timezone(timedelta(seconds=seconds), zone)
    except ValueError:
        # The number of seconds returned by "tm_gmtoff" might be invalid on Windows (year 2038+).
        # Curiously, the fallback workaround does not exhibit the same problem.
        return _fallback_tzinfo(timestamp)


def aware_now():
    now = datetime_.now()
    timestamp = now.timestamp()
    tzinfo = _get_tzinfo(timestamp)
    return datetime.combine(now.date(), now.time().replace(tzinfo=tzinfo))
