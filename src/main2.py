# import sys
# import read_write_functions 
# import parse_data
# import make_data_structure
# import sort_dictionary_values

# sys.argv = ('', './input/data.csv', './output/report.csv' )
# input = sys.argv[1]
# output = sys.argv[2]

# while __name__ == '__main__':
#     import read_write_functions 
#     input = './input/data.csv'
#     output = './output/report.csv'
#     import parse_data
#     headers1, data_entries1 = read_write_functions.read_csvfile_to_memory(input)
#     # #print('\nprint(data_entries)\n', data_entries)
#     # #print('\nprint(data_entries[0])\n', data_entries[0])
#     # data_field_names1 = parse_data.data_field_names(data_entries1)
#     # print('\nprint(data_field_names1)\n', data_field_names1)
#     # data_entries1 = parse_data.rows(data_entries1, data_field_names1)
#     # print('\nprint(data_entries1)\n', data_entries1)
#     # break
#     import make_data_structure
#     make_dict1 = make_data_structure.make_dict(headers1, data_entries1)
#     print('\nprint(make_dict1)\n', make_dict1)
#     import sort_dictionary_values
#     sorted_dict1 = sort_dictionary_values.sort_dict_by_values(make_dict1)
#     print('\nprint(sorted_dict1)\n', sorted_dict1)
#     export_csv_with_dictwriter(output, headers1, sorted_dict1)
#     break
