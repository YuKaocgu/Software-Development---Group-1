import Band_Assignment as BA
import Dorm_Assign as DA
import Applications_submission as app_sub
import After_Director_decisions as after_sub
import CheckIn as CI

def main():
    while True:
        humanInput = input ('\n'.join(['Menu: ','1: Input Applications', '2: Write Directors Decisions', '3: Run Band Assignment', '4: Run Dorm Assignment', '5: CheckIn' , '6: Exit Program', '']))
        while humanInput not in ['1','2','3','4', '5','6']:
            print ('invalid input')
            humanInput = input ('\n'.join(['Menu: ','1: Input Applications', '2: Write Directors Decisions', '3: Run Band Assignment', '4: Run Dorm Assignment', '5: CheckIn','6: Exit Program', '']))
        if humanInput == '1':
            app_sub.Applications()
        if humanInput == '2':
            after_sub.editApplication()
        if humanInput == '3':
            BA.band_assign()
        if humanInput == '4':
            DA.start_assign()
        if humanInput == '5':
            CI.CheckIn()
        if humanInput == '6':
            break
    