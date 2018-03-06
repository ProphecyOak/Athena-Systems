from GUI_ath import*
class Conversation_ath:
    commands = ["interest()"]
    user = "User"
    topics = {"baseball":"Sport"}
    def printCommands():
        Talk("Commands in the Conversation Module:",1)
        for x in range(len(Conversation_ath.commands)-1):
            Talk('the ' + x + ' function',-1)
        Talk('the ' + Conversation_ath.commands[-1] + ' function')
    def interests():
        print('honestly i havnt gotten the chance to do much, how about you ' + Conversation_ath.user)
        interest = str(input('what interests you? '))
        topic = interest.lower().find('ball')
        if topic != -1:
            answer = str(input('is that a sport? '))
            if answer.lower() == 'No':
                description = str(input('Oh cool, could you tell me about it? id like to take a note of this'))
                name = str(input('also what was the name again? '))
                Conversation_ath.topics[name] = description
            elif answer.lower() == 'yes':
                name = str(input('what was the name again? '))
                if name.lower() in Conversation_ath.topics.keys():
                    print('is it this? ' + name)
