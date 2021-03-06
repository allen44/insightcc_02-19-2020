import csv


def read_csvfile_to_memory(input_filename):
    """
    Args: a string representing a filename of csv file.
    Return: a list of strings representing column names from the top row of the csv, and the data fields from the rest of the csvfile.
    """
    data_entries = []
    headers = []
    with open(input_filename, 'r',) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data_entries.append(row)
    headers = data_entries.pop(0) 
    print(headers)
    print(data_entries)
    return(headers, data_entries)
    
# def write_memory_to_csvfile(output_filename, data_entries):
#     """
#     Args: a string representing a filename of output csv file.
#     """
#     data_entries = []
#     with open(output_filename, 'w',) as csvfile:
#         writer = csv.writer(csvfile, delimiter=',')
#         for row in writer:
#                 writer.writerow(row)
#     return None

# def import_csv_with_dictreader(input_filename, relavent_fieldnames):
#     """
#     Args: a string representing a filename of input csv file.
#     Return: a list of ordered dicts representing column names from the top row of the csv,as the keys, and the data fields from the rest of the csvfile as the values.
#     """
#     data_entries = []
#     reader = csv.DictReader(open(input_filename))
#     for row in (reader):
#         keys = (row.items())
#         print(keys)
#         print('\nrow\n', row)
#         print('items', list(keys))
#     #print('\nfieldnames\n',type(fieldnames))
#     #print('\nfieldnames\n',fieldnames)
#     return data_entries
    
def export_csv_with_dictwriter(output_filename, headers, sorted_dict):
    """
    Args: a string representing a filename of input csv file.
    Return: a list of  dicts representing column names from the top row of the csv,as the keys, and the data fields from the rest of the csvfile as the values.
    """
    try:
        with open(output_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for data in sorted_dict:
                writer.writerow(data)
            print("Success. Export to csv complete")
    except IOError:
        print("I/O error")

while __name__ == '__main__':
    import read_write_functions
    import pprint
    input = './input/data.csv'
    output = './output/report.csv'
    # relavent_fieldnames = {'Border', 'Date', 'Measure', 'Value'}
    headers1, data_entries1 = read_csvfile_to_memory(input)
    print ('headers1', headers1)
    print('data_entries1')
    pprint.pprint(data_entries1)
    # data_entries2 = import_csv_with_dictreader(input, relavent_fieldnames)
    # print('\ndata_entries2\n')
    # pprint.pprint(data_entries2)
    # print('\nprint(data_entries2)\n', data_entries2)
    # print(type(data_entries2))    
    import parse_data
    # headers = parse_data.headers(data_entries1)
    # print('\nprint(data_field_names1)\n', data_field_names1)
    # data_entries1 = parse_data.rows(data_entries1, data_field_names1)
    # print('\nprint(data_entries1)\n', data_entries1)
    import make_data_structure
    make_dict1 = make_data_structure.make_dict(headers1, data_entries1)
    print('\nprint(make_dict1)\n', make_dict1)
    import sort_dictionary_values
    sorted_dict1 = sort_dictionary_values.sort_dict_by_values(make_dict1)
    print('\nprint(sorted_dict1)\n', sorted_dict1)
    export_csv_with_dictwriter(output, headers1, sorted_dict1)
    break
