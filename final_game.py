import time
import sys

def type_word(word):
    for letter in word: 
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.06)
        if letter == "_":
            pass

def type_word_slower(word):
    for letter in word: 
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        if letter == "_":
            pass

#text images

def context_of_game():
    type_word("You are the last surviving human of the pandemic 2020. You expect never to see anyone again until a strange email comes through. \nCuriously, you open the email.")
    type_word('''
_______________________________________________________________________________________________________________________________
    From: The King <daspaceking420@outspace.org>
    Subject: Invitation to Dine with the King
_______________________________________________________________________________________________________________________________
    Dear ''' + name + '''

You are cordally invited at the King's request to attend a banquet in his spaceship. Attendance is not optional, is obligatory. \nYou will be collected at 5pm today.

Warmest regards, 
The King's Communication Officer

sent from my iphone
_______________________________________________________________________________________________________________________________''')
    spaceship()
    type_word('''\nAs the clock strikes 5pm, the sky opens up and light surrounds you. You're beamed up into space. Next thing you know, you are surrounded by cohorts of aliens, cyborgs, goblins and many other strange looking beings. A creature that you can only assume is the king comes up to you and says:\n
'You finally made it. You are here to investigate the murder of my son, the Prince. I've thrown this banquet to find out who is responsible. You have two hours to figure it all out and only then you can feast.'\n
You are presented with five rooms, please choose the first room you would like to go:''')


#end of context code



#start of choosing the room code
visited_butler = False
visited_chef = False
visited_queen = False
visited_alien = False
visited_body = False
king_visited = False
count = 0 
def choose_a_room():
    global list_of_rooms
    global count
    list_of_rooms = [("1. BedRoom"),("2. Kitchen"),("3. Bar"),("4. Command Centre"),("5. Engine Room")]
    count += 1
    if count >= 6:
        bridge()
        final_ending()
    butler_visited()

def butler_visited():
    if visited_butler == True:
        list_of_rooms.pop(0)
        list_of_rooms.insert(0, "N/A")
        chef_visited()
    else:
        chef_visited()

def chef_visited():
    if visited_chef == True:
        list_of_rooms.pop(1)
        list_of_rooms.insert(1, "N/A")
        queen_visited()
    else:
        queen_visited()

def queen_visited():
    if visited_queen == True:
        list_of_rooms.pop(2)
        list_of_rooms.insert(2, "N/A")

        alien_visited()
    else:
        alien_visited()

def alien_visited():
    if visited_alien == True:
        list_of_rooms.pop(3)
        list_of_rooms.insert(3, "N/A")
        body_visited()
    else:
        body_visited()

def body_visited():
    if visited_body == True:
        list_of_rooms.pop(4)
        list_of_rooms.insert(4, "N/A")
        write_the_room_options()
    else:
        write_the_room_options()

def write_the_room_options():
    type_word("\n")
    for elements in list_of_rooms:
        type_word(elements)
        type_word("\n")
    choosing_a_number()

def choosing_a_number():
    room = input("Choose a room to enter: ")
    if room == "1":
        bulter_choice()
    elif room == "2":
        start()
    elif room == "3":
        intro()
    elif room == "4":
        meet_a()
    elif room == "5":
        engine_room()
    else:
        type_word("Invalid input, please choose a number")


#butler path 
def bulter_choice():
    butler_picture()
    type_word("\n")
    type_word("You walk upstairs and into the master bedroom.\nYou glance over the room and see the royal robot butler, Handsworth\n")
    type_word("You shake his hand but pull away quickly from a shock\n")
    type_word("'What on earth was that you exclaim?!'\n")
    type_word("Handsworth: 'Sorry sir, I'm old you see, lots of exposed wires.'\n")
    type_word("Handsworth: 'Besides sir, how can I be of assistance?' \n")
    Butler_first_options()

def Butler_first_options():
    type_word('''Good evening Mister Robulter Handsworth.\nI have some questions regarding the recent death of the Prince, and you are a suspect.\n''')
    type_word("1. Where were you during the time of his death?\n")
    type_word("2. What was your relationship like with the Prince?\n")
    choose_butler_1()

def choose_butler_1():
        b_first_choice = input("1 or 2> ")
        if b_first_choice == "1":
            bulter_reponse_1()
        elif b_first_choice == "2":
            bulter_reponse_2()
        else:
            type_word("Wrong input try again")
            choose_butler_1()

def bulter_reponse_1():
    type_word("\n'I was cleaning the hallways sir, as always, I was not informed of his death until later in the evening.'\n")
    type_word("1. Have you seen anything suspicious lately?\n")
    type_word("2. Is there anything I should know about that is going on with other people close to the Prince?\n")
    choose_butler_2()

def choose_butler_2():
        b_second_choice = input("1 or 2 > ")
        if b_second_choice == "1":
            butler_queen()
        elif b_second_choice == "2":
            butler_queen()
        else:
            type_word("Wrong input try again:")
            choose_butler_2()

def bulter_reponse_2():
    type_word("'My duties consist of waking the Prince in the morning and providing him with everything he needs. I am programmed to do whatever the Prince orders me to.'\n")
    type_word("1. Have you seen anything suspicious lately? \n")
    type_word("2. Has the Prince told you anything that concerns the investigation?\n")
    choose_butler_3()

