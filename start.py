from random import randrange
from tkinter import *
from tkinter import ttk

from menu import *


class Taquin_etat_init:

    def __init__(self):
        self.labels = []
        self.white_index = 8
        self.rendertaquin()

    def taquin_randomize(self, labels):
        # possible values
        nbrs = [1, 2, 3, 4, 5, 6, 7, 8]
        # index of nbr
        i = 0
        # remove white fg from previous hidden taquin case
        labels[self.white_index]["fg"] = "black"
        # create a new one hidden taquin case
        white_label = randrange(9)
        self.white_index = white_label
        labels[white_label]["fg"] = "white"
        labels[white_label]["text"] = "0"

        for label in labels:
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

    def get_label_text(self):
        text = []
        for label in self.labels:
            text.append((label["text"], label["fg"]))
        return text

    def quit(self, window):
        text = self.get_label_text()
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
        label = Label(mainFrame, text="Welcome to the tquin game",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=10)

        label = Label(mainFrame, text="Choose taquin init state",
                      font=("Helvetica", 24), bg="#000033", fg="white")
        label.pack(pady=10)

        # the frame which contains the grid of taquin
        taquin_frame = Frame(mainFrame, bg="#000033")
        taquin_frame.pack()

        # the labels of taquin game
        self.labels.append(self.create_label(taquin_frame, 0, 0, 1))
        self.labels.append(self.create_label(taquin_frame, 0, 1, 2))
        self.labels.append(self.create_label(taquin_frame, 0, 2, 3))
        self.labels.append(self.create_label(taquin_frame, 1, 0, 4))
        self.labels.append(self.create_label(taquin_frame, 1, 1, 5))
        self.labels.append(self.create_label(taquin_frame, 1, 2, 6))
        self.labels.append(self.create_label(taquin_frame, 2, 0, 7))
        self.labels.append(self.create_label(taquin_frame, 2, 1, 8))
        self.labels.append(self.create_label(taquin_frame, 2, 2, 0, "white"))

        # some btn dope style
        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=15, width=20, font=("Helvetica", 16))

        btn_frame = Frame(mainFrame, bg="#000033")
        btn_frame.pack(pady=20)

        # the btn of randome
        btn_rand = ttk.Button(btn_frame, text="Randomize", style="BW1.TButton",
                              command=lambda:
                              self.taquin_randomize(self.labels))
        btn_rand.grid(row=0, column=0, padx=5)

        # the btn of of search methode
        btn_search = ttk.Button(
            btn_frame, text="Choose search methode", style="BW1.TButton", command=lambda:
            self.quit(top))
        btn_search.grid(row=0, column=1, padx=5)

        top.mainloop()


p = Taquin_etat_init()
