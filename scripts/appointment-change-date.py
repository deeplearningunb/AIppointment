import csv
import time
import datetime

with open('../datasets/treated_datasets/appointmentTreated.csv',mode = 'r+') as csv_file_2:
    with open('../datasets/original_datasets/appointment.csv',mode = 'r+') as csv_file:
    
    
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(csv_file_2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        line = 0

        for row in csv_reader:
            if line == 0:
                csv_writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]])
            else:
                csv_writer.writerow([row[0],row[1],row[2][:10],row[3][:10],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]])
            line = line + 1
        


            



