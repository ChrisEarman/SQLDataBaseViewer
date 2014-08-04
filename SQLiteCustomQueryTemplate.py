import sqlite3

#--------------------------------
#-Database Connection Functions--
#--------------------------------

#This function takes in a database name as a string 'dbName' and attempts to establish a connection to it
#If the database does not already exist this function creates the database
def dbConnect(dbName):
	global db
	global cursor
	try:
		db = sqlite3.connect(dbName)
		cursor = db.cursor()
		return "SUCCESS"
	except: 
		return "FAILED: dbConnection() - An Unexpected Error Occured"

#This function commits the current version of the current database to memory
def dbCommit():
	try:
		db.commit()
		return "SUCCESS"
	except NameError:
		return "FAILED: dbCommit() - NameError, most likely cause: db is not defined"
	except sqlite3.ProgrammingError:
		return "FAILED: dbCommit() - ProgrammingError, most likely cause: Cannot operate on a closed database"
	except:
		return "FAILED: dbCommit() - An Unexpected Error Occured"

#This function closes the current database connection
def dbClose():
	try:
		db.close()
		return "SUCCESS"
	except NameError:
		return "FAILED: dbClose() - NameError, most likely cause: db is not defined"
	#except:
		return "FAILED: dbClose() - An Unexpected Error Occured"



#--------------------------------
#--------Query Functions---------
#--------------------------------

#This function takes in a string 'query' and attempts to execute that string as a sql query
def execute(query):
	try:
		cursor.execute(query)
		retVal = cursor.fetchall()
		return retVal
	except:
		return "FAILED: execute() - proofread your query and make sure all connections are established correctly"

#This function takes in a string 'tableName', a list of strings 'columns', and a second list of strings 'types'
#If no types are specified then they default to text
#These are the parameters needed to properly create a SQLite table
def createTable(tableName,columns,types=[]):
	#cursor.execute("drop table if exists temps")
	query = "create table " + str(tableName) + "(" 
	if len(types) == 0:
		types = ["text"]*len(columns)
	if (len(columns) == len(types)):
		for i in range(0,len(columns)):
			query += str(columns[i]) + " " + str(types[i]) + ","
		query = query[:-1] + ")"
		#print(query)
	else: return "FAILED: list lenght mismatch between 'columns' and 'types'"

	try:
		cursor.execute(str(query))
	except sqlite3.OperationalError:
		return ("FAILED: createTable() - sqlite3.OperationalError, most likely cause: Table '"
	 	+ str(tableName) 
	 	+ "' already exists")
	except sqlite3.Warning:
		return "FAILED: updateWhere() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: createTable() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: createTable() - An Unexpected Error Occured"
	return "SUCCESS"
	#return query

#This function takes in a string 'tableName', finds the table denoted by that string, and deletes it from the database
def deleteTable(tableName):
	query = "drop table " + str(tableName)
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return ("FAILED: deleteTable() - sqlite3.OperationalError, most likely cause: Table '" + str(tableName) + "' does not exist")
	except sqlite3.Warning:
		return "FAILED: updateWhere() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: deleteTable() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: deleteTable() - An Unexpected Error Occured"
	return "SUCCESS"

#This function takes in a string 'tableName' and two lists of strings 'columns' and 'data'
#'tableName' signifies the name of the table in which the insert will occur
#'columns' signifies the columns of the table for which data will be provided
	#if no column list is provided then it is assumed 'data' will contain one element per column in the table
	#it is also assumed that this data will be in order and of the correct type
#'data' signifies the data that will be inserted into the designated columns
def insertInto(tableName, data, columns=[]):
	query = "insert into " + str(tableName) + " ("
	if len(columns) != 0:
		for col in columns:
			query += str(col)+ ","
		query = query[:-1] + ")"
	else:
		query = query[:-1]
	query += " values ("
	for d in data:
		print d
		query += "'" + str(d) + "',"
	query = query[:-1] + ")"
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return ("FAILED: insertInto() - sqlite3.OperationalError, most likely cause: Table '" + str(tableName) + "' does not exist")
	except sqlite3.IntegrityError:
		return ("FAILED: insertInto() - sqlite3.IntegrityError, most likely cause: column constraint not met (e.g. inserting non unique value into column with a unique constraint)")
	except sqlite3.Warning:
		return "FAILED: insertInto() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: insertInto() - NameError, most likely cause: failing to establish a connection to a database"
	#except:
	#	return "FAILED: insertInto() - An Unexpected Error Occured"
	return "SUCCESS"

