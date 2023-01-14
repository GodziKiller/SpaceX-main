from tkinter import *
from tkinter import ttk
import time




def change2(keskispasse):
    restartimage= PhotoImage(file="restart.png")
    restartbutton.config(image=restartimage)
    restartbutton.image= restartimage

def change3(keskispasse):
    quitimage= PhotoImage(file="quit.png")
    quitbutton.config(image=quitimage)
    quitbutton.image= quitimage

def change4(keskispasse):
    quitimage= PhotoImage(file="quit.png")
    quitbutton.config(image=quitimage)
    quitbutton.image= quitimage

def startgame():
    quitbutton.destroy()
    restartbutton.destroy()
    randomtrucquisertarien=100
    i=0
    window.destroy()
    exec(open("game.py").read())


window= Tk()
window.title("RESTARTMENU")

window.geometry("1080x720")
window.minsize(1080,720)






backmenu = PhotoImage(file="backmenu.png").zoom(2)


a=0
xbg=0
ybg=0
label1 = Label( window, image = backmenu)
label1.place(x = xbg, y = 0)




title = PhotoImage(file="title.png")
label= Label(window,image=title)
label.pack(fill="none", expand=True)




quitimage= PhotoImage(file="quit.png")
quitbutton =Button(window,image =quitimage, disabledforeground="#FFFFFF")
quitbutton.pack(fill="none", expand=True,side = BOTTOM)
quitbutton.bind("<Enter>",change3)
quitbutton.bind("<Leave>", change4)

restart= PhotoImage(file="restart.png")
restartbutton= Button(window,image = restart, disabledforeground="#FFFFFF",command=startgame)
restartbutton.pack(fill="none", expand=True)
restartbutton.bind("<Leave>", change2)




window.mainloop()