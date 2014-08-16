#This function takes in a query and parses out the Table name and returns that tablename - used in the execute function
def parseTableName(query):
	stringList = query.split()
	tableNameFound = False
	for i in stringList:
		if tableNameFound:
			return i
		elif str(i).lower() == "from":
			tableNameFound = True
		else:
			pass
	return "FAILED: parseTableName() - no TableName Found"

#This function takes in a query and parses out the list of columns requested in a select statment
#aliasingOn is a boolean parameter that dictates wether aliased output will display the table name (aliasing=False) or the alias (aliasing=True)
	#it is set by default to true
def parseColNames(query, aliasingOn = True):
	colList = extractColNames(preKeyWords(postSelect(query)),aliasingOn)
	#print colList
	return colList

#This function is used in parseColNames(), it takes in a query as a string and returns a whitespace split list with all the values after the first SELECT keyword
def postSelect(query):
	queryList = query.split()
	queryListLower = query.lower().split()
	try:
		sIndex = queryListLower.index('select') + 1
		return queryList[sIndex:]
	except:
		return []

#This function is used in parseColNames(), it takes in a postSelect() outputed list and return a whitespace split list with all the values before a listed sql keyword
def preKeyWords(queryList):
	sqlKeys = ['from','where']
	capIndex = len(queryList)
	queryListLower = []
	for string in queryList:
		queryListLower.append(string.lower())
	for key in sqlKeys:
		try:
			newIndex = queryListLower.index(key)
			if newIndex < capIndex:
					capIndex = newIndex
		except:
			pass
	return queryList[:capIndex]

#This function is used in parseColNames(), it takes in a preKeyWords(postSelect()) outputed list and returns a list of Column Names / Aliases
#aliasingOn is a boolean parameter that dictates wether aliased output will display the table name (aliasing=False) or the alias (aliasing=True)
	#it is set by default to true
def extractColNames(queryList,aliasingOn=True):
	query = ""
	for string in queryList:
			query += " " + string
	querySplit = query.split(',')
	colList = []
	for col in querySplit:
		newCol = col.rstrip().lstrip()
		newColLower = newCol.lower()
		newCol = newCol.split()
		newColLower = newColLower.split()
		if len(newCol) == 1:
			colList.append(newCol[0])
		elif 'as' in newColLower and aliasingOn == True:
			alias = ""
			for i in range((newColLower.index('as')+1),len(newCol)):
				alias += newCol[i] + " "
			alias = alias[:-1]
			if alias.endswith('"') or alias.endswith("'") or alias.endswith(']'):
				alias = alias[1:-1]
			colList.append(alias)
		elif 'as' in newColLower and aliasingOn == False:
			colList.append(newCol[0])
		else:
			colList.append("No Column or Alias Detected")
	if '*' in colList:
		return []
	return colList