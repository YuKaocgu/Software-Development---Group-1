import Report_BA as RBA
import Report_DA as RDA

def report_main():
    while True:
        humanInput = input ('\n'.join(['Report Menu: ','1: Assigned Bands', '2: Assigned Dorms', '0: Exit Program', '']))
        while humanInput not in ['1','2','0']:
            print ('Invalid Input')
            break
        if humanInput == '1':
            RBA.report_band_assign()
        if humanInput == '2':
            RDA.report_dorm_assign()
        if humanInput == '0':
            break
