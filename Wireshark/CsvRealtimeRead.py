import csv
import os
import sys

filename = sys.argv[1]
print(filename)
packets_list = []
path = 'data_testcsv/' + filename

with open(path, newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        packets_list.append(row)

print(len(packets_list))