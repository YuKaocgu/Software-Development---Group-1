Coverage tutorial:
1. make sure installing py.test and coverage.py
2. If not, using the code in command line:
	pip install pytest
	pip install coverage
3.Make sure the corrent path is the test folder.
ex: In the begining could be C:\Users\user1\
Using cd folderName to move to the next layer utnil it's the test folder.
ex: Type in "cd Desktop" in command line to let the path being C:\Users\user1\Desktop\
    Type in "cd.." to go to the previous layer.

To test Band, make sure the path is in ...\Coverage\Band (Same to the dorm)

4. Run the following code to run test
"coverage run --source Band -m py.test"  (If it's Dorm, change the word 'Dorm' to 'Band')

5. See the report
Using the code "coverage report" to see the report