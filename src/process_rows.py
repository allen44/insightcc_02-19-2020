import sys
import csv
from read_input import read_csvfile_to_memory as read_csv

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
    col_names1, row_data1, number_of_rows1 =  read_csv('./input/data.csv')
    columns1 = make_columns(col_names1, number_of_columns, number_of_rows)
    #column_data1 = process_data(col_names1, row_data1)
    print((columns1))
    break