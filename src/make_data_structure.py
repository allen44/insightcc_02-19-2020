def make_dict(data_field_names, rows):
    data_structure = []
    data_field_names.insert(0, 'Row Number')
    print(rows)
    print(data_field_names)
    keys = tuple(data_field_names)
    print(keys)
    values = rows[0]
    print('\nrows[0]\n', rows[0])
    for i in range(len(rows)):
        for idx, data in enumerate(rows[i]):
            values = rows[i]
            new_dict = dict(zip(keys, values))
            data_structure.append(new_dict)
            print('\nprint(new_dict)\n', new_dict)
    return data_structure



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
    make_dict1 = make_dict(data_field_names1, rows1)
    print('\nprint(make_dict1)\n', make_dict1)
    break