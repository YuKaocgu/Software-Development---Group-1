import Replace_Module as RM
import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
url = "DD.xlsx"
xl = pd.read_excel(url, "Sheet1", 0)

def main():
    url = "DD.xlsx"
    xl = pd.read_excel(url, "Sheet1", 0)
    def group():
        print(humanInput)
        print(pysqldf(
            "Select [ID Number],[First Name], [Last Name],[Gender],[Instrument],[Talent], [Status] from xl where [Status]='A' and [Band]="+humanInput+" order by [ID Number]"))
        RM.ID()

    while True:
        humanInput = input ('\n'.join(['Select band for replacement: ','1: Band 1', '2: Band 2', '3: Band 3','4: Band 4','5: Band 5','6: Band 6','7: Band 7','8: Band 8','0: Exit Program', '']))
        while humanInput not in ['1','2','3','4','5','6','7','8','0']:
            print ('Invalid Input')
            humanInput = input ('\n'.join(['Select band for replacement: ','1: Band 1', '2: Band 2', '3: Band 3','4: Band 4','5: Band 5','6: Band 6','7: Band 7','8: Band 8','0: Exit Program', '']))
        if humanInput in ['1','2','3','4','5','6','7','8']:
            group()
            break
        elif humanInput in ["0"]:
            break