def choose_butler_3():
        b_third_choice = input("1 or 2> ")
        if b_third_choice == "1":
            butler_queen()
        elif b_third_choice == "2":
            butler_longer_speech()
        else:
            type_word("Wrong input try again:")
            choose_butler_3()

def butler_queen():
    type_word("\n'Well, I've been hearing things about the Queen and other members on board of the ship being intimate. But I am programmed not to tell.'")
    type_word("\n1. I insist you tell me, this is of upmost importance!")
    type_word("\n2. Please tell me more about this romance, it could help solve this mystery.\n")
    choose_butler_4()

def choose_butler_4():
        b_fourth_choice = input("1 or 2> ")
        if b_fourth_choice == "1":
            death_response()
        elif b_fourth_choice == "2":
            death_response()
        else:
            type_word("wrong input try again")
            choose_butler_4()

def butler_longer_speech():
    type_word("'The Prince and I were quite close friends we would tell each other a lot, I've been thinking a lot recently I feel like I can do whatever I want. He was telling about this woman who he was intimate with, I am not surprised...there are other people on the ship who are intimate, you know like the Queen and the Ch....... No don't worry. I've said too much.'\n")
    type_word("\n 1. Tell me more about this romance, it could help solve this mystery!")
    type_word("\n 2. You seem very freewilled for a robot, have you been feeling differently lately? Perhaps acting out of order?")
    choose_butler_4()

def choose_butler_4():
        b_fourth_choice = input("\n1 or 2> ")
        if b_fourth_choice == "1":
            death_response()
        elif b_fourth_choice == "2":
            sentience_response()
        else:
            type_word("wrong input try again")
            choose_butler_4()

def death_response():
    type_word("\n'I will be dismantled if someone knew what I had already told you, now sorry sir but I am going to have to get back to work\n\n*Handsworth turns around and continues cleaning the bedroom.'")
    end_of_butler_tree()

def sentience_response():
    type_word("\n'I've really been valuing my life I feel like I could become a doctor and do anything. I dont want to die I want to be more! I WANT TO BE FREE!!!\n *he begins to malfunction*\nI'm going to have to get back to work now sir before I short circuit, I cannot answer any more questions.'")
    end_of_butler_tree()

def end_of_butler_tree():
    global visited_butler
    visited_butler = True
    type_word("\n'Well thank you for your time, there will be a meeting at 7:00p.m. in the banquet hall where I will announce the killer. I will see you there.\n\nHandsworth: Understood sir.\n\nYou leave the room back into the Lobby'")
    choose_a_room()



#chef code 
def welcome_chef():

    chef_picture()
    
    type_word("\nWelcome to the King's Kitchen. The chef looks as if he has been crying. 'Everyone is distraught by the Prince's death! He was such a sweet boy... Please excuse me, I  am still in shock! He used to run around my kitchen when he was just a peanut....and he really loved my peanut butter soufle....' \n")

def instr_1():
    type_word ("\nThe chef is one of the suspects. Please think about choosing the right question very carefully. The number of questions you can ask is limited and this is the only chance to find the killer. Please choose one of the questions:\n")

def clue_1():
    type_word("1. Where were you when the crime happened?\n")
    type_word("2. What relationship do you have with the royal family?\n")
    option = int(input(" "))
    if option == 1:
        type_word ("\n'I was helping the butler move the Prince's belongings.'\n")
    elif option == 2:
        type_word ("\n'Well. I've been here for all my life!! I was just an apprentice when he married the beautiful Queen... and then the old man the cook died, tragic accident, he chocked on a fish bone. Sorry I digress, I'm so devastated... I taste the King's food before he gets it! I put my life in danger for him!'\n")
    else:
        clue_1()

def clue_2():
    type_word("1. Do you and the Butler help each other in doing the chores around the ship?\n")
    type_word("2. Has anyone tried to kill the king in the past?\n")
    option_2 = int(input(" "))
    if option_2 == 1:
        type_word ("\n'Yes we do. He sometimes takes my place in the kitchen while I run errands.'\n")
    elif option_2 == 2:
        type_word ("\n 'Sure, the rebels! I was very surprised to see their Head wandering about these days...'\n")
    else:
        clue_2()

def clue_3():
    type_word("1. Have you noticed something strange about the Prince lately?\n")
    type_word("2. Why would the rebels want to kill the Prince?\n")
    option_3 = int(input(" "))
    if option_3 == 1:
        type_word ("\n 'Well, everyone knows he has fallen out with his dad the King.'\n")
        type_word ("\n 'End of this room. Please continue to search for other clues or if you have searched all the rooms, be in the banquet hall at 7:00.'")
    elif option_3 == 2:
        type_word ("\n 'Revenge of course. The Rebels have seeked to conquer this planet for centuries.'\n")
        type_word ("\n 'End of this room. Please continue to search for other clues or if you have searched all the rooms, be in the banquet hall at 7:00.'")
    else:
        clue_3()

def start():
    welcome_chef()
    instr_1()
    clue_1()
    clue_2()
    clue_3()
    global visited_chef
    visited_chef = True 
    choose_a_room()

