import queryParser
from Tkinter import *

#master is the master frame
#lists is the data exported from the database in the .fetchall() format
class multiList():
	def __init__(self, master, lists):
		self.cells = []
		self.stringVarList = []
		for i in range(len(lists)):
			self.cells.append([None]*len(lists[0]))
			self.stringVarList.append([None]*len(lists[0]))
			for j in range(len(lists[0])):
				self.stringVarList[i][j] = cellData(i,j,lists[i][j])
				self.cells[i][j] = Entry(master,textvariable = self.stringVarList[i][j].dataVar, relief = GROOVE, width = 20)
				self.cells[i][j].grid(row = i, column = j)
				if i % 2 == 0:
					self.cells[i][j].configure(bg = "#B8B8B8")
				else:
					self.cells[i][j].configure(bg = "#D4D4D4")
	def clear(self,*args):
		for k in range(len(self.cells)):
			for l in range(len(self.cells[k])):
				self.cells[k][l].grid_forget()

#i is the row of the data in the table
#j is the column of the data in the table
#data is the inforamtion at row,column = i,j in the table
class cellData():
	def __init__(self,i,j,data):
		self.row = i
		self.col = j
		self.origData = data
		self.dataVar = StringVar()
		self.dataVar.set(data)

	def printCell(self,*args):
		print "[" + str(self.row) + "," + str(self.col) + "]: orig - " + str(self.origData) + " , variable - " + self.dataVar.get()


