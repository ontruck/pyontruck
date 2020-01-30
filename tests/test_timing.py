from datetime import datetime
from freezegun import freeze_time
from pyontruck.timing import get_next_monday


@freeze_time('2020-01-30')
def test_get_next_monday_from_faked_present_moment():
    next_monday = get_next_monday()
    assert "2020-02-03" == next_monday.strftime("%Y-%m-%d")


def test_get_next_monday_from_specific_date():
    base_date = datetime(1980, 4, 29)
    next_monday = get_next_monday(base_date)
    assert "1980-05-05" == next_monday.strftime("%Y-%m-%d")
