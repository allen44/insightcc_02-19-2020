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
                print(start_date_index, end_date_index)
                print('len dicts_with_same_date: ' ,len(dicts_with_same_date))
                for line in dicts_with_same_date:
                    line.update({str(line.get('Date')+line.get('Border')+line.get('Measure')+'Value') : 0})#create a new dictionary key
                    print('New k:v pair: ' , {str(line.get('Date')+line.get('Border')+line.get('Measure')+'Value') : 0})
                for i,border in enumerate(borders):        #for dicts with the same data and border
                    for j, measure in enumerate(measures):   #for dicts with the same date, border and measure
                        #create a new dictionary key
                        dicts_with_same_date 
                        # print('measure =' , measure)            
                        # print(range(start_date_index,end_date_index))
                        # print('i = ', i ,  "Date: ", ascending_list_of_dicts[i-1]['Date'], 'Border :', border, 'Measure: ' , measure)
                        # sum the values with same keys 
                        result = copy()
                        for d in dicts_with_same_date: 
                            d[key] = result.get(k, 0) + d[k]
                        output_line = dict([['Date', row['Date']], ['Border', border] , ['Measure', measure], ['Value' , 0]])
                        output_list_of_dicts.append(output_line)
                        # output_list_of_dicts[output_index] = dict( 'Date' = row['Date'], 'Border' = border , 'Measure' =  measure, 'Value' = v, 'Average' = a)
                    # print('border = , ', border)
                    for measure in list(measures):
                        pass
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

data_entries5 = consolidate_measures(data_entries4)
# print('\n\ndata_entries5\n', data_entries5)

