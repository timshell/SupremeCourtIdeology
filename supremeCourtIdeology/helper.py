"""
Mayank Agrawal (timshell)
Imports all SC cases from csv file

07/08/15 MA wrote it
07/10/15 MA edited verifyData
			added comments
			created isSubset
07/11/15 MA created Justice class
10/14/15 MA fixed loading in Data
			created string and get functions for
			Justice class
testing git commits via subl
"""
import csv
justicesCSV = 'justices20102014.csv'

class Justice(object):

	def __init__(self, name):

		self.name = name
		self.conservativeVotes = 0
		self.liberalVotes = 0

	def addVoteDirection(self, direction):
		# 1 = conservative; 2 = liberal
		if direction == 1:
			self.conservativeVotes += 1
		else:
			self.liberalVotes += 1

	def getName(self):
		return self.name

	def getConservativeVotes(self):
		return self.conservativeVotes

	def getLiberalVotes(self):
		return self.liberalVotes

	def __str__(self):

		"""
		Justice Name: __________
			Conservative Votes: __________
			Liberal Votes: __________
		"""
		stringToReturn = '\nJustice Name: ' + self.name + ' \n'
		stringToReturn += '\tConservative Votes: ' + str(self.conservativeVotes) + '\n'
		stringToReturn += '\tLiberal Votes: ' +  str(self.liberalVotes) + '\n'
		return stringToReturn

justicesDict = {
	105: Justice('Scalia'),
	106: Justice('Kennedy'),
	108: Justice('Thomas'),
	109: Justice('Ginsburg'),
	110: Justice('Breyer'),
	111: Justice('Roberts'),
	112: Justice('Alito'),
	113: Justice('Sotomayor'),
	114: Justice('Kagan')
}

class Case(object):

	def __init__(self, caseID, majorityNum, minorityNum, caseName):

		self.caseID = caseID
		self.majorityNum = majorityNum
		self.minorityNum = minorityNum
		self.majorityArray = []
		self.minorityArray = []
		self.caseName = caseName
		self.caseIdeology = None    	

	def addVote(self, justiceID, vote, direction):
		if vote == 1: #1: dissent
		    self.minorityArray.append(justiceID)
		else: #2: majority
		    self.majorityArray.append(justiceID)

		justicesDict[justiceID].addVoteDirection(direction)

		if self.caseIdeology == None and vote == 2:
			if direction == 1:
				self.caseIdeology = 'conservative'
			elif direction == 2:
				self.caseIdeology = 'liberal'

	def getMajorityNum(self):
		return self.majorityNum

	def getMinorityNum(self):
		return self.minorityNum

	def getMajorityArray(self):
		return self.majorityArray

	def getMinorityArray(self):
		return self.minorityArray  

	def getCaseName(self):
		return self.caseName

	def getCaseIdeology(self):
		return self.caseIdeology   

	def __str__(self):

		"""
		For 5-4 split case, string will look as:

		Case Name: __________

		Majority:
		
			- Judge 1
			- Judge 2
			- Judge 3
			- Judge 4
			- Judge 5

		Minority:
			
			- Judge 6
			- Judge 7
			- Judge 8
			- Judge 9
		"""

		stringToReturn = '\nCase: ' + self.caseName + '\n\n' + 'Majority: \n'

		for justiceID in self.majorityArray:
			justiceName = justicesDict[justiceID].getName()
			stringToReturn +=  ' - ' + justiceName + '\n'
		
		stringToReturn += ' \nMinority: \n'
		
		for justiceID in self.minorityArray:
			justiceName = justicesDict[justiceID].getName()
			stringToReturn +=  ' - ' + justiceName + '\n'

		return stringToReturn




def loadData():

	with open(justicesCSV) as csvfile:
		
		casesToImport = csv.DictReader(csvfile)
		currentCaseID = ''
		currentCase = None
		allCases = []

		for row in casesToImport:
			
			caseID = row['caseID']
			justiceID = int(row['justiceID'])
			
			if caseID != currentCaseID:
				currentCaseID = caseID
				caseName = row['caseName']
				majVotes = int(row['majVotes'])
				minVotes = int(row['minVotes'])
				currentCase = Case(caseID, majVotes, minVotes, caseName)
				allCases.append(currentCase)

			if (row['majority'] != '') & ((justiceID not in currentCase.getMinorityArray()) & \
				(justiceID not in currentCase.getMajorityArray())):
				# the right side of the and statement makes sure cases are not counted twice
				# (they are sometimes included multiple times in the .csv)

				if row['direction'] != '':
					direction = int(row['direction'])
				else:
					direction = 0
				vote = int(row['majority'])
				
				currentCase.addVote(justiceID,vote, direction)

	assert(verifyData(allCases))
	return allCases

def verifyData(lstOfCases):
	for case in lstOfCases:
		if (len(case.getMinorityArray()) != case.getMinorityNum()) or (len(case.getMajorityArray()) != case.getMajorityNum()):
			print case
			return False
	return True


def isSubset(smallLst, bigLst):

	for element in smallLst:
		if element not in bigLst:
			return False
	return True









