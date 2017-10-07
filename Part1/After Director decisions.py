#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:35:45 2017

@author: ChristofferGamborg

Jeg mangler at få den til at iterere flere gange - et for loop i et for loop.
"""
from datetime import timedelta, datetime
import xlsxwriter
import csv
import pandas as pd
NewList = {}
FinalList = {}
DeclinedList = {}

def editApplication():
    with open('dict.csv') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:
            key = row[0]
            NewList[key] = row[1:]
    print('List loaded')
    for key in NewList:
        if NewList[key][10] == 'awaiting directors call':
            print(NewList[key][0], NewList[key][1])
            NewStatus = input ('Accepted or Declined (A or D): ')
            NewList[key][10] = NewStatus
            if NewStatus == 'D' or NewStatus == 'd':
                DeclinedList[key] = NewList[key]
                continue
            else:
                Talent = input ('Enter Talent (1-4): ')
                Instrument = input ('enter instrument: ')
                FinalList[key] = NewList[key]
                FinalList[key].append(Talent)
                FinalList[key].append(Instrument)
        else:
            print ('do nothing')
    workbook = xlsxwriter.Workbook('Data.xlsx')
    worksheet = workbook.add_worksheet()

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
    row = 1
    col = 0
    for key in FinalList.keys():
        worksheet.write(row, 0, key)
        worksheet.write_row(row, 1, FinalList[key])
        row += 1
    workbook.close()          
    print ('Accepted: ', FinalList)
    print ('Declined: ', DeclinedList)
