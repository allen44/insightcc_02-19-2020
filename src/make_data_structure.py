def make_dict(headers, data_entries):
    data_structure = []
    # headers.insert(0, 'Row Number')
    print(data_entries)
    print(headers)
    keys = tuple(headers)
    print(keys)
    values = data_entries[0]
    print('\data_entries[0]\n', data_entries[0])
    for i in range(len(data_entries)):
        values = data_entries[i]
        new_dict = dict(zip(keys, values))
        data_structure.append(new_dict)
        print('\nprint(new_dict)\n', new_dict)
    return data_structure

while __name__ == '__main__':
    import read_write_functions
    import pprint
    input = './input/data.csv'
    output = './output/report.csv'
    # relavent_fieldnames = {'Border', 'Date', 'Measure', 'Value'}
    headers1, data_entries1 = read_write_functions.read_csvfile_to_memory(input)
    print ('headers1', headers1)
    print('data_entries1')
    pprint.pprint(data_entries1)
    # data_entries2 = import_csv_with_dictreader(input, relavent_fieldnames)
    # print('\ndata_entries2\n')
    # pprint.pprint(data_entries2)
    # print('\nprint(data_entries2)\n', data_entries2)
    # print(type(data_entries2))    
    import parse_data
    import make_data_structure
    make_dict1 = make_data_structure.make_dict(headers1, data_entries1)
    print('\nprint(make_dict1)\n', make_dict1)
    import sort_dictionary_values
    sorted_dict1 = sort_dictionary_values.sort_dict_by_values(make_dict1)
    print('\nprint(sorted_dict1)\n', sorted_dict1)
    read_write_functions.export_csv_with_dictwriter(output, headers1, sorted_dict1)
    break
