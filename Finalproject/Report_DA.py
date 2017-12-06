import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf

url = "DD.xlsx"
xl = pd.read_excel(url, "Sheet1", 0)
pysqldf = lambda q: sqldf(q, globals())
sav = ExcelWriter("Dorm Assignment.xlsx")

def report_dorm_assign():

    M1 = pysqldf("Select [ID Number],[First Name], [Last Name], [Dorm] from xl where [Status]='A'  and [Dorm]='M1' order by [First Name]")
    M1.to_excel(sav, sheet_name='Male Dorm1', index=False)

    M2 = pysqldf("Select [ID Number],[First Name], [Last Name], [Dorm] from xl where [Status]='A'  and [Dorm]='M2' order by [First Name]")
    M2.to_excel(sav, sheet_name='Male Dorm2', index=False)

    M3 = pysqldf("Select [ID Number],[First Name], [Last Name], [Dorm] from xl where [Status]='A'  and [Dorm]='M3' order by [First Name]")
    M3.to_excel(sav, sheet_name='Male Dorm3', index=False)

    F1 = pysqldf("Select [ID Number],[First Name], [Last Name], [Dorm] from xl where [Status]='A'  and [Dorm]='F1' order by [First Name]")
    F1.to_excel(sav, sheet_name='Female Dorm1', index=False)

    F2 = pysqldf("Select [ID Number],[First Name], [Last Name], [Dorm] from xl where [Status]='A'  and [Dorm]='F2' order by [First Name]")
    F2.to_excel(sav, sheet_name='Female Dorm2', index=False)

    F3 = pysqldf("Select [ID Number],[First Name], [Last Name], [Dorm] from xl where [Status]='A'  and [Dorm]='F3' order by [First Name]")
    F3.to_excel(sav, sheet_name='Female Dorm3', index=False)

    WE = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='W'  and [Dorm]='' order by [First Name]")
    WE.to_excel(sav, sheet_name='Waiting List', index=False)

    DE = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Dorm]='' order by [First Name]")
    DE.to_excel(sav, sheet_name='Unassigned', index=False)

    sav.save()
