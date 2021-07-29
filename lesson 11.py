#csv

import csv

data = [[1,2,3],[4,5,6],[7,8,9]]

def write_to_csv(filename, data):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

def read_from_csv(fileneme):
    with open(fileneme, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
            return data


filename = 'data.csv'
# data_2 = [[1,2,3],[4,5,6],[7,8,9], [12,13,14]]
# write_to_csv(data=data_2, filename=filename)
# write_to_csv(filename,delimiter=';', data_2=data_2)

new_data = read_from_csv(filename)