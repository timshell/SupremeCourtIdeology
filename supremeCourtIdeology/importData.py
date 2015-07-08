"""
Mayank Agrawal (timshell)
Imports all SC cases from csv file
"""

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
    def __init__(self, caseID, majorityNum, minorityNum, caseName):
        self.caseID = caseID
        self.majorityNum = majorityNum
		self.minorityNum = minorityNum
		self.majorityArray = []
		self.minorityArray = []
		self.caseName = caseName    	

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

    def __str__(self):
		print
		print 'Case: %s' (self.caseName)
		print
		print 'Majority: \n'
		for justiceID in self.majorityArray:
		    print ' - %s \n' (justicesDict(justiceID))
		print 'Minority: \n'
		for justiceID in self.minorityArray:
	            print ' - %s \n' (justicesDict(justiceID))


casesToImport = open('SCDB_2014_01_justiceCentered_Citation.csv', 'r')
allCases = []
currentCaseID = ''
casesToImport.readline() #gets rid of headers
currentCase = None
currentLine = casesToImport.readline()
while currentLine != '':

    line = casesToImport.strip()
    line = line.split(',')
    """
    Indices:
 	 0: CaseID
	-1: Vote
	-2: Justice Name
	-3: Justice ID
	-4: Minority Votes
	-5: Majority Votes
	(1:-5): CaseName
    """
    if line[0] != currentCaseID:
	currentCase = allCases.append(Case(line[0], line[-5], line[-4], line[1:-5].join(',')))
	
    currentCase.addVote(line[-3],int(line[-1])
    currentLine = casesToImport.readline()

	
