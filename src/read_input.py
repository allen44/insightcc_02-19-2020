import csv

def read_csvfile_to_memory(input_filename):
    """
    Args: a string representing a filename of csv file.
    Return: a list of strings representing column names from the top row of the csv, and the data fields from the rest of the csvfile.
    """
    raw_data = []
    with open(input_filename, 'r',) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in (reader):
                raw_data.append(row)
    return(raw_data)
    

while __name__ == '__main__':
    raw_data = read_csvfile_to_memory('./input/data.csv')
    print(raw_data)
    break