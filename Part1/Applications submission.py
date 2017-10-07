from datetime import timedelta, datetime
import xlsxwriter
import csv
import pandas as pd
NewList = {}
FinalList = {}
DeclinedList = {}

applicationList = {1: ['chris',
  'Gamb',
  '04-12-17',
  '1',
  'Y',
  'N',
  'NA',
  'M',
  '26',
  'Rejected - Incomplete'],
 2: ['Anne-sophie',
  'Milling',
  'sjdng',
  'F',
  '27',
  '04-12-17',
  '1',
  'y',
  'y',
  'y',
  'awaiting directors call'],
 3: ['Yo',
  'Dawg',
  'sdjng',
  'M',
  '30',
  '04-12-17',
  '1',
  'y',
  'y',
  'y',
  'awaiting directors call']}

camp1=datetime.strptime("06-10-17", "%m-%d-%y")
camp2=datetime.strptime("07-08-17", "%m-%d-%y")
camp3=datetime.strptime("08-05-17", "%m-%d-%y")
 

def Applications():
    """ Applications should be an interface for the clerk to type in the applications recived for FuRS"""
    ListOfInformation = []
    KeyNumber = 0
    while True:
        humanInput = input("Enter n to add a person. Enter e to exit the program or enter P to print the list to file: " )
        if humanInput == 'n':
            KeyNumber += 1
            FirstName = input ("Enter the firstname of the applicant: ")
            LastName = input ("Enter the lastname of the applicant: ")
            Gender = input ("Enter gender of applicant (M or F): ")
            while Gender not in ['M','F']:
                print ('input must be M or F!')
                Gender = input ("Enter gender of applicant (M or F): ")
            Age = input ("Enter Age of applicant: ")
            Adress = input ("Enter the adresse of the applicant (Street adresse, Zip Code, City, State): ")
            Date = input ("Enter date of recived application (MM-DD-YY): ")
            Camp = input ("Enter the Camps they want to attend (1, 2 or 3): ")
            while Camp not in ['1','2','3']:
                print ('Please write either 1, 2 or 3')
                Camp = input ("Write 1, 2 or 3")
            if Camp == '1':
                transform = datetime.strptime(Date, "%m-%d-%y")
                difference = camp1 - transform
                ''' Make a function outside def timeCheck(Date)''' 
                if difference <= timedelta(32) or difference >= timedelta(90):
                    print('Application is recived either too late or too soon and is therefore invalid')
                    Status = 'Rejected - Time'
                    Essay = 'NA' 
                    Payment = 'NA'
                    Recording = 'NA'
                    ListOfInformation = [FirstName, LastName, Date, Camp, Essay, Payment, Recording, Gender, Age, Status]
                    applicationList[(KeyNumber)] = ListOfInformation
                    continue
                else: 
                    print ('Application recived in time. Continue process')
            elif Camp == '2':
                transform = datetime.strptime(Date, "%m-%d-%y")
                difference = camp2 - transform
                if difference <= timedelta(32) or difference >= timedelta(90):
                    print('Application is recived either too late or too soon and is therefore invalid')
                    Status = 'Rejected - Time'
                    Essay = 'NA' 
                    Payment = 'NA'
                    Recording = 'NA'
                    ListOfInformation = [FirstName, LastName, Date, Camp, Essay, Payment, Recording, Gender, Age, Status]
                    applicationList[(KeyNumber)] = ListOfInformation
                    continue
                else: 
                    print ('Application recived in time. Continue process')
            elif Camp == '3':
                transform = datetime.strptime(Date, "%m-%d-%y")
                difference = camp3 - transform
                if difference <= timedelta(32) or difference >= timedelta(90):
                    print('Application is recived either too late or too soon and is therefore invalid')
                    Status = 'Rejected - Time'
                    Essay = 'NA' 
                    Payment = 'NA'
                    Recording = 'NA'
                    ListOfInformation = [FirstName, LastName, Date, Camp, Essay, Payment, Recording, Gender, Age, Status]
                    applicationList[(KeyNumber)] = ListOfInformation
                    continue
                else: 
                    print ('Application recived in time. Continue process')
            Essay = input ("Does the Application contain an essay? (Y or N): ")
            while Essay not in ['Y', 'y', 'N', 'n']:
                print ('Please write either Y or N')
                Essay = input ("Does the Application contain an essay? (Y or N)")
            if Essay == 'N' or Essay == 'n':
                Payment = 'NA'
                Recording = 'NA'
                print('Payment did not clear, Application is therfore invalid')
                Status = 'Rejected - Payment'
                ListOfInformation = [FirstName, LastName, Date, Camp, Essay, Payment, Recording, Gender, Age, Status]
                applicationList[(KeyNumber)] = ListOfInformation
                continue
            elif Essay == 'Y' or Essay == 'y': 
                print ('Essay Included. Continue process')
            Payment = input ("Did the payment clear? (Y or N): ")
            while Payment not in ['Y', 'y', 'N', 'n']:
                print ('Please write either Y or N')
                Payment = input ("Did the payment clear? (Y or N): ")
            if Payment == 'N' or Payment == 'n':
                Recording = 'NA'
                print('The application did not have an recording, Application is therfore invalid')
                Status = 'Rejected - Incomplete'
                ListOfInformation = [FirstName, LastName, Date, Camp, Essay, Payment, Recording, Gender, Age, Status]
                applicationList[(KeyNumber)] = ListOfInformation
                continue
            elif Payment == 'Y' or Payment == 'y': 
                print ('Payment cleared. Continue process')
            Recording = input ("Did the application have an recording? (Y or N): ")
            while Recording not in ['Y', 'y', 'N', 'n']:
                print ('Please write either Y or N')
                Recording = input ("Did the application have an recording? (Y or N): ")
            if Recording == 'N' or Recording =='n':
                print('The application did not have an recording, Application is therfore invalid')
                Status = 'Rejected - Incomplete'
                ListOfInformation = [FirstName, LastName, Date, Camp, Essay, Payment, Recording, Gender, Age, Status]
                applicationList[(KeyNumber)] = ListOfInformation   
                continue
            elif Recording == 'Y' or Recording == 'y': 
                print ('Recording in application. Continue process')
            Status = 'awaiting directors call'
            ListOfInformation = [FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, Status]
            applicationList[(KeyNumber)] = ListOfInformation
        if humanInput == 'e':
            print (applicationList)
            break
        if humanInput == 'p':
            with open('dict.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Id, FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, Status"])
                for key, value in applicationList.items():
                    writer.writerow([key] + value)
            print ('List saved to file as dict.csv')
        print (applicationList)
        