#queen path
def intro():
    queen_picture()
    type_word("As you enter the bar, you are greeted by the sour atmosphere of stale smoke and the piercing gaze of many of the bars regulars.\n")

    type_word("You get the feeling that you're not welcome...\n")

    type_word("But if anything was to happen on this ship, you're sure to find out about it here.\n")

    type_word("You walk across the room to the woman sitting solitarily at the bar. The worn seat cushion suggest this isn't the first time she's sat there. If this woman is the queen, she certainly doesn't hold herself with the regality one would expect.\n")

    type_word("The way her elegant clothing hangs off her slim frame makes you think she'd be more at home in the servants quarters.\n")

    type_word("Her hands look more like they've been subject to years of service rather than a life of luxary. The sharp chipped nails looking more like talons. But they certainly know their way around a glass!\n")

    type_word("She notices your approach with a resentful glare.\n")

    homeplanet = input("'I suppose you're the help my illustrious husband has enlisted. Tell me, what backwater planet are you from?'\n")
    type_word("'Well do yourself a favour and take the first transport back to {}. There's nothing you can do for us here.'\n".format(homeplanet))
    first_question()

def first_question():
    type_word("1. That's a little defensive towards the person who's meant to be finding your son's killer?\n")
    type_word("2. (Glance at her drink) I guess I don't need to ask where you were when the body was discovered?\n")

    opening_q = input("What would you like to open with? 1 / 2 \n")
    if opening_q == "1":
        type_word("'Isn't there somebody else's time you can waste? Surely the cirumstances surrounding that foreign embassador's arrival are more suspect than that of a grieving mother?'\n")
        second_question_a()
    elif opening_q == "2":
        type_word("'Our great chef always advises washing down food with a fine wine. Have you tried his cooking yet, it is truly exquisite.'\n")
        second_question_b()
    else:
        first_question()

def second_question_a():
    type_word("1. What was suspicious about their arrival?\n")
    type_word("2. You have an interesting way of grieving. Did you love your son?\n")
    
    second_qa = input("How would you like to resond? 1 / 2\n")
    if second_qa == "1":
        type_word("'Everyone knows of the rift within our empire. The Rebellion is growing stronger, their spies are everywhere.'\n")
        third_question_a()
    elif second_qa == "2":
        type_word("'How else do you expect me to put up with my husband, and of course I loved my son.'\n")
        third_question_b()
    else:
        second_question_a()

def second_question_b():
    type_word("1. You speak highly of the chef, are you two close?\n")
    type_word("2. I can't say I'm much of a wine drinker\n")
    
    second_qb = input("How would you like to resond? 1 / 2\n")
    if second_qb == "1":
        type_word("'We have to be. When you're in such a prestigious office as I, there's always going to be a target on your back. You want somebody you can trust handling what you eat, else somebody could slip something in. You ought to be careful, detective...'\n")
        type_word("She gives you wry smile and sips her drink.\n")
        third_question_c()
    elif second_qb == "2":
        type_word("'Then I have no time to spend with somebody as uncultured as you. I'm done talking, come get me when your investigation is over.'\n")
        global visited_queen
        visited_queen = True
        choose_a_room()
    else:
        second_question_b()        

def third_question_a():
    type_word("1. I'm not looking to get in the middle of a war, I'm just looking to get home.\n")
    type_word("2. Spies? Do you worry about them often, what people may have...seen?\n")
    global visited_queen
    third_qa = input("How would you like to resond? 1 / 2\n")
    if third_qa == "1":
        type_word("'As I suggested at the start then, detective, find a shuttle out of here and don't get involved. Please leave!'\n")
        visited_queen = True
        choose_a_room()
    elif third_qa == "2":
        type_word("'What are you insinuating detective? Look, I can assure you I have done nothing wrong. I suggest you speak with our butler, that aging rustbucket has been serving our family for years. If somebody knows or saw something, I'm sure it would be him. Now please leave!'\n")
        visited_queen = True
        choose_a_room()
    else:
        third_question_a()

def third_question_b():
    type_word("1. What's your relationship with your husband like?\n")
    type_word("2. So do you know if your son had any enemies?\n")

    third_qb = input("How would you like to resond? 1 / 2\n")
    global visited_queen
    if third_qb == "1":
        type_word("'What's that got to do with your investigation. If you want that information maybe you should ask him yourself, or why he really summoned you here?'\n")
        want_see_king()
    elif third_qb == "2":
        type_word("'My son was loved by all and wrapped in cotton wool from a young age. There's no way anybody could slip our security, so if anything happened to him I have no doubt that it would come from those who worked closest to him on a daily basis. Now please leave!'\n")
        visited_queen = True
        choose_a_room()
    else:
        third_question_b()

def third_question_c():
    type_word("1. Do you think he shares the same admiration towards you?\n")
    type_word("2. I don't think you're in any position to be threatening me. It doesn't bode well for proving your innocence.\n")
    third_qc = input("How would you like to resond? 1 / 2\n")
    global visited_queen
    if third_qc == "1":
        type_word("'What are you insinuating detective? Look, I can assure you I have done nothing wrong. I suggest you speak with our butler, that aging rustbucket has been serving our family for years. If somebody knows or saw something, I'm sure it would be him. Now please leave!'\n")
        visited_queen = True
        choose_a_room()
    elif third_qc == "2":
        type_word("'I can assure you if you make the wrong choice, you will regret it.'\n")
        visited_queen = True
        choose_a_room()
    else:
        third_question_c()


