"""
"""
from datetime import timedelta, datetime
import xlsxwriter
import csv
import pandas as pd
NewList = {}
FinalList = {}
DeclinedList = {}
WaitingList = {}

def editApplication():
    humanInput = input('\n'.join([ 'Which year is the camp (20XX)', '']))
    fileName = humanInput + '.csv'
    with open(fileName) as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:
            key = row[0]
            NewList[key] = row[1:]
            print(NewList[key])
    print('List loaded')
    for key in NewList:
        if NewList[key][10] == 'awaiting directors call':
            print('')
            print('Applicant: ')
            print(NewList[key][0], NewList[key][1])
            NewStatus = input ('\n'.join(['A: Accepted', 'D: Declined', 'W: Waitinglist', '']))
            while NewStatus not in ['D','d','A','a','W','w']:
                print ('Invalid input! ')
                NewStatus = input ('Accepted, Declined or waitinglist (A, D or W): ')
            NewList[key][10] = NewStatus
            if NewStatus == 'D' or NewStatus == 'd':
                DeclinedList[key] = NewList[key]
                continue
            elif NewStatus in ['W','w']:
                Talent = input ('Enter Talent (1-4): ')
                while Talent not in ['1','2','3','4']:
                    print('Invalid Input! ')
                    Talent = input ('Enter Talent (1-4): ')
                Instrument = input ('\n'.join(['enter instrument: ', 'S = Singer', 'G = Guitarist', 'D = Drummer', 'B = Bassist','K = Keyboardist', 'I = Instrumentalist', '']))
                while Instrument not in ['S','s','G','g','D','d','B','b','K','k','I','i']:
                    print ('Invalid Input!')
                    Instrument = input ('\n'.join(['enter instrument: ', 'S = Singer', 'G = Guitarist', 'D = Drummer', 'B = Bassist','K = Keyboardist', 'I = Instrumentalist']))
                FinalList[key] = NewList[key]
                FinalList[key].append(Talent)
                FinalList[key].append(Instrument)
                
            elif NewStatus in ['A', 'a']:
                Talent = input ('Enter Talent (1-4): ')
                while Talent not in ['1','2','3','4']:
                    print('Invalid Input! ')
                    Talent = input ('Enter Talent (1-4): ')
                Instrument = input ('\n'.join(['enter instrument: ', 'S = Singer', 'G = Guitarist', 'D = Drummer', 'B = Bassist','K = Keyboardist', 'I = Instrumentalist', '']))
                while Instrument not in ['S','s','G','g','D','d','B','b','K','k','I','i']:
                    print ('Invalid Input!')
                    Instrument = input ('\n'.join(['enter instrument: ', 'S = Singer', 'G = Guitarist', 'D = Drummer', 'B = Bassist','K = Keyboardist', 'I = Instrumentalist']))
                FinalList[key] = NewList[key]
                FinalList[key].append(Talent)
                FinalList[key].append(Instrument)
        else:
            DeclinedList[key] = NewList[key]
            
    workbook = xlsxwriter.Workbook('DD.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet1 = workbook.add_worksheet()

    worksheet.write(0, 0, "ID Number")
    worksheet.write(0, 1, "First Name")
    worksheet.write(0, 2, "Last Name")
    worksheet.write(0, 3, "Adress")
    worksheet.write(0, 4, "Gender")
    worksheet.write(0, 5, "Age")
    worksheet.write(0, 6, "Date")
    worksheet.write(0, 7, "Camp")
    worksheet.write(0, 8, "Essay Included?")
    worksheet.write(0, 9, "Payment Cleared?")
    worksheet.write(0, 10, "Recording Included?")
    worksheet.write(0, 11, "Status")
    worksheet.write(0, 12, "Talent")
    worksheet.write(0, 13, "Instrument")
    worksheet.write(0, 14, "Dorm")
    worksheet.write(0, 15, "Band")
    row = 1
    col = 0
    for key in FinalList.keys():
        worksheet.write(row, 0, key)
        worksheet.write_row(row, 1, FinalList[key])
        row += 1

    worksheet1.write(0, 0, "ID Number")
    worksheet1.write(0, 1, "First Name")
    worksheet1.write(0, 2, "Last Name")
    worksheet1.write(0, 3, "Adress")
    worksheet1.write(0, 4, "Gender")
    worksheet1.write(0, 5, "Age")
    worksheet1.write(0, 6, "Date")
    worksheet1.write(0, 7, "Camp")
    worksheet1.write(0, 8, "Essay Included?")
    worksheet1.write(0, 9, "Payment Cleared?")
    worksheet1.write(0, 10, "Recording Included?")
    worksheet1.write(0, 11, "Status")
    worksheet1.write(0, 12, "Talent")
    worksheet1.write(0, 13, "Instrument")
    worksheet1.write(0, 14, "Dorm")
    worksheet1.write(0, 15, "Band")
    col = 0
    row = 1
    for key in DeclinedList.keys():
        worksheet1.write(row, 0, key)
        worksheet1.write_row(row, 1, DeclinedList[key])
        row += 1
    workbook.close()
    
    
    with open('FinalList.csv', 'w') as csv_file: #saves a file to be used by CheckIn.
                writer = csv.writer(csv_file)
                writer.writerow(["Id, FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, Status, Talent, Instrument"])
                for key, value in FinalList.items():
                    writer.writerow([key] + value)
                print ('List saved to file as FinalList.csv')
    print ('Accepted: ', FinalList)
    print ('Declined: ', DeclinedList)
    


