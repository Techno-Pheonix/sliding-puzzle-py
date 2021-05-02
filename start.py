from random import randrange
from tkinter import *
from tkinter import ttk
from copy import deepcopy
from menu import *


class Taquin_etat_init:

    def __init__(self):
        self.entrys = []

        # end haffa

        self.white_index = 8
        self.rendertaquin()

    def taquin_randomize(self, Entry):
        # possible values
        nbrs = [1, 2, 3, 4, 5, 6, 7, 8]
        # index of nbr
        i = 0
        # remove white fg from previous hidden taquin case
        Entry[self.white_index]["fg"] = "black"
        # create a new one hidden taquin case
        white_label = randrange(9)
        self.white_index = white_label
        Entry[white_label]["fg"] = "white"
        Entry[white_label]["text"] = "0"

        for label in Entry:
            if (label["fg"] != "white"):
                indx = randrange(len(nbrs))
                i = i+1
                label["text"] = str(nbrs[indx])
                nbrs.pop(indx)

    def create_label(self, frame, rowVal, colVal, val, textCol="black"):
        label = Label(frame, text=val, font=("Helvetica", 32),
                      bg="white", fg=textCol, padx="40", pady="40")
        label.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return label

    # create field (haffa)
    def create_field(self, frame, rowVal, colVal):
        e = Text(frame, font=("Helvetica", 40), height=2, width=4, bg="white")
        e.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return e

    def render_taquin(self, frame, Label_text):
        for x in range(9):
            self.entrys.append(self.create_field(frame, x//3, x % 3))
        label = Label(frame, text=Label_text,
                      font=("Helvetica", 24), bg="#000033", fg="white")
        label.grid(column=1, row=3)

    def get_label_text(self):
        text_init = []
        text_final = []

        i = 1
        inter = []

        for label in self.entrys:
            inter.append(label.get("1.0", "end-1c"))
            if (i <= 9):
                if (i % 3 == 0):
                    l = deepcopy(inter)
                    text_init.append(l)
                    inter.clear()

            else:
                if (i % 3 == 0):
                    l = deepcopy(inter)
                    text_final.append(l)
                    inter.clear()

            i = i+1
        return (text_init, text_final)

    def quit(self, window):
        text = self.get_label_text()
        print(text)
        window.destroy()
        x = Recherche_menu(text)

    def rendertaquin(self):
        # main taquin frame
        top = Tk()
        top.title("The home screen")
        top.state("zoomed")
        top['bg'] = '#000033'

        # intermmediate frame from design
        mainFrame = Frame(top, bg="#000033")
        mainFrame.place(relx=.5, rely=.5, anchor="c")

        # hello text
        label = Label(mainFrame, text="Welcome to the sliding puzzle game",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=10)

        label = Label(mainFrame, text="Choose the init state",
                      font=("Helvetica", 24), bg="#000033", fg="white")
        label.pack(pady=10)

        # the frame which contains the grid of taquin
        main_frame = Frame(mainFrame, bg="#000033")
        main_frame.pack()

        taquin_init = Frame(main_frame, bg="#000033")
        taquin_init.grid(column=0, row=0, padx=20)

        taquin_fin = Frame(main_frame, bg="#000033")
        taquin_fin.grid(column=1, row=0, padx=20)
        # the Entry of taquin game

        self.render_taquin(taquin_init, "Start")
        self.render_taquin(taquin_fin, "Goal")

        # some btn dope style
        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=15, width=20, font=("Helvetica", 16))

        btn_frame = Frame(mainFrame, bg="#000033")
        btn_frame.pack(pady=20)

        # the btn of random
        btn_rand = ttk.Button(btn_frame, text="Randomize", style="BW1.TButton",
                              command=lambda:
                              self.taquin_randomize(self.Entry))
        btn_rand.grid(row=0, column=0, padx=5)

        # the btn of of search methode
        btn_search = ttk.Button(
            btn_frame, text="Choose search methode", style="BW1.TButton", command=lambda:
            self.quit(top))
        btn_search.grid(row=0, column=1, padx=5)

        top.mainloop()


p = Taquin_etat_init()
