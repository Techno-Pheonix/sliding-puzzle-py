from tkinter import *
from tkinter import ttk
from scrollframe import *


class Recherche_menu:
    def __init__(self, init_labels):
        self.taquin_init_labels = init_labels
        self.fn()

    def dfs(self, window):
        window.destroy()
        x = scrollFrame()

      
      
        

    def fn(self):
        LogIn = Tk()
        LogIn.title("The home screen")

        LogIn.state("zoomed")

        LogIn['bg'] = '#000033'
        label = Label(LogIn, text="Select search method",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=80)

        spacingLabel = Label(LogIn, text="", font=(
            "Helvetica", 32), bg="#000033", fg="white")
        spacingLabel.pack(pady=5)

        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=20, width=30, font=("Helvetica", 16))

        Btn1 = ttk.Button(LogIn, text="Depth first search",
                          style="BW1.TButton", command=lambda: self.dfs(LogIn))
        Btn1.pack(pady=30)

        Btn2 = ttk.Button(LogIn, text="Breadth first search", style="BW1.TButton",
                          command=lambda: firstBtnClick(LogIn, "Users"))
        Btn2.pack(pady=30)

        Btn3 = ttk.Button(LogIn, text="A * search",style="BW1.TButton")
        Btn3.pack(pady=30)


        LogIn.mainloop()
