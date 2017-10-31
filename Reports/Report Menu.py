import Report_BA as RBA
import Report_DA as RDA

def report_main():
    while True:
        humanInput = input ('\n'.join(['Report Menu: ','1: Assigned Bands', '2: Assigned Dorms', '6: Exit Program', '']))
        while humanInput not in ['1','2','3','4', '5','6']:
            print ('invalid input')
            humanInput = input ('\n'.join(['Report Menu: ','1: Assigned Bands', '2: Assigned Dorms', '6: Exit Program', '']))
        if humanInput == '1':
            RBA.report_band_assignment()
        if humanInput == '2':
            RDA.report_dorm_assignment()
        if humanInput == '6':
            break