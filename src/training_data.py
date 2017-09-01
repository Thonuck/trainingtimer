import csv
import os


def save_data(dict_list):
    """
    saves the given data to the data file
    :param dict_list:
    :return:
    """
    file_name = get_file_name()
    fieldnames = list(dict_list[0].keys())
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in dict_list:
            writer.writerow(item)
    return file_name


def get_file_name(file_name="data_file.csv"):
    """
    create the full path to the result file. the file will be next to the script files. The file name itself can be
    changed by an optional argument file_name
    :return:
    """
    this_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = os.path.join(this_path, file_name)
    return file_path


def read_data():
    file_name = get_file_name()

    data = list()
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


def add_data(data_item):
    current_data = read_data()
    if not data_exists(current_data, data_item):
        current_data.append(data_item)
    else:
        raise AssertionError("Data already Exists!")
    save_data(current_data)


def get_matching_data(data_list, data):
    return [data_item for data_item in data_list if data_item == data]


def count_data(data_list, data):
    return len(get_matching_data(data_list, data))


def data_exists(data_list, data):
    return count_data(data_list, data) > 0


def remove(item_to_remove):
    data = read_data()
    data = [data_item for data_item in data if data_item != item_to_remove]
    # data.remove(item_to_remove)
    save_data(data)
    print(data)
