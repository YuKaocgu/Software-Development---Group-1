from datetime import timedelta, datetime
import xlsxwriter
import csv
import pandas as pd
NewList = {}
FinalList = {}
DeclinedList = {}

applicationList = {}

camp1=datetime.strptime("06-10-17", "%m-%d-%y")
camp2=datetime.strptime("07-08-17", "%m-%d-%y")
camp3=datetime.strptime("08-05-17", "%m-%d-%y")


 
def timeCheck(Date, Camp):
    transform = datetime.strptime(Date, "%m-%d-%y")
    if Camp == '1':
        difference = camp1 - transform 
    elif Camp == '2': 
        difference = camp2 - transform          
    else: 
        difference = camp3 - transform  
    if difference <= timedelta(32) or difference >= timedelta(90):
        return False
    else:
        return True

def checkIfY(X):
    if X in ['y', 'Y']:
        return True
    else:
        return False

def checkIfYorN(X):
    if X in ['y', 'Y','n','N']:
        return True
    else:
        return False


def fillData(Input):
    global Payment
    global Recording
    global Essay
    global fillStatus
    if Input in ['N','n']:
        print('Application was Incomplete')
        fillStatus = 'Rejected - Incomplete'
        print (fillStatus)
        return False
    
    elif checkIfY(Input) == True:
        return True
    else:
        print ('Wrong input, please check source')
        return False

 
def Applications():
    """ Applications should be an interface for the clerk to type in the applications recived for FuRS"""
    ListOfInformation = []
    FirstName = LastName = Adress = Gender = Age = Date = Essay = Payment = Recording = Status = 'NA'
    
    if not applicationList:
        KeyNumber = 0
    else:
        KeyNumber = max(applicationList)
    while True:
        humanInput = input('\n'.join([ 'N: To add a person.', 'P: to print the list to file. ','R: To return to the main menu', '']))
        if humanInput in ['n', 'N']:
            KeyNumber += 1
            FirstName = input ("Enter the first name of the applicant: ")
            LastName = input ("Enter the lastname of the applicant: ")
            Gender = input ('\n'.join(['Enter Gender: ','M = Male', 'F = Female', '']))
            while Gender not in ['M','F']:
                print ('input must be M or F!')
                Gender = input ('\n'.join(['Enter Gender: ','M = Male', 'F = Female', '']))
            Age = input ("Enter Age of applicant: ")
            while not Age.isdigit():
                print ('Input must be a number')
                Age = input ("Enter Age of applicant: ")
            Adress = input ("Enter Street adresse, City, Zip Code, State): ")
            Adress = Adress.replace(","," ")
            Date = input ("Enter date of recived application (MM-DD-YY): ")
            Camp = input ('\n'.join(["Enter the Camps they want to attend: ", "1 = June", "2 = July", "3 = August", '']))
            while Camp not in ['1','2','3']:
                print ('Invalid Input! Please write either 1, 2 or 3')
                Camp = input ('\n'.join(["Enter the Camps they want to attend: ", "1 = June", "2 = July", "3 = August", '']))
            if timeCheck(Date, Camp) == False:
                    print ('Application not recived in time.')
                    Status = 'Rejected - Time'
                    ListOfInformation = [FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, Status]
                    applicationList[(KeyNumber)] = ListOfInformation
                    continue
            else: 
                print ('Application recived in time. Continue process')
            Essay = input ("Does the Application contain an essay? (Y or N): ")
            while checkIfYorN(Essay) == False:
                print ('Please write either Y or N')
                Essay = input ("Does the Application contain an essay? (Y or N)")
            if fillData(Essay) == False:
                ListOfInformation = [FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, fillStatus]
                applicationList[(KeyNumber)] = ListOfInformation
                continue
            else: 
                print ('Essay Included. Continue process')
            Payment = input ("Did the payment clear? (Y or N): ")
            while checkIfYorN(Payment) == False:
                print ('Please write either Y or N')
                Payment = input ("Did the payment clear? (Y or N): ")
            if fillData(Payment) == False:
                ListOfInformation = [FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, fillStatus]
                applicationList[(KeyNumber)] = ListOfInformation
                continue
            elif Payment == 'Y' or Payment == 'y': 
                print ('Payment cleared. Continue process')
            Recording = input ("Did the application have a recording? (Y or N): ")
            while checkIfYorN(Recording) == False:
                print ('Please write either Y or N')
                Recording = input ("Did the application have a recording? (Y or N): ")
            if fillData(Recording) != True:
                print('The application did not have a recording, Application is therfore invalid')
                Status = 'Rejected - Incomplete'
                ListOfInformation = [FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, fillStatus]
                applicationList[(KeyNumber)] = ListOfInformation   
                continue
            elif checkIfY(Recording) == True: 
                print ('Recording in application. Continue process')
            Status = 'awaiting directors call'
            ListOfInformation = [FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, Status]
            applicationList[(KeyNumber)] = ListOfInformation
        if humanInput in ['r', 'R']:
            print (applicationList)
            break
        if humanInput in ['p', 'P']:
            with open('TempDatabase.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Id, FirstName, LastName, Adress, Gender, Age, Date, Camp, Essay, Payment, Recording, Status"])
                for key, value in applicationList.items():
                    writer.writerow([key] + value)
            print ('List saved to file as TempDatabase.csv')
        print (applicationList)
