from GUI_ath import*
import GlobalFile
u = 'User'

def command():
    Talk('Right now i can allow you to use these functions',1)
    time.sleep(2)
    Talk('The familiarName() function',1)
    time.sleep(2)
    Talk('The athImport() function')

def familiarName(x=1):
    GlobalFile.User = str(input('what would you like me to call you?\n>>> '))
    if x == 1:
        Talk('Ok, ' + GlobalFile.User + ', what would you like me to do now?')
    
def athImport():
    print("ok, for me to import something i need the module's name, and it needs to contain the compatible ATH tah for me to be able to utilize it.")
    time.sleep(3)
    print('think of it as giving me notes to study so i can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = input('what do you want me to import, ' + GlobalFile.User + ' , ?')
    time.sleep(1)
    if str(mod[-4:]) != '_ath':
        print('hey ' + GlobalFile.User + ' I cant read this, im gonna need you to find me a Program with the tag _ath')
    else:
        print('Ok, let me get this done. it may take a moment for me to finish it')
        exec("import "+mod,globals())
        exec("global "+mod,globals())
        time.sleep(2)
        print("there we go, i've imported what you asked for ," + GlobalFile.User + '.')

Talk('Welcome to the Athena Network.',1)
familiarName(0)
time.sleep(1)
Talk('Hello ' + GlobalFile.User + ' you can use the command() function to bring up a list of functions that are compatable with the network')
