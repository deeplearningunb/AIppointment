import csv
import time
import datetime

def searchTemperatureByDate(date):
    with open('../datasets/treated_datasets/temperatureTreated.csv',mode = 'r+') as temperatura_csv:
    
        temperature_reader = csv.reader(temperatura_csv, delimiter=',')

        for row in temperature_reader:
            if row[0] == date:
                return row[1]



with open('../datasets/treated_datasets/appointmentTreated.csv',mode = 'r+') as appointment_csv:
    with open('../datasets/final_datasets/appointment_and_temperature.csv',mode = 'r+') as appointment_and_temperature_csv:


        appointment_reader = csv.reader(appointment_csv, delimiter=',')
        writer = csv.writer(appointment_and_temperature_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        line = 0

        for row in appointment_reader:
            if line == 0:
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],"Temperature"])
            if line != 0:
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],searchTemperatureByDate(row[3])])
            print(line)
            print('\n')
            line = line + 1