#This function takes in a string 'tableName' and displays all of the data from that table
def selectStar(tableName):
	query = "select * from " + str(tableName)
	try:
		cursor.execute(query)
		#print(cursor.fetchall())
	except sqlite3.OperationalError:
		return ("FAILED: selectStar() - sqlite3.OperationalError, most likely cause: Table '" + str(tableName) + "' does not exist")
	except sqlite3.Warning:
		return "FAILED: selectStar() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: selectStar() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: selectStar() - An Unexpected Error Occured"
	return cursor.fetchall()

#This function is a simple select which takes in a required string 'tableName' an optional list of strings 'columns' and two optional strings 'whereColumn' and 'whereData'
#'tableName' signifies the table from which data is being selected
#'columns' signifies the list of columns that will be displayed
	#ommitting this parameter results in selecting all columns (*)
#'whereColumn' signifies the column for the where clause to check
#'whereData' signifies the data for the where clause to check for in column 'whereColumn'
#e.g. "select columns from tableName where whereColumn LIKE 'whereData'"
def select(tableName,whereColumn="",whereData="",columns="*",operand = "LIKE"):
	query = "select "
	if len(columns) == 0:
		columns="*"
	if len(operand) == 0:
		operand = "LIKE"
	for col in columns:
		query += " " + str(col) + ","
	query = query[:-1]
	query += " from " + str(tableName)
	if len(whereColumn) != 0:
		query += " where " + str(whereColumn) + " " + str(operand) + " '" + str(whereData) + "'"
	#print(query)
	try:
		cursor.execute(query)
		#print(cursor.fetchall())
	except sqlite3.OperationalError:
		return "FAILED: select() - sqlite3.OperationalError, most likely causes: a listed column, table, or operand does not exists"
	except sqlite3.Warning:
		return "FAILED: select() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: select() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: select() - An Unexpected Error Occured"
	return cursor.fetchall()

#This function takes in a string 'tableName', two lists of strings 'whereColumns' and 'whereData', and an optional list of strings 'columns'
#'tableName' signifies the table from which data is being selected
#'columns' signifies the list of columns that will be displayed
	#ommitting this parameter results in selecting all columns (*)
#'whereColumn' signifies the list of column for the WHERE AND clause to check
#'whereData' signifies the list data for the WHERE AND clause to check for in the respective columns listed in 'whereColumns'
#e.g. "select columns from tableName where whereColumn[0] LIKE 'whereData[0]' AND whereColumn[1] LIKE 'whereData[1]' AND ...."
def selectAND(tableName,whereColumns,whereData,columns="*",operand="LIKE"):
	query = "select "
	if len(whereColumns) != len(whereData):
		return "FAILED: selectAND() - lists whereColumns and whereData contain a different number of elements"
	elif len(whereColumns) == 1:
		return "FAILED: selectAND() - list whereColumns only contains one element, for simple selects use the select() function"	
	for col in columns:
		query += " " + str(col) + ","
	query = query[:-1]
	query += " from " + str(tableName) + " where "
	for i in range(0,len(whereColumns)):
		query += "(" + str(whereColumns[i]) + " " + str(operand) + " '" + str(whereData[i]) + "') AND "
	query = query[:-4]
	#print(query)
	try:
		cursor.execute(query)
		#print(cursor.fetchall())
	except sqlite3.OperationalError:
		return "FAILED: selectAND() - sqlite3.OperationalError, most likely causes: a listed column, table, or operand does not exists"
	except sqlite3.Warning:
		return "FAILED: selectAND() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: selectAND() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: selectAND() - An Unexpected Error Occured"
	return cursor.fetchall()

#This function takes in a string 'tableName', two lists of strings 'whereColumns' and 'whereData', and an optional list of strings 'columns'
#'tableName' signifies the table from which data is being selected
#'columns' signifies the list of columns that will be displayed
	#ommitting this parameter results in selecting all columns (*)
#'whereColumn' signifies the list of column for the WHERE OR clause to check
#'whereData' signifies the list data for the WHERE OR clause to check for in the respective columns listed in 'whereColumn'
#e.g. "select columns from tableName where whereColumn[0] LIKE 'whereData[0]' OR whereColumn[1] LIKE 'whereData[1]' OR ...."
def selectOR(tableName,whereColumns,whereData,columns="*",operand="LIKE"):
	query = "select "
	#print(str(len(whereColumns)) + " : " + str(len(whereData)))
	if len(whereColumns) != len(whereData):
		return "FAILED: slectOR() - lists whereColumns and whereData contain a different number of elements"
	elif len(whereColumns) == 1:
		return "FAILED: selectOR() - list whereColumns only contains one element, for simple selects use the select() function"	
	for col in columns:
		query += " " + str(col) + ","
	query = query[:-1]
	query += " from " + str(tableName) + " where "
	for i in range(0,len(whereColumns)):
		query += "(" + str(whereColumns[i]) + " " + str(operand) + " '" + str(whereData[i]) + "') OR "
	query = query[:-4]
	#print(query)
	try:
		cursor.execute(query)
		#print(cursor.fetchall())
	except sqlite3.OperationalError:
		return "FAILED: selectOR() - sqlite3.OperationalError, most likely causes: a listed column, table, or operand does not exists"
	except sqlite3.Warning:
		return "FAILED: selectOR() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: selectOR() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: selectOR() - An Unexpected Error Occured"
	return cursor.fetchall()

