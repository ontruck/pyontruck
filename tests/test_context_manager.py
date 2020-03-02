"""
test_pyontruck
----------------------------------

Tests for `pyontruck.context_manager` module.
"""
import pytest
from pyontruck.context_manager import edit_dict


@pytest.mark.parametrize("dictionary, key, value", [
    ({"foo": "bar", "xxx": "yyy"}, "xxx", "zzz"),
    ({7: 3, "xxx": [1, 2, 3]}, "xxx", "zzz"),
])
def test_edit_dict(dictionary, key, value):
    # Store the value we want to modify
    original_value = dictionary.get(key)

    # Modify dictionary inside context manager
    with edit_dict(key, value, dictionary):
        assert dictionary.get(key) == value

    assert dictionary.get(key) == original_value
