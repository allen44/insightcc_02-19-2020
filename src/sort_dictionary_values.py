def sort_dict_by_values(data_dict):
    sorted_data_dict = sorted(data_dict, reverse = True, key = lambda i: (i['Date'], i['Value'], i['Measure'], i['Border']))
    return sorted_data_dict


while __name__ == '__main__':
    import read_write_functions 
    input = './input/data.csv'
    output = './output/report.csv'
    import parse_data
    raw_data1 = read_write_functions.read_csvfile_to_memory(input)
    #print('\nprint(raw_data)\n', raw_data)
    #print('\nprint(raw_data[0])\n', raw_data[0])
    data_field_names1 = parse_data.data_field_names(raw_data1)
    print('\nprint(data_field_names1)\n', data_field_names1)
    rows1 = parse_data.rows(raw_data1, data_field_names1)
    print('\nprint(rows1)\n', rows1)
    import make_data_structure
    make_dict1 = make_data_structure.make_dict(data_field_names1, rows1)
    print('\nprint(make_dict1)\n', make_dict1)
    sorted_dict1 = sort_dict_by_values(make_dict1)
    print('\nprint(sorted_dict1)\n', sorted_dict1)
    break