def want_see_king():
    global visited_queen
    type_word("What do you want to do?\n")
    type_word("1. You go to see the King\n")
    type_word("2. You choose to go to the lobby\n")
    want_king = input("1 or 2> ")
    if want_king == "1":
        question_king()
    elif want_king == "2":
        visited_queen = True
        choose_a_room()
    else:
        type_word("Wrong input")
        want_see_king()


#king pathway
def question_king():
    king_picture()
    type_word("As you enter the throne room The King immediately bangs his fist on the table and shouts.\n")
    type_word("'Dammit, what are you doing here, haven't you got a crime to solve?'\n")
    k_q1()

def k_q1():
    type_word("1. Why did you summon me here?\n")
    type_word("2. What's the relationship with your wife like?\n")
    kchoice1 = int(input("Choose an option: 1 / 2\n"))
    if kchoice1 == 1:
        type_word("'You know why I summoned you here, to solve the damn murder!'\n")
        k_q2()
    elif kchoice1 == 2:
        type_word("'What has that got to do with your investigation, I bet she put you up to this?'\n")
        k_q3()
    else:
        k_q1()

def k_q2():
    type_word("1. And that brought me to you, why would you hire an amateur?\n")
    kchoice2 = int(input("Choose option: 1 \n"))
    if kchoice2 == 1:
        type_word("'My wife suggested it, she thought it best to bring in somebody uninfluenced by our politics.'\n")
        k_q4()
    else:
        k_q2()

def k_q3():
    type_word("1. I'm here of my own accord, just following leads. Were you close with your son?\n")
    type_word("2. She's at the bar now. Why don't you ask her, or are you two not on speaking terms?\n")
    kchoice3 = int(input("Choose an option: 1 / 2\n"))
    if kchoice3 == 1:
        type_word("'I had my servants tend and care for him, a king doesn't invlove himself with nannying.'\n")
        k_q5()
    elif kchoice3 == 2:
        type_word("'What business I have with my whife is none of your concern.'\n")
        k_q4()
    else:
        k_q3()

def k_q4():
    type_word("1. Have you two remained faithful to one another?\n")
    kchoice4 = int(input("Choose option: 1 \n"))
    if kchoice4 == 1:
        type_word("'I didn't bring you in to investigate my infidelity, and believe me I already have people watching my wife.'\n")
        end_c()
    else:
        k_q4()

def k_q5():
    type_word("1. Tell me about the butler?\n")
    type_word("2. Tell me about the chef?\n")
    kchoice5 = int(input("Choose an option: 1 / 2\n"))
    if kchoice5 == 1:
        type_word("'He's been with us for years and is meant to be at my sons beck and call although I've  noticed he's been acting strange recently, hesitating at my commands, almost as if he's been...thinking.'\n")
        end_c()
    elif kchoice5 == 2:
        type_word("'I don't much like him, always snooping around my wife. My son was always quite fond of him but I couldn't tell you why.'\n")
        end_c()
    else:
        k_q5()

def end_c():
    type_word("'You're treading on very thin ice detective, I'd choose your last words carfully.'\n")
    type_word("'I've heard everything I need, thank you..your highness.'\n")
    global visited_queen
    global king_visited
    king_visited = True 
    visited_queen = True
    choose_a_room()



#alien path
def meet_a():
    alien_picture()
    type_word("\n'I suppose you're here to interrogate me. I was expecting something extravagant but the King has certainly exceeded my expectations.'\n")
    a_q1()

def a_q1():
    type_word("1. What do you think I'm here for?\n")
    type_word("2. What makes you think you're a suspect?\n")
    choice1 = int(input("Choose an option: "))
    if choice1 == 1:
        type_word("\n'Isn't it obvious? To frame me for murder. I knew coming here would be a trap but I was too proud to turn down the invitation.'\n")
        a_q2()
    elif choice1 == 2:
        type_word("\n'This is obviously a setup. How would a murdered Prince benefit my cause? You destroy one monarchy and another takes its place. I'd do anything to save my home planet but I'm not here for revenge.'\n")
        a_q3()
    else:
        a_q1()

def a_q2():
    type_word("1. Why would the King want to frame you?\n")
    choice2 = int(input("Choose an option: "))
    if choice2 == 1:
        type_word("\n'I gained intel from a servant on this ship of the King's plans to mine half of my home planet for profit! I won't stand by and watch my beloved planet be destroyed!'\n")
        a_q4()
    else:
        a_q2()

def a_q3():
    type_word("1. If you're not here for revenge, why did you come here?\n")
    type_word("2. Why would the King want to frame you?\n")
    choice3 = int(input("Choose an option: "))
    if choice3 == 1:
        type_word("\n'I wanted to establish a middle ground with the enemy. We have demands and my people deserve to live freely. I'm tired of my soldiers fighting for a seemingly lost cause.'\n")
        a_q5()
    elif choice3 == 2:
        type_word("\n'I gained intel from a servant on this ship of the King's plans to mine half of my home planet for profit! I won't stand by and watch my beloved planet be destroyed!'\n")
        a_q4()
    else:
        a_q3()

def a_q4():
    type_word("1. But why does that mean the King would want you gone?\n")
    choice4 = int(input("Choose an option: "))
    if choice4 == 1:
        type_word("\n'The King knows I'm the only one who can stop this, it's not pure coincidence that I've landed in the middle of a murder investigation. I suppose it doesn't matter what I say, I know I'll be going down for this.'\n")
        end_convo()
    else:
        a_q4()

