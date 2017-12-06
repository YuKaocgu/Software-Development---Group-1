import openpyxl as px
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf

url = "DD.xlsx"
xl = pd.read_excel(url, "Sheet1", 0)
pysqldf = lambda q: sqldf(q, globals())
sav = ExcelWriter("Band Assignment.xlsx")

def report_band_assign():


    B1 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='1' order by [First Name]")
    B1.to_excel(sav, sheet_name='Band1', index=False)


    B2 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='2' order by [First Name]")
    B2.to_excel(sav, sheet_name='Band2', index=False)

    B3 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='3' order by [First Name]")
    B3.to_excel(sav, sheet_name='Band3', index=False)

    B4 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='4' order by [First Name]")
    B4.to_excel(sav, sheet_name='Band4', index=False)

    B5 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='5' order by [First Name]")
    B5.to_excel(sav, sheet_name='Band5', index=False)

    B6 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='6' order by [First Name]")
    B6.to_excel(sav, sheet_name='Band6', index=False)

    B7 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='7' order by [First Name]")
    B7.to_excel(sav, sheet_name='Band7', index=False)

    B8 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='8' order by [First Name]")
    B8.to_excel(sav, sheet_name='Band8', index=False)

    BE = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='W'  and [Band]='' order by [First Name]")
    BE.to_excel(sav, sheet_name='Waiting List', index=False)

    BE = pysqldf(
        "Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='' order by [First Name]")
    BE.to_excel(sav, sheet_name='Unassigned', index=False)
    sav.save()
