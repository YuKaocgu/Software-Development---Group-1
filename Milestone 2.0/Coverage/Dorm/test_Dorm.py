import numpy
import openpyxl as px
import pandas as pd
import warnings
from Dorm import *
import Dorm as DA
import pytest
def test_Band_Assign():
    Dorm1 = [12,12,14,14,16,16,18,18]
    Dorm2 = [11,13,15,17]
    Dorm3 = [12,14]
    Dorm4 = []
    Dorm5 = [16]
    Dorm6 = [16,18]
    Dorm7 = [12,12,14,14,16,16,18,18]
    Dorm8 = [12,12,14,14,16,16,18]
    Dorm9 = [12,12,14,14,16,16,18]
    Dorm10 = [12,12,14,14,16,16,18]
    assert DA.isFull(Dorm1) == True
    assert DA.isFull(Dorm2) == False
    assert DA.isFull(Dorm3) == False
    assert DA.avg(Dorm1) == 15
    assert DA.avg(Dorm2) == 14
    assert DA.avg(Dorm3) == 13
    assert DA.avg(Dorm4) == 0
    assert DA.dorm_assign(Dorm1,Dorm2,Dorm3,15) == 3   #TFF
    assert DA.dorm_assign(Dorm1,Dorm2,Dorm3,11) == 2   #TFF
    assert DA.dorm_assign(Dorm4,Dorm2,Dorm3,11) == 1   #FFF
    assert DA.dorm_assign(Dorm4,Dorm5,Dorm6,11) == 3   #FFF
    assert DA.dorm_assign(Dorm1,Dorm7,Dorm8,11) == 3   #TTF
    assert DA.dorm_assign(Dorm1,Dorm9,Dorm8,11) == 2   #TFT
    assert DA.dorm_assign(Dorm10,Dorm9,Dorm8,11) == 1  #FTT
    assert DA.dorm_assign(Dorm2,Dorm7,Dorm3,11) == 3  #FTF
    assert DA.dorm_assign(Dorm4,Dorm5,Dorm1,11) == 2  #FFT


