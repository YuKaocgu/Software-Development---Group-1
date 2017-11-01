import openpyxl as px
import pandas as pd

def test():
    url = ""
    b1 = {'gender':[],'ID':1}
    b2 = {'gender':[],'ID':2}
    b3 = {'gender':[],'ID':3}
    b4 = {'gender':[],'ID':4}
    b5 = {'gender':[],'ID':5}
    b6 = {'gender':[],'ID':6}
    b7 = {'gender':[],'ID':7}
    b8 = {'gender':[],'ID':8}


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
    if len(band) < 6:
        return True
    else:
        return False
def checkInstrument(band,ins):
    if ins not in band.keys():
        return True
    else:
        return False

def checkTalent(band,talent):
    if countTalent(band,talent) < 2:
        if sumOfTalent(band)+talent <= 15:
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
        if i in ['S','D','K','I','G','B']:
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

def avg(band_age):
    if len(band_age) == 0:
        return 0
    else:
        return sum(band_age)/len(band_age)
#band2 assign: check talent -> make choice on age -> return ID -> Assigning
def test2():
    b1 = {'age':[],'ID':1}
    b2 = {'age':[],'ID':2}
    b3 = {'age':[],'ID':3}
    b4 = {'age':[],'ID':4}
    b5 = {'age':[],'ID':5}
    b6 = {'age':[],'ID':6}
    b7 = {'age':[],'ID':7}
    b8 = {'age':[],'ID':8}

def talentStatus(b1,b2,b3,b4,b5,b6,b7,b8,ins,talent):
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
    if checkInstrument(b5,ins):
        if checkTalent(b5,talent):
            b_total.append(b5)
    if checkInstrument(b6,ins):
        if checkTalent(b6,talent):
            b_total.append(b6)
    if checkInstrument(b7,ins):
        if checkTalent(b7,talent):
            b_total.append(b7)
    if checkInstrument(b8,ins):
        if checkTalent(b8,talent):
            b_total.append(b8)
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