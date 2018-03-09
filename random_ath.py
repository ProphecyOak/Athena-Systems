from GUI_ath import*
import GlobalFile
import random

GlobalFile.Commands["Random"] = ["randNums()"]

def randNums(n):
    for x in range(n-1):
        Talk(random.random(),1)
    Talk(random.random())
