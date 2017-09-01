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
    test_data = list()
    test_data.append(dict(datum="11.10.1975", name="Thomas"))
    test_data.append(dict(datum="10.09.2012", name="Tim"))
    test_data.append(dict(datum="10.11.1980", name="Andrea"))
    file_name = src.training_data.save_data(test_data)
    assert (os.path.exists(file_name) == True)

    new_data = src.training_data.read_data()
    assert (new_data == test_data)


def test_append_data():
    """
    test the appending of new data to the csv file.
    :return:
    """
    new_item = dict(datum="11.01.1972", name="Gabriele")

    src.training_data.add_data(new_item)
    new_data = src.training_data.read_data()
    assert (src.training_data.get_matching_data(new_data, new_item) != [])

    with pytest.raises(AssertionError):
        src.training_data.add_data(new_item)


def test_exists():
    """
    tests the existant check of the data handling module
    :return:
    """
    test_data = src.training_data.read_data()
    search_item = dict(datum="11.01.1972", name="Gabriele")
    items = src.training_data.get_matching_data(test_data, search_item)

    assert (items == [search_item])


def test_delete_item():
    test_data = src.training_data.read_data()

    item_to_remove = dict(datum="11.10.1975", name="Thomas")
    assert (src.training_data.data_exists(test_data, item_to_remove) == True)

    src.training_data.remove(item_to_remove)

    test_data = src.training_data.read_data()
    assert (src.training_data.data_exists(test_data, item_to_remove) == False)
