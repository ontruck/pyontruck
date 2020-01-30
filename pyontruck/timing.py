import pytz
import re
from datetime import datetime, timedelta

ES_REGION = 'Europe/Madrid'
ES_TIMEZONE = pytz.timezone(ES_REGION)
UK_REGION = 'Europe/London'
UK_TIMEZONE = pytz.timezone(UK_REGION)
FR_REGION = 'Europe/Paris'
FR_TIMEZONE = pytz.timezone(FR_REGION)
NL_REGION = 'Europe/Amsterdam'
NL_TIMEZONE = pytz.timezone(NL_REGION)

TIMEZONES = {
    'ES': ES_TIMEZONE,
    'UK': UK_TIMEZONE,
    'FR': FR_TIMEZONE,
    'NL': NL_TIMEZONE,
}


def get_next_monday(date=None):
    now = date or datetime.utcnow()
    num_days_to_add = 7 - now.weekday()
    return now + timedelta(days=num_days_to_add)


def get_naive_time_utc(datetime_value, country_code='ES'):
    """ Localize naive data and get its utc value """
    timezone = TIMEZONES[country_code]
    return timezone.localize(datetime_value).astimezone(pytz.utc)


def parse_to_timedelta(time_val):
    """
    Given a *time_val* (string) such as '5d', returns a timedelta object
    representing the given value (e.g. timedelta(days=5)).  Accepts the
    following '<num><char>' formats:

    =========   ======= ===================
    Character   Meaning Example
    =========   ======= ===================
    s           Seconds '60s' -> 60 Seconds
    m           Minutes '5m'  -> 5 Minutes
    h           Hours   '24h' -> 24 Hours
    d           Days    '7d'  -> 7 Days
    =========   ======= ===================

    Examples::

        >>> parse_to_timedelta('7d')
        datetime.timedelta(7)
        >>> parse_to_timedelta('24h')
        datetime.timedelta(1)
        >>> parse_to_timedelta('60m')
        datetime.timedelta(0, 3600)
        >>> parse_to_timedelta('120s')
        datetime.timedelta(0, 120)
    """

    if not re.match(r"^\d+[smhd]$", time_val):
        raise Exception('time_val has incorrect format')

    num = int(time_val[:-1])
    if time_val.endswith('s'):
        return timedelta(seconds=num)
    elif time_val.endswith('m'):
        return timedelta(minutes=num)
    elif time_val.endswith('h'):
        return timedelta(hours=num)
    elif time_val.endswith('d'):
        return timedelta(days=num)
