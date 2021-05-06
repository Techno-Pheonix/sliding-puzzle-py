import tkinter as tk
from tkinter import ttk


class scrollFrame:

    def __init__(self, taquin_init_labels, values):
        self.values = values
        self.rech_sequance = taquin_init_labels
        self.render()

    def create_label(self, frame, rowVal, colVal, val, textCol="black"):
        label = tk.Label(frame, text=val, font=("Helvetica", 32),
                         bg="white", fg=textCol, padx="40", pady="40")
        label.grid(row=rowVal, column=colVal, padx=3, pady=3)
        return label

    def affiche_taquin(self, frame, vals):
        for i in range(len(vals)):
            for j in range(len(vals[i])):
                if (vals[i][j] == "0"):
                    self.create_label(frame, i, j, vals[i][j], "white")
                else:
                    self.create_label(frame, i, j, vals[i][j])

    def return_menu(self, window):
        window.destroy()
        import menu as m
        y = m.Recherche_menu(self.values)

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
            (450, 100), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        i = 0

        for x in self.rech_sequance:
            if (i % 3 == 0):
                taquin_frame = tk.Frame(scrollable_frame, bg="#000033")
                taquin_frame.pack(expand=True)
            taquin_row = tk.Frame(taquin_frame, bg="#000033")
            taquin_row.grid(row=i//3, column=i % 3, padx=10, pady=10)
            self.affiche_taquin(taquin_row, x)
            label = tk.Label(taquin_row, text="step"+str(i+1),
                             font=("Helvetica", 24), bg="#000033", fg="white")
            label.grid(row=4, column=1)
            i = i+1

        style = ttk.Style()
        style.configure('BW1.TButton', forground="bleu", padding=10,
                        height=20, width=30, font=("Helvetica", 16))

        Btn = ttk.Button(scrollable_frame, text="return", style="BW1.TButton",
                         command=lambda: self.return_menu(root))
        Btn.pack(pady=30)
        container.pack(fill=tk.BOTH, expand=True)

        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        root.mainloop()


#x = scrollFrame()
