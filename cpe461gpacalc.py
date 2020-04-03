from Tkinter import *
import tkMessageBox
class App:
	def __init__(self,parent):
		self.parent = parent
		self.frame_1 = Frame(parent)
		self.frame_1.pack()
        		
		self.lbl_1 = Label(self.frame_1,text="Current CGPA :")
		self.lbl_1.grid(row=0,column=0)
		self.entry_1 = Entry(self.frame_1)
		self.entry_1.grid(row=0,column=1)

		self.lbl_2 = Label(self.frame_1,text="Units Completed :")
		self.lbl_2.grid(row=1,column=0)
		self.entry_2 = Entry(self.frame_1)
		self.entry_2.grid(row=1,column=1)