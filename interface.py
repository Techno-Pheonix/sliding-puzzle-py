from tkinter import *
from tkinter import ttk


class dfs_taquin:

    def __init__(self, init_labels):
        self.labels = []
        self.taquin_init_labels = init_labels
        self.rendertaquin()

    def create_label(self, frame, rowVal, colVal, val, textCol="black"):
        label = Label(frame, text=val, font=("Helvetica", 32),
                      bg="white", fg=textCol, padx="40", pady="40")
        label.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return label

    def quit(self, window):
        window.destroy()
        x = Recherche_menu(self.labels)

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
        for label in self.taquin_init_labels:
            self.labels.append(self.create_label(taquin_frame, i//3, i %
                                                 3, label[0], label[1]))
            i = i+1

        # some btn dope style
        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=15, width=26, font=("Helvetica", 16))

        # the btn of randome
        btn_rand = ttk.Button(mainFrame, text="Start", style="BW1.TButton")
        btn_rand.pack(pady=15)

        top.mainloop()
