import time
from tkinter import *
from playsound import playsound

root = Tk()
root.title("Bridge Clock v. 1.01  © 2024 Tibor Menyhért")
root.geometry('%dx%d+%d+%d' % (620, 300, 800, 500))
ovladanie=Tk()
ovladanie.title("Ovládanie")
ovladanie.geometry('%dx%d+%d+%d' % (250, 100, 500, 500))

var = StringVar()
pismo='Times 200'
 #label = Label( root, textvariable=var, relief=RAISED , font=('Times', 200))
label = Label( root, textvariable=var, relief=RAISED , font=pismo)
pociatok=time.time()
print(pociatok)
doba=int(input('Koľko minút na kolo: '))
doba=doba*60

def casovac():
    global pociatok
    label.grid(row=0,column=1,columnspan=3)
    uplynulo=doba-(time.time()-pociatok)
    if uplynulo<0 :
        #pociatok=time.time()
        label.config(bg='red')
        uplynulo=-uplynulo
    if int(uplynulo)%60<10:
        prefix='0'
    else:
        prefix=''
    var.set(str(int(uplynulo/60))+':'+prefix+str(int(uplynulo)%60))
   
    #if uplynulo<121 and int(uplynulo)%30==0:
    #    playsound('alarm.mp3')
    root.after(1000, casovac)
        

def reset():
   global pociatok
   pociatok=time.time()
   label.config(bg='white')

def pridaj():
    global pociatok
    pociatok=pociatok+60

pridajB=Button(ovladanie, text ="+", command = pridaj,font=('Times', 30))

def uber():
    global pociatok
    pociatok=pociatok-60

uberB=Button(ovladanie, text ="-", command = uber, font=('Times', 30))

resetB = Button(ovladanie, text ="Reset", command = reset, font=('Times', 30))
resetB.grid(row=1, column=1)
pridajB.grid(row=1, column=2)
uberB.grid(row=1,column=3)
casovac()
root.mainloop()

resetB.pack()
pridajB.pack()
uberB.pack()
