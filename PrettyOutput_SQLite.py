import SQLiteCustomQueryTemplate as backend

def outputFormat(output,divider = " ",nameInclude = False,tableName = "",typeInclude = False):
	newOutput = "..."
	if isinstance(output,list):
		if len(output) == 0: 
			return "[]"
		maxLengths = []
		titles = []
		#This if statement initializes the titles list which holds the column names
		if nameInclude:
			query = "PRAGMA table_info(" + str(tableName) + ")"
			colNames = backend.execute(query)
			#print query
			#print colNames
			if isinstance(colNames,list):
				for i in range(len(output[0])):
					newTitle = str(colNames[i][1])
					if typeInclude:
						newTitle += "(" + str(colNames[i][2]) + ")"
					titles.append(newTitle)
			else:
				print "FAILED: prettyOutput_SQLite.outputForma() - invalide entry"
				nameInclude = False
				typeInclude = False
		#print titles
		#This loop finds the largest string in each column and stores that data for later use
		for i in range(len(output[0])): #cycle columns
			maxL = 0
			if nameInclude:
				newOutput += "\n"
				maxL = len(titles[i])
			for j in range(len(output)): #cycle rows
				if  maxL < len(str(output[j][i])):
					maxL = len(str(output[j][i]))
			maxLengths.append(maxL)
		#This loop adds the column names to the output
		for t in titles:
			newOutput += str(t) + str(divider)
		#This loop formats the output
		for i in range(len(output)): #cycle rows
			newOutput += "\n"
			for j in range(len(output[i])):
				newOutput += str(output[i][j])
				for k in range(len(str(output[i][j])),maxLengths[j]):
					newOutput += " "	
				newOutput += str(divider)
		return newOutput
	else:
		return output

#--------------------
#------Tests---------
#--------------------
#backend.dbConnect('test.db')

#output = backend.selectStar('pokemon where num1 < 9')
#output = backend.execute('select * from pokemon where num1 < 22')
#print isinstance(output,list)
#print output
#print outputFormat(output,divider=" ",nameInclude=True,tableName="pokemon",typeInclude=True)

#backend.dbClose()