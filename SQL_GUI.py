from Tkinter import *
import webbrowser
import SQLiteCustomQueryTemplate as backend
import PrettyOutput_SQLite as prettyOutput


main = Tk()
main.title("SQL_c")
main.geometry("902x350+100+100")
outputFrame = Frame(main)
executeFrame = Frame(main)
buttonFrame = Frame(main)

templateWin = Toplevel(main)
templateWin.title("Query Builder")
templateWin.geometry("900x200+100+100")
templateFrame = Frame(templateWin)
templateWin.withdraw()
frame0 = Frame(templateWin)

functionLabelVar = StringVar()
functionLabelVar.set("[NONE]")
functionLabel = Label (templateWin, text = functionLabelVar.get())
functionLabel.grid(row = 0, column = 0)

#-------------------------
#------buttonFrame--------
#-------------------------
def callConnect(event=[]):
	executeQuery('dbConnect')
def callCommit(event=[]):
	executeQuery('dbCommit')
def callClose(event=[]):
	executeQuery('dbClose')
def tempWinCloseButton():
	try:
		templateWin.withdraw()
	except:
		print "Invalid closeButton() Call"
def tempActivate(event=[]):
	templateWin.deiconify()
def runExecute(event=[]):
	executeQuery('execute')
def clearBoard(event=[]):
	#print 'clear'
	queryOutputField.config(state = "normal")
	queryOutputField.delete(0.0,END)
	queryOutputField.config(state = "disabled")

dbLabel = Label(buttonFrame, text = "DataBase")
dbLabel.grid(row = 0, column = 0, columnspan = 2)
dbEntry = Entry(buttonFrame, width = 15 , bd = 2)
dbEntry.bind("<Return>", callConnect)
dbEntry.grid(row = 1, column = 0)
dbConnectButton = Button(buttonFrame, text = "Connect", command = callConnect, width = 9)
dbConnectButton.grid(row = 1, column = 1)
dbCommitButton = Button(buttonFrame, text = "Commit", command = callCommit, width = 25)
dbCommitButton.grid(row = 2, column = 0, columnspan = 2)
dbCloseButton = Button(buttonFrame, text = "Close DataBase", command = callClose, width = 25)
dbCloseButton.grid(row = 3, column = 0, columnspan = 2)
templateButton = Button(buttonFrame, text = "Template", command = tempActivate, width = 25)
templateButton.grid(row = 4, column = 0, columnspan = 2)
clearBoardButton = Button(buttonFrame, text = "Clear Board", command = clearBoard, width = 25)
clearBoardButton.grid(row = 5, column = 0, columnspan = 2)
executeButton = Button(buttonFrame, text = "Run Query", command = runExecute, width = 25, height = 2)
executeButton.grid(row = 6, column = 0, columnspan = 2)

buttonFrame.grid(row = 0, column = 0, rowspan = 2, sticky = N)

#-------------------------
#templateFrame Attributes-
#-------------------------

templateWin.protocol('WM_DELETE_WINDOW',tempWinCloseButton)

templateFrame.grid(row=2, column = 1)
templateFrameSubs = [None]*10
labelStrings = [None]*10
labelTop = [None]*10
entryBox = [None]*10
for i in range(0,10):
	templateFrameSubs[i] = Frame(templateFrame)
	labelStrings[i] = StringVar()
	labelTop[i] = Label(templateFrameSubs[i], textvariable = labelStrings[i]).pack(side=TOP)
	entryBox[i] = Entry(templateFrameSubs[i])
	entryBox[i].pack(side=BOTTOM)

inputScrollbar = Scrollbar(executeFrame)
inputScrollbar.pack(side=RIGHT,fill=Y)
textTop = Text(executeFrame,width = 103, height = 10,yscrollcommand = inputScrollbar.set)
textTop.pack(side = LEFT, fill=BOTH)
executeFrame.grid(row = 0, column = 1)

inputScrollbar.config(command = textTop.yview)

#-------------------------
#-------menuBar-----------
#-------------------------

def donothing():
	filewin = Toplevel(main)
	label = Label(filewin, text="Info: No Action Preformed")
	label.pack()

def exit():
	backend.dbClose()
	main.quit()

