# def headers(data_entries):
#     headers = list(data_entries[0])
#     # data_entries_first_row = data_entries.pop(0)
#     print('\nprint(data_entries)\n', data_entries)
#     # print('\nprint(data_entries_first_row)\n', data_entries_first_row)
#     for i, string in enumerate(data_entries_first_row):
#         # print('print(string)', string)
#         headers[i]= string
#     # print(headers)
#     return headers

# def rows(data_entries, headers):
#     #number_of_rows = len(data_entries)
#     #number_of_data_fields = len(headers)
#     rows_list = [[]]
#     for idx, item in enumerate(data_entries):
#         #print('\ndata_entries[idx]\n', idx, '\n', data_entries[idx])
#         #print('\n', i, '\n', j, '\n', data_entries)
#         #print('\n', i, '\n', j, '\n')
#         data_entries[idx].insert(0, idx)
#         rows_list.append(item)
#         #print('\nrows_list\n', rows_list)
#     rows_list.pop(0) #remove the blank list at idx 0
#     return rows_list


# def delete_column(data_structure, column_name):
#     # deleting columns of list of lists 
#     # using pop() + list comprehension    
#     # printing original list 
#     print ("The original list is : " + str(data_structure)) 
    
#     # using pop() + list comprehension 
#     # deleting column element of row 
#     [j.pop(1) for j in data_structure] 

def delete_dict_keys(dic, unwanted_keys):
    # Remove multiple keys from dictionary 
    # Using pop() + list comprehension     
    # initializing Remove keys 
    remove_keys = unwanted_keys
    
    # printing original dictionary 
    print("The original dictionary is : " + str(dic)) 
    
    # Using pop() + list comprehension 
    # Remove multiple keys from dictionary 
    [dic.pop(key) for key in remove_keys] 
    
    # printing result  
    print("Dictionary after removal of keys : " + str(dic)) 
        
    # printing result  
    print ("The modified mesh after column deletion : " +  str(dic))
    return None

while __name__ == '__main__':
    import read_write_functions
    import pprint
    input = './input/data.csv'
    output = './output/report.csv'
    # relavent_fieldnames = {'Border', 'Date', 'Measure', 'Value'}
    headers1, data_entries1 = read_write_functions.read_csvfile_to_memory(input)
    print ('headers1', headers1)
    print('data_entries1')
    pprint.pprint(data_entries1)
    # data_entries2 = import_csv_with_dictreader(input, relavent_fieldnames)
    # print('\ndata_entries2\n')
    # pprint.pprint(data_entries2)
    # print('\nprint(data_entries2)\n', data_entries2)
    # print(type(data_entries2))    
    import parse_data
    import make_data_structure
    make_dict1 = make_data_structure.make_dict(headers1, data_entries1)
    print('\nprint(make_dict1)\n', make_dict1)
    import sort_dictionary_values
    sorted_dict1 = sort_dictionary_values.sort_dict_by_values(make_dict1)
    print('\nprint(sorted_dict1)\n', sorted_dict1)
    read_write_functions.export_csv_with_dictwriter(output, headers1, sorted_dict1)
    break
