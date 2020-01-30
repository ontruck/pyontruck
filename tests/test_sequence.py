"""
test_pyontruck
----------------------------------

Tests for `pyontruck.sequence` module.
"""
import pytest
from pyontruck.sequence import remove_duplicates, clean_nones


@pytest.fixture
def list_without_duplicates():
    return [1, 2, 3, 4, 5, 'a', 'e', 'i', 'o', 'u']


@pytest.fixture
def list_with_duplicates():
    return [1, 2, 3, 4, 5, 'a', 'e', 'i', 'o', 'u', 1, 2, 3, 4, 5]


@pytest.fixture
def none_list():
    return [None, None, None]


def test_clean_nones_from_list_without_nones(list_without_duplicates):
    assert list_without_duplicates == clean_nones(list_without_duplicates)


def test_clean_nones_from_none_list(none_list):
    assert [] == clean_nones(none_list)


def test_clean_nones_from_mixed_list(none_list, list_without_duplicates):
    assert list_without_duplicates == clean_nones(list_without_duplicates + none_list)


def test_clean_nones_from_something_that_is_not_a_list():
    with pytest.raises(TypeError):
        clean_nones(1)


def test_remove_duplicates_from_list_without_duplicates(list_without_duplicates):
    assert list_without_duplicates == remove_duplicates(list_without_duplicates)


def test_remove_duplicates_from_list_with_duplicates(list_without_duplicates, list_with_duplicates):
    assert list_without_duplicates == remove_duplicates(list_with_duplicates)


def test_remove_duplicates_from_something_that_is_not_a_list():
    with pytest.raises(TypeError):
        remove_duplicates(1)