prettyOutputOn = BooleanVar()
prettyOutputOn.set(True)
colNameInclude = BooleanVar()
colNameInclude.set(True)
colTypeInclude = BooleanVar()
colTypeInclude.set(True)
colDivider = StringVar()
colDivider.set(" | ")
def propertiesEdit():
	propertyWin = Toplevel(main)
	propertyWin.maxsize(200,200)
	propertyWin.minsize(200,200)
	propertyWin.title("Properties")
	prettyFrame = Frame(propertyWin)
	colNamesFrame = Frame(propertyWin)
	colTypesFrame = Frame(propertyWin)
	colDividerFrame = Frame(propertyWin)

	prettyOTrue = Radiobutton(prettyFrame, text="On",variable=prettyOutputOn,value=True)
	prettyOFalse = Radiobutton(prettyFrame, text="Off",variable=prettyOutputOn,value=False)
	colNamesTrue = Radiobutton(colNamesFrame, text="On",variable=colNameInclude,value=True)
	colNamesFalse = Radiobutton(colNamesFrame, text="Off",variable=colNameInclude,value=False)
	colTypesTrue = Radiobutton(colTypesFrame, text="On",variable=colTypeInclude,value=True)
	colTypesFalse = Radiobutton(colTypesFrame, text="Off",variable=colTypeInclude,value=False)
	colDividerEntry = Entry(colDividerFrame, textvariable=colDivider,width=13)
	prettyLabel = Label(prettyFrame, text = "Pretty Output:",width=20, anchor = W)
	colNamesLabel = Label(colNamesFrame, text = "Include Column Names:",width=20, anchor = W)
	colTypesLabel = Label(colTypesFrame, text = "Include Column Types:",width=20, anchor = W)
	colDividerLabel = Label(colDividerFrame, text = "Column Divider:", anchor = W)
	
	prettyLabel.grid(row = 0, column = 0)
	prettyOTrue.grid(row = 1, column = 0)
	prettyOFalse.grid(row = 1, column = 1)
	prettyFrame.grid(row = 0, column = 0, sticky = W)
	
	colNamesLabel.grid(row = 0, column = 0)
	colNamesTrue.grid(row = 1, column = 0)
	colNamesFalse.grid(row = 1, column = 1)
	colNamesFrame.grid(row = 1, column = 0, sticky = W)

	colTypesLabel.grid(row = 0, column = 0)
	colTypesTrue.grid(row = 1, column = 0)
	colTypesFalse.grid(row = 1, column = 1)
	colTypesFrame.grid(row = 2, column = 0, sticky = W)

	colDividerLabel.grid(row = 0, column = 0)
	colDividerEntry.grid(row = 0, column = 1)
	colDividerFrame.grid(row = 3, column = 0, sticky = W)

def openWiki():
	webbrowser.open("https://github.com/ChrisEarman/SQLDataBaseViewer/wiki")


menubar = Menu(main)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear Board", command=clearBoard)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Properties", command=propertiesEdit)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=openWiki)
menubar.add_cascade(label="Help", menu=helpmenu)

main.config(menu = menubar)

#-------------------------
#-------frame0------------
#-------------------------

def getText(event=[]):
	#print functionLabelVar.get()
	executeQuery(str(functionLabelVar.get()))
	#print dumbytext

def functionClickEvent(event=[]):
	functionLabelVar.set(functionList.get(ACTIVE))
	functionLabel.config(text = functionLabelVar.get())
	templateFrameTransform(str(functionList.get(ACTIVE)))

runButton = Button (templateWin, text = "RUN",command=getText)
runButton.grid(row=3,column=0)

functionScrollbar = Scrollbar(frame0)
functionScrollbar.pack(side=RIGHT,fill=Y)


functionList = Listbox(frame0, selectmode = BROWSE, height = 10, yscrollcommand = functionScrollbar.set)
#functionList.insert(1, "dbConnect")
#functionList.insert(2, "dbCommit")
#functionList.insert(3, "dbClose")
functionList.insert(4, "createTable")
functionList.insert(5, "deleteTable")
functionList.insert(6, "insertInto")
functionList.insert(7, "selectStar")
functionList.insert(8, "select")
functionList.insert(9, "selectAND")
functionList.insert(10, "selectOR")
functionList.insert(11, "selectIN")
functionList.insert(12, "updateWhere")
functionList.insert(13, "updateWhereAND")
functionList.insert(14, "updateWhereOR")
functionList.insert(15, "updateWhereIN")
functionList.insert(16, "delete")
#functionList.insert(0, "execute")

functionList.pack(side = LEFT, fill = BOTH)
functionList.bind("<Double-Button-1>", functionClickEvent)
functionScrollbar.config(command = functionList.yview)

frame0.grid(row = 2, column = 0)


#-------------------------
#-----outputFrame---------
#-------------------------

outputScrollbar = Scrollbar(outputFrame)
outputScrollbar.pack(side=RIGHT,fill=Y)
outputScrollbarX = Scrollbar(outputFrame, orient = HORIZONTAL)
outputScrollbarX.pack(side=BOTTOM,fill=X)
#outputScrollbar.pack(fill = Y)

