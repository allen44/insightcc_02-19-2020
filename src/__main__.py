import csv 

while __name__ == '__main__':
    with open('./input/data.csv', 'r',) as file:
        reader = csv.reader(file, )
        for row in reader:
            print(row)
   
    break