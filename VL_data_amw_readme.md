# This code will help analyze VL data and prepare it for the viral load report
	* The most current version of the script is VL_data_amw_v3
The input file needs to be a text file (tsv). This can be downloaded from EHR in the correct format.
To run the program it is easiest to be in the same directory as the program. You can use cd to change directories.
This program needs to be run in python3 with pandas and numpy installed. 
###	Check the version of python by typing python into the terminal
	In python you can check whether pandas is installed by typing import pandas into the terminal. The same can be done for numpy.
	
To install python3 download it and follow instructions in installer. Once python3 is installed we need to install pandas. Use the command pip3 install pandas from the bash terminal
	* if you get a syntax error you may need to install pip using the command sudo apt-get install pip3

## To run:
	in command line type: python3 then program name -i then drag the input file into the terminal. Hit enter
       ex: >> python3 VL_data_amw_v3 -i (drag in input file)
The output file will be found in the same folder as the input file, with the same name as the input file, with the extension:  _averaged.csv