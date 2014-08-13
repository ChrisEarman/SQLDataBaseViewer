class multiList():
	def __init__(self, listMaster, framMaster, lists):
		scrollbar = Scrollbar(framMaster, orient=VERTICAL)
		self.listsLen = len(lists[0])
		self.col = [None]*len(lists)
		for i in range(len(lists[0])):
			self.col[i] = Listbox(listMaster, selectmode = BROWSE, yscrollcommand = scrollbar.set)
			self.col[i].pack(side=LEFT,fill=BOTH,expand=True)
		for i in range(len(lists)):
			for j in range(len(lists[i])):
				self.col[j].insert(i,lists[i][j])
				if i % 2 == 0:
					self.col[j].itemconfig(i,bg='#B8B8B8')
				else:
					self.col[j].itemconfig(i,bg='#D4D4D4')
		scrollbar.config(command=self.yview)
		scrollbar.pack(side=RIGHT, fill=Y)

	def yview(self, *args):
		for i in range(self.listsLen):
			apply(self.col[i].yview,args)


practiceOutput1 = [(386, u'Deoxys-A', u'Psychic', u'', 50, 180, 20, 180, 20, 150, 600, 100),
 (386, u'Deoxys-N', u'Psychic', u'', 50, 150, 50, 150, 50, 150, 600, 100),
 (386, u'Deoxys-S', u'Psychic', u'', 50, 95, 90, 95, 90, 180, 600, 100),
 (289, u'Slaking', u'Normal', u'', 150, 160, 100, 95, 65, 100, 670, 111.666666666667),
 (486, u'Regigigas', u'Normal', u'', 110, 160, 110, 80, 110, 100, 670, 111.666666666667),
 (648, u'Meloetta-S', u'Normal', u'Fighting', 100, 128, 90, 77, 77, 128, 600, 100),
 (291, u'Ninjask', u'Bug', u'Flying', 61, 90, 45, 50, 50, 160, 456, 76),
 (567, u'Archeops', u'Rock', u'Flying', 75, 140, 65, 112, 65, 110, 567, 94.5),
 (384, u'Rayquaza', u'Dragon', u'Flying', 105, 150, 90, 150, 90, 95, 680, 113.333333333333),
 (461, u'Weavile', u'Dark', u'Ice', 70, 120, 65, 45, 85, 125, 510, 85),
 (612, u'Haxorus', u'Dragon', u'', 76, 147, 90, 60, 70, 97, 540, 90),
 (150, u'Mewtwo', u'Psychic', u'', 106, 110, 90, 154, 90, 130, 680, 113.333333333333)]


class popUp():
	def __init__(self, master, lists):
		popUp1 = Toplevel(master)
		#popUp1.minsize(500,200)
		self.tableCanvas = Canvas(popUp1)
		self.subFrame = Frame(self.tableCanvas)
		self.scroller = Scrollbar(popUp1, orient=HORIZONTAL, command = self.tableCanvas.xview)

		self.tableCanvas.configure(xscrollcommand=self.scroller.set)			
		self.tableCanvas.create_window((0,0), window = self.subFrame, anchor = NW)
		self.subFrame.bind("<Configure>",self.myfunction)

		self.scroller.pack(side=BOTTOM, fill = X)
		multiList(self.subFrame,popUp1,lists)
		self.tableCanvas.pack(side = LEFT,fill=BOTH,expand=True)	
	def myfunction(self,*args):
		self.tableCanvas.configure(scrollregion=self.tableCanvas.bbox("all"))

#------------
#----code----
#------------

from Tkinter import *

root = Tk()




def showPopUp():	
	popUp(root,practiceOutput1)

display = Button(root, text = "DISPLAY",command=showPopUp)
display.pack()
root.mainloop()
