import sys
import read_write_functions 
import parse_data
import make_data_structure
import data_table_functions

sys.argv = ('', './input/data.csv', './output/report.csv' )
input = sys.argv[1]
output = sys.argv[2]

while __name__ == '__main__':
    input = './input/data.csv'
    output = './output/report.csv'
    import parse_data
    headers1, data_entries1 = read_write_functions.import_csv_with_dictreader(input)
    # data_entries1 = read_write_functions.read_csvfile_to_memory(input)
    # #print('\nprint(data_entries)\n', data_entries)
    # #print('\nprint(data_entries[0])\n', data_entries[0])
    # data_field_names1 = parse_data.data_field_names(data_entries1)
    # print('\nprint(data_field_names1)\n', data_field_names1)
    # data_entries1 = parse_data.rows(data_entries1, data_field_names1)
    # print('\nprint(data_entries1)\n', data_entries1)
    # break
    sorted_dict_ascending1 = data_table_functions.sort_dict_by_values_ascending(data_entries1)
    print('\nprint(sorted_dict_ascending1)\n', sorted_dict_ascending1)
    read_write_functions.export_csv_with_dictwriter(output, headers1, sorted_dict_ascending1)
    break
