"""
LUNDI 5 DECEMBRE 2022

AUTEURS William MASIH,Yannis ELJEBBARI,Hugo BINDER
Code pour faire un space invader


"""


from tkinter import *

kaarisx=0

Mafenetre=Tk()
#Mafenetre.attributes('-fullscreen', True)
background= PhotoImage(file = 'background.gif')
kaaris=PhotoImage(file= 'kaarisvaisseau.png')
Mafenetre.geometry('1500x1000+400+200')



Framebase=Frame(Mafenetre, relief ='groove', bg='green',width=1500,height=1000)

Framebase.pack(fill=BOTH, expand=True)

Canevas= Canvas(Framebase,width=1500,height=1000)
Canevas.pack(fill=BOTH, expand=True)

Canevas.create_image(0,0,anchor=NW, image=background)

Canevaskaaris=Canvas(Canevas,width=100,height=100)
Canevaskaaris.pack(side=BOTTOM,pady=10)
Canevaskaaris.create_image(0,0,anchor=NW, image=kaaris)



# Label(Frame1,text="",bg='green').pack()


# Frame1 = Frame(Mafenetre, relief ='groove', bg='green')
# Frame1.pack(side='top', padx=10, pady =10)
# Label(Frame1,text="",bg='green').pack()




# Frame2 = Frame(Mafenetre, relief = 'groove', bg='bisque')
# Frame2.pack(side='left')

# Label(Frame2,text='test',bg='green').pack()
# test=StringVar()
# Champ = Entry(Frame2,textvariable= test)
# Champ.focus_set()
# Champ.pack(side='left')
# Button2 = Button(Frame2, text='jouer')
# Button2.pack()













Mafenetre.mainloop()
