import GlobalFile
NewCommands = {"conversation_ath":['interests()']}
n = NewCommands
topics = {"Football":"Ball game where two teams try to carry the Football to the other team's endzone withot being tackled"}
def commandConvo(x=1):
    print('from the Conversation notes, i can let you use these commands')
    for x in ConvoCommands:
        print('the ' + x + ' function')
    if x == 1:
        print('Did you want to talk about something?')

def interests():
    #its asks athena 'what are your interests?'
    global topics
    print('honestly i havnt gotten the chance to do much, how about you ' + GlobalFile.User)
    interest = str(input('what interests you? '))
    topic = interest.find('ball')
    if topic != -1:
        answer = str(input('is that a sport? '))
        if answer == 'No':
            description = str(input('Oh cool, could you tell me about it? id like to take a note of this'))
            name = str(input('also what was the name again? '))
            topics[name] = description
        elif answer == 'yes':
            name = str(input('what was the name again? '))
            if name in topics:
                print('is it that one ' + name)
                
