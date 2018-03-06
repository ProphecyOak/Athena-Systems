import time


u = 'User'


def command():
    print('Right now i can allow you to use these functions')
    time.sleep(1)
    print('The familiarName() function')
    time.sleep(1)
    print('The athImport() function')

def familiarName(x=1):
    global u
    u = str(input('what would you like me to call you?\n>>> '))
    if x == 1:
        print('Ok, ' + u + ', what would you like me to do now?')
    
def athImport():
    print("Ok, for me to import something i need the module's name, and it needs to contain the compatible ATH tah for me to be able to utilize it.")
    time.sleep(3)
    print('Think of it as giving me notes to study so i can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = input('What do you want me to import, ' + u + ' , ?\n>>> ')

    
print('Welcome to the Athena Network.')
familiarName(0)
time.sleep(1)
print('Hello ' + u + ' you can use the command() function to bring up a list of functions that are compatable with the network')
    
