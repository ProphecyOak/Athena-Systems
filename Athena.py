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
    Talk("Ok, for me to import something i need the module's name, and it needs to contain the compatible ATH tah for me to be able to utilize it.",1)
    time.sleep(3)
    Talk('Think of it as giving me notes to study so i can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = input('What do you want me to import, ' + u + ' , ?\n>>> ')

    
Talk('Welcome to the Athena Network.',1)
familiarName(0)
time.sleep(1)
Talk('Hello ' + u + ' you can use the command() function to bring up a list of functions that are compatable with the network')
