import openpyxl as px
import pandas as pd
import pytest

    

def check(band,band_gender,gender,ins,talent):
    if isNotFull(band):
        if checkGender(band_gender,gender):
            if checkInstrument(band,ins):
                if checkTalent(band,talent):
                    return True
                else:
                    return False
            else: return False
        else:
            return False
    else:
        return False


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

def checkTalent(band,talent):
    if countTalent(band,talent) == 0:
        return True
    elif countTalent(band,talent) == 1:
        if talent == 1:
            check1 = countTalent(band,2)
            check2 = countTalent(band,3)
            if check1 == 2:
                return False
            else:
                return True
            if check2 == 2:
                return False
            else:
                return True
        elif talent == 4:
            check1 = countTalent(band,2)
            check2 = countTalent(band,3)
            if check1 == 2:
                return False
            else:
                return True
            if check2 == 2:
                return False
            else:
                return True
        elif talent == 2:
            check1 = countTalent(band,1)
            check2 = countTalent(band,4)
            if check1 == 2:
                return False
            else:
                return True
            if check2 == 2:
                return False
            else:
                return True
        elif talent == 3:
            check1 = countTalent(band,1)
            check2 = countTalent(band,4)
            if check1 == 2:
                return False
            else:
                return True
            if check2 == 2:
                return False
            else:
                return True
        else:
            if sumOfTalent(band,talent) + talent <= 15:
                return True
            else:
                return False    
    else: 
        return False



def checkGender(band_gender,gender):
    if countGender(band_gender,gender) < 3:
        return True
    else:
        return False

def countTalent(band,talent):
    result = countIf(band.values(),talent)
    return result

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
            result += band[i]
    return result

def countIf(list,x):
    count = 0
    for i in list:
        if x == i:
            count += 1
    return count


def talentStatus(b1,b2,b3,b4,ins,talent):
    b_total = []
    if checkInstrument(b1,ins):
        if checkTalent(b1,talent):
            b_total.append(b1)
    if checkInstrument(b2,ins):
        if checkTalent(b2,talent):
            b_total.append(b2)
    if checkInstrument(b3,ins):
        if checkTalent(b3,talent):
            b_total.append(b3)
    if checkInstrument(b4,ins):
        if checkTalent(b4,talent):
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
        age_list.append( abs(avg(b['age'])-age ) )
    return age_list

def avg(band_age):
    if len(band_age) == 0:
        return 0
    else:
        return sum(band_age)/len(band_age)
