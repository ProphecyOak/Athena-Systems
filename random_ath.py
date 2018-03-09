from GUI_ath import*
import GlobalFile
import random

commandDict = GlobalFile.Commands
commandDict["Random"] = ["randNums()"]
GlobalFile.Commands = commandDict

def randNums(n):
    for x in range(n-1):
        Talk(random.random(),1)
    Talk(random.random())