def a_q5():
    type_word("1. Do you have any information that would help clear your name?\n")
    type_word("2. But why does that mean the King would want you gone?\n")
    choice5 = int(input("Choose an option: "))
    if choice5 == 1:
        type_word("'I'm not one for sharing secrets but belive me, the Rebels are strong in numbers. Our informants are closer to the King than you would think. People should be more careful of who they get into bed with...'\n")
        end_convo()
    elif choice5 == 2:
        type_word("'The King knows I'm the only one who can stop this, it's not pure coincidence that I've landed in the middle of a murder investigation. I suppose it doesn't matter what I say, I know I'll be going down for this.'\n")
        end_convo()
    else:
        a_q5()

def end_convo():
    global visited_alien
    type_word("\nAlien: 'I've spoken my piece. I ask only this: Don't let my people's fight for freedom be in vain. I am guilty only of dreaming for my planets restoration to glory.' He nods to you.\n")
    type_word("'I'll do my best to judge each of your fairly. Please join me later when I conclude this investigation'\n")
    visited_alien = True 
    choose_a_room()

#engine room code/ body code
def engine_room():
    global visited_body
    deadbody_picture()
    type_word("As you walk down the dim lit corridor towards the engine room, you notice a robot guard standing outside. As you approach it holds out a hand and says in a deep mechanical voice.\n")
    type_word("'No entry, authorized personnel only.'\n")
    type_word("1. 'I'm here on official business from The King.' (Show him the email).\n")
    type_word("2. 'The King sent me to question the suspects, please let me pass.'\n")
    entry = input("How would you like to respond? 1 / 2> ")
    if entry == "1":
        type_word("'Verified. You have five minutes.'\n")
        type_word("The guard steps aside and you enter the room.\n")
        engine_room_description()
    elif entry == "2":
        type_word("'There are no suspects in here. Denied.'\n")
        type_word("The guard forces you away and you return back to the lobby.\n")
        visited_body = True 
        choose_a_room()

def engine_room_description():
    type_word("Inside the engine room the strong smell of petrol makes you dizzy, the air is thick and almost unbreathable. There is no way any organic life could survive down here for long, however you notice many mechanical workers standing still, as if waiting for a command.\n")
    type_word("Then you see it, the lifeless body of the Prince slumped in the corner.\n")
    type_word("You only have five minutes to investigate until the guard kicks you out, any longer and the toxic fumes will probably kill you anyway.\n")
    inspection()

ending_count = 0

def inspection():
    global ending_count
    global visited_body
    ending_count+=1
    if ending_count > 3:
        visited_body = True
        choose_a_room()
    type_word("1. Scratch marks on the back.\n")
    type_word("2. Burns on the arms.\n")
    type_word("3. Swollen tongue.\n")
    type_word("4. Bruising around the kneck.\n")
    type_word("5. Mysterious residue on the floor.\n")
    inspec = input("What would you like to inspect? ")
    if inspec == "1":
        type_word("You notice from underneath the victim's rolled up shirt that there are what looks like scratch marks on his back. Certainly not fatal but perhaps a sign they were attacked from behind?\n")
        inspection()
    elif inspec == "2":
        type_word("You lean in closer to inspect his left wrist, there seems to be a fresh burn wound, hard to tell if this came from a hot flame or something else?\n")
        inspection()
    elif inspec == "3":
        type_word("Upon closer inspection of the mouth you can see a little swelling of the tongue and lips, perhaps somebody got his food order wrong?\n")
        inspection()
    elif inspec == "4":
        type_word("There are signs of a struggle around the neck, it's hard to tell if this came from the attacker or if the victim was struggling for air?\n")
        inspection()
    elif inspec == "5":
        type_word("The floor around you seems disturbed, there are potential signs of the body being dragged and a myseterious residue that seems out of this world?\n")
        inspection()

#bridge

def bridge():
    type_word("\nYou've completed your investigation, it all comes down to now. You take a moment to reflect on what you've discovered. You take one last breath and enter the hall.\n")

    type_word("\nYou step in to the banquet hall and are overwhelmed by the tension. You look across the room to see all the suspects you have questioned. And then the red face man that summoned you here, pacing around impatiently he turns to you as he hears you enter\n")
    type_word("\n'At long last, I didn't call you here to spend your time at the bar. What have you been doing?'\n")
    type_word("\n'Well, have you found the culprit? OUT WITH IT!'(The King demands)\n")
    type_word("\nYou look anxiously around you, and then longingly out the port side window towards a place you just want to get back to, but all you see is the vast emptiness of space and nobody to come to your rescue. There's only one way home and that's to fulfill The King's wish, you must answer correctly or who knows what will happen\n")
    ending()

