import openpyxl as px
import pandas as pd
import pytest

def test_Band_Assign():
    #Test the function in Band assign
    ''' Function list:
    isNotFull(band)
    countIns(band)
    checkInstrument(band,ins)
    checkTalent(band,talent)
    checkGender(band_gender,gender)
    countTalent(band,talent)
    countGender(band_gender,gender)
    sumOfTalent(band)
    countIf(list,x)
    talentStatus(b1,b2,b3,b4,ins,talent)
    ageChoice(b_total,age)
    buildAgeList(b_total,age)
    avg(band_age)
    '''
    # First Bands Initialize
    b1 = {'gender':[]}
    b2 = {'S':1,'K':2,'B':3,'I':4,'D':1,'G':4, 'gender':['M','F','F','M','F','M']}
    b3 = {'S':1,'K':2,'B':3,'I':4,'D':2, 'gender':['M','F','F','M','F']}
    # Second Bands Initialize
    mb1 = {'G':1,'age':[18],'ID':"1"}
    mb2 = {'S':1,'K':2,'B':3,'I':4,'D':1,'G':4,'age':[16,17,18,13,13,15],'ID':"2"}
    mb3 = {'S':1,'K':2,'B':3,'I':4,'D':2,'age':[15,11,13,14,12],'ID':"3"}
    mb4 = {'age':[],'ID':"4"}
    # Test countIns(band)
    assert countIns(b1) == 0
    assert countIns(b2) == 6
    assert countIns(b3) == 5
    # Test isNotFull(band)
    assert isNotFull(b1) == True
    assert isNotFull(b2) == False
    assert isNotFull(b3) == True
    # Test checkInstrument(band,ins)
    assert checkInstrument(b1,'S') == True
    assert checkInstrument(b2,'S') == False
    assert checkInstrument(b3,'S') == False
    assert checkInstrument(b3,'G') == True
    # Test checkTalent(band,talent)
    assert checkTalent(b1,1) == True
    assert checkTalent(b2,2) == False
    assert checkTalent(b3,4) == False
    assert checkTalent(b1,3) == True
    # Test checkGender(band_gender,gender)
    assert checkGender(b1['gender'],"M") == True
    assert checkGender(b2['gender'],"M") == False
    assert checkGender(b2['gender'],"F") == False
    assert checkGender(b3['gender'],"M") == True
    assert checkGender(b3['gender'],"F") == False
    # Test countTalent(band,talent)
    assert countTalent(b1,1) == 0
    assert countTalent(b2,1) == 2
    assert countTalent(mb1,1) == 1
    # Test countGender(band_gender,gender)
    assert countGender(b1['gender'],"M") == 0
    assert countGender(b2['gender'],"M") == 3
    assert countGender(b3['gender'],"F") == 3
    # Test sumOfTalent(band)
    assert sumOfTalent(b1) == 0
    assert sumOfTalent(b2) == 15
    assert sumOfTalent(b3) == 12
    # Test countIf(list,x)
    assert countIf(b1['gender'],"M") == 0
    assert countIf(b2['gender'],"M") == 3
    assert countIf(mb2['age'],13) == 2
    assert countIf(mb3['age'],13) == 1
    # Test talentStatus(b1,b2,b3,b4,ins,talent)
    assert talentStatus(mb1,mb2,mb3,mb4,'G',4) == [mb4]
    assert talentStatus(mb1,mb2,mb3,mb4,'G',3) == [mb3,mb4]
    # Test ageChoice(b_total,age)
    b_total = talentStatus(mb1,mb2,mb3,mb4,'G',3)
    assert ageChoice(b_total,16) == "4"
    # Test buildAgeList(b_total,age)
    assert buildAgeList(b_total,16) == [3,16]
    # Test avg(band_age)
    assert avg(mb1['age']) == 18
    assert avg(mb3['age']) == 13
    assert avg(mb4['age']) == 0

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

def getLetters(letter):
    if 'a' <= letter <= 'z':
        return chr(ord(letter)-32),letter
    elif 'A' <= letter <= 'Z':
        return letter,chr(ord(letter)+32)
    else:
        return letter,letter


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
