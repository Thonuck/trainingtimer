import csv
import os

def write_data(filename, data):
    if len(data) == 0:
        raise AssertionError("Data dictionary is empty!")
    
    with open(filename, 'w') as csvfile:
        fieldnames = list(data[0].iterkeys())
            
        #fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for single_data in data:
            writer.writerow(single_data)

def read_data(filename):
    data = list()
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            data.append(row)
    return data


def csv_path(csv_file_name):
    path = os.path.split(__file__)[0]
    path = os.path.realpath(path)
    return os.path.join(path, csv_file_name)


if __name__ == "__main__":
    data = [{'first_name': 'Lovely', 'last_name': 'Spam'},
            {'first_name': 'Wonderful', 'last_name': 'Spam'},
            {'first_name': 'Other', 'last_name': 'one'}]

    write_data(csv_path("test.csv"), data)

    ret_data = read_data(csv_path("test.csv"))
    print(ret_data)


    


    
