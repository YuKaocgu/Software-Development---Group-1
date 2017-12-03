import Group_BA as RBA
import Group_DA as RDA

#def change_main_main():
while True:
    humanInput = input ('\n'.join(['Replacement Menu: ','1: By Bands', '2: By Dorms', '0: Exit Program', '']))
    while humanInput not in ['1','2','0']:
        print ('Invalid Input')
        humanInput = input ('\n'.join(['Replacement Menu: ','1: By Bands', '2: By Dorms', '0: Exit Program','']))
    if humanInput == '1':
        RBA.main()

    if humanInput == '2':
        RDA.main()
    if humanInput == '0':
        break

