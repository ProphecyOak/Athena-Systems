#from time import *
import time
print('Welcome to the Athena Network.')
u = 'User'
time.sleep(1)
print('Hello ' + u + ' you can use the command() function to bring up a list of functions that are compatable with the network')
def command():
    print('Right now i can allow you to use these functions')
    time.sleep(1)
    print('the familiarName() function')
    time.sleep(1)
    print('the athImport() function')

def familiarName():
    u = str(input('what would you like me to call you? '))
    print('ok, ' + u + ', what would you like me to do now?')
    
def athImport():
    print("ok, for me to import something i need the module's name, and it needs to contain the compatible ATH tah for me to be able to utilize it.")
    time.sleep(3)
    print('think of it as giving me notes to study so i can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = input('what do you want me to import, ' + u + ' , ?')
    
