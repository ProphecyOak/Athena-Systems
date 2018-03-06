

from GUI_ath import*

u = 'User'


def command():
    Talk('Right now i can allow you to use these functions',1)
    time.sleep(2)
    Talk('The familiarName() function',1)
    time.sleep(2)
    Talk('The athImport() function')

def familiarName(x=1):
    global u
    u = str(input('what would you like me to call you?\n>>> '))
    if x == 1:
        Talk('Ok, ' + u + ', what would you like me to do now?')
    
    
def athImport():
    print("ok, for me to import something i need the module's name, and it needs to contain the compatible ATH tah for me to be able to utilize it.")
    time.sleep(3)
    print('think of it as giving me notes to study so i can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = input('what do you want me to import, ' + u + ' , ?')
    time.sleep(1)
    if str(mod[-4:]) != '_ath':
        print('hey ' + u + ' I cant read this, im gonna need you to find me a Program with the tag _ath')
    else:
        print('Ok, let me get this done. it may take a moment for me to finish it')
        import exec(mod)
        time.sleep(2)
        print("there we go, i've imported what you asked for ," + u + '.')

    
Talk('Welcome to the Athena Network.',1)
familiarName(0)
time.sleep(1)
Talk('Hello ' + u + ' you can use the command() function to bring up a list of functions that are compatable with the network')