#This function takes in two strings 'tableName' and whereColumn, a list of strings 'whereData', and an optional list of strings 'columns'
#'tableName' signifies the table from which data is being selected
#'columns' signifies the list of columns that will be displayed
	#ommitting this parameter results in selecting all columns (*)
#'whereColumn' signifies column for the WHERE IN clause to check
#'whereData' signifies the list data for the WHERE IN clause to check for within 'whereColumn'
	#the value in this variable is case sensitive
#e.g. "select columns from tableName where whereColumn IN (whereData[0],whereData[1],whereData[2],.....)
def selectIN(tableName,whereColumn,whereData,columns="*"):
	query = "select "
	for col in columns:
		query += " " + str(col) + ","
	query = query[:-1]
	query += " from " + str(tableName) + " where " + str(whereColumn) + " in ("
	for dat in whereData:
		query += "'" + str(dat) + "',"
	query = query[:-1] + ")"
	try:
		cursor.execute(query)
		#print(cursor.fetchall())
	except sqlite3.OperationalError:
		return "FAILED: selectIN() - sqlite3.OperationalError, most likely cause: a listed column does not exist or table does not exists"
	except sqlite3.Warning:
		return "FAILED: selectIN() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: selectIN() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: selectIN() - An Unexpected Error Occured"
	return cursor.fetchall()

#This function takes in three strings 'tableName', 'whereCol', and 'whereData' and two lists of strings 'setCols' and 'setData'
#'tableName' signifies the table from which data is being selected
#'setCols' is a list of columns to be updated
#'setData' is a list of data to be entered into the columns listed by 'setCols'
#'whereCol' is the column name for the WHERE clause
	#This variable is not type sensitive
#'whereData' is the data we wish to find in the column 'whereCol' from the WHERE clause
def updateWhere(tableName,setCols,setData,whereCol,whereData,operand="LIKE"):
	query = "update " + str(tableName) + " set "
	if len(setCols) != len(setData):
		return "FAILED: updateWhere() - list length mismatch between 'setCols' and 'setData'"
	for i in range(0,len(setCols)):
		query += str(setCols[i])  + "='" + str(setData[i]) + "',"
	query = query[:-1] + " where " + str(whereCol) + " " + str(operand) + " '" + str(whereData) + "'"
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return "FAILED: updateWhere() - sqlite3.OperationalError, most likely causes: a listed column, table, or operand does not exists"
	except sqlite3.Warning:
		return "FAILED: updateWhere() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: updateWhere() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: updateWhere() - An Unexpected Error Occured"
	return "SUCCESS"

#This function takes in a string 'tableName' and four lists of strings 'setCols', 'setData', 'whereCols', and 'whereData'
#'tableName' signifies the table from which data is being selected
#'setCols' is a list of columns to be updated
#'setData' is a list of data to be entered into the columns listed by 'setCols'
#'whereCols' is the list of column names for the WHERE ANDclause
	#This variable is not type sensitive
#'whereData' is the list of data we wish to find in the columns listed by 'whereCols' from the WHERE AND clause
def updateWhereAND(tableName,setCols,setData,whereCols,whereData,operand="LIKE"):
	query = "update " + str(tableName) + " set "
	if len(setCols) != len(setData):
		return "FAILED: updateWhere() - list length mismatch between 'setCols' and 'setData'"
	for i in range(0,len(setCols)):
		query += str(setCols[i])  + "='" + str(setData[i]) + "',"
	query = query[:-1] + " where "
	for i in range(0,len(whereCols)):
		query += "(" + str(whereCols[i]) + " " + str(operand) + " '" + str(whereData[i]) + "') AND "
	query = query[:-4]
	#print(query)
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return "FAILED: updateWhereAND() - sqlite3.OperationalError, most likely causes: a listed column, table, or operand does not exists"
	except sqlite3.Warning:
		return "FAILED: updateWhereAND() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: updateWhereAND() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: updateWhereAND() - An Unexpected Error Occured"
	return "SUCCESS"

#This function takes in a string 'tableName' and four lists of strings 'setCols', 'setData', 'whereCols', and 'whereData'
#'tableName' signifies the table from which data is being selected
#'setCols' is a list of columns to be updated
#'setData' is a list of data to be entered into the columns listed by 'setCols'
#'whereCols' is the list of column names for the WHERE OR clause
	#This variable is not type sensitive
