import GlobalFile
GlobalFile.Commands["Conversation"] = ["interests()"]

topics = {'sport':{"Football":"Ball game where two teams try to carry the Football to the other team's endzone withot being tackled"}}


def interests():
    #its asks athena 'what are your interests?'
    print("Honestly I haven't gotten the chance to do much " + GlobalFile.User +".")
    interest = str(input('What interests you?\n>>> ')
    topic = interest.find('ball')
    if topic != -1:
        answer = str(input('Is that a sport?\n>>> '))
        if answer == 'No':
            description = str(input("Oh cool, could you tell me about it? I'd like to take a note of this.\n>>> "))
            description = description.lower()
            name = str(input('Also, what was the name again?\n>>> ')
            topic = str(input('What kind of topic would you put this under?\n>>> '))
            topic = topic.lower()
            verify = topic.find('sport')
            if verify not != -1:
                print('hey that is a sport, or at least thats what ive been told')
                    topic = 'sport'
            topics[topic[name]] = description
        elif answer == 'yes'
            name = str(input('What was the name again?\n>>> '))
            if name in topics[sport]:
                print('Is it ' + name+"?")
            elif name not in topics[sport]:
                description = str(input("Could you tell me more, I'm not quite familiar with that.\n>>> ")
                topics[name] = description
                                  
        
