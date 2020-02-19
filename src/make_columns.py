def data_field_names(raw_data):
    data_field_names = list(range(len(raw_data[0])))
    raw_data_first_row = raw_data.pop(0)
    print('\nprint(raw_data)\n', raw_data)
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
    for idx, item in enumerate(raw_data):
        #print('\nraw_data[idx]\n', idx, '\n', raw_data[idx])
        #print('\n', i, '\n', j, '\n', raw_data)
        #print('\n', i, '\n', j, '\n')
        raw_data[idx].insert(0, idx)
        rows_list.append(item)
        #print('\nrows_list\n', rows_list)
    rows_list.pop(0) #remove the blank list at idx 0
    return rows_list

while __name__ == '__main__':
    import read_input 
    input = './input/data.csv'
    output = './output/report.csv)'
    import make_columns
    raw_data1 = read_input.read_csvfile_to_memory(input)
    print('\nprint(raw_data1)\n', raw_data1)
    #print('\nprint(raw_data)\n', raw_data)
    #print('\nprint(raw_data[0])\n', raw_data[0])
    data_field_names1 = data_field_names(raw_data1)
    print('\nprint(data_field_names1)\n', data_field_names1)
    rows1 = rows(raw_data1, data_field_names1)
    print('\nprint(rows1)\n', rows1)
    break