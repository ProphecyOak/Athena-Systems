import time
import GlobalFile
from tkinter import*
root = Tk()
def Talk(speech,x=0):
    GlobalFile.curLabels.append(Label(root,text=speech))
    print(len(GlobalFile.curLabels))
    if GlobalFile.curRow < 10:
        GlobalFile.curLabels[-1].grid(row=GlobalFile.curRow,column=0,sticky="w")
    else:
        GlobalFile.curLabels[0].grid_forget()
        GlobalFile.curLabels = GlobalFile.curLabels[1:]
        for y in range(10):
            GlobalFile.curLabels[y].grid_forget()
            GlobalFile.curLabels[y].grid(row=y,column=0,sticky="w")
        GlobalFile.curLabels[-1].grid(row=11,column=0,sticky="w")
    GlobalFile.curRow += 1
    print(len(GlobalFile.curLabels))
    if x == 0:
        Talk("",1)
    print(len(GlobalFile.curLabels))
    root.update()
def Listen():
    pass
    
