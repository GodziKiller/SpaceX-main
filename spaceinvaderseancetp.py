#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:21:26 2022

@author: hugo.binder
"""

from tkinter import *
import threading
import time
import random
import pygame


#valeur position initiale vaisseau/alien
posvx=550
posvy=650
posax=random.randint(50,1230)
posay=100
ListeTirs=[]
ListeAlien=["booba.png","JUL.png","GIMS.png"]
ListeTirsBooba=[]
Listeennemis=[]
Listeprotections=[]
Listeprotx=[]
vies=3
nbprot=9
niveau=1
vitessetir=2000
Score=0
print("ca fonctionne")
#création des objets et méthodes

class Spaceship:
    def __del__(self):
        print ("deleted")
    def __init__(self):
        self.x=posvx
        self.y=posvy
        self.apparence = Canevas.create_image(self.x,self.y,anchor='nw',image=ImageVaisseau,tag="kaaris")
    def affichage(self):
        Canevas.coords(self.apparence,self.x,self.y)

    def deplacement(self,dir):
        global posvx
        if dir==1:
            if self.x<1245:
                self.x+=10
                posvx=self.x
            else:
                self.x=0
        elif dir==-1:
            if self.x>0:
                self.x+=-10
                posvx=self.x
            else:
                self.x=1245
        else:
            pass
        self.affichage()




class Alien:
    def __del__(self):
        print ("deleted")    
    posay=100
    def __init__(self,posax,niveau):
        self.boobay=Alien.posay
        self.boobax=posax
        self.envie=True
        self.boobadx=random.randint(-10,10)
        self.image=PhotoImage(file=ListeAlien[niveau-1])
        self.apparence = Canevas.create_image(self.boobax,self.boobay,image=self.image)
        # self.truc=Canevas.create_line(self.boobax-50, self.boobay-50, self.boobax+50 ,self.boobay+50 , fill='white')
    def affichage(self):
        Canevas.coords(self.apparence,self.boobax,self.boobay)
        # Canevas.coords(self.truc,self.boobax-50, self.boobay-50, self.boobax+50 ,self.boobay+50 )






class protection:
    global Listeprotections
    def __del__(self):
        print ("deleted")
    def __init__(self,lavariablex):
        self.x=lavariablex
        self.xvalide=0
        self.y=600
        self.apparence=Canevas.create_rectangle(self.x,self.y,self.x+50,self.y+20,fill='blue')


            
    def checkcollision(self):
        global ListeTirsBooba
        for Prot in Listeprotections:
            for booba in Listeennemis:
                if booba.boobax<=Prot.x+50 and booba.boobax+50>Prot.x-50:
                    if booba.boobay+50>Prot.y-20 and booba.boobay<Prot.y+20:
                        print("BOOBA TOUCHE PROTEVTION")
                        Canevas.delete(Prot.apparence)
                        gagagou=Listeprotections.index(Prot)
                        del Listeprotections[gagagou]
                        Canevas.delete(booba.apparence)
                        del Listeennemis[0]
                        booba.boobay=650
                        restartbooba()
                

            


class TirSpaceship:
    compteur=0
    def __del__(self):
        print ("deleted")
    def __init__(self):
        self.tirx=posvx
        self.tiry=posvy
        # self.apparence=Canevas.create_line(self.x+15 , self.y-50 , self.x+15 ,self.y , fill='white')
        self.apparence=Canevas.create_image(self.tirx+15, self.tiry, image=ImageTir)
        self.tirage=1
        TirSpaceship.compteur+=1
        print("letirvamonter")
        self.tirmonte()

    
    def affichage(self):
        Canevas.coords(self.apparence , self.tirx+15 , self.tiry)


    def tirmonte(self):
        if self.tirage==1:
            self.tiry-=10
            self.affichage()
            self.fintir()
            Mafenetre.after(5,self.tirmonte)

    def fintir(self):
        global ListeTirs,Score,Listeennemis,niveau,vitessetir
        if self.tiry<0:
            if ListeTirs!=[]:

                print("finito")
                self.tirage==0
                Canevas.delete(self.apparence)
                del ListeTirs[0]


        for booba in Listeennemis:

            if self.tirx<=booba.boobax+50 and self.tirx+15>booba.boobax-50:
                if self.tiry+15>booba.boobay-50 and self.tiry<booba.boobay+50:
                    # Canevas.delete(booba.apparence)
                    # # booba.apparence = Canevas.create_image(booba.boobax,booba.boobay,image=ImageAlienmort)

                    # # boobamort(booba)
                    # print("touché")
                    # Canevas.after(1000)
                    # print("careprend")
                    Score+=10
                    affichageautre(vies,Score)
                    if Score ==100:
                        print("next level")
                        niveau+=1
                        vitessetir=int(vitessetir/2)
                        pygame.mixer.music.load("JOULE.wav")
                        pygame.mixer.music.play(loops=-1, start=0.0)
                        del ListeTirsBooba[0]


                    if Score ==200:
                        print("next level")
                        niveau+=1
                        vitessetir=int(vitessetir/1.5)
                        pygame.mixer.music.load("BELLA.wav")
                        pygame.mixer.music.play(loops=-1, start=0.0)
                        del ListeTirsBooba[0]
                                           
                    Canevas.delete(booba.apparence)
                    del Listeennemis[0]
                    booba.boobay=650
                    del booba
                    restartbooba()               

                    Canevas.delete(self.apparence)

                    self.tiry=-10






class TirBooba:
    compteur=0
    def __del__(self):
        print ("deleted")
    def __init__(self,booba):
        self.tirx=booba.boobax
        self.tiry=booba.boobay
        # self.apparence=Canevas.create_line(self.x+15 , self.y-50 , self.x+15 ,self.y , fill='white')
        self.apparence=Canevas.create_image(self.tirx+15, self.tiry, image=ImageTir)
        print("letirvadescendre")
        self.tirdescent()

    
    def affichage(self):
        Canevas.coords(self.apparence , self.tirx+15 , self.tiry)


    def tirdescent(self):
        self.tiry+=10
        self.affichage()
        self.fintirbooba()
        Mafenetre.after(50,self.tirdescent)

    def fintirbooba(self):
        global ListeTirsBooba,Score,Listeennemis,vies
        for booba in Listeennemis:
            for tir in ListeTirsBooba:
                if tir.tiry>700:
                    Canevas.delete(tir.apparence)
                    if len(ListeTirsBooba)>1:
                        del ListeTirsBooba[0]



        for booba in Listeennemis:
            for tir in ListeTirsBooba:
                if tir.tirx<=vaisseau.x+15 and tir.tirx+15>vaisseau.x:
                    if tir.tiry+15>vaisseau.y and tir.tiry<vaisseau.y+15:
                        print("BOOBA A TIRE SUR KAARIS")
                        del ListeTirsBooba[0]
                        Canevas.delete(tir.apparence)
                        vies-=1
                        affichageautre(vies,Score)
            for Prot in Listeprotections:
                if self.tirx<=Prot.x+50 and self.tirx+15>Prot.x:
                    if self.tiry+15>Prot.y and self.tiry<Prot.y+20:
                        print("COLLISION AVEC PROTECTION")
                        gagagou=Listeprotections.index(Prot)
                        del Listeprotections[gagagou]
                        Canevas.delete(Prot.apparence)
                        Canevas.delete(self.apparence)
                        if len(ListeTirsBooba)>1:
                             del ListeTirsBooba[0]
        
        


# création des fonctions à appliquer sur chaque  objet
def mouvementAlien():

    global Score,Listeennemis,Listeprotections,vies
    #print(len(Listeennemis),len(ListeTirsBooba))
    if Listeennemis!=[]:
        for booba in Listeennemis:              
            booba.boobay +=2
            boobadx=random.randint(-10,10)
            booba.boobax += boobadx
            if vaisseau.x<=booba.boobax+50 and vaisseau.x+15>booba.boobax-50:
                if vaisseau.y+15>booba.boobay-50 and vaisseau.y<booba.boobay+50:
                    print("BOOBA A TOUCHE KAARIS")
                    Canevas.delete(booba.apparence)
                    del Listeennemis[0]
                    del booba
                    restartbooba()
                    mouvementAlien()
                    vies-=1
                    affichageautre(vies,Score)
            
            if booba.boobax+50>=1200:
                booba.boobadx=1200

            if booba.boobax-50<=0:
                booba.boobadx=0

            if booba.boobay>650:
                Canevas.delete(booba.apparence)
                del Listeennemis[0]
                del booba
                restartbooba()
                mouvementAlien()
        for Prot in Listeprotections:
            if booba.boobax<=Prot.x+50 and booba.boobax+50>Prot.x-50:
                if booba.boobay+50>Prot.y-20 and booba.boobay<Prot.y+20:
                    Canevas.delete(Prot.apparence)
                    gagagou=Listeprotections.index(Prot)
                    del Listeprotections[gagagou]
                    Canevas.delete(booba.apparence)
                    del Listeennemis[0]
                    del booba
                    restartbooba()
                    mouvementAlien()

        booba.affichage()


        Mafenetre.after(50,mouvementAlien)
    else:
        return

    #         booba.affichage()
    # print(Listeennemis)
    # Mafenetre.after(50,MouvementAlien)



def restartbooba():
    posax=random.randint(50,1230)
    booba=Alien(posax,niveau)   
    Listeennemis.append(booba)
    print("Y'a UN ERSTART")



def tirbooba():
    for booba in Listeennemis:
        tiralien=TirBooba(booba)   
        ListeTirsBooba.append(tiralien)

    Mafenetre.after(vitessetir,tirbooba)


#detection clavier


def left(event):
    vaisseau.deplacement(-1)

def right(event):
    vaisseau.deplacement(1)

def Tir(event):
    print("creerle tir")
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('TIRsound.wav'))
    nouveautir=TirSpaceship()
    ListeTirs.append(nouveautir)


def affichageautre(vies,score):

    label2.config(text='SCORE:    '+str(score))
    boutton.config(text=' QUITTER ')
    if vies==3:
        pass
    elif vies==2:
        boutton3.destroy()
    elif vies==1:
        boutton2.destroy()
    else:
        exit()

#Création d'une fenêtre
Mafenetre=Tk()
Mafenetre.geometry("1280x720")
Framebase=Frame(Mafenetre, relief ='groove', bg='green',width=1280,height=720)
Framebase.pack(fill=BOTH, expand=True)



#importation liste des images
ImageVaisseau=PhotoImage(file='kaarisvaisseau.png')
ImageBackground=PhotoImage(file='backgroundstars.png')
ImageAlien=PhotoImage(file=ListeAlien[niveau-1])
ImageTir=PhotoImage(file='cd.png')
ImageCoeur=PhotoImage(file='heart.png')


#formation des canvas
Canevas= Canvas(Framebase,width=1280,height=720)
Canevas.create_image(600,300,image=ImageBackground)
Canevas.pack(fill=BOTH, expand=True)





label2 = Label(Canevas, text="SCORE:   0", fg="red")
label2.place(x=100)



boutton1 = Button(Canevas, image=ImageCoeur)
boutton1.place(x=400)

boutton2 = Button(Canevas, image=ImageCoeur)
boutton2.place(x=450)

boutton3 = Button(Canevas, image=ImageCoeur)
boutton3.place(x=500)


boutton = Button(Canevas, text =" QUITTER ", command = exit)
boutton.place(x=1100)

#attribution des touches
Mafenetre.bind("<Left>",left)
Mafenetre.bind("<Right>",right)
Mafenetre.bind("<space>",Tir)






#création des objets
vaisseau=Spaceship()
booba=Alien(posax,niveau)
Listeennemis.append(booba)



a=1280-nbprot*50
b=a/nbprot
lavariablex=b/2


for i in range (nbprot):

    Lignedefront=protection(lavariablex)
    Listeprotections.append(Lignedefront)
    lavariablex+=b+50





mouvementAlien()
tirbooba()
# t1=threading.Thread(target=lambda : booba.mouvementAlien())
# t1.start()

#lancement de la musique
pygame.mixer.init(frequency=44100, size=-16, channels=3, buffer=1012)
pygame.mixer.music.load("TCHOUINE.wav")
pygame.mixer.music.play(loops=-1, start=0.0)

Mafenetre.mainloop()