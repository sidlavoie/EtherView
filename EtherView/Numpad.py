# Numpad_______________________________________________________________________________________________
# Modified from code by scotty3785 https://stackoverflow.com/questions/63914121/numpad-in-tkinter-python
import tkinter
from tkinter import *
from tkinter import simpledialog


def enumerate_row_column(iterable, num_cols):
    for idx, item in enumerate(iterable):
        row = idx // num_cols
        col = idx % num_cols
        yield row, col, item


class NumpadEntry(Entry):
    def __init__(self, parent=None, **kw):
        Entry.__init__(self, parent, **kw)
        self.bind('<FocusIn>', self.numpadEntry)
        self.bind('<FocusOut>', self.numpadExit)
        self.edited = False

    def numpadEntry(self, event):
        if self.edited is False:
            print("You Clicked on me")
            self['bg'] = '#ffffcc'
            self.edited = True
            new = numPad(self)
        else:
            self.edited = False

    def numpadExit(self, event):
        self['bg'] = '#ffffff'


class numPad(simpledialog.Dialog):
    def __init__(self, master=None, textVariable=None):
        self.top = Toplevel(master=master)
        self.top.protocol("WM_DELETE_WINDOW", self.ok)
        self.createWidgets()
        self.master = master

    def createWidgets(self):
        close = Button(self.top, text="X", command=self.ok, background="red")
        close.grid(row=0, column=3)
        btn_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Del']
        # create and position all buttons with a for-loop
        btn = []
        # Use custom generator to give us row/column positions
        for r, c, label in enumerate_row_column(btn_list, 3):
            # partial takes care of function and argument
            cmd = lambda x=label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=5, height=2, command=cmd)
            # position the button
            cur.grid(row=r + 1, column=c)
            btn.append(cur)

    def click(self, label):
        print(label)
        if label == 'Del':
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText[:-1])
        elif label == 'Close':
            self.ok()
        else:
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText + label)

    def ok(self):
        self.master.selection_clear()
        self.top.destroy()
        self.top.master.focus()

