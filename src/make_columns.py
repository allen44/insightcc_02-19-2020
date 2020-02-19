def data_field_names(raw_data):
    data_field_names = list(range(len(raw_data[0])))
    raw_data_first_row = raw_data.pop(0)
    # print('\nprint(raw_data_first_row)\n', raw_data_first_row)
    for i, string in enumerate(raw_data_first_row):
        # print('print(string)', string)
        data_field_names[i]= string
    # print(data_field_names)
    return data_field_names

def rows(raw_data, data_field_names):
    #number_of_rows = len(raw_data)
    #number_of_data_fields = len(data_field_names)
    rows_list = [[]]
    #print('enumerate(raw_data)', enumerate(raw_data))
    for idx, item in enumerate(raw_data):
        #print('\n', i, '\n', j, '\n', raw_data)
        #print('\n', i, '\n', j, '\n')
        rows_list.append(item)
    rows_list.pop(0) #remove the blank list at idx 0
    return rows_list

while __name__ == '__main__':
    import csv
    import read_input
    raw_data1 = read_input.read_csvfile_to_memory('./input/data.csv')
    #print('\nprint(raw_data)\n', raw_data)
    #print('\nprint(raw_data[0])\n', raw_data[0])
    data_field_names1 = data_field_names(raw_data1)
    print('\nprint(data_field_names1)\n', data_field_names1)
    rows1 = rows(raw_data1, data_field_names1)
    print('\nprint(rows1)\n', rows1)
    break