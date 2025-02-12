"""
    Лабораторная работа №1
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-26Б
    Назначение: калькулятор для перевода из 10 в 4 систему счисления и обратно
"""

# Файл window.py - Главное окно калькулятора


import tkinter as tk
from functions import *
from config import *
from ui import AppUI


class CalculatorWindow(AppUI):
    def __init__(self):
        super().__init__(WIN_TITLE, WIN_SIZE)
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
        self.bind("<BackSpace>", self.delete)
        self.bind("<c>", self.clear)

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

    def change2dec(self, event=None):
        self.isDecSys = True
        self.updateCurrentSystem()
        self.value.set(self.decValLabel.cget("text"))

    def change2quad(self, event=None):
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
        if prevVal == "0" and symb != ".": prevVal = ""
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
        elif key == ".":
            self.pointButton.invoke()
        elif key == "-":
            self.negateButton.invoke()

    def negate(self, event=None):
        val = self.value.get()
        if val[0] == '-':
            val = val[1:]
        elif val[0] != '0' or (len(val) > 2 and val[1] == '.'):
            val = '-' + val
        self.value.set(val)
        self.updateLabels()

    def clear(self, event=None):
        self.value.set("0")
        self.updateLabels()

    def delete(self, event=None):
        prevVal = self.value.get()[:-1]
        if len(prevVal) == 0 or (prevVal == "-"): prevVal = "0"
        self.value.set(prevVal)
        self.updateLabels()


if __name__ == "__main__":
    window = CalculatorWindow()
    window.mainloop()
    