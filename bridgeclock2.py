import time
from tkinter import *

root = Tk()
root.title("Bridge Clock v. 1.02  CC BY 2024 Tibor Menyhért")
root.geometry('%dx%d+%d+%d' % (600, 300, 10, 10))
ovladanie=Tk()
ovladanie.title("Setup")
ovladanie.geometry('%dx%d+%d+%d' % (360, 80, 620, 10))
var = StringVar()
vare = StringVar()
velkostP=200
label = Label( root, textvariable=var, relief=RAISED , font='Times 200')
le=Label( ovladanie, textvariable=vare,relief=RAISED, font='Times 25', text='Lap time:')
e=Entry(ovladanie, bd=1, width=3, font='Times 25')
e.insert(0,'15')

def setpismo(velkostP):
    pismo="Times "+str(velkostP)
    label.config(font=pismo)
        
def zvacsi():
    global velkostP
    velkostP=velkostP+20
    setpismo(velkostP)

def zmensi():
    global velkostP
    velkostP=velkostP-20
    setpismo(velkostP)

def casovac():
    global pociatok,doba
    uplynulo=doba-(time.time()-pociatok)
    if uplynulo<0 :
        label.config(bg='red')
        uplynulo=-uplynulo
    if int(uplynulo)%60<10:
        prefix='0'
    else:
        prefix=''
    var.set(str(int(uplynulo/60))+':'+prefix+str(int(uplynulo)%60))
    root.after(1000, casovac)
        
def reset():
   global pociatok
   pociatok=time.time()
   label.config(bg='white')

def pridaj():
    global pociatok
    pociatok=pociatok+60

pridajB=Button(ovladanie, text ="+", command = pridaj,font=('Times', 25))

def uber():
    global pociatok
    pociatok=pociatok-60

uberB=Button(ovladanie, text ="-", command = uber, font=('Times', 25))
resetB = Button(ovladanie, text ="Reset", command = reset, font=('Times', 25))
sizeD = Button(ovladanie, text ="15↓", command = zmensi, font=('Times', 15))
sizeU = Button(ovladanie, text ="15↑", command = zvacsi, font=('Times', 25))

def start():
    global doba,pociatok
    resetB.grid(row=1, column=1)
    pridajB.grid(row=1, column=2)
    uberB.grid(row=1,column=3)
    sizeD.grid(row=1,column=4)
    sizeU.grid(row=1,column=5)
    doba=int(e.get())*60
    label.grid(row=0,column=1,columnspan=3)
    le.destroy()
    e.destroy()
    start.destroy()
    pociatok=time.time()
    casovac()
    
start=Button(ovladanie, text ="min Start", command = start, font=('Times', 25))
le.grid(row=2,column=1)
e.grid(row=2,column=2)
start.grid(row=2,column=3)
root.mainloop()
