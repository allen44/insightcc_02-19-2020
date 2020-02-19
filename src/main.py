import sys
import read_input 
import make_columns

sys.argv = ('', './input/data.csv', './output/report.csv' )
input = sys.argv[1]
output = sys.argv[2]

while __name__ == '__main__':
    import read_input 
    input = './input/data2.csv'
    output = './output/report.csv)'
    import make_columns
    raw_data1 = read_input.read_csvfile_to_memory(input)
    #print('\nprint(raw_data)\n', raw_data)
    #print('\nprint(raw_data[0])\n', raw_data[0])
    data_field_names1 = make_columns.data_field_names(raw_data1)
    print('\nprint(data_field_names1)\n', data_field_names1)
    rows1 = make_columns.rows(raw_data1, data_field_names1)
    print('\nprint(rows1)\n', rows1)
    break