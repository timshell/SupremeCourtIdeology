"""
Mayank Agrawal (timshell)
Analyzes data of SCOTUS rulings

7/10/15 MA wrote dissentJudges, ideologicalSplit
"""

from helper import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dissentingJudges(allCases):

	# Lists indicating how many judges were in the minority
	zeroDissent = []
	oneDissent = []
	twoDissent = []
	threeDissent = []
	fourDissent = []

	variationsOfDissent = {
		0: zeroDissent,
		1: oneDissent,
		2: twoDissent,
		3: threeDissent,
		4: fourDissent,
	}

	lstOfDissent = []
	for i in range(len(variationsOfDissent)):
		lstOfDissent.append(variationsOfDissent[i])

	for case in allCases:
		# Load into lists based on number of dissenting judges
		variationsOfDissent[case.getMinorityNum()].append(case)


	for key in variationsOfDissent:
		nineJudges = []
		eightJudges = []
		
		for case in variationsOfDissent[key]:
			if (case.getMinorityNum() + case.getMajorityNum()) == 9:
				nineJudges.append(case)
			else:
				eightJudges.append(case)

		print '\n %d dissenters:' % (key)
		print '\t - 8 Judges: %d' % len(eightJudges)
		print '\t - 9 Judges: %d' % len(nineJudges)

def ideologicalSplit(lstOfCases):

	# refer to justicesDict in helper.py
	liberalBloc = [106, 109, 110, 113, 114]
	conservativeBloc = [105, 106, 108, 111, 112]

	ideologicalSplit = 0

	for case in lstOfCases:
		if isSubset(case.getMinorityArray(), liberalBloc) or isSubset(case.getMinorityArray(), conservativeBloc):
			ideologicalSplit += 1

	return ideologicalSplit

def main():

	allCases = loadData()
	dissentingJudges(allCases)

	numConVotes = []
	numLibVotes = []

	for key in justicesDict:
		numConVotes.append(justicesDict[key].getConservativeVotes())
		numLibVotes.append(justicesDict[key].getLiberalVotes())
	
	plt.scatter(np.array(numConVotes), np.array(numLibVotes))
	plt.show()
	

main()






