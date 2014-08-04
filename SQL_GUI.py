from Tkinter import *
import webbrowser
import SQLiteCustomQueryTemplate as backend
import PrettyOutput_SQLite as prettyOutput


main = Tk()
main.title("SQL_c")
main.geometry("885x300+100+100")
frame0 = Frame(main)
frame1 = Frame(main)
frameTop = Frame(main)

functionLabel = Label (main, text = "[NONE]")
functionLabel.grid(row = 0, column = 0, pady = 20)

#-------------------------
#--frameTop Attributes----
#-------------------------

frameTop.grid(row=0, column = 1)
frameTopSubs = [None]*10
labelStrings = [None]*10
labelTop = [None]*10
entryBox = [None]*10
for i in range(0,10):
	frameTopSubs[i] = Frame(frameTop)
	labelStrings[i] = StringVar()
	labelTop[i] = Label(frameTopSubs[i], textvariable = labelStrings[i]).pack(side=TOP)
	entryBox[i] = Entry(frameTopSubs[i])
	entryBox[i].pack(side=BOTTOM)

executeFrame = Frame(frameTop)
inputScrollbar = Scrollbar(executeFrame)
inputScrollbar.pack(side=RIGHT,fill=Y)
textTop = Text(executeFrame,width = 103, height = 3,yscrollcommand = inputScrollbar.set)
textTop.pack(side = LEFT, fill=BOTH)
executeFrame.pack()

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
colNameInclude.set(False)
colTypeInclude = BooleanVar()
colTypeInclude.set(False)
colDivider = StringVar()
colDivider.set(" ")
def propertiesEdit():
	propertyWin = Toplevel(main)
	propertyWin.title("Properties")
	prettyOTrue = Radiobutton(propertyWin, text="On",variable=prettyOutputOn,value=True)
	prettyOFalse = Radiobutton(propertyWin, text="Off",variable=prettyOutputOn,value=False)
	colNamesTrue = RadioButton(propertyWin, text="On",variable=colNameInclude,value=True)
	colNamesFalse = RadioButton(propertyWin, text="Off",variable=colNameInclude,value=False)
	colTypesTrue = RadioButton(propertyWin, text="On",variable=colTypeInclude,value=True)
	colTypesFalse = RadioButton(propertyWin, text="Off",variable=colTypeInclude,value=False)

def openWiki():
	webbrowser.open("https://github.com/ChrisEarman/SQLDataBaseViewer/wiki")

def clearBoard():
	#print 'clear'
	queryOutputField.config(state = "normal")
	queryOutputField.delete(0.0,END)
	queryOutputField.config(state = "disabled")

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
	functionLabel.configure(text=str(functionList.get(ACTIVE)))
	executeQuery(str(functionList.get(ACTIVE)))
	#print dumbytext

def functionClickEvent(event=[]):
	functionLabel.configure(text=str(functionList.get(ACTIVE)))
	frameTopTransform(str(functionList.get(ACTIVE)))

runButton = Button (main, text = "RUN",command=getText)
runButton.grid(row=2,column=0)

functionScrollbar = Scrollbar(frame0)
functionScrollbar.pack(side=RIGHT,fill=Y)

functionList = Listbox(frame0, selectmode = BROWSE, height = 10, yscrollcommand = functionScrollbar.set)
functionList.insert(1, "dbConnect")
functionList.insert(2, "dbCommit")
functionList.insert(3, "dbClose")
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
functionList.insert(0, "execute")

functionList.pack(side = LEFT, fill = BOTH)
functionList.bind("<Double-Button-1>", functionClickEvent)
functionScrollbar.config(command = functionList.yview)

frame0.grid(row = 1, column = 0)


#-------------------------
#-------frame1------------
#-------------------------

outputScrollbar = Scrollbar(frame1)
outputScrollbar.pack(side=RIGHT,fill=Y)
#outputScrollbar.pack(fill = Y)

queryOutputField = Text(frame1, bd = 2, height = 10, width = 103, yscrollcommand = outputScrollbar.set )
queryOutputField.configure(state='disabled')
queryOutputField.pack(side = LEFT, fill=BOTH)
frame1.grid(row = 1, column = 1, rowspan = 2, sticky = NW)

outputScrollbar.config(command = queryOutputField.yview)
queryOutputField.bind("<Return>", getText)

#-------------------------
#-------frameTop----------
#-------------------------


#EA.bind("<Return>", getText)

