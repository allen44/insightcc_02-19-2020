import sys
sys.argv = ('', './input/data.csv', './output/report.csv' )
input = sys.argv[1]
output = sys.argv[2]

input = 'C:/Users/allen/Documents/GitHub/insightcc_02-19-2020/input/data.csv'
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
    dates = []
    measures = []
    output_list_of_dicts = []
    start_new_date_counter = 1
    start_date_index = 0
    end_date_index = 0

    for i, row in enumerate(ascending_list_of_dicts):
        print('\ngettingset of dates, i = ', i)
        # get set of dates
        # if i == 0 :
        #     start_date_index = 0
        #     dates.append(row['Date'])
        #     dates.append(['Measures'])
        if ascending_list_of_dicts[i]['Date'] == ascending_list_of_dicts[i-1]['Date']:
            print('allgood')
            # print('inside second if loop...', 'start_date_index = ', start_date_index, 'end_date_index = ', end_date_index)
        else: #ascending_list_of_dicts[i]['Date'] != ascending_list_of_dicts[i-1]['Date']:
            # date is different from previous line
            #How many lines since last date change
            end_date_index = i + 1
            lines_since_last_date_change = end_date_index - start_date_index
            # print('lines_since_last_date_change', lines_since_last_date_change)
            # get set of measures
            for subset in ascending_list_of_dicts[start_date_index:end_date_index]:
                print('get set of measures, [start_date_index:end_date_index]', start_date_index, ':', end_date_index)
                # print('ascending_list_of_dicts[start_date_index:end_date_index]', ascending_list_of_dicts[start_date_index:end_date_index])
                # measures = 
            start_date_index = i+1

    return output_list_of_dicts
                




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
    print('\n\nstarting callulate_averages function')
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
# print('\n\ndata_entries4\n', data_entries4)

data_entries5 = consolidate_measures(data_entries4)
print('\n\ndata_entries5\n', data_entries5)
