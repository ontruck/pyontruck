from datetime import datetime
from freezegun import freeze_time
import pytest
import pytz
from pytest_cases import pytest_parametrize_plus, fixture_ref

from pyontruck.timing import get_next_monday, get_naive_time_utc


@pytest.fixture
@freeze_time('2020-01-30')
def get_frozen_datetime():
    return datetime.now()


@freeze_time('2020-01-30')
def test_get_next_monday_from_faked_present_moment():
    next_monday = get_next_monday()
    assert "2020-02-03" == next_monday.strftime("%Y-%m-%d")


def test_get_next_monday_from_specific_date():
    base_date = datetime(1980, 4, 29)
    next_monday = get_next_monday(base_date)
    assert "1980-05-05" == next_monday.strftime("%Y-%m-%d")


@pytest_parametrize_plus("datetime_value, country_code, exception_raised", [
    (datetime.now(), 'XX', KeyError),
    (1, 'ES', AttributeError)
])
def test_naive_time_utc_errors(datetime_value, country_code, exception_raised):
    with pytest.raises(exception_raised):
        get_naive_time_utc(datetime_value, country_code=country_code)


@pytest_parametrize_plus("datetime_value, country_code, timezone_region", [
    (fixture_ref(get_frozen_datetime), 'ES', 'Europe/Madrid'),
    (fixture_ref(get_frozen_datetime), 'UK', 'Europe/London'),
    (fixture_ref(get_frozen_datetime), 'FR', 'Europe/Paris'),
    (fixture_ref(get_frozen_datetime), 'NL', 'Europe/Amsterdam')
])
def test_naive_time_utc(datetime_value, country_code, timezone_region):
    assert pytz.timezone(timezone_region).localize(datetime_value).astimezone(pytz.utc) == get_naive_time_utc(
        datetime_value, country_code=country_code)
