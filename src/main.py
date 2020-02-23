import sys
sys.argv = ('', './input/data.csv', './output/report.csv' )
input = sys.argv[1]
output = sys.argv[2]

input = 'C:/Users/allen/Documents/GitHub/insightcc_02-19-2020/input/Border_Crossing_Entry_Data.csv'
output = 'C:/Users/allen/Documents/GitHub/insightcc_02-19-2020/output/data.csv'
data_entries = []
import csv

def import_csv_with_dictreader(input_filename):
    """
    Args: a string representing a filename of input csv file.
    Return: a list of ordered dicts representing column names from the top row of the csv,as the keys, and the data fields from the rest of the csvfile as the values.
    """
    values = []
    keys = []
    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="," )
        for i, row in enumerate(list(reader)):
            if i == 0:
                keys = row[None]
                #print('keys', keys)
            else:
                values.append(row[None])
                #print(i, row[None])
    data_entries = []
    for i, row in enumerate(values):
        data_entries.append(dict(zip(keys, values[i])))
       # print('\n\ndata_entries\n', i, data_entries[i])
       # print('\n\ndata_entries\n', data_entries) 
    return data_entries

def make_copy_of_data_with_only_relavent_keys(data_entries): 
    relavent_keys = ['Border', 'Date', 'Measure', 'Value']
    '''
    Removing multiple keys from dictionary by creating
    a copy of dictionary and iterating over it
    '''
    for i, row in enumerate(data_entries):
        # Create a temporary copy of dictionary
        copyOfDict = dict(row)
        # Iterate over the temporary dictionary and delete corresponding key from original dictionary
        for key in copyOfDict.keys() :
            if key not in relavent_keys:
                del data_entries[i][key]
        # print("Modified Dictionary ", i , data_entries[i])
    # print(data_entries)
    return data_entries

def sort_dict_by_date(list_of_dicts, ascending):
    """
    args: list_of_dicts is the input data table, ascending is a bool
    """
    from operator import itemgetter
    sorted_list_of_dicts = sorted(list_of_dicts, key=itemgetter('Date', 'Value', 'Measure', 'Border'))
    # print('\n\nsorted_list_of_dicts\n', ascending, '\n', sorted_list_of_dicts)
    return sorted_list_of_dicts

def add_new_column(ascending_list_of_dicts, name_of_new_key):
    """
    args: ascending_list_of_dicts is the input data table in ascending order, name_of_new_key is a string for the name of the new key
    """
    for row in ascending_list_of_dicts:
        row.update({name_of_new_key: 0})
        #print(row)
    return ascending_list_of_dicts

