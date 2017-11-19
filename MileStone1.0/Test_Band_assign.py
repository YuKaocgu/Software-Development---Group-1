import Band_Function_Rev_V2 as BA
from Band_Function_Rev_V2 import *

def Test_Band_Assign():
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
    mb1 = {'G':1,'age':[18],'ID':1}
    mb2 = {'S':1,'K':2,'B':3,'I':4,'D':1,'G':4,'age':[16,17,18,13,13,15],'ID':2}
    mb3 = {'S':1,'K':2,'B':3,'I':4,'D':2,'age':[15,11,13,14,12],'ID':3}
    mb4 = {'age':[],'ID':4}
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
    # Test checkTalent(band,talent)
    assert BA.checkTalent(b1,1) == True
    assert BA.checkTalent(b2,2) == False
    assert BA.checkTalent(b3,4) == False
    assert BA.checkTalent(b1,3) == True
    # Test checkGender(band_gender,gender)
    assert BA.countGender(b1['gender'],"M") == True
    assert BA.countGender(b2['gender'],"M") == False
    assert BA.countGender(b2['gender'],"F") == False
    assert BA.countGender(b3['gender'],"M") == True
    assert BA.countGender(b3['gender'],"F") == False
    # Test sumOfTalent(band)
    assert BA.sumOfTalent(b1) == 0
    assert BA.sumOfTalent(b2) == 15
    assert BA.sumOfTalent(b3) == 12
    # Test countIf(list,x)
    assert BA.countIf(b1['gender'],"M") == 0
    assert BA.countIf(b2['gender'],"M") == 3
    assert BA.countIf(mb2['age'],13) == 2
    assert BA.countIf(mb3['age'],13) == 1
    # Test talentStatus(b1,b2,b3,b4,ins,talent)
    assert BA.talentStatus(mb1,mb2,mb3,mb4,'G',4) == [mb4]
    assert BA.talentStatus(mb1,mb2,mb3,mb4,'G',3) == [mb3,mb4]
    # Test ageChoice(b_total,age)
    b_total = BA.talentStatus(mb1,mb2,mb3,mb4,'G',3)
    assert BA.ageChoice(b_total,16) == "4"
    # Test buildAgeList(b_total,age)
    
    # Test avg(band_age)
    assert avg(mb1['age']) == 18
    assert avg(mb3['age']) == 13
    assert avg(mb4['age']) == 0