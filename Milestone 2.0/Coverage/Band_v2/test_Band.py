import openpyxl as px
import pandas as pd
import pytest
from Band import *
import Band as BA

def test_Band_Assign():
    #Test the function in Band assign
    ''' Function list:
    talentStatus2(b1,b2,b3,b4,b5,b6,b7,b8,ins)
    isNotFull(band)
    countIns(band)
    checkInstrument(band,ins)
    checkGender(band_gender,gender)
    countGender(band_gender,gender)
    sumOfTalent(band)
    countIf(list,x)
    talentStatus(b1,b2,b3,b4,ins,talent)
    ageChoice(b_total,age)
    buildAgeList(b_total,age)
    avg(band_age)
    avg_talent(band)
    '''
    # First Bands Initialize
    b1 = {'gender':[],'ID':"1"}
    b2 = {'S':1,'K':2,'B':3,'I':4,'D':1,'G':4, 'gender':['M','F','F','M','F','M'],'ID':"2"}
    b3 = {'S':1,'K':2,'B':3,'I':4,'D':2, 'gender':['M','F','F','M','F'],'ID':"3"}
    b4 = {'S':1,'K':2,'B':3,'I':4,'D':2, 'gender':['M','F','F','M','F'],'ID':"4"}
    b5 = {'gender':[],'ID':"5"}
    b6 = {'gender':[],'ID':"6"}
    b7 = {'gender':[],'ID':"7"}
    b8 = {'gender':[],'ID':"8"}

    # Second Bands Initialize
    mb1 = {'G':1,'age':[18],'ID':"1"}
    mb2 = {'S':1,'K':2,'B':3,'I':4,'D':1,'G':4,'age':[16,17,18,13,13,15],'ID':"2"}
    mb3 = {'S':1,'K':2,'B':3,'I':4,'D':2,'age':[15,11,13,14,12],'ID':"3"}
    mb4 = {'age':[],'ID':"4"}
    # Test talentStatus2(b1,b2,b3,b4,b5,b6,b7,b8,ins)
    assert BA.talentStatus2(b1,b2,b3,b4,b5,b6,b7,b8,"S") == [b1,b5,b6,b7,b8]


    # Test countIns(band)
    assert BA.countIns(b1) == 0
    assert BA.countIns(b2) == 6
    assert BA.countIns(b3) == 5
    # Test isNotFull(band)
    assert BA.isNotFull(b1) == True
    assert BA.isNotFull(b2) == False
    assert BA.isNotFull(b3) == True
    # Test checkInstrument(band,ins)
    assert BA.checkInstrument(b1,'S') == True
    assert BA.checkInstrument(b2,'S') == False
    assert BA.checkInstrument(b3,'S') == False
    assert BA.checkInstrument(b3,'G') == True
    # Test checkGender(band_gender,gender)
    assert BA.checkGender(b1['gender'],"M") == True
    assert BA.checkGender(b2['gender'],"M") == False
    assert BA.checkGender(b2['gender'],"F") == False
    assert BA.checkGender(b3['gender'],"M") == True
    assert BA.checkGender(b3['gender'],"F") == False
    # Test countGender(band_gender,gender)
    assert BA.countGender(b1['gender'],"M") == 0
    assert BA.countGender(b2['gender'],"M") == 3
    assert BA.countGender(b3['gender'],"F") == 3
    # Test sumOfTalent(band)
    assert BA.sumOfTalent(b1) == 0
    assert BA.sumOfTalent(b2) == 15
    assert BA.sumOfTalent(b3) == 12
    # Test countIf(list,x)
    assert BA.countIf(b1['gender'],"M") == 0
    assert BA.countIf(b2['gender'],"M") == 3
    assert BA.countIf(mb2['age'],13) == 2
    assert BA.countIf(mb3['age'],13) == 1
    # Test talentStatus(b1,b2,b3,b4,ins)
    assert BA.talentStatus(mb1,mb2,mb3,mb4,'G') == [mb3,mb4]
    # Test ageChoice(b_total,age)
    b_total = BA.talentStatus(mb1,mb2,mb3,mb4,'G')
    assert BA.ageChoice(b_total,16) == "4"
    # Test buildAgeList(b_total,age)
    assert BA.buildAgeList(b_total,16) == [3,16]
    # Test avg(band_age)
    assert BA.avg(mb1['age']) == 18
    assert BA.avg(mb3['age']) == 13
    assert BA.avg(mb4['age']) == 0
    # Test avg_talent(band)
    assert BA.avg_talent(b1) == 0
    assert BA.avg_talent(b2) == 2.5
    assert BA.avg_talent(b3) == 2.4
    assert BA.avg_talent(b4) == 2.4
    

