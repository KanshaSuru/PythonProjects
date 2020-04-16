import tkinter as tk
from tkinter import ttk
__author__ = "Bonagni"

class TKinterGUI(tk.Frame, ttk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_UI()

    def initialize_UI(self):
        #create and instanciate the tk GUI

        #use Geometry module to manage the space
        #root.geometry("800x600")

        #Ttk Frame widget is a container, used to group other widgets together.
        self.Frame = ttk.Frame(self.parent, padding=(10,50))
        self.parent.title("Practicing with TK-inter GUI")
        self.parent.grid()

        #store input
        self.userName = tk.StringVar()
        self.displayName = tk.StringVar()

        #define the Name Label
        self.nameLable = ttk.Label(self.parent, text = "Your Name: ")
        #nameLable.pack(side="left", padx=(10,10))
        self.nameLable.grid(column=0, row=0, sticky="E")

        #define the input textfield
        self.txtName = ttk.Entry(self.parent, width="20", textvariable=self.userName)
        #txtName.pack(side ="left")
        self.txtName.grid(column=1, row=0, padx=10, sticky="EW")
        #set docus in the text input field
        self.txtName.focus()

        #define the display Name Label
        self.displayNameLable = ttk.Label(self.parent, text = "output", textvariable= self.displayName)
        #displayNameLable.pack(side="left", padx=(10,10))
        self.displayNameLable.grid(column=1, row=1, sticky="E")



        #define the greeting button
        self.greetingButton = ttk.Button(self.parent, text="Greet", command= self.sayHi)
        #greetingButton.pack(side="left")
        self.greetingButton.grid(column=3, row=0, padx=10, sticky="EW")

        #define the button which ends the session
        self.quitButton = tk.Button(self.parent, text="Quit", command=root.destroy)
        #quitButton.pack(side="right")
        self.quitButton.grid(column =0, row=2, sticky ="S")

    def sayHi(self):
        """
        Prints greating
        if no username is entered then "world" will be used.
        """
        msg = """Hi welcome to your first GUI in python using tkinter """ + self.userName.get() or "World!"
        self.displayName.set(msg)

#call the page to life
if __name__ == '__main__':
    root = tk.Tk()
    run = TKinterGUI(root)
    root.mainloop()
