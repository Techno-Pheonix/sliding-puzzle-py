from tkinter import *
from tkinter import ttk
from dfs import *


class dfs_taquin:

    def __init__(self, values):
        self.labels = []
        self.values = values
        self.rendertaquin()

    def create_label(self, frame, rowVal, colVal, val):
        label = Label(frame, text=val, font=("Helvetica", 32),
                      bg="white", fg="black", padx="40", pady="40")
        label.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return label

    def start_rech(self):
        print(self.labels)
        x = dfs(self.labels, self.values)
        x.recherche(self.values[0], self.values[1])

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
        label = Label(mainFrame, text="Deapth first search",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=20)

        # the frame which contains the grid of taquin
        taquin_frame = Frame(mainFrame, bg="#000033")
        taquin_frame.pack()

        # the labels of taquin game
        i = 0
        for label in self.values[0]:
            for x in label:
                self.labels.append(self.create_label(taquin_frame, i//3, i %
                                                     3, x))
                i = i+1

        # some btn dope style
        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=15, width=26, font=("Helvetica", 16))

        # the btn of randome
        btn_rand = ttk.Button(mainFrame, text="Start",
                              style="BW1.TButton", command=lambda: self.start_rech())
        btn_rand.pack(pady=15)

        top.mainloop()
