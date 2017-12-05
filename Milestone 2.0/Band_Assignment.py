import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf
import warnings

def First_Band_Assign():
    url = "DD.xlsx"
    xl = pd.read_excel(url, "Sheet1", 0)
    warnings.simplefilter("ignore") 
    # Fill in Data .
    wb = px.load_workbook(url)
    ws = wb.get_sheet_by_name("Sheet1")
    sheet = wb.active
    b1 = {'gender':[],'ID':"1"}
    b2 = {'gender':[],'ID':"2"}
    b3 = {'gender':[],'ID':"3"}
    b4 = {'gender':[],'ID':"4"}
    b5 = {'gender':[],'ID':"5"}
    b6 = {'gender':[],'ID':"6"}
    b7 = {'gender':[],'ID':"7"}
    b8 = {'gender':[],'ID':"8"}

    nRow = 1
    nlRow = ws.max_row + 1
    nlColumn = ws.max_column


    for row in range(nRow, nlRow):
        status = ws['L' + str(row)].value
        if status == 'A':
            gender = ws['E' + str(row)].value
            ins = ws['N' + str(row)].value
            talent = int(ws['M' + str(row)].value)
            b_total = bandStatus2(b1,b2,b3,b4,b5,b6,b7,b8,ins)
            choice = talentChoice(b_total,talent)
            if choice == '1':
                b1[ins] = talent
                b1['gender'].append(gender)
                ws["P"+str(row)] = 1
            elif choice == '2':
                b2[ins] = talent
                b2['gender'].append(gender)
                ws["P"+str(row)] = 2
            elif choice == '3':
                b3[ins] = talent
                b3['gender'].append(gender)
                ws["P"+str(row)] = 3
            elif choice == '4':
                b4[ins] = talent
                b4['gender'].append(gender)
                ws["P"+str(row)] = 4
            elif choice == '5':
                b5[ins] = talent
                b5['gender'].append(gender)
                ws["P"+str(row)] = 5
            elif choice == '6':
                b6[ins] = talent
                b6['gender'].append(gender)
                ws["P"+str(row)] = 6
            elif choice == '7':
                b7[ins] = talent
                b7['gender'].append(gender)
                ws["P"+str(row)] = 7
            elif choice == '8':
                b8[ins] = talent
                b8['gender'].append(gender)
                ws["P"+str(row)] = 8
        wb.save(url)


#band2 assign: check instrument -> make choice on age and talent -> return ID -> Assigning
def Second_Band_Assign():
    url = "DD.xlsx"
    xl = pd.read_excel(url, "Sheet1", 0)
    warnings.simplefilter("ignore")
    # Fill in Data .
    wb = px.load_workbook(url)
    ws = wb.get_sheet_by_name("Sheet1")
    sheet = wb.active

    mb1 = {'age':[],'ID':"1"}
    mb2 = {'age':[],'ID':"2"}
    mb3 = {'age':[],'ID':"3"}
    mb4 = {'age':[],'ID':"4"}

    fb1 = {'age':[],'ID':"1"}
    fb2 = {'age':[],'ID':"2"}
    fb3 = {'age':[],'ID':"3"}
    fb4 = {'age':[],'ID':"4"}
    nRow = 1
    nlRow = ws.max_row + 1
    nlColumn = ws.max_column
    for row in range(nRow, nlRow):
        status = ws['L' + str(row)].value
        if status == 'A':
            gender = ws['E' + str(row)].value
            age = int(ws['F' + str(row)].value)
            ins = ws['N' + str(row)].value
            talent = int(ws['M' + str(row)].value)
            if gender == "M":
                b_total = bandStatus(mb1,mb2,mb3,mb4,ins)
                choice = second_Band_Choice(b_total,age,talent)
                if choice == "1":
                    ws['Q'+str(row)] = 'M1'
                    mb1['age'].append(age)
                    mb1[ins] = talent
                elif choice == "2":
                    ws['Q'+str(row)] = 'M2'
                    mb2['age'].append(age)
                    mb2[ins] = talent
                elif choice == "3":
                    ws['Q'+str(row)] = 'M3'
                    mb3['age'].append(age)
                    mb3[ins] = talent
                elif choice == "4":
                    ws['Q'+str(row)] = 'M4'
                    mb4[ins] = talent 
            elif gender == "F":
                b_total = bandStatus(fb1,fb2,fb3,fb4,ins)
                choice = second_Band_Choice(b_total,age,talent)
                if choice == "1":
                    ws['Q'+str(row)] = 'F1'
                    fb1['age'].append(age)
                    fb1[ins] = talent
                elif choice == "2":
                    ws['Q'+str(row)] = 'F2'
                    fb2['age'].append(age)
                    fb2[ins] = talent
                elif choice == "3":
                    ws['Q'+str(row)] = 'F3'
                    fb3['age'].append(age)
                    fb3[ins] = talent
                elif choice == "4":
                    ws['Q'+str(row)] = 'F4'
                    fb4['age'].append(age)
                    fb4[ins] = talent  
        wb.save(url)
def talentChoice(b_total,talent):
    def_talent_list = buildTalentList(b_total,talent)
    for i in range(len(def_talent_list)):
        if def_talent_list[i] == max(def_talent_list):
            return b_total[i]['ID']



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
def bandStatus2(b1,b2,b3,b4,b5,b6,b7,b8,ins):
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

def countTalent(band,talent):
    result = countIf(band.values(),talent)
    return result

def countGender(band_gender,gender):
    count = 0

    for g in band_gender:
        if g == gender:
            count += 1
    return count
def countIf(list,x):
    count = 0
    for i in list:
        if x == i:
            count += 1
    return count



def bandStatus(b1,b2,b3,b4,ins):
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
def second_Band_Choice(b_total,age,talent):
    def_age_list = buildAgeList(b_total,age)
    def_talent_list = buildTalentList(b_total,talent)
    weight_List = []
    for i in range(len(def_age_list)):
        weight_List.append(def_age_list[i]*0.5+def_talent_list[i]+0.5)
    for i in range(len(weight_List)):
        if weight_List[i] == max(weight_List):
            return b_total[i]['ID']

def buildAgeList(b_total,age):
    age_list = []
    for b in b_total:
        age_list.append( abs(avg(b['age'])- age ) )
    return age_list
def buildTalentList(b_total,talent):
    talent_list = []
    for b in b_total:
        talent_list.append( abs(  avg_talent(b)-talent ) )
    return talent_list

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
