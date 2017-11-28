import Replace_Module as RM
import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf

url = "G:\Master - FE & IST\Information Systems And Technology\Software Development And Programming\Project\Algorithim\Group Changes\DD.xlsx"
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
            "Select [ID Number],[First Name], [Last Name],[Gender],[Instrument],[Talent], [Status] from xl where [Status]='A' and [Dorm]="+humanInput+" order by [ID Number]"))
        RM.replace_module()


    while True:
        humanInput = input ('\n'.join(['Select the m to change: ','1: Band 1', '2: Band 2', '3: Band 3','4: Band 4','5: Band 5','6: Band 6','7: Band 7','8: Band 8','0: Exit Program', '']))
        while humanInput not in ['1','2','3','4','5','6','7','8','0']:
            print ('Invalid Input')
            humanInput = input ('\n'.join(['Select the band to change: ','1: Band 1', '2: Band 2', '3: Band 3','4: Band 4','5: Band 5','6: Band 6','7: Band 7','8: Band 8','0: Exit Program', '']))
        if humanInput in ['1','2','3','4','5','6','7','8']:
            group()
        elif humanInput in ["0"]:
            break