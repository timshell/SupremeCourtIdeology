"""
Mayank Agrawal (timshell)
Imports all SC cases from csv file
"""
import csv
justicesCSV = 'justices20102014.csv'

justicesDict = {
	105: 'Scalia',
	106: 'Kennedy',
	108: 'Thomas',
	109: 'Ginsburg',
	110: 'Breyer',
	111: 'Roberts',
	112: 'Alito',
	113: 'Sotomayor',
	114: 'Kagan'
}

class Case(object):

	def __init__(self, caseID, majorityNum, minorityNum, caseName, justicesDict):

		self.caseID = caseID
		self.majorityNum = majorityNum
		self.minorityNum = minorityNum
		self.majorityArray = []
		self.minorityArray = []
		self.caseName = caseName
		self.justicesDict = justicesDict    	

	def addVote(self, justiceID, vote):
		if vote == 2:
		    self.minorityArray.append(justiceID)
		else:
		    self.majorityArray.append(justiceID)

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

	def __str__(self):

		stringToReturn = '\nCase: ' + self.caseName + '\n\n' + 'Majority: \n'

		for justiceID in self.majorityArray:
			justiceName = self.justicesDict[justiceID]
			stringToReturn +=  ' - ' + justiceName + '\n'
		
		stringToReturn += ' \nMinority: \n'
		for justiceID in self.minorityArray:
			justiceName = self.justicesDict[justiceID]
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
				currentCase = Case(caseID, majVotes, minVotes, caseName, justicesDict)
				allCases.append(currentCase)

			if row['vote'] != '':

				vote = int(row['vote'])
				currentCase.addVote(justiceID,vote)

	#verifyData(allCases)

	return allCases

def verifyData(lstOfCases):
	for case in lstOfCases:
		if (len(case.getMinorityArray()) != case.getMinorityNum()) or (len(case.getMajorityArray()) != case.getMajorityNum()):
			print case


loadData()












