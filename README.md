# Software-Development---Group-1
Welcome to the Software-Development---Group-1 readme file 
We have developed a module for FuRS (Future Rock Stars) summer camp. It is a module intended to be run in your favorite Python application.

To run the program download all of the files in the finalproject folder and run the module main() in main.py. This will open a menu that connects all of the modules together, so you can run them in the order you would like.
There is a subfolder with our testfiles, please see the end of this document for instructions on how to run our test files.

There is a few things still to be done, most notably there is a catch problem with the report, in order for it to run properly you would need to close the project, restart the kernel and run the main.py again in order to see the array's in the python application.

we used a few special packages that you might need to pip install. If you are running through anaconda most of them should be installed, with the exception of pandasql please see the following list for all packages used:

    datetime
    xlsxwriter
    csv
    pandas
    pandasql
    warnings
    openpyxl
    numpy
    pytest

We have wrapped up the class for which this was developed, we will therefore not be updating any of the files in here. Feel free to download and use this in any way.

Test:
Coverage tutorial:
1. make sure you have installed py.test and coverage.py
2. If not, use the following code in command line:
	pip install pytest
	pip install coverage
3. Make sure you have the correct path to the test folder.
ex: it could be C:\Users\user1\
Using 'cd folderName' to move to the next layer until you reach the test folder.
ex: Type in "cd Desktop" in command line let the path be C:\Users\user1\Desktop\
    Type in "cd.." to go to the previous layer.

4. Test all the files
Using the code 'py.test' in command line to see run the automated test.
