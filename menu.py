from tkinter import *
from tkinter import ttk

from dfs import *


class Recherche_menu:
    def __init__(self, init_labels):
        self.taquin_init_labels = init_labels
        self.fn()

    def dfs(self, window):
        window.destroy()
        dfs = dfs_taquin(self.taquin_init_labels)

    def fn(self):
        LogIn = Tk()
        LogIn.title("The home screen")

        LogIn.state("zoomed")

        LogIn['bg'] = '#000033'
        label = Label(LogIn, text="Select recherche method",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=80)

        spacingLabel = Label(LogIn, text="", font=(
            "Helvetica", 32), bg="#000033", fg="white")
        spacingLabel.pack(pady=5)

        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=20, width=30, font=("Helvetica", 16))

        Btn1 = ttk.Button(LogIn, text="Recherche profendeur",
                          style="BW1.TButton", command=lambda: self.dfs(LogIn))
        Btn1.pack(pady=30)

        Btn2 = ttk.Button(LogIn, text="Recherche largeur", style="BW1.TButton",
                          command=lambda: firstBtnClick(LogIn, "Users"))
        Btn2.pack(pady=30)

        Btn3 = ttk.Button(LogIn, text="Recherche A*",
                          style="BW1.TButton", command=lambda: Quit(LogIn))
        Btn3.pack(pady=30)

        LogIn.mainloop()
