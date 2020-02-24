# def make_dict(headers, data_entries):
#     data_structure = []
#     # headers.insert(0, 'Row Number')
#     print(data_entries)
#     print(headers)
#     keys = tuple(headers)
#     print(keys)
#     values = data_entries[0]
#     print('\data_entries[0]\n', data_entries[0])
#     for i in range(len(data_entries)):
#         values = data_entries[i]
#         new_dict = dict(zip(keys, values))
#         data_structure.append(new_dict)
#         print('\nprint(new_dict)\n', new_dict)
#     return data_structure

# def consolidate_measures(ascending_list_of_dicts):
#     import collections, functools, operator 
#     date = ''
#     measures_set = set([])
#     borders_set = set([])
#     output_list_of_dicts = []
#     start_date_index = 0
#     end_date_index = 0
#     output_index = 0
#     for i, row in enumerate(ascending_list_of_dicts):
#         # print('top of outer for loop 0')
#         # output_list_of_dicts.append(ascending_list_of_dicts[i])
#         # print('\ngettingset of dates, i = ', i, ' Date = ', row['Date'])
#         # get set of dates
#         if i == 0 :
#             start_date_index = 0
#             date = row['Date']
#         elif ascending_list_of_dicts[i]['Date'] == ascending_list_of_dicts[i-1]['Date']:
#             pass
#             # print('allgood', 'i =', i, row['Date'], start_date_index)
#             #print('inside second if loop...', 'start_date_index = ', start_date_index, 'end_date_index = ', end_date_index)
#         else: #ascending_list_of_dicts[i]['Date'] != ascending_list_of_dicts[i-1]['Date'],   # date is different from previous line
#             end_date_index = i
#             date = row['Date']
#             # get set of measures
#             for j, d in enumerate(ascending_list_of_dicts[start_date_index:end_date_index]):
#                 # print('get set of measures, [start_date_index:end_date_index]', start_date_index, ':', end_date_index)
#                 # print('ascending_list_of_dicts[start_date_index:end_date_index]', ascending_list_of_dicts[start_date_index:end_date_index])
#                 measures_set.add(ascending_list_of_dicts[j]['Measure'])
#             print('found Measures: ', measures_set)
#             # get set of borders
#             for j, d in enumerate(ascending_list_of_dicts[start_date_index:end_date_index]):
#                 # print('get set of borders, [start_date_index:end_date_index]', start_date_index, ':', end_date_index)
#                 # print('ascending_list_of_dicts[start_date_index:end_date_index]', ascending_list_of_dicts[start_date_index:end_date_index])
#                 borders_set.add(ascending_list_of_dicts[j]['Border'])
#             print('found Borders: ', borders_set, '[start_date_index:end_date_index]', start_date_index, ':', end_date_index)
#             #make new keys for dicts
#             # print('range(start_date_index, end_date_index)', range(start_date_index, end_date_index))
#             # print('start_date_index', start_date_index, type(start_date_index))
#             # print('end_date_index', end_date_index, type(end_date_index))
#             for j in range(start_date_index, end_date_index): #range where dates are same
#                 # change sets to lists
#                 measures = list(measures_set)
#                 borders = list(borders_set)
#                 # print('top of inner for loop')
#                 # print(start_date_index, type(start_date_index))
#                 # print(end_date_index, type(end_date_index))
#                 #initialize a 2x2 list for border and measure sums
#                 matrix_of_sums = [[0 for item in range(0, len(measures))] for item in range(0, len(borders))]
#                 print(matrix_of_sums)
#                 dicts_with_same_date = ascending_list_of_dicts[start_date_index: end_date_index]
#                 date_subset_dict = dicts_with_same_date
#                 print('len dicts_with_same_date: ' ,len(dicts_with_same_date))
#                 print(start_date_index, end_date_index)
#                 print(type(date_subset_dict))
#                 for line in date_subset_dict:
#                     line.update({str(line.get('Date')+line.get('Border')+line.get('Measure')+' Value') : 0})#create a new dictionary key
#                     # print('New k:v pair: ' , {str(line.get('Date')+line.get('Border')+line.get('Measure')+'Value') : 0})
#                     # print(line)
#                 result = {}
#                 for d in date_subset_dict: 
#                     d[key] = result.get(k, 0) + d[k]
#                 output_line = dict([['Date', row['Date']], ['Border', border] , ['Measure', measure], ['Value' , 0]])
#                 output_list_of_dicts.append(output_line)
#                 # for i,border in enumerate(borders):        #for dicts with the same data and border
#                 #     for j, measure in enumerate(measures):   #for dicts with the same date, border and measure
#                 #         #create a new dictionary key
#                 #         # print('measure =' , measure)            
#                 #         # print(range(start_date_index,end_date_index))
#                 #         # print('i = ', i ,  "Date: ", ascending_list_of_dicts[i-1]['Date'], 'Border :', border, 'Measure: ' , measure)
#                         # sum the values with same keys 
#                         # output_list_of_dicts[output_index] = dict( 'Date' = row['Date'], 'Border' = border , 'Measure' =  measure, 'Value' = v, 'Average' = a)
#                     # print('border = , ', border)
#                     # for measure in list(measures):
#                     #     pass
#                         # print('measure =' , measure)            
#                         # print(range(start_date_index,end_date_index )   
#             start_date_index = i
#         measures_set.clear()
#         borders_set.clear()
#         # print('start_date_index =', start_date_index, type(start_date_index))
#         # print('end_date_index =', end_date_index, type(end_date_index))
#     # print('measures = ',set(measures))
#     # print('borders =', set(borders))

#     return output_list_of_dicts

# while __name__ == '__main__':
#     import read_write_functions
#     import pprint
#     input = './input/data.csv'
#     output = './output/report.csv'
#     # relavent_fieldnames = {'Border', 'Date', 'Measure', 'Value'}
#     headers1, data_entries1 = read_write_functions.read_csvfile_to_memory(input)
#     print ('headers1', headers1)
#     print('data_entries1')
#     pprint.pprint(data_entries1)
#     # data_entries2 = import_csv_with_dictreader(input, relavent_fieldnames)
#     # print('\ndata_entries2\n')
#     # pprint.pprint(data_entries2)
#     # print('\nprint(data_entries2)\n', data_entries2)
#     # print(type(data_entries2))    
#     import parse_data
#     import make_data_structure
#     make_dict1 = make_data_structure.make_dict(headers1, data_entries1)
#     print('\nprint(make_dict1)\n', make_dict1)
#     import sort_dictionary_values
#     sorted_dict1 = sort_dictionary_values.sort_dict_by_values(make_dict1)
#     print('\nprint(sorted_dict1)\n', sorted_dict1)
#     read_write_functions.export_csv_with_dictwriter(output, headers1, sorted_dict1)
#     break
