import csv

def read_csvfile_to_memory(input_filename):
    """
    Args: a string representing a filename of csv file.
    Return: a list of strings representing column names from the top row of the csv, and the data fields from the rest of the csvfile.
    """
    raw_data = []
    with open(input_filename, 'r',) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in (reader):
                raw_data.append(row)
    return(raw_data)
    
def write_memory_to_csvfile(output_filename, raw_data):
    """
    Args: a string representing a filename of output csv file.
    """
    raw_data = []
    with open(output_filename, 'rw',) as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in (writer):
                pass
    return None

def import_csv_with_dictreader(input_filename):
    """
    Args: a string representing a filename of input csv file.
    Return: a list of ordered dicts representing column names from the top row of the csv,as the keys, and the data fields from the rest of the csvfile as the values.
    """
    reader = csv.DictReader(open(input_filename))
    raw_data = []
    for row in (reader):
        raw_data.append(row)
    return raw_data

def export_csv_with_dictwriter(output_filename, data_field_names, sorted_dict):
    """
    Args: a string representing a filename of input csv file.
    Return: a list of ordered dicts representing column names from the top row of the csv,as the keys, and the data fields from the rest of the csvfile as the values.
    """
    try:
        with open(output_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data_field_names)
            writer.writeheader()
            for data in sorted_dict:
                writer.writerow(data)
    except IOError:
        print("I/O error")

while __name__ == '__main__':
    import read_write_functions 
    input = './input/data.csv'
    output = './output/report.csv'
    # raw_data1 = read_csvfile_to_memory(input)
    # print('\nprint(raw_data1)\n', raw_data1)
    raw_data2 = import_csv_with_dictreader(input)
    print('\nprint(raw_data2)\n', raw_data2)
    print(type(raw_data2))
    break