def consolidate_measures(ascending_list_of_dicts):
    import collections, functools, operator 
    date = ''
    measures_set = set([])
    borders_set = set([])
    output_list_of_dicts = []
    start_date_index = 0
    end_date_index = 0
    output_index = 0
    for i, row in enumerate(ascending_list_of_dicts):
        # print('top of outer for loop 0')
        # output_list_of_dicts.append(ascending_list_of_dicts[i])
        # print('\ngettingset of dates, i = ', i, ' Date = ', row['Date'])
        # get set of dates
        if i == 0 :
            start_date_index = 0
            date = row['Date']
        elif ascending_list_of_dicts[i]['Date'] == ascending_list_of_dicts[i-1]['Date']:
            pass
            # print('allgood', 'i =', i, row['Date'], start_date_index)
            #print('inside second if loop...', 'start_date_index = ', start_date_index, 'end_date_index = ', end_date_index)
        else: #ascending_list_of_dicts[i]['Date'] != ascending_list_of_dicts[i-1]['Date'],   # date is different from previous line
            end_date_index = i
            date = row['Date']
            # get set of measures
            for j, d in enumerate(ascending_list_of_dicts[start_date_index:end_date_index]):
                # print('get set of measures, [start_date_index:end_date_index]', start_date_index, ':', end_date_index)
                # print('ascending_list_of_dicts[start_date_index:end_date_index]', ascending_list_of_dicts[start_date_index:end_date_index])
                measures_set.add(ascending_list_of_dicts[j]['Measure'])
            print('found Measures: ', measures_set)
            # get set of borders
            for j, d in enumerate(ascending_list_of_dicts[start_date_index:end_date_index]):
                # print('get set of borders, [start_date_index:end_date_index]', start_date_index, ':', end_date_index)
                # print('ascending_list_of_dicts[start_date_index:end_date_index]', ascending_list_of_dicts[start_date_index:end_date_index])
                borders_set.add(ascending_list_of_dicts[j]['Border'])
            print('found Borders: ', borders_set, '[start_date_index:end_date_index]', start_date_index, ':', end_date_index)
            #make new keys for dicts
            # print('range(start_date_index, end_date_index)', range(start_date_index, end_date_index))
            # print('start_date_index', start_date_index, type(start_date_index))
            # print('end_date_index', end_date_index, type(end_date_index))
            for j in range(start_date_index, end_date_index): #range where dates are same
                # change sets to lists
                measures = list(measures_set)
                borders = list(borders_set)
                # print('top of inner for loop')
                # print(start_date_index, type(start_date_index))
                # print(end_date_index, type(end_date_index))
                #initialize a 2x2 list for border and measure sums
                matrix_of_sums = [[0 for item in range(0, len(measures))] for item in range(0, len(borders))]
                print(matrix_of_sums)
                dicts_with_same_date = ascending_list_of_dicts[start_date_index: end_date_index]
                date_subset_dict = dicts_with_same_date
                print('len dicts_with_same_date: ' ,len(dicts_with_same_date))
                print(start_date_index, end_date_index)
                print(type(date_subset_dict))
                for line in date_subset_dict:
                    line.update({str(line.get('Date')+line.get('Border')+line.get('Measure')+' Value') : 0})#create a new dictionary key
                    # print('New k:v pair: ' , {str(line.get('Date')+line.get('Border')+line.get('Measure')+'Value') : 0})
                    # print(line)
                result = {}
                for d in date_subset_dict: 
                    d[key] = result.get(k, 0) + d[k]
                output_line = dict([['Date', row['Date']], ['Border', border] , ['Measure', measure], ['Value' , 0]])
                output_list_of_dicts.append(output_line)
                # for i,border in enumerate(borders):        #for dicts with the same data and border
                #     for j, measure in enumerate(measures):   #for dicts with the same date, border and measure
                #         #create a new dictionary key
                #         # print('measure =' , measure)            
                #         # print(range(start_date_index,end_date_index))
                #         # print('i = ', i ,  "Date: ", ascending_list_of_dicts[i-1]['Date'], 'Border :', border, 'Measure: ' , measure)
                        # sum the values with same keys 
                        # output_list_of_dicts[output_index] = dict( 'Date' = row['Date'], 'Border' = border , 'Measure' =  measure, 'Value' = v, 'Average' = a)
                    # print('border = , ', border)
                    # for measure in list(measures):
                    #     pass
                        # print('measure =' , measure)            
                        # print(range(start_date_index,end_date_index )   
            start_date_index = i
        measures_set.clear()
        borders_set.clear()
        # print('start_date_index =', start_date_index, type(start_date_index))
        # print('end_date_index =', end_date_index, type(end_date_index))
    # print('measures = ',set(measures))
    # print('borders =', set(borders))

    return output_list_of_dicts
                
