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
#import pygame
#valeur position initiale vaisseau/alien
posvx=550
posvy=650
posax=random.randint(50,1230)
posay=100
ListeTirs=[]
ListeTirsBooba=[]
Listeennemis=[]
Score=0
print("ca fonctionne")
#création des objets et méthodes

class Spaceship:
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
        elif dir==-1:
            if self.x>0:
                self.x+=-10
                posvx=self.x
        else:
            pass
        self.affichage()




class Alien:
    posay=100
    def __init__(self,posax):
        self.boobay=Alien.posay
        self.boobax=posax
        self.envie=True
        self.boobady=5
        self.boobadx=random.randint(-10,10)
        self.apparence = Canevas.create_image(self.boobax,self.boobay,image=ImageAlien)
        # self.truc=Canevas.create_line(self.boobax-50, self.boobay-50, self.boobax+50 ,self.boobay+50 , fill='white')
    def affichage(self):
        Canevas.coords(self.apparence,self.boobax,self.boobay)
        # Canevas.coords(self.truc,self.boobax-50, self.boobay-50, self.boobax+50 ,self.boobay+50 )


class TirSpaceship:
    compteur=0
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
        global ListeTirs,Score,Listeennemis
        if self.tiry<0:
            print("finito")
            self.tirage==0
            Canevas.delete(self.apparence)
            print(ListeTirs)
            del ListeTirs[0]
            TirSpaceship.compteur-=1
        for booba in Listeennemis:

            if self.tirx<=booba.boobax+50 and self.tirx+15>booba.boobax-50:
                if self.tiry+15>booba.boobay-50 and self.tiry<booba.boobay+50:
                    # Canevas.delete(booba.apparence)
                    # # booba.apparence = Canevas.create_image(booba.boobax,booba.boobay,image=ImageAlienmort)

                    # # boobamort(booba)
                    # print("touché")
                    # Canevas.after(1000)
                    # print("careprend")
                    booba.boobay=850
                    self.tiry=-10
                    Score+=10
                    print(Score)
                    if Score >=100:
                        print("next level")
                        exit()




class TirBooba:
    compteur=0
    def __init__(self,booba):
        self.tirx=booba.boobax
        self.tiry=booba.boobay
        # self.apparence=Canevas.create_line(self.x+15 , self.y-50 , self.x+15 ,self.y , fill='white')
        self.apparence=Canevas.create_image(self.tirx+15, self.tiry, image=ImageTir)
        self.tirage=1
        print("letirvadescendre")
        self.tirdescent()

    
    def affichage(self):
        Canevas.coords(self.apparence , self.tirx+15 , self.tiry)


    def tirdescent(self):
        if self.tirage==1:
            self.tiry+=10
            self.affichage()
            self.fintirbooba()
            Mafenetre.after(50,self.tirdescent)

    def fintirbooba(self):
        global ListeTirsBooba,Score,Listeennemis
        if ListeTirsBooba!=[]:
            if self.tiry>650:
                self.tirage==0
                Canevas.delete(self.apparence)
                del ListeTirsBooba[0]
                self.tiry=100
                TirBooba.compteur-=1
                print(TirBooba.compteur)
                Mafenetre.after(1000,tirbooba)
            

        for booba in Listeennemis:

            if self.tirx<=vaisseau.x+5 and self.tirx+15>vaisseau.x-5:
                if self.tiry+15>vaisseau.y -5 and self.tiry<vaisseau.y+5:
                     exit()
        


# création des fonctions à appliquer sur chaque objet
def mouvementAlien():
    global Score
    if Listeennemis!=[]:
        for booba in Listeennemis:
                
            booba.boobay +=booba.boobady
            boobadx=random.randint(-10,10)
            booba.boobax += boobadx
            if vaisseau.x<=booba.boobax+50 and vaisseau.x+15>booba.boobax-50:
                if vaisseau.y+15>booba.boobay-50 and vaisseau.y<booba.boobay+50:
                    exit()
            if booba.boobax+50>=1300:
                booba.boobadx=-booba.boobadx
            if booba.boobax-50<=0:
                booba.boobadx=-booba.boobadx
            if booba.boobay>650:
                Score+=5
                Canevas.delete(booba.apparence)
                del Listeennemis[0]
                del booba
                mouvementAlien()
                restartbooba()
        booba.affichage()
        Mafenetre.after(50,mouvementAlien)
    else:
        return

    #         booba.affichage()
    # print(Listeennemis)
    # Mafenetre.after(50,MouvementAlien)



def restartbooba():

    posax=random.randint(50,1230)
    booba=Alien(posax)   
    Listeennemis.append(booba)

    mouvementAlien()

def tirbooba():
    for booba in Listeennemis:

        tiralien=TirBooba(booba)   
        ListeTirsBooba.append(tiralien)


#detection clavier


def left(event):
    vaisseau.deplacement(-1)

def right(event):
    vaisseau.deplacement(1)

def Tir(event):
    print("creerle tir")
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('TIRsound.wav'))
    nouveautir=TirSpaceship()
    ListeTirs.append(nouveautir)





#Création d'une fenêtre
Mafenetre=Tk()
Mafenetre.geometry("1280x720")
Framebase=Frame(Mafenetre, relief ='groove', bg='green',width=1500,height=1000)
Framebase.pack(fill=BOTH, expand=True)



#importation liste des images
ImageVaisseau=PhotoImage(file='kaarisvaisseau.png')
ImageBackground=PhotoImage(file='backgroundopera.png')
ImageAlien=PhotoImage(file='booba.png')
ImageAlienmort=PhotoImage(file="boobachoc.png")
ImageTir=PhotoImage(file='cd.png')


#formation des canvas
Canevas= Canvas(Framebase,width=1500,height=1000)
Canevas.create_image(600,300,image=ImageBackground)
Canevas.pack(fill=BOTH, expand=True)

#attribution des touches
Mafenetre.bind("<Left>",left)
Mafenetre.bind("<Right>",right)
Mafenetre.bind("<space>",Tir)






#création des objets
vaisseau=Spaceship()
booba=Alien(posax)
Listeennemis.append(booba)
mouvementAlien()
tirbooba()
# t1=threading.Thread(target=lambda : booba.mouvementAlien())
# t1.start()

#lancement de la musique
#pygame.mixer.init(frequency=44100, size=-16, channels=3, buffer=1012)
#pygame.mixer.music.load("TCHOUINE.wav")
#pygame.mixer.music.play(loops=-1, start=0.0)

Mafenetre.mainloop()