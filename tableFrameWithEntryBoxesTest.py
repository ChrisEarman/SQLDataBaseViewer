
class multiList():
	def __init__(self, listMaster, lists):
		self.cells = [[None]*len(lists[0])]*len(lists)
		self.stringVarList = [[None]*len(lists[0])]*len(lists)
		for i in range(len(lists)):
			for j in range(len(lists[0])):
				self.stringVarList[i][j]= cellData(i,j,lists[i][j])
				self.cells[i][j] = Entry(listMaster,textvariable = self.stringVarList[i][j].dataVar)
				self.cells[i][j].grid(row = i, column = j)


class cellData():
	def __init__(self,i,j,data):
		self.i = i
		self.j = j
		self.data = data
		self.dataVar = StringVar()
		self.dataVar.set(data)

practiceColumnNames = ['Number','Name','Type1','Type2','HP','Att','Def','SpA','SpD','Spe','TotalBaseStats','Avg']
practiceOutput1 = [(460, u'Abomasnow', u'Grass', u'Ice', 90, 92, 75, 92, 85, 60, 494, 82.3333333333333),
 (63, u'Abra', u'Psychic', u'', 25, 20, 15, 105, 55, 90, 310, 51.6666666666667),
 (359, u'Absol', u'Dark', u'', 65, 130, 60, 75, 60, 75, 465, 77.5),
 (617, u'Accelgor', u'Bug', u'', 80, 70, 40, 100, 60, 145, 495, 82.5),
 (142, u'Aerodactyl', u'Rock', u'Flying', 80, 105, 65, 60, 75, 130, 515, 85.8333333333333),
 (306, u'Aggron', u'Steel', u'Rock', 70, 110, 180, 60, 60, 50, 530, 88.3333333333333),
 (190, u'Aipom', u'Normal', u'', 55, 70, 55, 40, 55, 85, 360, 60),
 (65, u'Alakazam', u'Psychic', u'', 55, 50, 45, 135, 85, 120, 490, 81.6666666666667),
 (594, u'Alomomola', u'Water', u'', 165, 75, 80, 40, 45, 65, 470, 78.3333333333333),
 (334, u'Altaria', u'Dragon', u'Flying', 75, 70, 90, 70, 105, 80, 490, 81.6666666666667),
 (424, u'Ambipom', u'Normal', u'', 75, 100, 66, 60, 66, 115, 482, 80.3333333333333),
 (591, u'Amoonguss', u'Grass', u'Poison', 114, 85, 70, 85, 80, 30, 464, 77.3333333333333),
 (181, u'Ampharos', u'Electric', u'', 90, 75, 75, 115, 90, 55, 500, 83.3333333333333),
 (347, u'Anorith', u'Rock', u'Bug', 45, 95, 50, 40, 50, 75, 355, 59.1666666666667),
 (24, u'Arbok', u'Poison', u'', 60, 85, 69, 65, 79, 80, 438, 73),
 (59, u'Arcanine', u'Fire', u'', 90, 110, 80, 100, 80, 95, 555, 92.5),
 (493, u'Arceus', u'Normal', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Bug', u'Bug', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Dark', u'Dark', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Dragon', u'Dragon', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Electric', u'Electric', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Fighting', u'Fighting', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Fire', u'Fire', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Flying', u'Flying', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Ghost', u'Ghost', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Grass', u'Grass', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Ground', u'Ground', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Ice', u'Ice', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Poison', u'Poison', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Psychic', u'Psychic', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Rock', u'Rock', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Steel', u'Steel', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (493, u'Arceus-Water', u'Water', u'', 120, 120, 120, 120, 120, 120, 720, 120),
 (566, u'Archen', u'Rock', u'Flying', 55, 112, 45, 74, 45, 70, 401, 66.8333333333333),
 (567, u'Archeops', u'Rock', u'Flying', 75, 140, 65, 112, 65, 110, 567, 94.5),
 (168, u'Ariados', u'Bug', u'Poison', 70, 90, 70, 60, 60, 40, 390, 65),
 (348, u'Armaldo', u'Rock', u'Bug', 75, 125, 100, 70, 80, 45, 495, 82.5),
 (304, u'Aron', u'Steel', u'Rock', 50, 70, 100, 40, 40, 30, 330, 55),
 (144, u'Articuno', u'Ice', u'Flying', 90, 85, 100, 95, 125, 85, 580, 96.6666666666667),
 (531, u'Audino', u'Normal', u'', 103, 60, 86, 60, 86, 50, 445, 74.1666666666667),
 (610, u'Axew', u'Dragon', u'', 46, 87, 60, 30, 40, 57, 320, 53.3333333333333),
 (482, u'Azelf', u'Psychic', u'', 75, 125, 70, 125, 70, 115, 580, 96.6666666666667),
 (184, u'Azumarill', u'Water', u'', 100, 50, 80, 50, 80, 50, 410, 68.3333333333333),
 (298, u'Azurill', u'Normal', u'', 50, 20, 40, 20, 40, 20, 190, 31.6666666666667),
 (371, u'Bagon', u'Dragon', u'', 45, 75, 60, 40, 30, 50, 300, 50),
 (343, u'Baltoy', u'Ground', u'Psychic', 40, 40, 55, 40, 70, 55, 300, 50),
 (354, u'Banette', u'Ghost', u'', 64, 115, 65, 83, 63, 65, 455, 75.8333333333333),
 (339, u'Barboach', u'Water', u'Ground', 50, 48, 43, 46, 41, 60, 288, 48),
 (550, u'Basculin', u'Water', u'', 70, 92, 65, 80, 55, 98, 460, 76.6666666666667),
 (411, u'Bastiodon', u'Rock', u'Steel', 60, 52, 168, 47, 138, 30, 495, 82.5),
 (153, u'Bayleef', u'Grass', u'', 60, 62, 80, 63, 80, 60, 405, 67.5),
 (614, u'Beartic', u'Ice', u'', 95, 110, 80, 70, 80, 50, 485, 80.8333333333333),
 (267, u'Beautifly', u'Bug', u'Flying', 60, 70, 50, 90, 50, 65, 385, 64.1666666666667),
 (15, u'Beedrill', u'Bug', u'Poison', 65, 80, 40, 45, 80, 75, 385, 64.1666666666667),
 (606, u'Beheeyem', u'Psychic', u'', 75, 75, 75, 125, 95, 40, 485, 80.8333333333333),
 (374, u'Beldum', u'Steel', u'Psychic', 40, 55, 80, 35, 60, 30, 300, 50),
 (182, u'Bellossom', u'Grass', u'', 75, 80, 85, 90, 100, 50, 480, 80),
 (69, u'Bellsprout', u'Grass', u'Poison', 50, 75, 35, 70, 30, 40, 300, 50),
 (400, u'Bibarel', u'Normal', u'Water', 79, 85, 60, 55, 60, 71, 410, 68.3333333333333),
 (399, u'Bidoof', u'Normal', u'', 59, 45, 40, 35, 40, 31, 250, 41.6666666666667),
 (625, u'Bisharp', u'Dark', u'Steel', 65, 125, 100, 60, 70, 70, 490, 81.6666666666667),
 (9, u'Blastoise', u'Water', u'', 79, 83, 100, 85, 105, 78, 530, 88.3333333333333),
 (257, u'Blaziken', u'Fire', u'Fighting', 80, 120, 70, 110, 70, 80, 530, 88.3333333333333),
 (242, u'Blissey', u'Normal', u'', 255, 10, 10, 75, 135, 55, 540, 90),
 (522, u'Blitzle', u'Electric', u'', 45, 60, 32, 50, 32, 76, 295, 49.1666666666667),
 (525, u'Boldore', u'Rock', u'', 70, 105, 105, 50, 40, 20, 390, 65),
 (438, u'Bonsly', u'Rock', u'', 50, 80, 95, 10, 45, 10, 290, 48.3333333333333),
 (626, u'Bouffalant', u'Normal', u'', 95, 110, 95, 40, 95, 55, 490, 81.6666666666667),
 (628, u'Braviary', u'Normal', u'Flying', 100, 123, 75, 57, 75, 80, 510, 85),
 (286, u'Breloom', u'Grass', u'Fighting', 60, 130, 80, 60, 60, 70, 460, 76.6666666666667),
 (437, u'Bronzong', u'Steel', u'Psychic', 67, 89, 116, 79, 116, 33, 500, 83.3333333333333),
 (436, u'Bronzor', u'Steel', u'Psychic', 57, 24, 86, 24, 86, 23, 300, 50),
 (406, u'Budew', u'Grass', u'Poison', 40, 30, 35, 50, 70, 55, 280, 46.6666666666667),
 (418, u'Buizel', u'Water', u'', 55, 65, 35, 60, 30, 85, 330, 55),
 (1, u'Bulbasaur', u'Grass', u'Poison', 45, 49, 49, 65, 65, 45, 318, 53),
 (427, u'Buneary', u'Normal', u'', 55, 66, 44, 44, 56, 85, 350, 58.3333333333333),
 (412, u'Burmy', u'Bug', u'', 40, 29, 45, 29, 45, 36, 224, 37.3333333333333),
 (12, u'Butterfree', u'Bug', u'Flying', 60, 45, 50, 80, 80, 70, 385, 64.1666666666667),
 (331, u'Cacnea', u'Grass', u'', 50, 85, 40, 85, 40, 35, 335, 55.8333333333333),
 (332, u'Cacturne', u'Grass', u'Dark', 70, 115, 60, 115, 60, 55, 475, 79.1666666666667),
 (323, u'Camerupt', u'Fire', u'Ground', 70, 100, 70, 105, 75, 40, 460, 76.6666666666667),
 (455, u'Carnivine', u'Grass', u'', 74, 100, 72, 90, 72, 46, 454, 75.6666666666667),
 (565, u'Carracosta', u'Water', u'Rock', 74, 108, 133, 83, 65, 32, 495, 82.5),
 (318, u'Carvanha', u'Water', u'Dark', 45, 90, 20, 65, 20, 65, 305, 50.8333333333333),
 (268, u'Cascoon', u'Bug', u'', 50, 35, 55, 25, 25, 15, 205, 34.1666666666667),
 (351, u'Castform', u'Normal', u'', 70, 70, 70, 70, 70, 70, 420, 70),
 (10, u'Caterpie', u'Bug', u'', 45, 30, 35, 20, 20, 45, 195, 32.5),
 (251, u'Celebi', u'Psychic', u'Grass', 100, 100, 100, 100, 100, 100, 600, 100),
 (609, u'Chandelure', u'Ghost', u'Fire', 60, 55, 90, 145, 90, 80, 520, 86.6666666666667),
 (113, u'Chansey', u'Normal', u'', 250, 5, 5, 35, 105, 50, 450, 75),
 (6, u'Charizard', u'Fire', u'Flying', 78, 84, 78, 109, 85, 100, 534, 89),
 (4, u'Charmander', u'Fire', u'', 39, 52, 43, 60, 50, 65, 309, 51.5),
 (5, u'Charmeleon', u'Fire', u'', 58, 64, 58, 80, 65, 80, 405, 67.5),
 (441, u'Chatot', u'Normal', u'Flying', 76, 65, 45, 92, 42, 91, 411, 68.5),
 (421, u'Cherrim', u'Grass', u'', 70, 60, 70, 87, 78, 85, 450, 75),
 (420, u'Cherubi', u'Grass', u'', 45, 35, 45, 62, 53, 35, 275, 45.8333333333333),
 (152, u'Chikorita', u'Grass', u'', 45, 49, 65, 49, 65, 45, 318, 53),
 (390, u'Chimchar', u'Fire', u'', 44, 58, 44, 58, 44, 61, 309, 51.5),
 (358, u'Chimecho', u'Psychic', u'', 65, 50, 70, 95, 80, 65, 425, 70.8333333333333),
 (170, u'Chinchou', u'Water', u'Electric', 75, 38, 38, 56, 56, 67, 330, 55)]


class popUp():
	def __init__(self, master, lists,colNames):
		self.popUp1 = Toplevel(master)
		self.popUp1.bind("<MouseWheel>",self.OnMouseWheely)
		self.popUp1.bind("<Shift-MouseWheel>",self.OnMouseWheelx)
		#popUp1.minsize(500,200)
		self.columnNameCanvas = Canvas(self.popUp1)
		self.tableCanvas = Canvas(self.popUp1)
		self.subFrame = Frame(self.tableCanvas)
		self.colNameFrame = Frame(self.columnNameCanvas)
		self.scrollerx = Scrollbar(self.popUp1, orient=HORIZONTAL, command = self.CanvasXScroll)
		self.scrollery = Scrollbar(self.popUp1, orient=VERTICAL, command = self.tableCanvas.yview)

		self.tableCanvas.configure(xscrollcommand=self.scrollerx.set, yscrollcommand=self.scrollery.set)
		self.columnNameCanvas.configure(xscrollcommand = self.scrollerx.set)			
		self.tableCanvas.create_window((0,0), window = self.subFrame, anchor = NW)
		self.columnNameCanvas.create_window((0,0), window = self.colNameFrame, anchor = NW)
		self.subFrame.bind("<Configure>",self.tableCanvasResize)
		self.colNameFrame.bind("<Configure>",self.columnNameCanvasResize)

		self.scrollerx.pack(side=BOTTOM, fill = X)
		self.scrollery.pack(side=RIGHT, fill = Y)
		self.colNamesConfig(colNames)
		multiList(self.subFrame,lists)
		self.tableCanvas.pack(side = TOP,fill=BOTH,expand=True)

	def CanvasXScroll(self,*args):
		self.tableCanvas.xview(*args)
		self.columnNameCanvas.xview(*args)
	def OnMouseWheely(self,event):
		self.tableCanvas.yview("scroll", int(event.delta/-60),"units") #divided by negative number to invert scroll and reduce magnitude of scroll
	def OnMouseWheelx(self,event):
		self.tableCanvas.xview("scroll", int(event.delta/60),"units") #divided to reduce magnitude of scroll
	def tableCanvasResize(self,*args):
		self.tableCanvas.configure(scrollregion=self.tableCanvas.bbox("all"))
	def columnNameCanvasResize(self,*args):
		self.columnNameCanvas.configure(scrollregion=self.columnNameCanvas.bbox("all"))

	def colNamesConfig(self,colNames):
		self.titles = [None]*len(colNames)
		for i in range(len(colNames)):
			self.titles[i] = Label(self.colNameFrame, text = colNames[i])
			self.titles[i].grid(row = 0, column = i)


#------------
#----code----
#------------

from Tkinter import *



root = Tk()

sup = StringVar()
sup.set('sup')


def showPopUp():	
	popUp(root,practiceOutput1,practiceColumnNames)
	

display = Button(root, text = "DISPLAY",command=showPopUp)
display.pack()
root.mainloop()