def frameTopTransform(function):
	executeFrame.pack_forget()
	for frame in frameTopSubs:
		#this resets the frameTop frame
		frame.grid_forget() 
	if function == 'execute':
		executeFrame.pack()
	elif function == 'dbConnect':
		frameTopSubs[0].grid(row=0, column=0)
		labelStrings[0].set("DataBase")
	elif function == 'dbCommit':
		pass
	elif function == 'dbClose':
		pass
	elif function == 'createTable':
		for i in range(0,3):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("ColumnNames")
		labelStrings[2].set("ColumnTypes [Optional]")
	elif function == 'deleteTable':
		frameTopSubs[0].grid(row=0,column=0)
		labelStrings[0].set("TableName")		
	elif function == 'insertInto':
		for i in range(0,3):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("Values")
		labelStrings[2].set("ColumnNames [Optional]")
	elif function == 'selectStar':
		frameTopSubs[0].grid(row=0,column=0)
		labelStrings[0].set("TableName")
	elif function == 'select':
		for i in range(0,5):
			frameTopSubs[i].grid(row=0,column=i)		
		labelStrings[0].set("TableName")
		labelStrings[1].set("WhereColumn [Optional]")
		labelStrings[2].set("WhereValue [Optional]")
		labelStrings[3].set("ColumnNames [Optional]")
		labelStrings[4].set("Operand [Optional]")
	elif function == 'selectAND' or function == 'selectOR':
		for i in range(0,5):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("WhereColumns")
		labelStrings[2].set("WhereValues")
		labelStrings[3].set("ColumnNames [Optional]")
		labelStrings[4].set("Operand [Optional]")
	elif function == 'selectIN':
		for i in range(0,4):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")
		labelStrings[1].set("WhereColumn")
		labelStrings[2].set("WhereValues")
		labelStrings[3].set("Columns [Optional]")
	elif function == 'updateWhere':
		for i in range(0,6):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("SetColumns")	
		labelStrings[2].set("SetValues")	
		labelStrings[3].set("WhereColumn")	
		labelStrings[4].set("WhereValue")	
		labelStrings[5].set("Operand [Optional]")	
	elif function == 'updateWhereAND' or function == 'updateWhereOR':
		for i in range(0,6):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("SetColumns")	
		labelStrings[2].set("SetValues")	
		labelStrings[3].set("WhereColumns")	
		labelStrings[4].set("WhereValues")	
		labelStrings[5].set("Operand [Optional]")	
	elif function == 'updateWhereIN':
		for i in range(0,5):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("SetColumns")	
		labelStrings[2].set("SetValues")	
		labelStrings[3].set("WhereColumn")	
		labelStrings[4].set("WhereValues")		
	elif function == 'delete':
		for i in range(0,4):
			frameTopSubs[i].grid(row=0,column=i)
		labelStrings[0].set("TableName")	
		labelStrings[1].set("WhereColumn")	
		labelStrings[2].set("WhereData")	
		labelStrings[3].set("Operand [Optional]")		
	else:
		print "frameTopTransform(): command not recognized"

#This function takes in a query and parses out the Table name and returns that tablename - used in the execute function
def parseTableName(query):
	stringList = query.split(" ")
	tableNameFound = False
	for i in stringList:
		if tableNameFound:
			return i
		elif str(i).lower() == "from":
			tableNameFound = True
		else:
			pass
	return "FAILED: paresTableName() - no TableName Found"

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
			subOutput = backend.execute(query)
			if "select" in query.lower():
				table = parseTableName(query)
				#print table
				subOutput = prettyOutput.outputFormat(subOutput,tableName = table)
			if subOutput == "[]": 
				subOutput = "SUCCESS - No Output: " + query 
			output += str(subOutput) + "\n"
	elif function == 'dbConnect':
		output = backend.dbConnect(str(entryBox[0].get()))
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
		output = prettyOutput.outputFormat(output,divider=" | ",nameInclude=True,tableName=entryBox[0].get(),typeInclude=True)
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
	elif function == 'selectAND' or function == 'selectOR':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','whereColumns','whereData','columns','operand']
		for i in [1,2,3]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [4]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += "))"
		#print query
		exec query
	elif function == 'selectIN':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','whereColumn','whereData','columns']
		for i in [2,3]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [1]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += "))"
		#print query
		exec query
	elif function == 'updateWhere':
		query = "output = backend." + function + "(entryBox[0].get()"
		parameter = ['tableName','setCols','setData','whereCol','whereData','operand']
		for i in [1,2]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = " + str(entryBox[i].get().split(','))
		for i in [3,4,5]:
			if len(entryBox[i].get()) != 0:
				query += "," + parameter[i] + " = '" + entryBox[i].get() + "'"
		query += "))"
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
		query += "))"
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
		query += "))"
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
		query += "))"
		#print query
		exec query
	else:
		print "frameTopTransform(): command not recognized"
	
	queryOutputField.insert(1.0,output)
	queryOutputField.configure(state="disabled")


main.mainloop()