#master is the master frame
#backend is the connection to SQLite
#dbName is the database desired to connect to
class popUp():
	def __init__(self, master, backend, dbName):
		self.backend = backend
		self.backend.dbConnect(dbName)
		self.popUp1 = Toplevel(master)
		self.popUp1.title('Live Table Editor')
		self.tableScrollFrame = Frame(self.popUp1)
		self.queryViewFrame = Frame(self.popUp1)
		self.queryDisplay()
		self.queryViewFrame.pack(side = TOP, fill = X)
		self.tableScrollFrame.pack(side = BOTTOM, fill = BOTH, expand = True)

		self.popUp1.bind("<MouseWheel>",self.OnMouseWheely)
		self.popUp1.bind("<Shift-MouseWheel>",self.OnMouseWheelx)
		#popUp1.minsize(500,200)
		self.columnNameCanvas = Canvas(self.tableScrollFrame, height = 12)
		self.tableCanvas = Canvas(self.tableScrollFrame)
		self.subFrame = Frame(self.tableCanvas)
		self.colNameFrame = Frame(self.columnNameCanvas)
		self.scrollerx = Scrollbar(self.tableScrollFrame, orient=HORIZONTAL, command = self.CanvasXScroll)
		self.scrollery = Scrollbar(self.tableScrollFrame, orient=VERTICAL, command = self.tableCanvas.yview)

		self.tableCanvas.configure(xscrollcommand=self.scrollerx.set, yscrollcommand=self.scrollery.set)
		self.columnNameCanvas.configure(xscrollcommand = self.scrollerx.set)			
		self.tableCanvas.create_window((0,0), window = self.subFrame, anchor = NW)
		self.columnNameCanvas.create_window((0,0), window = self.colNameFrame, anchor = NW)
		self.subFrame.bind("<Configure>",self.tableCanvasResize)
		self.colNameFrame.bind("<Configure>",self.columnNameCanvasResize)

		self.scrollerx.pack(side=BOTTOM, fill = X)
		self.scrollery.pack(side=RIGHT, fill = Y)
		self.tableObj = multiList(self.subFrame,[['Input Query to Fill Table']]) #initializes an empty table object (a runtime error occurs if this line is ommitted)
		self.colNamesConfig([]) #initializes an empty self.titles variable (a runtime error occurs if this line is ommitted)
		self.columnNameCanvas.pack(side = TOP, fill = X)
		self.tableCanvas.pack(side = TOP, fill = BOTH, expand = True)

		self.menubar = Menu(self.popUp1)

		self.filemenu = Menu(self.menubar,tearoff = 0)
		self.filemenu.add_command(label='Exit',command=self.popUp1.quit)
		self.menubar.add_cascade(label='File', menu=self.filemenu)

		self.limitMenu = Menu(self.menubar,tearoff = 0)
		self.rowLimit = IntVar()
		self.rowLimit.set(100)
		self.limitOn = BooleanVar()
		self.limitOn.set(False)
		self.limitMenu.add_command(label = 'Limit Properties', command = self.limitPropertiesWin)
		self.menubar.add_cascade(label='Edit',menu=self.limitMenu)

		self.popUp1.config(menu = self.menubar)

		self.rowCount = 0
		self.colCount = 0
		self.tableName = ''

	#----------------------
	#---Menu-commands------
	#----------------------
	def limitPropertiesWin(self,*args):
			self.limitWin = Toplevel(self.popUp1)
			self.limitWin.title('Limit Properties')
			limitOTrue = Radiobutton(self.limitWin, text = 'On', variable=self.limitOn,value=True)
			limitOFalse = Radiobutton(self.limitWin, text = 'Off', variable=self.limitOn,value=False)
			limitOLabel = Label(self.limitWin, text = "Include Row Limit:", width = 20)
			limitValue = Entry(self.limitWin, textvariable=self.rowLimit, width=20)
			limitValueLabel = Label(self.limitWin, text = "Row Limit:", width = 20)

			limitOLabel.grid(row = 0, column = 0)
			limitOTrue.grid(row = 1, column = 0)
			limitOFalse.grid(row = 1, column = 1)
			limitValueLabel.grid(row = 2, column = 0)
			limitValue.grid(row = 2, column = 1)
			
	#----------------------
	#---Menu-commands-end--
	#----------------------


	def CanvasXScroll(self,*args):
		self.tableCanvas.xview(*args)
		self.columnNameCanvas.xview(*args)
	def OnMouseWheely(self,event):
		self.tableCanvas.yview("scroll", int(event.delta/-60),"units") #divided by negative number to invert scroll and reduce magnitude of scroll
	def OnMouseWheelx(self,event):
		self.CanvasXScroll("scroll", int(event.delta/60),"units") #divided to reduce magnitude of scroll
	def tableCanvasResize(self,*args):
		self.tableCanvas.configure(scrollregion=self.tableCanvas.bbox("all"))
	def columnNameCanvasResize(self,*args):
		self.columnNameCanvas.configure(scrollregion=self.columnNameCanvas.bbox("all"))

	def colNamesConfig(self,colNames):
		self.titles = [None]*len(colNames)
		self.colNamesVar = [None]*len(colNames)
		for i in range(len(colNames)):
			self.colNamesVar[i] = StringVar()
			self.colNamesVar[i].set(colNames[i])
			self.titles[i] = Entry(self.colNameFrame, textvariable = self.colNamesVar[i], width = 20, relief = GROOVE, state = "readonly", readonlybackground = "#393939", fg = "#FFFFFF")
			self.titles[i].grid(row = 0, column = i, sticky = NW)
	def colNamesClear(self):
		for i in range(len(self.titles)):
			self.titles[i].grid_forget()


	def queryDisplay(self,query = ""):
		self.query = StringVar()
		self.query.set(query)
		self.queryEntry = Entry(self.queryViewFrame, textvariable = self.query, relief = GROOVE)
		self.queryEntry.pack(side = LEFT, fill = X , ipady = 4, anchor = E, expand = True)

		self.commitButton = Button(self.queryViewFrame, text = "Commit Table Changes", command = self.commitChanges)
		self.commitButton.pack(side = RIGHT)

		self.changeQueryButton = Button(self.queryViewFrame, text = "Change Query", command = self.changeQuery)
		self.changeQueryButton.pack(side = RIGHT)
		
	def commitChanges(self,*args):
		for i in range(self.rowCount):
			flagRowForUpdate = False
			for j in range(self.colCount):
				if not str(self.tableObj.stringVarList[i][j].dataVar.get()) == str(self.tableObj.stringVarList[i][j].origData):
					flagRowForUpdate = True
			if flagRowForUpdate:
				updateQuery = "UPDATE " + str(self.tableName) + " SET "
				whereStatement = " WHERE "
				for j in range(self.colCount):
					updateQuery += str(self.colNamesVar[j].get()) + "='" + str(self.tableObj.stringVarList[i][j].dataVar.get()) + "', "
					whereStatement += str(self.colNamesVar[j].get()) + "='" + str(self.tableObj.stringVarList[i][j].origData) + "' AND "
					self.tableObj.stringVarList[i][j].origData = self.tableObj.stringVarList[i][j].dataVar.get()
				updateQuery = updateQuery[:-2] + whereStatement[:-4] #concatenates strings and removes trailing commas and AND clause
				
				
				self.backend.execute(updateQuery)
		self.backend.dbCommit()

	def changeQuery(self,*args):
		query = self.queryEntry.get()
		self.tableName = str(queryParser.parseTableName(query))
		if self.limitOn.get():
			query += ' Limit ' + str(self.rowLimit.get())

		retVal = self.backend.execute(query)
		if retVal == []:
			print 'no data'
			self.rowCount = 0
			self.colCount = 0
		elif retVal == "FAILED: execute() - proofread your query and make sure all connections are established correctly":
			print retVal
		else:
			self.output = retVal
			self.rowCount = len(self.output)
			self.colCount = len(self.output[0])
			self.tableObj.clear()
			self.tableObj = multiList(self.subFrame,self.output)
		retVal2 = queryParser.parseColNames(query,False)
		if retVal2 == []:
			query2 = "PRAGMA table_info(" + str(self.tableName) + ")"
			retVal3 = self.backend.execute(query2)
			self.colNameList = []
			for i in retVal3:
				self.colNameList.append(i[1])
			#print self.colNameList
		else:
			self.colNameList = retVal2
			#print self.colNameList

		self.colNamesClear()
		self.colNamesConfig(self.colNameList)