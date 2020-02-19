import sys
import read_write_functions 
import parse_data
import make_data_structure
import sort_dictionary_values

sys.argv = ('', './input/data.csv', './output/report.csv' )
input = sys.argv[1]
output = sys.argv[2]

while __name__ == '__main__':
    import read_write_functions 
    input = './input/data.csv'
    output = './output/report.csv'
    import parse_data
    # raw_data1 = read_write_functions.read_csvfile_to_memory(input)
    # #print('\nprint(raw_data)\n', raw_data)
    # #print('\nprint(raw_data[0])\n', raw_data[0])
    # data_field_names1 = parse_data.data_field_names(raw_data1)
    # print('\nprint(data_field_names1)\n', data_field_names1)
    # rows1 = parse_data.rows(raw_data1, data_field_names1)
    # print('\nprint(rows1)\n', rows1)
    # break
    raw_data2 = read_write_functions.import_csv_with_dictreader(input)
    print('\nprint(raw_data2)\n', raw_data2)
    # print(type(raw_data2))
    break