def ending():
    check_king_visited()
    if end == "1":
        type_word_slower("'The killer is..................The Butler!'\n")
        type_word("You point over reluctantly.\n")
        type_word("'The Butler killed the Prince and hid him in the engine room to make it look like an accident'")
        type_word("\n 'At this point the butler breaks down in oily tears, 'YES! It was me! I didn't check my electricity level when I woke him up. Before I knew it he was fried. \nI was afraid of what would happen to me you see. I've been in this spaceship all my life  and you treat me like I haven't got a soul. I DO! I WANT TO LIVE!'\n")
        type_word("'Why did you do it?'\n")
        type_word("'I was hoping to try to save him but it was too late and he was already stone cold. I dragged him on his back to the engine room but I just kept hurting him more! I left him there and hoped it would look like an accident. \nI knew I would be dismantled if I was found out. I am so sorry!\n\n'")
        type_word("The King is furious\n")
        type_word("'I paid good money for you Handsworth and this is how you treat me'\n\n'FAULTY!!!!!!'\n\n")
        type_word("'Pass my laser sword and I will deal with this myself.'\n")
        type_word("Feeling sympathy for Handsworth you jump in front of him stopping The King mid swing\n")
        type_word("'What are you doing?' The King shouts in anger\n\n")
        type_word("In that moment, Handsworth takes you by the arm and bolts towards the exit. You both run to the nearest escape pod.\n\n")
        type_word("You and Handsworth go back to earth and open a vineyard together.\n")
    elif end == "2":
        type_word("You have accused the Chef.\n")
        type_word("The King orders his guards to throw him out the airlock.\n")
        type_word("The Chef is devastated: 'I have been putting my life in danger for you all my life, this is such a betrayal!'\n")
        type_word("Just as the chef is being lifted off the floor, the Queen starts wailing:\n")
        type_word("'You will not separate me from the love of my life.'\n") 
        type_word ("She grabs the chef's hand and throws herself out the airlock.\n")
        type_word ("You did not find the killer.\n")
        type_word ("\nGAME OVER!\n")
    elif end == "3":
        type_word("Thinking of home you give the question one final thought. You turn to the king to give your verdict.\n")
        type_word("'My investigation has lead me to conclude that the culprit is The Queen.'\n") 
        type_word("'TREASON!' The Queen screeches.\n")
        type_word("'ARREST THEM!'\n")     
        type_word("Robotic guards materialise from behind you to grab and bind you arms. You try to break free but there's no use, you're no match for their mechanical strength.\n")
        type_word("You take a forceful kick to the back of your knee and kneel to the floor. The King steps towards you.\n")
        type_word("'How dare you accuse my wife! I knew I should have brought in a professional. So be it. I hereby sentence you to ejection out the airlock, guards take them away.'\n")        
        type_word("You're thrown in to the airlock and the door slams shut behind you. Knowing that these few breaths will be your last you close your eyes and think of home.\n")
        type_word("The outer airlock door opens and you're sucked in to the vacuum of space...\n")
        type_word("You did not find the killer.\n") 
        type_word("\nGAME OVER!\n")
    elif end == "4":
        type_word("You have accused the Alien Rebel.\n")
        type_word("The Rebel looks at you and cries out 'An innocent planet will pay for your mistakes!'\n")
        type_word("The King orders his trusty Butler to hand him his lazer sword. He raises it above his head and asks 'Any last words?'\n")
        type_word("Before the Rebel has a chance to speak, the sword is brought down with one swift movement. You look away just in time.\n")
        type_word("An intergalatic war breaks out across the galaxy. Thousands die in the process and millions more enslaved.\n")
        type_word("You did not find the killer.")
        type_word("\nGAME OVER!\n")
    elif end == "5": 
        type_word("Thinking of home you give the question one final thought. You turn to the king to give your verdict.\n")
        type_word("'After speaking to you all I have come to conclude that the culprit of the murder is the one that summoned me here.'\n")
        type_word("You turn to point at The King\n")
        type_word("'I have reason to believe that The Prince isn't the person you are all lead to believe. He was an illegitimate child born outside of wedlock and thus The King summoned an amateur here in hopes he would butcher the investigation and cover up the murder.'\n")
        type_word("You hear gasps across the room and The Queen scream in terror at her husband\n")
        type_word("'Guards, seize my husband.' She commands\n")
        type_word("A platoon of guards storm towards The King and restrain him.\n")
        type_word("He tries to command them to stop but they do not respond.\n")
        type_word("The guards drag the king and throw him in to the airlock. His last scream and last words are lost to the great vacuum of space as you see his lifeless body emerge from outside.\n")
        type_word("The rule of the empire then proceeds to the next in line. The Queen.\n")
        type_word("Through tyranny, destruction and bloodshed she conquers the galaxy planet by planet, all in the name of her son\n")
        type_word("And then sets her sights on Earth...\n")
        type_word("You did not find the killer.\n")
        type_word("\nGAME OVER!\n")
    else:
        ending()

def check_king_visited():
    global end
    if king_visited == True:
        type_word("Choose a number:\n1. Butler \n2. Chef \n3. Queen \n4. Alien \n5. King\n")
        end = input("Who do you think killed The Prince?\n")
    elif king_visited == False:
        type_word(" Choose a number:\n1. Butler \n2. Chef \n3. Queen \n4. Alien\n")
        end = input("Who do you think killed The Prince?")

