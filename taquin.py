import tkinter
from tkinter import *

mainapp = Tk() #create window
mainapp.geometry('1280x720+300+150') #n7ot el settings toul ou 3ordh (+300+150 bech tji fel wost)
# #forced window size
mainapp.minsize(1280,720)
mainapp.maxsize(1920,1080)
#end forced window size
mainapp.title('Hafhouf Jobs System V1.0')
mainapp.configure(bg='#00ccff')#background color
mainapp.iconbitmap(r'hafhouf.ico')

class taquin:
  initial_state = [[3,2,7],[8,6,0],[1,5,4]]
  final_state = [[1,2,3],[8,0,4],[7,6,5]]
  t=[]
  def __init__(self):
    self.t == self.initial_state
  def est_etat_final():
    return self.t == self.final_state

def main():
    mainapp.title('Hafhouf Jobs System V1.0')
    for c in mainapp.winfo_children():
        c.destroy()

    #creation de mainframe
    mainframe=Frame(mainapp,bg='#00ccff')
    mainframe.pack(expand = 1)

    welcome = Label(mainframe, text = "Welcome to Hafhouf Jobs System" , font=("Verdana", 40) ,bg='#00ccff', fg='white' )
    welcome.pack(pady = 100)

    # create admin Buttons
    b1=Button(mainframe, text="Admin", height="1", width="30",font=("Verdana", 30), command=lambda: admin(mainapp), fg='#00ccff').pack(pady = 20)

    # create a job seeker button
    b2=Button(mainframe, text="Job Seeker", height="1", width="30", font=("Verdana", 30),fg='#00ccff',command=lambda:jobmenu(mainapp)).pack(pady = 20)
    mainframe1=LabelFrame(mainapp, bg="#00ccff").pack()
    mainlabel=Label(mainframe1, text="Developped By : Mohamed Aziz Hafhouf", font=("Verdana", 15), bg='#00ccff',fg='white').pack()

    mainframe2=LabelFrame(mainapp, bg="#00ccff").pack()
    mainversion=Label(mainframe2, text="V 1.0", font=("Verdana", 15), bg='#00ccff',fg='white').pack(side="right")

    mainapp.mainloop() #loop bech to93ed el window dhahra
main()