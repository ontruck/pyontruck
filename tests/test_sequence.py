"""
test_pyontruck
----------------------------------

Tests for `pyontruck.sequence` module.
"""
import pytest
from pytest_cases import pytest_parametrize_plus, fixture_ref
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


@pytest.fixture
def list_without_duplicates_and_nones(list_without_duplicates, none_list):
    return list_without_duplicates + none_list


# If you want to use fixtures as parametrize arguments, need pytest_cases extension
# Ref: https://stackoverflow.com/questions/42228895/how-to-parametrize-a-pytest-fixture/56871701#56871701
@pytest_parametrize_plus("expected_list, list_to_test", [
    (fixture_ref(list_without_duplicates), fixture_ref(list_without_duplicates)),
    ([], fixture_ref(none_list)),
    (fixture_ref(list_without_duplicates), fixture_ref(list_without_duplicates_and_nones))
])
def test_clean_nones(expected_list, list_to_test):
    assert expected_list == clean_nones(list_to_test)


def test_clean_nones_error():
    with pytest.raises(TypeError):
        clean_nones(1)


@pytest_parametrize_plus("expected_list, list_to_test", [
    (fixture_ref(list_without_duplicates), fixture_ref(list_without_duplicates)),
    (fixture_ref(list_without_duplicates), fixture_ref(list_with_duplicates))
])
def test_remove_duplicates(expected_list, list_to_test):
    assert expected_list == remove_duplicates(list_to_test)


def test_remove_duplicates_errors():
    with pytest.raises(TypeError):
        remove_duplicates(1)
