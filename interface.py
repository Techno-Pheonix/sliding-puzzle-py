from tkinter import *
from tkinter import ttk
from dfs1 import *
from bfs import *
from scrollframe import *
from A_StarSearch import *


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

    def start_rech(self, label):
        if (self.search_type == "dfs"):
            dfs(self.values[0], self.values[1])
            self.rech_sequance = trace
            for j in trace:
                i = 0
                for x in self.labels:
                    if (j[i//3][i % 3] == "0"):
                        x["fg"] = "white"
                    else:
                        x["fg"] = "black"
                    x["text"] = j[i//3][i % 3]
                    i = i+1
                if (estEtatFinal(j,  self.values[1])):
                    label["text"] = "sucess"
                else:
                    label["text"] = "echec"
                    label["fg"] = "red"
            #x = dfs(self.labels, self.values)
            #self.rech_sequance = x.recherche(self.values[0], self.values[1])
        elif (self.search_type == "bfs"):
            x = bfs(self.labels, self.values)
            self.rech_sequance = x.recherche(
                self.values[0], self.values[1], label)
        else:
            x = a_star(self.labels, self.values)
            self.rech_sequance = x.recherche(
                self.values[0], self.values[1], label)

    def see_detail(self, window):
        window.destroy()
        x = scrollFrame(self.rech_sequance, self.values)

    def return_menu(self, window):
        window.destroy()
        import menu as m
        y = m.Recherche_menu(self.values)

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
        label = Label(mainFrame, text="",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=20)
        if (self.search_type == "dfs"):
            label["text"] = "Depth-first search"
        elif (self.search_type == "bfs"):
            label["text"] = "Breadth-first search"
        else:
            label["text"] = "A star search"
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

        label = Label(mainFrame, text="",
                      font=("Helvetica", 32), bg="#000033", fg="white")
        label.pack(pady=20)

        # the btn of randome
        btn_frame = Frame(mainFrame, bg="#000033")
        btn_frame.pack(pady=20)

        btn_rand = ttk.Button(btn_frame, text="Details", style="BW1.TButton",
                              command=lambda:
                              self.see_detail(top))
        btn_rand.grid(row=0, column=0, padx=5)

        # the btn of of search methode
        btn_search = ttk.Button(
            btn_frame, text="start", style="BW1.TButton", command=lambda: self.start_rech(label))
        btn_search.grid(row=0, column=1, padx=5)

        btn_search = ttk.Button(
            btn_frame, text="return", style="BW1.TButton", command=lambda: self.return_menu(top))
        btn_search.grid(row=0, column=2, padx=5)

        top.mainloop()


# x = interface_taquin(([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']], [

 #   ['1', '2', '3'], ['4', '5', '6'], ['0', '7', '8']]), "dfs")
