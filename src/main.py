import sys
import csv
from read_input import read_csvfile_to_memory as read_csv

input = ''
try:
    input = sys.argv[1]
except:
    pass
    input = './input/data.csv'

output =''
try:
    output = sys.argv[2]
except:
    pass
    #output = './output/report.csv)'

while __name__ == '__main__':
    print(read_csv(input))
    break