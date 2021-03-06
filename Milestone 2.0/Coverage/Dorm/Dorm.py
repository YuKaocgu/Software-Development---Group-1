import numpy
import openpyxl as px
import pandas as pd
import warnings
import pytest

def isFull(dorm):
    if (len(dorm) == 8):
        return True
    else:
        return False
def avg(data_List):
    if len(data_List) == 0:
        return 0
    else:
        return sum(data_List)/len(data_List)
def dorm_assign(Dorm1,Dorm2,Dorm3,age):
    Dorm_Status = [isFull(Dorm1),isFull(Dorm2),isFull(Dorm3)]
    if Dorm_Status == [False,False,False]:
        check_list = [ abs(avg(Dorm1)-age),abs(avg(Dorm2)-age),abs(avg(Dorm3)-age)]
        if max(check_list) == abs(avg(Dorm1)-age):
            Dorm1.append(age)
            return 1
        elif max(check_list) == abs(avg(Dorm2)-age):
            Dorm2.append(age)
            return 2
        else:
            Dorm3.append(age)
            return 3

    elif Dorm_Status == [True,False,False]:
        if abs(avg(Dorm2)-age) > abs(avg(Dorm3)-age):
            Dorm2.append(age)
            return 2
        else:
            Dorm3.append(age) 
            return 3
    elif Dorm_Status == [False,True,False]:
        if abs(avg(Dorm1)-age) > abs(avg(Dorm3)-age):
            Dorm1.append(age)
            return 1
        else:
            Dorm3.append(age) 
            return 3
    elif Dorm_Status == [False,False,True]:
        if abs(avg(Dorm1)-age) > abs(avg(Dorm2)-age):
            Dorm1.append(age)
            return 1
        else:
            Dorm2.append(age) 
            return 2
    elif Dorm_Status == [False,True,True]:
        Dorm1.append(age)
        return 1
    elif Dorm_Status == [True,False,True]:
        Dorm2.append(age)
        return 2
    elif Dorm_Status == [True,True,False]:
        Dorm3.append(age)
        return 3
