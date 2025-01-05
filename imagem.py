import tkinter as tk
from tkinter import ttk
import math


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Científica")
        self.geometry("400x500")
        self.config(bg="lightblue")

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14, "bold"), padding=10)
        style.configure("TEntry", font=("Arial", 18))

        self.display = ttk.Entry(self, font=("Arial", 18), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        botoes = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("C", 5, 0),
            ("√", 5, 1),
            ("x²", 5, 2),
            ("ln", 5, 3),
            ("sin", 6, 0),
            ("cos", 6, 1),
            ("tan", 6, 2),
            ("!", 6, 3),
        ]

        for texto, linha, coluna in botoes:
            ttk.Button(
                self,
                text=texto,
                command=lambda t=texto: self.on_button_click(t),
                style="TButton",
            ).grid(row=linha, column=coluna, sticky="nsew")

        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, texto):
        if texto == "C":
            self.display.delete(0, tk.END)
        elif texto == "=":
            try:
                self.display.insert(tk.END, " = " + str(eval(self.display.get())))
            except Exception as e:
                self.display.insert(tk.END, " Erro")
        elif texto == "√":
            try:
                valor = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, math.sqrt(valor))
            except ValueError:
                self.display.insert(tk.END, " Erro")
        elif texto == "x²":
            try:
                valor = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, valor**2)
            except ValueError:
                self.display.insert(tk.END, " Erro")
        elif texto == "ln":
            try:
                valor = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, math.log(valor))
            except ValueError:
                self.display.insert(tk.END, " Erro")
        elif texto == "sin":
            try:
                valor = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, math.sin(math.radians(valor)))
            except ValueError:
                self.display.insert(tk.END, " Erro")
        elif texto == "cos":
            try:
                valor = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, math.cos(math.radians(valor)))
            except ValueError:
                self.display.insert(tk.END, " Erro")
        elif texto == "tan":
            try:
                valor = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, math.tan(math.radians(valor)))
            except ValueError:
                self.display.insert(tk.END, " Erro")
        elif texto == "!":
            try:
                valor = int(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, math.factorial(valor))
            except ValueError:
                self.display.insert(tk.END, " Erro")
        else:
            self.display.insert(tk.END, texto)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