queryOutputField = Text(outputFrame, bd = 2, height = 10, width = 103, yscrollcommand = outputScrollbar.set, xscrollcommand = outputScrollbarX.set, wrap = NONE)
queryOutputField.configure(state='disabled')
queryOutputField.pack(side = LEFT, fill=BOTH)
outputFrame.grid(row = 1, column = 1, rowspan = 1, sticky = NW)

outputScrollbar.config(command = queryOutputField.yview)
outputScrollbarX.config(command = queryOutputField.xview)


#-------------------------
#----templateFrame--------
#-------------------------


#EA.bind("<Return>", getText)

def templateFrameTransform(function):
	for frame in templateFrameSubs:
		#this resets the templateFrame frame
		frame.grid_forget() 
	if function == 'execute':
		pass
	elif function == 'dbConnect':
		templateFrameSubs[0].grid(row=0, column=0)
		labelStrings[0].set("DataBase")
	elif function == 'dbCommit':
		pass
	elif function == 'dbClose':
		pass
	elif function == 'createTable':
		for i in range(0,3):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("ColumnNames")
		labelStrings[2].set("ColumnTypes [Optional]")
	elif function == 'deleteTable':
		templateFrameSubs[0].grid(row=0,column=0)
		labelStrings[0].set("TableName")		
	elif function == 'insertInto':
		for i in range(0,3):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("Values")
		labelStrings[2].set("ColumnNames [Optional]")
	elif function == 'selectStar':
		templateFrameSubs[0].grid(row=0,column=0)
		labelStrings[0].set("TableName")
	elif function == 'select':
		for i in range(0,5):
			templateFrameSubs[i].grid(row=0,column=i)		
		labelStrings[0].set("TableName")
		labelStrings[1].set("WhereColumn [Optional]")
		labelStrings[2].set("WhereValue [Optional]")
		labelStrings[3].set("ColumnNames [Optional]")
		labelStrings[4].set("Operand [Optional]")
	elif function == 'selectAND' or function == 'selectOR':
		for i in range(0,5):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("WhereColumns")
		labelStrings[2].set("WhereValues")
		labelStrings[3].set("ColumnNames [Optional]")
		labelStrings[4].set("Operand [Optional]")
	elif function == 'selectIN':
		for i in range(0,4):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("WhereColumn")
		labelStrings[2].set("WhereValues")
		labelStrings[3].set("Columns [Optional]")
	elif function == 'updateWhere':
		for i in range(0,6):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("SetColumns")	
		labelStrings[2].set("SetValues")	
		labelStrings[3].set("WhereColumn")	
		labelStrings[4].set("WhereValue")	
		labelStrings[5].set("Operand [Optional]")	
	elif function == 'updateWhereAND' or function == 'updateWhereOR':
		for i in range(0,6):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("SetColumns")	
		labelStrings[2].set("SetValues")	
		labelStrings[3].set("WhereColumns")	
		labelStrings[4].set("WhereValues")	
		labelStrings[5].set("Operand [Optional]")	
	elif function == 'updateWhereIN':
		for i in range(0,5):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("SetColumns")	
		labelStrings[2].set("SetValues")	
		labelStrings[3].set("WhereColumn")	
		labelStrings[4].set("WhereValues")		
	elif function == 'delete':
		for i in range(0,4):
			templateFrameSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("WhereColumn")	
		labelStrings[2].set("WhereData")	
		labelStrings[3].set("Operand [Optional]")		
	else:
		print "templateFrameTransform(): command not recognized"


#-------------------------
#-------backend-----------
#-------------------------


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
	return "FAILED: paresTableName() - no TableName Found"

#This function takes in a query and parses out the list of columns requested in a select statment
def parseColNames(query):
	colList = extractColNames(preKeyWords(postSelect(query)))
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
def extractColNames(queryList):
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
		elif 'as' in newColLower:
			alias = ""
			for i in range((newColLower.index('as')+1),len(newCol)):
				alias += newCol[i] + " "
			alias = alias[:-1]
			if alias.endswith('"') or alias.endswith("'") or alias.endswith(']'):
				alias = alias[1:-1]
			colList.append(alias)
		else:
			colList.append("No Column or Alias Detected")
	if '*' in colList:
		return []
	return colList

