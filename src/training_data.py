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
    #fieldnames = ['datum', 'counter']
    with open(file_name, 'w') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in dict_list:
            writer.writerow(item)


def get_file_name(file_name="data_file.csv"):
    """
    create the full path to the result file. the file will be next to the script files. The file name itself can be
    changed by an optional argument file_name
    :return:
    """
    this_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = os.path.join(this_path, file_name)
    print("saving to file [{}]".format(file_path))
    return file_path


def read_data():
    pass


def add_result_data():
    pass