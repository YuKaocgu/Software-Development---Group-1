from Register import *
import Register as RA
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:35:53 2017

@author: ChristofferGamborg
"""
from datetime import timedelta, datetime

camp1=datetime.strptime("06-10-17", "%m-%d-%y")
camp2=datetime.strptime("07-08-17", "%m-%d-%y")
camp3=datetime.strptime("08-05-17", "%m-%d-%y")
def test_Register():
    """ Test fillData """
    assert RA.fillData('N') == False
    assert RA.fillData('n') == False
    assert RA.fillData('y') == True
    assert RA.fillData('1') == False
    assert RA.fillData('nj') == False
        
    """ Test timeCheck """
    assert RA.timeCheck ('04-12-17', '1') == True
    assert RA.timeCheck ('05-09-17', '1') == False
    assert RA.timeCheck ('05-08-17', '1') == True
    assert RA.timeCheck ('03-12-17', '1') == False
    assert RA.timeCheck ('03-13-17', '1') == True

    """ Test checkIfY """
    assert RA.checkIfY('y') == True
    assert RA.checkIfY('Y') == True
    assert RA.checkIfY('1') == False
    assert RA.checkIfY('n') == False
    assert RA.checkIfY('N') == False

    """ Test CheckIfYorN """
    assert RA.checkIfYorN('n') == True
    assert RA.checkIfYorN('N') == True
    assert RA.checkIfYorN('y') == True
    assert RA.checkIfYorN('Y') == True
    assert RA.checkIfYorN('yn') == False
    assert RA.checkIfYorN('a') == False
    assert RA.checkIfYorN('1') == False



 
