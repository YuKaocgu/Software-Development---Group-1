import Band_Assignment as BA
import Dorm_Assign as DA
import Applications_submission as app_sub
import After_Director_decisions as after_sub
import CheckIn as CI
import Group_Change_Menu as Group_Change
import Report_Menu as Report

def main():
    while True:
        humanInput = input ('\n'.join(['Menu: ','1: Input Applications', '2: Write Directors Decisions', '3: Run Band Assignment', '4: Run Dorm Assignment', '5: CheckIn' , '6: M and F bands', '7: Manual switch', '8: Print report','9: Exit', '']))
        while humanInput not in ['1','2','3','4', '5','6','7','8','9']:
            print ('invalid input')
            humanInput = input ('\n'.join(['Menu: ','1: Input Applications', '2: Write Directors Decisions', '3: Run Band Assignment', '4: Run Dorm Assignment', '5: CheckIn' , '6: M and F bands', '7: Manual switch', '8: Print report','9: Exit', '']))
        if humanInput == '1':
            app_sub.Applications()
        if humanInput == '2':
            after_sub.editApplication()
        if humanInput == '3':
            BA.First_Band_Assign()
            print("Bands successfully assigned") 
        if humanInput == '4':
            DA.start_assign()
            print("Dorms successfully assigned") 
        if humanInput == '5':
            CI.CheckIn()
        if humanInput == '6':
            BA.Second_Band_Assign()
            print("Bands successfully assigned into groups of all Males and All Females") 
        if humanInput == '7':
            Group_Change.change_menu()
        if humanInput == '8':
            Report.report_main()
        if humanInput == '9':
            break
    
    