def parse_subsets_with_same_value(input_table, input_key):
    """
    Given an ascending-sorted input_table and a key (from a key:value pair), returns a lists of subsets of the input_table where all rows have the same value for a given key.
    Parameters:
    input_table: type is list of dictionaries.
    input_key: type is string.
    Return:
    table_subset: type is a list of a list of dictionaries. 
    """
    table_subset_list = []
    input_value_set = set([])
    start_slice_index_list = []
    end_slice_index_list = []
    # sort input_table by key / input unit check to ensure that only only ascending sorted tables are used
    from operator import itemgetter
    input_table = sorted(input_table, key=itemgetter(input_key))
    #Parse_subsets_with_same_value using the unit-checked input
    table_length = len(input_table)
    for i, row in enumerate(input_table):
        if i == 0:
            start_slice_index_list.append(i)
            input_key_set = row[input_key]
        elif input_table[i][input_key] == input_table[i-1][input_key]: # value is same as previous line
            if i == (table_length - 1): #final row in table
                print('reached final row in table, final line is same as previous line')
                end_slice_index_list.append(i + 1)
                input_value_set.add(input_table[i][input_key])
        else: #input_table[i][input_key] == input_table[i-1][input_key]:,   # value is different from previous line
            print('value is different from previous line')
            end_slice_index_list.append(i)
            input_value_set.add(input_table[i-1][input_key])
            start_slice_index_list.append(i)
            if i == (table_length - 1): #final row in table
                print('reached final row in table, final line is different from previous as previous line')
                end_slice_index_list.append(i + 1)
                input_value_set.add(input_table[i][input_key])

    input_value_list = sorted(list(input_value_set))

    print('number of items in list = ', i+1)
    print('\ntable_subset_list\n', table_subset_list)
    print('\ninput_value_list = \n', input_value_list)
    print('\nstart_slice_index_list\n', start_slice_index_list)
    print('\nend_slice_index_list\n', end_slice_index_list)

    output_table = []
    for i, value in enumerate(input_value_list):
        output_table.append(input_table[start_slice_index_list[i] : end_slice_index_list[i]]) 
    return output_table



    #     dates.append(row.date)
    # for i, row in enumerate(ascending_list_of_dicts):
    #     if dates ==  []:
    #         dates[i] = row['Date']
    #     elif True:
    #         dates = row['Date']
    # #         measures = row['Measure']
    #         print('\ndates', dates)
    #         print('measures', measures)

def calulate_averages(ascending_list_of_dicts):
    print('\n\nstarting calculate_averages function')
    for row_num, row in enumerate(ascending_list_of_dicts):
        # for 
        print(row_num, row)
    return ascending_list_of_dicts
        # if row[]

data_entries1 = import_csv_with_dictreader(input)

#print('\n\ndata_entries1\n', data_entries1) 

data_entries2 = make_copy_of_data_with_only_relavent_keys(data_entries1)
# print('\n\ndata_entries2\n', data_entries2)
#remove_unecessary_keys(data_entries1)

#print(data_entries1)

data_entries3 = sort_dict_by_date(data_entries2, True)
#print('\n\ndata_entries3\n', data_entries3)

data_entries4 = add_new_column(data_entries3, 'Average')
# for i, row in enumerate(data_entries4):
    # print('\ndata_entries4\n', i, row.values())

# data_entries5 = consolidate_measures(data_entries4)
# print('\n\ndata_entries5\n', data_entries5)

# print(type(data_entries4))
# print(type(data_entries4[0]))
import pprint
subsets_with_same_date = parse_subsets_with_same_value(data_entries4, 'Date')

# print(type(subsets_with_same_date))
# print(type(subsets_with_same_date[0]))
# print(type(subsets_with_same_date[0][0]))

subsets_with_same_border = []
for same_date_subset in subsets_with_same_date:
    subsets_with_same_border.append(parse_subsets_with_same_value(same_date_subset, 'Border'))

print(type(subsets_with_same_border))
print(type(subsets_with_same_border[0]))
print(type(subsets_with_same_border[0][0]))
print(type(subsets_with_same_border[0][0][0]))

print('subsets_with_same_date, stats')
print('len(subsets_with_same_date))', len(subsets_with_same_date))
print('len(subsets_with_same_date[0]))', len(subsets_with_same_date[0]))
print('len(subsets_with_same_date[1]))', len(subsets_with_same_date[1]))
print('len(subsets_with_same_date[2]))', len(subsets_with_same_date[2]))

print('subsets_with_same_border, stats')
print('len(subsets_with_same_border))', len(subsets_with_same_border))
print('len(subsets_with_same_border[0]))', len(subsets_with_same_border[0]))
print('len(subsets_with_same_border[1]))', len(subsets_with_same_border[1]))
print('len(subsets_with_same_border[2]))', len(subsets_with_same_border[2]))
print('len(subsets_with_same_border[0][0]))', len(subsets_with_same_border[0][0]))
print('len(subsets_with_same_border[0][1]))', len(subsets_with_same_border[0][1]))
print('len(subsets_with_same_border[1][0]))', len(subsets_with_same_border[1][0]))
print('len(subsets_with_same_border[1][1]))', len(subsets_with_same_border[1][1]))
print('len(subsets_with_same_border[2][0]))', len(subsets_with_same_border[2][0]))
print('len(subsets_with_same_border[2][1]))', len(subsets_with_same_border[2][1]))