from tkinter import *
from tkinter import ttk
from dfs import *
from BFS import *
from scrollframe import *


class interface_taquin:

    def __init__(self, values, search_type):
        self.search_type = search_type
        self.labels = []
        self.values = values
        self.rendertaquin()
        self.rech_sequance = []

    def create_label(self, frame, rowVal, colVal, val, text_col="black"):
        label = Label(frame, text=val, font=("Helvetica", 32),
                      bg="white", fg=text_col, padx="40", pady="40")
        label.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return label

    def start_rech(self):
        if (self.search_type == "dfs"):
            x = dfs(self.labels, self.values)
            self.rech_sequance = x.recherche(self.values[0], self.values[1])
        elif (self.search_type == "bfs"):
            x = bfs(self.labels, self.values)
            self.rech_sequance = x.recherche(self.values[0], self.values[1])
        else:
            i = 1

    def see_detail(self, window):
        window.destroy()
        x = scrollFrame(self.rech_sequance)

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
                if (x == "0"):
                    self.labels.append(self.create_label(taquin_frame, i//3, i %
                                                         3, x, "white"))
                else:
                    self.labels.append(self.create_label(taquin_frame, i//3, i %
                                                         3, x))
                i = i+1

        # some btn dope style
        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=15, width=26, font=("Helvetica", 16))

        # the btn of randome
        btn_frame = Frame(mainFrame, bg="#000033")
        btn_frame.pack(pady=20)

        btn_rand = ttk.Button(btn_frame, text="Details", style="BW1.TButton",
                              command=lambda:
                              self.see_detail(top))
        btn_rand.grid(row=0, column=0, padx=5)

        # the btn of of search methode
        btn_search = ttk.Button(
            btn_frame, text="start", style="BW1.TButton", command=lambda: self.start_rech())
        btn_search.grid(row=0, column=1, padx=5)

        top.mainloop()
