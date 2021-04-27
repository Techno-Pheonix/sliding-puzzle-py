import tkinter as tk
from tkinter import ttk

class ast:

    root = tk.Tk()
    root.title("The home screen")
    root.state("zoomed")
    root['bg'] = '#000033'

    container = ttk.Frame(root)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    #content 
    for i in range(50):
        Btn1 = ttk.Button(scrollable_frame, text="Recherche profendeur",
                        style="BW1.TButton")
        Btn1.pack(pady=30)

    container.pack(fill=tk.BOTH, expand=True)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