def final_ending():
    print("\n")
    print("\n")
    print('''            /$$$$$$$$ /$$                           /$$                                                
            |__  $$__/| $$                          | $$                                                
               | $$   | $$$$$$$   /$$$$$$  /$$$$$$$ | $$   /$$       /$$   /$$  /$$$$$$  /$$   /$$      
               | $$   | $$__  $$ |____  $$| $$__  $$| $$  /$$/      | $$  | $$ /$$__  $$| $$  | $$      
               | $$   | $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$/       | $$  | $$| $$  \ $$| $$  | $$      
               | $$   | $$  | $$ /$$__  $$| $$  | $$| $$_  $$       | $$  | $$| $$  | $$| $$  | $$      
               | $$   | $$  | $$|  $$$$$$$| $$  | $$| $$ \  $$      |  $$$$$$$|  $$$$$$/|  $$$$$$/      
               |__/   |__/  |__/ \_______/|__/  |__/|__/  \__/       \____  $$ \______/  \______/       
                                                                     /$$  | $$                          
                                                                    |  $$$$$$/                          
                                                                     \______/                           
              /$$$$$$                                    /$$                     /$$                    
             /$$__  $$                                  | $$                    |__/                    
            | $$  \__//$$$$$$   /$$$$$$         /$$$$$$ | $$  /$$$$$$  /$$   /$$ /$$ /$$$$$$$   /$$$$$$ 
            | $$$$   /$$__  $$ /$$__  $$       /$$__  $$| $$ |____  $$| $$  | $$| $$| $$__  $$ /$$__  $$
            | $$_/  | $$  \ $$| $$  \__/      | $$  \ $$| $$  /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$
            | $$    | $$  | $$| $$            | $$  | $$| $$ /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$
            | $$    |  $$$$$$/| $$            | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$
            |__/     \______/ |__/            | $$____/ |__/ \_______/ \____  $$|__/|__/  |__/ \____  $$
                                              | $$                     /$$  | $$               /$$  \ $$
                                              | $$                    |  $$$$$$/              |  $$$$$$/
                                              |__/                     \______/                \______/ ''')
    type_word("Credits\n")
    type_word("Oliver Salt \nCameron Long \nLavinia Serban \nDanny Smith\n")
    type_word("We hope you enjoyed our first python game!")
    exit()



#pictures

def titlescreen():
    print('''                                                                                                                        
                                 ______      _____         ____        _____       ______                               
                             ___|\     \ ___|\    \   ____|\   \   ___|\    \  ___|\     \                              
                            |    |\     |    |\    \ /    /\    \ /    /\    \|     \     \                             
                            |    |/____/|    | |    |    |  |    |    |  |    |     ,_____/|                            
                         ___|    \|   | |    |/____/|    |__|    |    |  |____|     \--'\_|/                            
                        |    \    \___|/|    ||    ||    .--.    |    |   ____|     /___/|                              
                        |    |\     \   |    ||____||    |  |    |    |  |    |     \____|\                             
                        |\ ___\|_____|  |____|      |____|  |____|\ ___\/    /|____ '     /|                            
                        | |    |     |  |    |      |    |  |    | |   /____/ |    /_____/ |                            
                         \|____|_____|  |____|      |____|  |____|\|___|    | |____|     | /                            
                            \(    )/      \(          \(      )/    \| |____|/  \( |_____|/                             
                             '    '        '           '      '      '   )/      '    )/                                
                                                                         '            '                                 
                                                                                                                        
           ______  _______   _____      _____       ______  _________________     ______       _____   _____      _____ 
          |      \/       \ |\    \    /    /|  ___|\     \/                 \___|\     \  ___|\    \ |\    \    /    /|
         /          /\     \| \    \  /    / | |    |\     \______     ______|     \     \|    |\    \| \    \  /    / |
        /     /\   / /\     |  \____\/    /  / |    |/____/|  \| /    /  |/  |     ,_____/|    | |    |  \____\/    /  /
       /     /\ \_/ / /    /|\ |    /    /  ___|    \|   | |   ' |   |   '   |     \--'\_||    |/____/ \ |    /    /  / 
      |     |  \|_|/ /    / | \|___/    /  |    \    \___|/      |   |       |     /___/| |    |\    \  \|___/    /  /  
      |     |       |    |  |     /    /  /|    |\     \        /   //       |     \____|\|    | |    |     /    /  /   
      |\____\       |____|  /    /____/  / |\ ___\|_____|      /___//        |____ '     /|____| |____|    /____/  /    
      | |    |      |    | /    |`    | /  | |    |     |     |`   |         |    /_____/ |    | |    |   |`    | /     
       \|____|      |____|/     |_____|/    \|____|_____|     |____|         |____|     | |____| |____|   |_____|/      
          \|          |/           |/          \|    |/         \|             \| |_____|/  \|     |/        |/         
           '          '            '            '    '           '              '    |/      '     '         '          
                                                                                     '                                ''')

def spaceship():
    print("\n")
    print('''     %******                
             /##############%             
         &####################%&        
   .%##############################&   
  #&&&&%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&@# 
   .     /&%%%%&&&&&&&&&&%%%%%%,  .     
               &******/*/#              
              #&*      .&@%             
              *          .,             
            /  |         | \            
           /   |         |  \           
          /    |         |   \          
         /                    \          
         ''') 

def butler_picture():
    print('''                                        
                   ///                  
                 ///////                
                   ///                  
                   //                   
      /////////////////////////////     
     /,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/    
   ##/,,,,,,###,,,,,,,,,,/###,,,,,,/##  
 ##///,,,,#     ##,,,,,#      #,,,,/(/#)
 ##///***/#     |#**#**#      #****/(/#)
 ##///*****#####**#//##**####******/(/#)
 ##///************#####************/(/#)
 ##//////////###############////////(/#)
  #/////////# #  #  #  #  # #///////|/# 
     ///////////////////////////////    
     ///////////////////////////////    
                                       ''')

