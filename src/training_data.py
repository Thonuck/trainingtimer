import csv
import os


class PlankData(object):
    def __init__(self, file_name="data_file.csv"):
        self.file_name = self.__determine_file_name(file_name)
        self.data = self.load()

    def clean_data(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            self.data = list()

    def save(self):
        """
        saves the given data to the data file
        :param dict_list:
        :return:
        """
        fieldnames = list(self.data[0].keys())
        with open(self.file_name, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.data:
                writer.writerow(item)
        return self.file_name

    @staticmethod
    def __determine_file_name(file_name):
        """
        create the full path to the result file. the file will be next to the script files. The file name itself can be
        changed by an optional argument file_name
        :return:
        """
        this_path = os.path.split(os.path.realpath(__file__))[0]
        file_path = os.path.join(this_path, file_name)
        return file_path

    def load(self):
        data = list()

        try:
            open(self.file_name, "r")
        except FileNotFoundError:
            return data

        with open(self.file_name) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
        return data

    def add(self, data_item):

        if not self.exists(data_item):
            self.data.append(data_item)
        else:
            print(self.data)
            raise AssertionError("Data already Exists!")

        self.save()

    def remove(self, item_to_remove):
        self.data = [data_item for data_item in self.data if data_item != item_to_remove]
        self.save()

    def get_matching_data(self, data_item):
        matching_data = [item for item in self.data if item == data_item]
        return matching_data

    def count(self, data_item):
        return len(self.get_matching_data(data_item))

    def size(self):
        return len(self.data)

    def exists(self, data_item):
        if self.count(data_item) > 0:
            return True
        else:
            return False

    def remove(self, item_to_remove):
        self.data = [data_item for data_item in self.data if data_item != item_to_remove]

    def remove_by_indices(self, index_list):
        new_nodes = [x for i, x in enumerate(self.data) if i not in index_list]
        self.data = new_nodes
