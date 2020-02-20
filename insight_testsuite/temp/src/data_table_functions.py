import collections
import pprint


def sort_dict_by_values(data_table):
    sorted_data_dict = sorted(data_table, reverse = True, key = lambda i: (i['Date'], i['Value'], i['Measure'], i['Border']))
    return sorted_data_dict

def sort_dict_by_values_ascending(data_table):
    sorted_data_dict_ascending = sorted(data_table, reverse = False, key = lambda i: (i['Date'], i['Value'], i['Measure'], i['Border']))
    return sorted_data_dict_ascending

def get_set_of_all_values_for_keys(any_data_table, key_list):
    all_values_for_key = [{}]
        # Using list comprehension 
        # Get values of particular key in list of dictionaries 
    for i, item in enumerate(key_list):
        all_values_for_key =  ( d[i] for d in any_data_table )
    print(all_values_for_key)
    return all_values_for_key

def running_sum_for_same_column(sorted_data_table_ascending, column_name, index_start, index_end, increment):
    """
    args: data_table is a list of dicts, column_name is a string
    return: 
    """
    print ("\n\ninitial dictionary", str(sorted_data_table_ascending)) 
    for row in sorted_data_table_ascending:
        #print('\nrow\n', row)
        if column_name in row.keys():
            print('\ncolumn_name', column_name)
            print('\nrow.keys()', row.keys())
            print('column_name.value()\n', row[column_name])
            print(f'The original dictionary is :  {row}') 
            # Using list() + keys() + index() 
            # Key index in Dictionary 
            res = list(row.keys()).index('Value') 
            # printing result  
            print("Index of search key is : " + str(res))
            row.update({column_name, Value})
                # sum the values with same keys 
                # counter = collections.Counter() 
                # for d in sorted_data_table:
                #     print("\ninitial(2) dictionary", str(sorted_data_table))   
                #     counter.update(d) 
                #     print ("\ninitial(3) dictionary", str(sorted_data_table)) 
                # augmented_sorted_data_table = dict(counter) 
                
                # print("\nresultant dictionary : ", str(augmented_sorted_data_table)) 
                #Sum the total number of crossings (Value) of each type of vehicle or equipment,
                #  or passengers or pedestrians, that crossed the border that month, regardless of what port was used.
                #


# def new_column_maker(data_table):
#     set_of_measures = {'Truck Containers Full', 'Trains', 'Pedestrians', 'Truck Containers Empty',}
#     for row in sorted_data_table:
#         if (US-Canada Border and ) in row.values():
#             row.update((new_key, ))


while __name__ == '__main__':
    import read_write_functions
    import pprint
    input = './input/data.csv'
    output = './output/report.csv'
    key_list1 = ['Border', 'Date', 'Measure']
    # relavent_fieldnames = {'Border', 'Date', 'Measure', 'Value'}
    headers1, data_entries1 = read_write_functions.import_csv_with_dictreader(input)
    #headers1, data_entries1 = read_csvfile_to_memory(input)
    print ('headers1', headers1)
    print('data_entries1')
    pprint.pprint(data_entries1)
    # data_entries2 = import_csv_with_dictreader(input, relavent_fieldnames)
    # print('\ndata_entries2\n')
    # pprint.pprint(data_entries2)
    # print('\nprint(data_entries2)\n', data_entries2)
    # print(type(data_entries2))    
    import parse_data
    # headers = parse_data.headers(data_entries1)
    # print('\nprint(data_field_names1)\n', data_field_names1)
    # data_entries1 = parse_data.rows(data_entries1, data_field_names1)
    # print('\nprint(data_entries1)\n', data_entries1)
    import make_data_structure
    import data_table_functions
    sorted_dict_ascending1 = data_table_functions.sort_dict_by_values_ascending(data_entries1)
    read_write_functions.export_csv_with_dictwriter(output, headers1, sorted_dict_ascending1)
    all_values_for_key_list1 = get_set_of_all_values_for_keys(sorted_dict_ascending1, key_list1)
    print(all_values_for_key_list1)
    running_sum_for_same_column(sorted_dict_ascending1, 'Measure', len(sorted_dict_ascending1), 0, -1)
    read_write_functions.export_csv_with_dictwriter('./output/report2.csv', headers1, sorted_dict1)
    break
