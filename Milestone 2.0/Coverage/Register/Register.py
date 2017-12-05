#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:35:53 2017

@author: ChristofferGamborg
"""
from datetime import timedelta, datetime

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
        print ('Application not recived in time.')
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



