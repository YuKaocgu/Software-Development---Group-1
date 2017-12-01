import openpyxl as px
import pandas as pd
import pytest

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
    assert countGender(b1['gender'],"M") == True
    assert countGender(b2['gender'],"M") == False
    assert countGender(b2['gender'],"F") == False
    assert countGender(b3['gender'],"M") == True
    assert countGender(b3['gender'],"F") == False
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
    
    # Test avg(band_age)
    assert avg(mb1['age']) == 18
    assert avg(mb3['age']) == 13
    assert avg(mb4['age']) == 0
'''
def test():
    url = ""
    b1 = {'gender':[]}
    b2 = {'gender':[]}
    b3 = {'gender':[]}
    b4 = {'gender':[]}
    b5 = {'gender':[]}
    b6 = {'gender':[]}
    b7 = {'gender':[]}
    b8 = {'gender':[]}

    count = 1

    for student in List:
        if check(b1,b1['gender'],student.gender,student.ins,student.talent):
            b1[student.ins] = student.talent
            b1['gender'].append(student.gender)
            xls["N"+str(count)] = 1
        elif check(b2,b2['gender'],student.gender,student.ins,student.talent):
            b2[student.ins] = student.talent
            b2['gender'].append(student.gender)
            xls["N"+str(count)] = 2
        elif check(b3,b3['gender'],student.gender,student.ins,student.talent):
            b3[student.ins] = student.talent
            b3['gender'].append(student.gender)
            xls["N"+str(count)] = 3
        elif check(b4,b4['gender'],student.gender,student.ins,student.talent):
            b4[student.ins] = student.talent
            b4['gender'].append(student.gender)
            xls["N"+str(count)] = 4
        elif check(b5,b5['gender'],student.gender,student.ins,student.talent):
            b5[student.ins] = student.talent
            b5['gender'].append(student.gender)
            xls["N"+str(count)] = 5
        elif check(b6,b6['gender'],student.gender,student.ins,student.talent):
            b6[student.ins] = student.talent
            b6['gender'].append(student.gender)
            xls["N"+str(count)] = 6
        elif check(b7,b7['gender'],student.gender,student.ins,student.talent):
            b7[student.ins] = student.talent
            b7['gender'].append(student.gender)
            xls["N"+str(count)] = 7
        elif check(b8,b8['gender'],student.gender,student.ins,student.talent):
            b8[student.ins] = student.talent
            b8['gender'].append(student.gender)
            xls["N"+str(count)] = 8
        count += 1
    xls.save(url)
'''
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
        if (talent == 1 or talent == 4) and (countTalent(band,2) == 2 or countTalent(band,3) == 2):
            return False
        elif (talent == 2 or talent == 3) and (countTalent(band,1) == 2 or countTalent(band,4) == 2):
            return False
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


#band2 assign: check talent -> make choice on age -> return ID -> Assigning
'''
def test2():
    url = ""
    count = 1
    mb1 = {'age':[],'ID':"1"}
    mb2 = {'age':[],'ID':"2"}
    mb3 = {'age':[],'ID':"3"}
    mb4 = {'age':[],'ID':"4"}

    fb1 = {'age':[],'ID':"1"}
    fb2 = {'age':[],'ID':"2"}
    fb3 = {'age':[],'ID':"3"}
    fb4 = {'age':[],'ID':"4"}
    for student in List:
        if student.gender == "M":
            b_total = talentStatus(mb1,mb2,mb3,mb4,student.ins,student.talent)
            choice = ageChoice(b_total,student.age)
            if choice == "1":
                xls['Q'+str(count)] = 1
                mb1['age'].append(student.age)
                mb1[student.ins] = student.talent
            elif choice == "2":
                xls['Q'+str(count)] = 2
                mb2['age'].append(student.age)
                mb2[student.ins] = student.talent
            elif choice == "3":
                xls['Q'+str(count)] = 3
                mb3['age'].append(student.age)
                mb3[student.ins] = student.talent
            elif choice == "4":
                xls['Q'+str(count)] = 4
                mb4[student.ins] = student.talent 
        elif student.gender == "F":
            if choice == "1":
                xls['Q'+str(count)] = 1
                fb1['age'].append(student.age)
                fb1[student.ins] = student.talent
            elif choice == "2":
                xls['Q'+str(count)] = 2
                fb2['age'].append(student.age)
                fb2[student.ins] = student.talent
            elif choice == "3":
                xls['Q'+str(count)] = 3
                fb3['age'].append(student.age)
                fb3[student.ins] = student.talent
            elif choice == "4":
                xls['Q'+str(count)] = 4
                fb4['age'].append(student.age)
                fb4[student.ins] = student.talent  
        count += 1
    xls.save(url)
'''
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
