from expression import Mul,Num,Add,Div,Sub
from tkinter import *

class ExpresionGUI(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        width , height = 75,30
        mainFrame = Frame(master, width = width , height = height).grid(
        row = 0 ,column = 0, rowspan = 1 ,columnspan = 2, sticky = (N,E,W,S)
        )
        self.eValue = StringVar()

        self.entry = Entry(master, font = 'c',textvariable = self.eValue)
        self.entry.grid(row = 0 ,column = 0 ,columnspan = 2 , sticky = (N,E,W,S))

        eButton = Button(master,text = 'Evaluate',command = self.evaluate)
        eButton.grid(row = 1 ,column = 0 , columnspan= 2,sticky = (N,E,W,S))

        # allowing the mainFrame to adjust itself accordingly to changes of the master
        #self.master.rowconfigure(0,weight=1)
        #self.master.columnconfigure(0,weight=1)

        # not allowing resizability
        self.master.resizable(False,False)

    def evaluate(self):
        '''Performing four operation Mul.Div,Sub,Add which are excepted to have the
        from ---> example add(1,2) or Add(1,2) otherwise an exception is raised'''

        exInput = (self.entry.get())

        if str(exInput[0:3]) not in ['Add','Mul','Div','Sub','add','sub','mul','div']:
            self.entry.delete(0,END)
            self.entry.insert(0,'Invalid input')
            self.entry.after(2000 , lambda: self.entry.delete(0,END))
            raise ValueError('Invalid input')
        else:
            expresion = eval(exInput)
            # checking for addition
            if str(exInput[0:3]).title() == 'Add':
                # eval turns the given expresion to a object of appropriate type
                # example string input Add(1,2) ---> (1) + (2) of type add
                self.entry.delete(0,END)
                self.entry.insert(0,str(eval(exInput)) + ' = ' +
                str((Add(Num(expresion.left),Num(expresion.right)).eval())))
                self.entry.after(2000,lambda: self.entry.delete(0,END))

            elif str(exInput[0:3]).title() == 'Mul':
                self.entry.delete(0,END)
                self.entry.insert(0,str(eval(exInput)) + ' = ' +
                str((Mul(Num(expresion.left),Num(expresion.right)).eval())))
                self.entry.after(2000,lambda: self.entry.delete(0,END))

            elif str(exInput[0:3]).title() == 'Sub':
                self.entry.delete(0,END)
                self.entry.insert(0,str(eval(exInput)) + ' = ' +
                str((Sub(Num(expresion.left),Num(expresion.right)).eval())))
                self.entry.after(2000,lambda: self.entry.delete(0,END))

            elif str(exInput[0:3]).title() == 'Div':
                self.entry.delete(0,END)
                self.entry.insert(0,str(eval(exInput)) + ' = ' +
                str((Div(Num(expresion.left),Num(expresion.right)).eval())))
                self.entry.after(2000,lambda: self.entry.delete(0,END))
            else:
                self.entry.delete(0,END)
                self.entry.insert(0,'Invalid input')
                self.entry.after(2000,lambda: self.entry.delete(0,END))


if __name__ == '__main__':
    root = Tk()
    my_app = ExpresionGUI(root)
    root.title('Epresion Evaluator')
    root.mainloop()
