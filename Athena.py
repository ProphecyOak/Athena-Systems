import time

u = 'User'

commands = ['familiarName()', 'athImport()']
def command():
    print('Right now i can allow you to use these functions')
    time.sleep(1)
    for x in commmands:
        print('the ' + x + ' function')
        time.sleep(1)
    
def familiarName(x=1):
    global u
    u = str(input('what would you like me to call you? '))
    print('ok, ' + u + ', what would you like me to do now?')
    if x == 1:
        print('Ok, ' + u + ', what would you like me to do now?')
    
def athImport():
    print("ok, for me to import something i need the module's name, and it needs to contain the compatible ATH tah for me to be able to utilize it.")
    time.sleep(3)
    print('think of it as giving me notes to study so i can do more cool things for you ^-^')
    time.sleep(1)
    #print list of available ones
    mod = exec(input('what do you want me to import, ' + u + ' , ?'))
    time.sleep(1)
    if str(mod[-4:]) != '_ath':
        print('hey ' + u + ' I cant read this, im gonna need you to find me a Program with the tag _ath')
    else:
        print('Ok, let me get this done. it may take a moment for me to finish it')
        import mod
        time.sleep(2)
        print("there we go, i've imported what you asked for ," + u + '.')

print('Welcome to the Athena Network.')
time.sleep(1)
familiarName(0)
time.sleep(2)
print('Fyi ' + u + ' You can use the command() function to find other functions im able to use')
