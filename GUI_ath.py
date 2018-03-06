from tkinter import*
root = Tk()
curLabels = []
curRow = 0
def Talk(speech,x=0):
    global curLabels
    global curRow
    curLabels.append(Label(text=speech))
    if curRow < 10:
        curLabels[-1].grid(row=curRow,column=0,sticky="w")
    else:
        curLabels = curLabels[1:]
        for x in range(10):
            curLabels[x].grid_forget()
            curLabels[x].grid(row=x,column=0,sticky="w")
        curLabels[-1].grid(row=10,column=0,sticky="w")
    curRow += 1
    if x == 0:
        Talk(" ",1)
    root.update()
def Listen():
    pass
