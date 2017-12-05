import Replace_Module as RM
import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf

url = "DD.xlsx"
xl = pd.read_excel(url, "Sheet1", 0)
pysqldf = lambda q: sqldf(q, globals())
# Fill in Data .
wb = px.load_workbook(url)
ws = wb.get_sheet_by_name("Sheet1")
sheet = wb.active

def main():



    def group():
        print(humanInput)
        print(pysqldf(
            "Select [ID Number],[First Name], [Last Name],[Gender],[Instrument],[Talent], [Status] from xl where [Status]='A' and [Dorm]="+"'"+humanInput+"'"+" order by [ID Number]"))
        RM.replace_module()
        wb.close()

    while True:
        humanInput = input ('\n'.join(['Select Dorm for replacement: ','M1: Male Dorm 1', 'M2: Male Dorm 2', 'M3: Male Dorm 3','F1: Female Dorm 1', 'F2: Female Dorm 2', 'F3: Female Dorm 3','0: Exit Program', '']))
        while humanInput not in ['F1','F2','F3','M1','M2','M3','0']:
            print ('Invalid Input')
            humanInput = input ('\n'.join(['Select Dorm for replacement: ','M1: Male Dorm 1', 'M2: Male Dorm 2', 'M3: Male Dorm 3','F1: Female Dorm 1', 'F2: Female Dorm 2', 'F3: Female Dorm 3','0: Exit Program', '']))
        if humanInput in ['F1','F2','F3','M1','M2','M3']:
            group()
            wb.close()
            break
        elif humanInput in ["0"]:
            break
