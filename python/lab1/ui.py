import tkinter as tk
from config import *


class AppUI(tk.Tk):
    def __init__(self, win_title, win_geometry):
        super().__init__()

        self.title(win_title)
        self.geometry(win_geometry)
        self.resizable(False, False)
        self.config(background=MAIN_BACKGROUND_COLOR)

    def initLabel(self, frame: tk.Frame, text: str, **kwargs) -> tk.Label:
        return tk.Label(
            frame,
            text=text,
            background=MAIN_BACKGROUND_COLOR,
            font=(MAIN_FONT, 14),
            justify="left",
            foreground=TEXT_COLOR,
            disabledforeground=DISABLED_COLOR,
            **kwargs,
        )
    
    def initKeyboardButton(self, frame: tk.Frame, text: str, color=FUNC_COLOR, **kwargs) -> tk.Button:
        return tk.Button(
            frame,
            text=text,
            font=(MAIN_FONT, 14, "bold"),
            relief="flat",
            foreground=TEXT_COLOR,
            activebackground=FIRST_ACCENT_COLOR,
            activeforeground=TEXT_COLOR,
            border=0,
            background=color,
            width=500,
            cursor="hand2",
            **kwargs,
        )

    def setupUI(self):
        # Основное поле калькулятора
        self.mainLabel = tk.Label(
            self,
            text="0",
            anchor="e",
            background=SECOND_ACCENT_COLOR,
            foreground=TEXT_COLOR,
            font=(MAIN_FONT, 20, "bold"),
            padx=15,
            pady=15,
        )
        self.mainLabel.pack(fill="x")

        # Поля представления числа в десятичной системе счисления
        self.decFrame = tk.Frame(self, background=MAIN_BACKGROUND_COLOR, cursor="hand2")
        self.decFrame.grid_columnconfigure(0, minsize=60)
        self.decFrame.pack(fill="x", padx=10, pady=[10, 0])
        
        self.decNameLabel = self.initLabel(self.decFrame, "DEC")
        self.decNameLabel.grid(sticky="w", row=0, column=0)
        self.decNameLabel.bindtags((str(self.decFrame),) + self.decNameLabel.bindtags()[1:])

        self.decValLabel = self.initLabel(self.decFrame, "0")
        self.decValLabel.grid(row=0, column=1)
        self.decValLabel.bindtags((str(self.decFrame),) + self.decValLabel.bindtags()[1:])

        # Поля представления числа в четверичной системе счисления
        self.quadFrame = tk.Frame(self, background=MAIN_BACKGROUND_COLOR, cursor="hand2")
        self.quadFrame.grid_columnconfigure(0, minsize=60)
        self.quadFrame.pack(fill="x", padx=10)

        self.quadNameLabel = self.initLabel(self.quadFrame, "QUAD")
        self.quadNameLabel.grid(sticky="w", row=0, column=0)
        self.quadNameLabel.bindtags((str(self.quadFrame),) + self.quadNameLabel.bindtags()[1:])

        self.quadValLabel = self.initLabel(self.quadFrame, "0")
        self.quadValLabel.grid(row=0, column=1)
        self.quadValLabel.bindtags((str(self.quadFrame),) + self.quadValLabel.bindtags()[1:])

        # Клавиатура
        self.keyboardFrame = tk.Frame(self, background=MAIN_BACKGROUND_COLOR)
        for i in range(3): self.keyboardFrame.columnconfigure(i, weight=1)
        for i in range(4): self.keyboardFrame.grid_rowconfigure(i, weight=1)

        self.keyboardFrame.pack(padx=10, pady=10, expand=True)

        # Операции +/-, С, <-
        self.negateButton = self.initKeyboardButton(self.keyboardFrame, "+/-")
        self.negateButton.grid(padx=3, pady=3, row=0, column=0, sticky="nsew")

        self.clearButton = self.initKeyboardButton(self.keyboardFrame, "CL")
        self.clearButton.grid(padx=3, pady=3, row=0, column=1, sticky="nsew")

        self.deleteButton = self.initKeyboardButton(self.keyboardFrame, "<=")
        self.deleteButton.grid(padx=3, pady=3, row=0, column=2, sticky="nsew")

        # Цифры
        self.btn0 = self.initKeyboardButton(self.keyboardFrame, "0", SECOND_ACCENT_COLOR)
        self.btn0.grid(padx=3, pady=3, row=4, column=1, sticky="nsew")

        self.btn1 = self.initKeyboardButton(self.keyboardFrame, "1", SECOND_ACCENT_COLOR)
        self.btn1.grid(padx=3, pady=3, row=3, column=0, sticky="nsew")

        self.btn2 = self.initKeyboardButton(self.keyboardFrame, "2", SECOND_ACCENT_COLOR)
        self.btn2.grid(padx=3, pady=3, row=3, column=1, sticky="nsew")

        self.btn3 = self.initKeyboardButton(self.keyboardFrame, "3", SECOND_ACCENT_COLOR)
        self.btn3.grid(padx=3, pady=3, row=3, column=2, sticky="nsew")

        self.btn4 = self.initKeyboardButton(self.keyboardFrame, "4", SECOND_ACCENT_COLOR)
        self.btn4.grid(padx=3, pady=3, row=2, column=0, sticky="nsew")

        self.btn5 = self.initKeyboardButton(self.keyboardFrame, "5", SECOND_ACCENT_COLOR)
        self.btn5.grid(padx=3, pady=3, row=2, column=1, sticky="nsew")

        self.btn6 = self.initKeyboardButton(self.keyboardFrame, "6", SECOND_ACCENT_COLOR)
        self.btn6.grid(padx=3, pady=3, row=2, column=2, sticky="nsew")

        self.btn7 = self.initKeyboardButton(self.keyboardFrame, "7", SECOND_ACCENT_COLOR)
        self.btn7.grid(padx=3, pady=3, row=1, column=0, sticky="nsew")

        self.btn8 = self.initKeyboardButton(self.keyboardFrame, "8", SECOND_ACCENT_COLOR)
        self.btn8.grid(padx=3, pady=3, row=1, column=1, sticky="nsew")

        self.btn9 = self.initKeyboardButton(self.keyboardFrame, "9", SECOND_ACCENT_COLOR)
        self.btn9.grid(padx=3, pady=3, row=1, column=2, sticky="nsew")

        self.pointButton = self.initKeyboardButton(self.keyboardFrame, ".")
        self.pointButton.grid(padx=3, pady=3, row=4, column=0, sticky="nsew")

        self.buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
