from GUI_ath import*
import GlobalFile
GlobalFile.init()
def command():
    Talk('Right now I can allow you to use these functions:',1)
    Talk('The familiarName() function   -Changes user name',1)
    Talk('The athImport() function  -Imports additional Athena functionality')

def familiarName(x=1):
    GlobalFile.User = str(input('What would you like me to call you?\n>>> '))
    if x == 1:
        Talk('Ok, ' + GlobalFile.User + ', What would you like me to do now?')
    
def athImport():
    print("Ok, for me to import something I need the module's name, and it needs to contain the compatible '_ath' tag for me to utilize it.")
    print('Think of it as giving me notes to study so I can do more cool things for you. ^-^')
    mod = input('What do you want me to import, ' + GlobalFile.User + '?\n>>> ')
    if str(mod[-4:]) != '_ath':
        print('Sorry ' + GlobalFile.User + ", I cant read this, I'm gonna need you to find me a program with the tag '_ath'")
    else:
        print('Ok, let me get this done. it may take a moment for me to finish it')
        exec("import "+mod,globals())
        exec("global "+mod,globals())
        print("There we go, I've imported what you asked for, " + GlobalFile.User + '.')
def initiate():
    Talk('Welcome to the Athena Network.',1)
    familiarName(0)
    Talk('Hello ' + GlobalFile.User + ', you can use command() to bring up a list of functions that are compatable with the network')

initiate()
