import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf
import warnings

def talentChoice(b_total,talent):
    def_talent_list = buildTalentList(b_total,talent)
    for i in range(len(def_talent_list)):
        if def_talent_list[i] == max(def_talent_list):
            return b_total[i]['ID']

def buildTalentList(b_total,talent):
    talent_list = []
    for b in b_total:
        talent_list.append( abs(  avg_talent(b)-talent ) )
    return talent_list


def isNotFull(band):
    if countIns(band) < 6:
        return True
    else:
        return False
        
def countIns(band):
    count = 0
    for i in band.keys():
        if  i in ['S','s','D','d','K','k','I','i','G','g','B','b']:
            count += 1
    return count

def checkInstrument(band,ins):
    if ins not in band.keys():
        return True
    else:
        return False
def talentStatus2(b1,b2,b3,b4,b5,b6,b7,b8,ins):
    b_total = []
    if isNotFull(b1):
        if checkInstrument(b1,ins):
            b_total.append(b1)
    if isNotFull(b2):
        if checkInstrument(b2,ins):
            b_total.append(b2)
    if isNotFull(b3):
        if checkInstrument(b3,ins):
            b_total.append(b3)
    if isNotFull(b4):
        if checkInstrument(b4,ins):
            b_total.append(b4)
    if isNotFull(b5):
        if checkInstrument(b5,ins):
            b_total.append(b5)
    if isNotFull(b6):
        if checkInstrument(b6,ins):
            b_total.append(b6)
    if isNotFull(b7):
        if checkInstrument(b7,ins):
            b_total.append(b7)
    if isNotFull(b8):
        if checkInstrument(b8,ins):
            b_total.append(b8)
    return b_total


def checkGender(band_gender,gender):
    if countGender(band_gender,gender) < 3:
        return True
    else:
        return False


def countGender(band_gender,gender):
    count = 0

    for g in band_gender:
        if g == gender:
            count += 1
    return count

def sumOfTalent(band):
    result = 0
    for i in band.keys():
        if i in ['S','s','D','d','K','k','I','i','G','g','B','b']:
            result = result + int(band[i])
    return result

def countIf(list,x):
    count = 0
    for i in list:
        if x == i:
            count += 1
    return count



def talentStatus(b1,b2,b3,b4,ins):
    b_total = []
    if isNotFull(b1):
        if checkInstrument(b1,ins):
            b_total.append(b1)
    if isNotFull(b2):
        if checkInstrument(b2,ins):
            b_total.append(b2)
    if isNotFull(b3):
        if checkInstrument(b3,ins):
            b_total.append(b3)
    if isNotFull(b4):
        if checkInstrument(b4,ins):
            b_total.append(b4)
    return b_total

def ageChoice(b_total,age):
    def_age_list = buildAgeList(b_total,age)
    for i in range(len(def_age_list)):
        if def_age_list[i] == max(def_age_list):
            return b_total[i]['ID']

def buildAgeList(b_total,age):
    age_list = []
    for b in b_total:
        age_list.append( abs(avg(b['age'])- age ) )
    return age_list

def avg(band_age):
    if len(band_age) == 0:
        return 0
    else:
        return sum(band_age)/len(band_age)
def avg_talent(band):
    if countIns(band) == 0:
        return 0
    else:
        return sumOfTalent(band)/countIns(band)

def sumOfTalent(band):
    result = 0
    for i in band.keys():
        if i in ['S','s','D','d','K','k','I','i','G','g','B','b']:
            result = result + int(band[i])
    return result
