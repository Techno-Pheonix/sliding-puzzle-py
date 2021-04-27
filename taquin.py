import tkinter
from tkinter import *

mainapp = Tk() #create window
mainapp.geometry('1280x720+300+150') #n7ot el settings toul ou 3ordh (+300+150 bech tji fel wost)
# #forced window size
mainapp.minsize(1280,720)
mainapp.maxsize(1920,1080)
#end forced window size
mainapp.title('Sliding Puzzle AI Solver')
mainapp.configure(bg='#00ccff')#background color
#mainapp.iconbitmap(r'hafhouf.ico')


class taquin:
  initial_state = [[3,2,7],[8,6,0],[1,5,4]]
  final_state = [[1,2,3],[8,0,4],[7,6,5]]
  t=[]
  def __init__(self):
    self.t == self.initial_state
  def est_etat_final():
    return self.t == self.final_state

def main():
    mainapp.title('Sliding Puzzle AI Solver V1.0')
    for c in mainapp.winfo_children():
        c.destroy()

    #creation de mainframe
    mainframe=Frame(mainapp,bg='#00ccff')
    mainframe.pack(pady="10")

    welcome = Label(mainframe, text = "Sliding Puzzle AI Solver" , font=("Verdana", 40) ,bg='#00ccff', fg='white' )
    welcome.pack(pady="20")

    
    mainframe1=LabelFrame(mainapp, bg="#00ccff").pack()
    mainframe2=LabelFrame(mainapp, bg="#00ccff").pack()

    mainframe=Frame(mainapp,width=1350, height=650, bd=12)
    mainframe.pack(side="top")

    f1 = Frame(mainframe, width=450, height=650, bd=12, relief="raise", bg="#00ccff")
    f1.pack(side="left")

    f2 = Frame(mainframe, width=450, height=650, bd=12, relief="raise",  bg="#00ccff")
    f2.pack(side="left")

    f3 = Frame(mainframe, width=450, height=650, bd=12, relief="raise", bg = "#00ccff")
    f3.pack(side="right")

    #frame 1
    titlef1=Label(f1,text="Settings : ", font=("Verdana", 15), bg='#00ccff', fg='white').pack(side="top",pady=10)
    fcheck = Frame(f1, width=200,height=37,bg='#00ccff')
    fcheck.pack()
    option = 0
    randombtn = Button(fcheck, text="Randomize", width=15, height=2, font=("Verdana", 10))
    randombtn.pack(pady=10)

    r1 = Radiobutton(fcheck,value=0, text = "     A Star     ",variable=option,font=("Verdana",13), bg='#00ccff')
    
    r2 = Radiobutton(fcheck,value=1 ,text = " Depth First  ",variable=option,font=("Verdana", 13), bg='#00ccff')
    
    r3 = Radiobutton(fcheck,value=2 ,text = "Breadth First ",variable=option,font=("Verdana", 12), bg='#00ccff')
    r1.pack()
    r2.pack()
    r3.pack()

    solvebtn = Button(fcheck, text="Solve", width=15, height=2, font=("Verdana", 10))
    solvebtn.pack(pady=10)
    
    #end frame1

  
    #hné n7otou fi woset el frame el wostaneya 


    #end frame 2

    #frame 3
    titlef3=Label(f3,text="Terminal : ", font=("Verdana", 20), bg='#00ccff', fg='white').pack(side="top")
    missionframe = Frame(f3, width=450, height=650)

    missionframe2 = Frame(f3, width=450, height=650)    
    mission_entry = Text(missionframe2, font=("Verdana", 10), width=33, height=15)
    mission_entry.pack()
    missionframe2.pack(pady=10)

    #end frame 3
    betweenframe=Frame(mainapp,bg='#00ccff')
    betweenframe.pack(pady=10)
    #developed by
    mainlabel=Label(mainframe1, text="Developped By : Phoenix Team", font=("Verdana", 15), bg='#00ccff',fg='white').pack()



    mainapp.mainloop() #loop bech to93ed el window dhahra
main()