#'whereData' is the list of data we wish to find in the columns listed by 'whereCols' from the WHERE OR clause
def updateWhereOR(tableName,setCols,setData,whereCols,whereData,operand="LIKE"):
	query = "update " + str(tableName) + " set "
	if len(setCols) != len(setData):
		return "FAILED: updateWhere() - list length mismatch between 'setCols' and 'setData'"
	for i in range(0,len(setCols)):
		query += str(setCols[i])  + "='" + str(setData[i]) + "',"
	query = query[:-1] + " where "
	for i in range(0,len(whereCols)):
		query += "(" + str(whereCols[i]) + " " + str(operand) + " '" + str(whereData[i]) + "') OR "
	query = query[:-4]
	#print(query)
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return "FAILED: updateWhereOR() - sqlite3.OperationalError, most likely causes: a listed column, table, or operand does not exists"
	except sqlite3.Warning:
		return "FAILED: updateWhereOR() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: updateWhereOR() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: updateWhereOR() - An Unexpected Error Occured"
	return "SUCCESS"

#This function takes in two strings 'tableName' and 'whereCol', and it takes in three lists of strings 'setCols','setData', and 'whereData'
#'tableName' signifies the table from which data is being selected
#'setCols' is a list of columns to be updated
#'setData' is a list of data to be entered into the columns listed by 'setCols'
#'whereCol' is the column name for the WHERE IN clause
	#This variable is type sensitive
#'whereData' is the list of data we wish to find in the column 'whereCol' from the WHERE IN clause
def updateWhereIN(tableName,setCols,setData,whereCol,whereData):
	query = "update " + str(tableName) + " set "
	if len(setCols) != len(setData):
		return "FAILED: updateWhere() - list length mismatch between 'setCols' and 'setData'"
	for i in range(0,len(setCols)):
		query += str(setCols[i])  + "='" + str(setData[i]) + "',"
	query = query[:-1] + " where " + str(whereCol) + " in ("
	for dat in whereData:
		query += "'" + str(dat) + "',"
	query = query[:-1] + ")"
	#print query
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return "FAILED: updateWhereIN() - sqlite3.OperationalError, most likely cause: a listed column does not exist or table does not exists"
	except sqlite3.Warning:
		return "FAILED: updateWhereIN() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: updateWhereIN() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: updateWhereIN() - An Unexpected Error Occured"
	return "SUCCESS"

def delete(tableName,whereCol,whereData,operand="="):
	query = "delete from " + str(tableName) + " where " + str(whereCol) + " " + str(operand) + " '" + str(whereData) + "'"
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		return "FAILED: delete() - sqlite3.OperationalError, most likely cause: a listed column does not exist or table does not exists"
	except sqlite3.Warning:
		return "FAILED: delete() - sqlite3.Warning, most likely cause: attempted execution of multiple statements, possible SQL injection attempt...tisk,tisk"
	except NameError:
		return "FAILED: delete() - NameError, most likely cause: failing to establish a connection to a database"
	except:
		return "FAILED: delete() - An Unexpected Error Occured"
	return "SUCCESS"

#--------------------------------
#------------tests---------------
#--------------------------------

#dbConnect('HeyUsers.db')
#createTable("HeyUserSummary",["UserName","Alias","PhoneNumber"])
#insertInto("HeyUserSummary",['LadyKiller','Chris','1-000-000-0000'],['UserName','Alias','PhoneNumber'])
#insertInto("HeyUserSummary",['TheBigC','Karl','notAnInt'])
#insertInto("HeyUserSummary",['TheFlasker','Matt','1245'])
#selectStar("HeyUserSummary")
#print(updateWhere("HeyUserSummary",["Alias","PhoneNumber"],["Bob","199299"],"UserName","LadyKilleR"))
#print(updateWhere("HeyUserSummary",["Alias","PhoneNumber"],["Bob","199299"],"UserName","LadyKilleR'; drop table HeyUserSummary; '"))
#select("HeyUserSummary")
#print(selectOR("HeyUserSummary",["UserName","Alias"],["ladykiller","Karl"]))
#select("HeyUserSummary")
#print(selectIN("HeyUserSummary","Alias",["Karl","chris","matt"],["UserName"]))
#deleteTable("HeyUserSummary")
#dbCommit()
#print(dbCommit())
#dbClose()
#print(dbCommit())
#print("done")
#updateWhereAND("Table","abc","def","123","456")
#updateWhereOR("Table","abc","def","123","456")
#updateWhereIn("Table","abc","def","one","12345")