def executeQuery(function):
	queryOutputField.configure(state="normal")
	output = ""
	queryOutputField.insert(1.0, "\n")
	if function == 'execute':
		subOutput = ""
		querytext = textTop.get(1.0,END).rstrip() #removes tailing whitespace
		#removes the tailing ; if present
		if querytext.endswith(';'): 
			querytext = querytext[:-1]
		queryList = querytext.split(';')
		for query in queryList:
			#print query
			#parseColNames(query)
			subOutput = backend.execute(query)
			if "select" in query.lower():
				table = parseTableName(query)
				#print table
				if prettyOutputOn.get():
					subOutput = prettyOutput.outputFormat(subOutput, tableName=table, nameInclude=colNameInclude.get(), typeInclude=colTypeInclude.get(), divider=colDivider.get(), columnList=parseColNames(query))
			if subOutput == "[]": 
				subOutput = "SUCCESS - No Output: " + query 
			output += str(subOutput) + "\n"
	elif function == 'dbConnect':
		output = backend.dbConnect(str(dbEntry.get()))
		#print backend.dbConnect(str(EA.get()))
		#print str(function + " " + EA.get())
	elif function == 'dbCommit':
		output = backend.dbCommit()
	elif function == 'dbClose':
		output = backend.dbClose()
		#print backend.dbClose()
	elif function == 'createTable':
		query = "output = backend.createTable('" + entryBox[0].get() + "'," + str(entryBox[1].get().split(','))
		if len(entryBox[2].get()) != 0:
			query += "," + str(entryBox[2].get().split(','))
		query += ")" 
		exec query
	elif function == 'deleteTable':
		output = backend.deleteTable(str(entryBox[0].get()))
	elif function == 'insertInto':
		for i in range(1,3):
			print entryBox[i].get().split(',')
		if len(entryBox[2].get()) == 0:
			output = backend.insertInto(str(entryBox[0].get()),str(entryBox[1].get()).split(','))
		else:
			output = backend.insertInto(str(entryBox[0].get()),str(entryBox[1].get()).split(','),str(entryBox[2].get()).split(','))
	elif function == 'selectStar':
		output = backend.selectStar(str(entryBox[0].get()))
		if prettyOutputOn.get():
			output = prettyOutput.outputFormat(output, tableName=entryBox[0].get(), nameInclude=colNameInclude.get(), typeInclude=colTypeInclude.get(), divider=colDivider.get())
	elif function == 'select':
		query = "output = backend.select(entryBox[0].get()"
		parameter = ['tableName','whereColumn','whereData','columns','operand']
		for i in [3]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [1,2,4]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		print query
		exec query
		if prettyOutputOn.get():
			output = prettyOutput.outputFormat(output, tableName=entryBox[0].get(), nameInclude=colNameInclude.get(), typeInclude=colTypeInclude.get(), divider=colDivider.get())
	elif function == 'selectAND' or function == 'selectOR':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','whereColumns','whereData','columns','operand']
		for i in [1,2,3]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [4]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		#print query
		exec query
		if prettyOutputOn.get():
			output = prettyOutput.outputFormat(output, tableName=entryBox[0].get(), nameInclude=colNameInclude.get(), typeInclude=colTypeInclude.get(), divider=colDivider.get())
	elif function == 'selectIN':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','whereColumn','whereData','columns']
		for i in [2,3]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [1]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		#print query
		exec query
		if prettyOutputOn.get():
			output = prettyOutput.outputFormat(output, tableName=entryBox[0].get(), nameInclude=colNameInclude.get(), typeInclude=colTypeInclude.get(), divider=colDivider.get())
	elif function == 'updateWhere':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','setCols','setData','whereCol','whereData','operand']
		for i in [1,2]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [3,4,5]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		#print query
		exec query
	elif function == 'updateWhereAND' or function == 'updateWhereOR':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','setCols','setData','whereCols','whereData','operand']
		for i in [1,2,3,4]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [5]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		#print query
		exec query
	elif function == 'updateWhereIN':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','setCols','setData','whereCol','whereData','operand']
		for i in [1,2,4]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [3,5]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		#print query
		exec query
	elif function == 'delete':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','whereCol','whereData','operand']
		for i in []:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [1,2,3]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += ")"
		#print query
		exec query
	else:
		print "executeQuery(): command not recognized"
	#Default formatting for non-PrettyOutput outputs
	if prettyOutputOn.get() == False:
		print output
		newOutput = output.split('), ')
		output = ""
		for x in newOutput:
			output += str(x) + '),\n '
		output = output[:-4]
	queryOutputField.insert(1.0,output)
	queryOutputField.configure(state="disabled")

#-------------------------
#-------short-cuts--------
#-------------------------

main.bind("<F2>",runExecute)
main.bind("<F3>",clearBoard)
main.bind("<F4>",callCommit)
main.bind("<F5>",callClose)
main.bind("<F6>",tempActivate)

main.mainloop()