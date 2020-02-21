from read_input import read_csvfile_to_memory

def make_columns(col_names, number_of_columns, number_of_rows):
    columns = list(range(number_of_columns), range(number_of_rows) )
    for col_number in columns:
        columns
    for i in col_names:
        columns = col_names[i]
    return columns
    
# def process_data(col_names, row_data):
#     column_data =[
#         for col_idx, row_data in enumerate(row_data):
#         column_data.append(row_data[col_idx])
#         for row_idx, col_names in enumerate(col_names):
#             column_data.append(row_data[row_idx])
#             print(type(row_data[row_idx]))
#             print((row_data[row_idx]))
#     return column_data




while __name__ == '__main__':
    import read_input
    raw_data1 = read_input.read_csvfile_to_memory('./input/data.csv')
    #print('\nprint(raw_data)\n', raw_data)
    #print('\nprint(raw_data[0])\n', raw_data[0])
    data_field_names1 = data_field_names(raw_data1)
    print('\nprint(data_field_names1)\n', data_field_names1)
    rows1 = rows(raw_data1, data_field_names1)
    print('\nprint(rows1)\n', rows1)
    break