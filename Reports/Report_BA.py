
import pandas as pd
from pandas import ExcelWriter
from pandasql import sqldf

def report_band_assign():

    url = "G:\Master - FE & IST\Information Systems And Technology\Software Development And Programming\Project\Algorithim\Correctly formatted Excel file\DD.xlsx"
    sav = ExcelWriter("G:\Band Assignment.xls")

    xl = pd.read_excel(url,"Sheet1",0)
    pysqldf = lambda q: sqldf(q, globals())


    B1 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='1' order by [Band]")
    B1.to_excel(sav, sheet_name='Band1', index=False)


    B2 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='2' order by [Band]")
    B2.to_excel(sav, sheet_name='Band2', index=False)

    B3 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='3' order by [Band]")
    B3.to_excel(sav, sheet_name='Band3', index=False)

    B4 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='4' order by [Band]")
    B4.to_excel(sav, sheet_name='Band4', index=False)

    B5 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='5' order by [Band]")
    B5.to_excel(sav, sheet_name='Band5', index=False)

    B6 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='6' order by [Band]")
    B6.to_excel(sav, sheet_name='Band6', index=False)

    B7 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='7' order by [Band]")
    B7.to_excel(sav, sheet_name='Band7', index=False)

    B8 = pysqldf("Select [ID Number],[First Name], [Last Name], [Band] from xl where [Status]='A'  and [Band]='8' order by [Band]")
    B8.to_excel(sav, sheet_name='Band8', index=False)

    sav.save()
