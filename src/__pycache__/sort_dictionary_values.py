@@ -4,20 +4,30 @@ def sort_dict_by_values(data_dict):


while __name__ == '__main__':
    import read_write_functions 
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
    raw_data1 = read_write_functions.read_csvfile_to_memory(input)
    #print('\nprint(raw_data)\n', raw_data)
    #print('\nprint(raw_data[0])\n', raw_data[0])
    data_field_names1 = parse_data.data_field_names(raw_data1)
    print('\nprint(data_field_names1)\n', data_field_names1)
    rows1 = parse_data.rows(raw_data1, data_field_names1)
    print('\nprint(rows1)\n', rows1)
    # headers = parse_data.headers(data_entries1)
    # print('\nprint(data_field_names1)\n', data_field_names1)
    # data_entries1 = parse_data.rows(data_entries1, data_field_names1)
    # print('\nprint(data_entries1)\n', data_entries1)
    import make_data_structure
    make_dict1 = make_data_structure.make_dict(data_field_names1, rows1)
    make_dict1 = make_data_structure.make_dict(headers1, data_entries1)
    print('\nprint(make_dict1)\n', make_dict1)
    sorted_dict1 = sort_dict_by_values(make_dict1)
    import sort_dictionary_values
    sorted_dict1 = sort_dictionary_values.sort_dict_by_values(make_dict1)
    print('\nprint(sorted_dict1)\n', sorted_dict1)
    break
    read_write_functions.export_csv_with_dictwriter(output, headers1, sorted_dict1)
    break