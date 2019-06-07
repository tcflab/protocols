import pandas as pd
import argparse
import os
import numpy as np

parser = argparse.ArgumentParser(description='Script to average viral load and CT metrics in Viral Services tsv')
parser.add_argument('-i',metavar='input', type=str,help="input results")
parser.add_argument('-o',metavar='output', type=str,help="merged output results", default="")
args = parser.parse_args()


inputfile = pd.read_csv(args.i, sep = "\t")
inputfilename = args.i.split(".")[:-1]
if not args.o:
	outputfilename = "".join(inputfilename) + "_averaged.csv"
else:
	outputfilename = args.o

inputfile.fillna("", inplace=True)
inputfile['CT'] = pd.to_numeric(inputfile['CT'])
columnstokeep = ['Subject Id', 'Run Date', 'Experiment', 'Nucleic Acid Type', 'Sample Date', 'Assay Name', 'Folder', 'Source Material', 'Comment']

inputfile = inputfile.groupby(columnstokeep, as_index=False, sort=False)['Viral Load', 'CT'].mean()

#this next line will replace Viral Load values that are <100 with the string <100
for i, VL in inputfile['Viral Load'].iteritems():
#we need to iterate through the series (this is not a list). iteritems has 2 values for each position in the row, the index (which we define as i) and our variable defined as VL 	
	if VL <= 100:
		inputfile['Viral Load'].replace(VL, "< 100", inplace=True)
	elif VL > 100: #this next line converts the viral load values to scientific notation
		inputfile.loc[i,['Viral Load']] = np.format_float_scientific(VL, precision=2, exp_digits=2)
		
results = inputfile.loc[:, ['Subject Id', 'Sample Date', 'Source Material', 'Comment', 'Viral Load']]
print (results)
outputfile = results.to_csv(os.path.join(outputfilename), index=False)
