"""
This module holds the tests to check the functionality of the csv reading and writing module
training_data.py
"""
import os
import pytest
import src.training_data


def test_save_and_read_data():
    """
    Creates a simple data set and stores it to the csv with default filename
    :return:
    """
    test_data = src.training_data.PlankData()
    test_data.clean_data()
    test_data.add(dict(datum="11.10.1975", name="Thomas"))
    test_data.add(dict(datum="10.09.2012", name="Tim"))
    test_data.add(dict(datum="10.11.1980", name="Andrea"))
    file_name = test_data.save()
    assert (os.path.exists(file_name) == True)

    assert (test_data.size() == 3)


def test_add_data():
    """
    test the appending of new data to the csv file.
    :return:
    """
    new_item = dict(datum="11.01.1972", name="Gabriele")

    test_data = src.training_data.PlankData()
    test_data.add(new_item)

    assert (test_data.get_matching_data(new_item) != [])

    with pytest.raises(AssertionError):
        test_data.add(new_item)


def test_exists():
    """
    tests the existant check of the data handling module
    :return:
    """
    test_data = src.training_data.PlankData()
    search_item = dict(datum="11.01.1972", name="Gabriele")
    items = test_data.get_matching_data(search_item)

    assert (items == [search_item])


def test_delete_item():
    test_data = src.training_data.PlankData()

    item_to_remove = dict(datum="11.10.1975", name="Thomas")
    assert (test_data.exists(item_to_remove) == True)

    test_data.remove(item_to_remove)

    assert (test_data.exists(item_to_remove) == False)
