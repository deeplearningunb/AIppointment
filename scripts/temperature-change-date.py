import csv
import time
import datetime

with open('../datasets/treated_datasets/temperatureTreated.csv',mode = 'r+') as csv_file_2:
    with open('../datasets/original_datasets/temperature.csv',mode = 'r+') as csv_file:
    
    
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(csv_file_2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        line = 0

        for row in csv_reader:
            if line == 0:
                csv_writer.writerow([row[0],row[1]])
            if line != 0:
                string = row[0]
                data = datetime.datetime.strptime(string,'%d/%m/%Y')
                csv_writer.writerow([data.date(),row[1]])
            line = line + 1
            