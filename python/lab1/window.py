import tkinter as tk
from functions import *
from config import *
from ui import AppUI


class CalculatorWindow(AppUI):
    def __init__(self):
        super().__init__("Calculator", "300x380")
        self.setupUI()

        self.isDecSys = True
        self.updateCurrentSystem()
        self.decFrame.bind("<ButtonPress-1>", self.change2dec)
        self.quadFrame.bind("<ButtonPress-1>", self.change2quad)
        
        for i in range(10):
            self.buttons[i].config(state="normal", command=lambda x=i: self.enterSymb(str(x)))

        self.pointButton.config(command=lambda: self.enterSymb("."))
        self.negateButton.config(command=self.negate)
        self.clearButton.config(command=self.clear)
        self.deleteButton.config(command=self.delete)

        self.bind("<Key>", self.onPressKeyboardButton)

        self.value = tk.StringVar(self, "0")
        self.mainLabel.config(textvariable=self.value)

    def updateCurrentSystem(self):
        if self.isDecSys:
            self.decNameLabel.config(state="normal")
            self.decValLabel.config(state="normal")
            self.quadNameLabel.config(state="disabled")
            self.quadValLabel.config(state="disabled")
            for i in range(4, 10):
                self.buttons[i].config(state="normal")
            
        else:
            self.decNameLabel.config(state="disabled")
            self.decValLabel.config(state="disabled")
            self.quadNameLabel.config(state="normal")
            self.quadValLabel.config(state="normal")
            for i in range(4, 10):
                self.buttons[i].config(state="disabled")

    def change2dec(self, event):
        self.isDecSys = True
        self.updateCurrentSystem()
        self.value.set(self.decValLabel.cget("text"))

    def change2quad(self, event):
        self.isDecSys = False
        self.updateCurrentSystem()
        self.value.set(self.quadValLabel.cget("text"))


    def updateLabels(self):
        if self.isDecSys:
            self.decValLabel.config(text=deleteZeros(f"{float(self.value.get()):.{PRECISION}f}"))
            self.quadValLabel.config(text=deleteZeros(to4(self.value.get(), PRECISION)))

        else:
            self.decValLabel.config(text=deleteZeros(from4(self.value.get(), PRECISION)))
            self.quadValLabel.config(text=deleteZeros(f"{float(self.value.get()):.{PRECISION}f}"))

    def enterSymb(self, symb: str):
        prevVal = self.value.get()
        if prevVal == "0": prevVal = ""
        try:
            self.value.set(prevVal + symb)
            self.updateLabels()
        except:
            self.value.set(prevVal)
            self.updateLabels()

    def onPressKeyboardButton(self, event: tk.Event):
        key = event.char
        if key.isdigit():
            self.buttons[int(key)].invoke()

    def negate(self):
        pass

    def clear(self):
        self.value.set("0")
        self.updateLabels()

    def delete(self):
        prevVal = self.value.get()[:-1]
        if len(prevVal) == 0: prevVal = "0"
        self.value.set(prevVal)
        self.updateLabels()


if __name__ == "__main__":
    window = CalculatorWindow()
    window.mainloop()
    