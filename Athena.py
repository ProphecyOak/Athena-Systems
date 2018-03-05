#from time import *
import time
print('Welcome to the Athena Network.')
u = 'User'
time.sleep(1)
print('Hello ' + u + ' you can use the command() function to bring up a list of functions that are compatable with the network')
def command():
    print('Right now I can allow you to use these functions')
    time.sleep(1)
    print('The familiarName() function')
    time.sleep(1)
    print('The athImport() function')

def familiarName():
    u = str(input('What would you like me to call you? '))
    print('Ok, ' + u + ', what would you like me to do now?')
    
def athImport():
    print("Ok, for me to import something I need the module's name, and it needs to contain the compatible ATH tag for me to be able to utilize it.")
    time.sleep(3)
    print('Think of it as giving me notes to study so I can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = input('What do you want me to import, ' + u + ' , ?')
    
