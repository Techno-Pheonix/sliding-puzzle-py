import tkinter as tk
from tkinter import ttk


class scrollFrame:

    def __init__(self, taquin_init_labels):
        self.x = taquin_init_labels
        print(self.x)
        self.render()

    def create_label(self, frame, rowVal, colVal, val, textCol="black"):
        label = tk.Label(frame, text=val, font=("Helvetica", 32),
                         bg="white", fg=textCol, padx="40", pady="40")
        label.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return label

    def affiche_taquin(self, frame):
        self.create_label(frame, 0, 0, 1)
        self.create_label(frame, 0, 1, 2)
        self.create_label(frame, 0, 2, 3)
        self.create_label(frame, 1, 0, 4)
        self.create_label(frame, 1, 1, 5)
        self.create_label(frame, 1, 2, 6)
        self.create_label(frame, 2, 0, 7)
        self.create_label(frame, 2, 1, 8)
        self.create_label(frame, 2, 2, 0, "white")

    def render(self):
        root = tk.Tk()
        root.title("The home screen")
        root.state("zoomed")
        root['bg'] = '#000033'

        container = tk.Frame(root)
        canvas = tk.Canvas(container, bg="#000033")
        scrollbar = ttk.Scrollbar(
            container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#000033")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (100, 100), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i in range(4):
            taquin_frame = tk.Frame(scrollable_frame, bg="#000033")
            taquin_frame.pack(expand=True)
            for j in range(3):
                taquin_row = tk.Frame(taquin_frame, bg="#000033")
                taquin_row.grid(row=i, column=j, padx=10, pady=10)
                self.affiche_taquin(taquin_row)
                label = tk.Label(taquin_row, text="step"+str(i*3+j+1),
                                 font=("Helvetica", 24), bg="#000033", fg="white")
                label.grid(row=4, column=1)

        container.pack(fill=tk.BOTH, expand=True)

        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        root.mainloop()


#x = scrollFrame()
