"""
LUNDI 5 DECEMBRE 2022

AUTEURS William MASIH,Yannis ELJEBBARI,Hugo BINDER
Code pour faire un space invader


"""


from tkinter import *
import threading
import time

kaarisx=650
boobax=50
boobay=200
boobadx=10
y=0
print(boobax)

Mafenetre=Tk()
#Mafenetre.attributes('-fullscreen', True)
background= PhotoImage(file = 'background.gif')
kaaris=PhotoImage(file= 'kaarisvaisseau.png')
booba=PhotoImage(file= 'booba.png')
cd=PhotoImage(file= 'cd.png')


Mafenetre.geometry('1500x1000+400+200')



Framebase=Frame(Mafenetre, relief ='groove', bg='green',width=1500,height=1000)

Framebase.pack(fill=BOTH, expand=True)

Canevas= Canvas(Framebase,width=1500,height=1000)
Canevas.pack(fill=BOTH, expand=True)

Canevas.create_image(0,0,anchor=NW, image=background)
kaarisimage=Canevas.create_image(kaarisx,850,image=kaaris)
boobaimage=Canevas.create_image(boobax,200,image=booba)
tirer=False
cdx=kaarisx
cdy=795


# Canevaskaaris=Canvas(Canevas,width=100,height=100)
# #Canevaskaaris.pack(side=BOTTOM,pady=10)
# Canevaskaaris.place(x=kaarisx,y=850)

# Canevaskaaris.create_image(0,0,anchor=NW, image=kaaris)

class dvd:
    def __init__(self):
        self.posx=0
        self.posy=795
        
    

def deplacerbooba(boobadx):
    global boobax,cdy,cdx,tirer
    gag=Canevas.create_image(kaarisx,cdy,image=cd)
    while True:
        
        boobax+=boobadx
            
        if boobax+50>=1500:
            boobadx=-boobadx
        if boobax-50<=0:
            boobadx=-boobadx
        if cdy<= 0:
            tirer = False
            cdy=795
            gag=Canevas.create_image(kaarisx,cdy,image=cd)
        if tirer == True:        
            Canevas.move(gag,0,-10)
            cdy-=10    
        print(cdy)
        print(tirer)
        Canevas.move(boobaimage,boobadx,0)

        time.sleep(0.05)

def tir(event):
    global kaarisx,tirer,cdx,cdy
    if tirer==False:          
        tirer=True
        cdx=kaarisx
        gag=Canevas.create_image(kaarisx,cdy,image=cd)
        prin(cdy)
    else:
        return


t1=threading.Thread(target=lambda : deplacerbooba(boobadx))
t1.start()


def left(event):
    global kaarisx,cdx
    if kaarisx-50<=0:
        return
    else:
            
        x = -10
        kaarisx+=x
        cdx+=x
        Canevas.move(kaarisimage,x,y)
    
def right(event):
    global kaarisx,cdx
    if kaarisx+50>=1500:
        return
    else:
            
        x = 10
        kaarisx+=x
        cdx+=x
        Canevas.move(kaarisimage,x,y)
        


Mafenetre.bind("<Left>",left)
Mafenetre.bind("<Right>",right)
Mafenetre.bind("<space>",tir)




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