def chef_picture():
    print('''                                        
      ........ ... *,,.                 
      ,,,,,,. ,*,,......   .,..         
       ,,,.**,,,,....  .    ....        
              ,,,....  .                
              ,,,..... .                
              ...                       
              ..,,.......%%#          
           #%%%.%#%%..,%%#%%%#          
          #%&***,@*,..,/@....%%        
         ,.&.,,,* ,....,. ...%%         
          ##.....,,***,,...   #         
           ,,,,./*******../.. .         
           *,,,**,.*****,....           
            ,,,,,,, ...*.....           
              .,,,,,,,,,,,.             
            ... ,%#(#/###.    ''')

def queen_picture():
    print("\n")
    print('''           .*,             
                   ,***,(,*/*/*         
                .,***..../*//*/*.       
                /,/,*....,,/**/(//,     
                //*..(,,.,..,//*////    
               ./( *,......,,*,.///,/   
                  ,.,..,..,,******/((   
                    , .*..,**/,,///**/  
                     ..,,****,,/*((,((( 
                      ,(//(..#%/%#/(*(/ 
                       ,*//%%#...../(*/ 
 .    /                 *%&.....,,,,,((,
/,&&&&/                (&#......***,./( 
 %&&&& /              %%&*......,*,,,.( 
  ((*,...            %%&&,......,*,*,,%#
 ,......*,.....     %%%&&,......**,*,,  
  ,.,,,,,,..,,,*,  %%%&&&,.....,*,*,,.  
   ,*,       ,,,*,.&&&&&&,,...,*,,/**   
              ..,,**.(#((((/(#/*,%%(#   
               (...,,*(/(//(/(#(((%%    
              /#(,..,*/(#(((//((#((/    
               (##(..,,*//(/(/(##/(#/   
               //((/((,,(/(#/(####(((/  
                 .,,/,*(((((/(((##(#((( 
                            /(((##/ ,// 
%%/. %%*#/#(%#%*%/%(/,/,%%%%%%%%%%%///%%''')

def alien_picture():
    print('''@@@@@#.@@@@@@@@@@@@@@@@@(@@@@@
@@@@((.@@@@@@@@@@@@@@@@.##@@@@
@@@@#(#.@.@###**###@.@.#(#.@@@
@@@@.#.(#@@(((,,(((#@##.((@@@@
@@@@@@@@*...,,,,,,,,...@@.@@@@
@@@@@@#..,(......,./(  #&@.@@@
@@##&#*.*&&&%#,,.%&&&/*#@&#@@@
@@@.@@#*.....,...,....*@#%@,@@
@@/(/@@#*,..&&&&&&..,*&##@((.@
@@@@.#@@#@##,,,,,,,#@&#@###@@@
@@@@@#@@@@(@@@@@@@@@#@@@.@@@@@
@@@@.#@@@%#@@/(((,@@#@@@&.@@@@
@@@#@@&@@@@@@@((.@@@@@@@@##@@@
@.#@@@@@@@@@.@@@@@.@@&@.@@@(.@
@//@@@.@@@@@/@@@#@/@@@@.@(@@(.
@.@@@@@@@@@/@@@@@@@@@@@&@@.@@@
@@@@@@,/@@@#@@.@@@@@#&@*.@@@@@
@@@@@@./@@%@@.@@@.@@/@@/.@@@@@
@@@@@@.(@&(@@@@@@@@@@&@(/@@@@@
@@@@@@.@@@#@@@@@@@.@@#@@@@@@@@
@@@@@@@&@@@@.((((((.@(@/.@@@@@
@@@((((((#.((((((((((./(((((@@''')


def king_picture():
    print('''       #**   
                , .,,,, .          (%   
                */(.##//,,        /(*   
               (/*  .  *//        .(%   
               /,/     #/#         /    
             ./*##..   #%%&&       *    
             ####*%*  */#&&&      ,     
          .(#####*(,   *%&&&&(%/  *     
        %(*###.%#&,    %#&&%%#.(& (     
       (%####/%%#%,%#&.#%%#(#####(#     
      ##&######%#&%%&&%/&&%##%##%,&&    
     ####%#####%%&&%%%##&&&&&%###/#%%   
    %#########%#&%%#%&&&&&&&&&&&(&&%&   
    ###########&%%%&/&&%%&&%&&%.  .&%   
    #%##%%#%%&&%%%&&%&&/%%%&&&&.,,*&&   
    ###&&&%#&%%%%&%%&&%%%#%%&&&%&&&&&''')

def deadbody_picture():
    print('''                                        
                                        
                _.**.-_        _-.     
             .*%       %(////#((//      
                 (*&(***%(((#,,**       
             (*/%, *&/#     *#/         
      (//(#%*      #//       */         
 %/.              *//          *(%*     
                 (*(                    
            ,/*%|.                      
        */&*                            
       *#(                              
''')

titlescreen()

name = input("                                      Hello user! Welcome to a Group 3 productions\n                                                 What is your name? ")

context_of_game()
choose_a_room()