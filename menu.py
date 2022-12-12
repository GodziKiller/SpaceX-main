import pygame
from pygame.locals import *
from tkinter import *
from tkinter import ttk
import time




def change(keskispasse):
    playimage= PhotoImage(file="play2.png")
    playbutton.config(image=playimage)
    playbutton.image= playimage

def change2(keskispasse):
    playimage= PhotoImage(file="play.png")
    playbutton.config(image=playimage)
    playbutton.image= playimage

def change3(keskispasse):
    quitimage= PhotoImage(file="quit2.png")
    quitbutton.config(image=quitimage)
    quitbutton.image= quitimage

def change4(keskispasse):
    quitimage= PhotoImage(file="quit.png")
    quitbutton.config(image=quitimage)
    quitbutton.image= quitimage

def startgame():
    quitbutton.destroy()
    playbutton.destroy()
    label.pack_forget()
    progressbar= ttk.Progressbar(window, orient= HORIZONTAL, length=600, mode= "determinate")
    progressbar.pack(pady=300)
    randomtrucquisertarien=100
    i=0
    for i in range(1,100,1):
        progressbar["value"] = i
        window.update_idletasks()
        time.sleep(0.05)
    progressbar["value"] = 100
    window.destroy()
    pygame.mixer.music.stop()
    exec(open("game.py").read())


window= Tk()
window.title("                                                                                                                                                                 MAIN MENU")

window.geometry("1080x720")
window.minsize(1080,720)
window.iconbitmap("logo.ico")





backmenu = PhotoImage(file="backmenu.png").zoom(2)


a=0
xbg=0
ybg=0
label1 = Label( window, image = backmenu)
label1.place(x = xbg, y = 0)




hero=PhotoImage(file="hero.png").zoom(5).subsample(60)
label= Label(window,image=hero,background= "#85D2FE")
label.pack(fill="none", expand=True)



quitimage= PhotoImage(file="quit.png")
quitbutton =Button(window,image =quitimage, bg="#323D39",command=quit)
quitbutton.pack(fill="none", expand=True,side = BOTTOM)
quitbutton.bind("<Enter>",change3)
quitbutton.bind("<Leave>", change4)

play= PhotoImage(file="play.png")
playbutton= Button(window,image = play, bg="#323D39",command=startgame)
playbutton.pack(fill="none", expand=True)
playbutton.bind("<Enter>",change)
playbutton.bind("<Leave>", change2)


pygame.mixer.init(frequency=44100, size=-16, channels=3, buffer=1012)
pygame.mixer.music.load("menufinal.wav")
pygame.mixer.music.play(loops=-1, start=0.0)











window.mainloop()