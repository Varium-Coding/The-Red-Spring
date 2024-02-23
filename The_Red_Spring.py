import time
import math
import random
import sys
bookinvestigate = False
mayorcheck = False
mayortalk = False
runemayortalk = False
runebookinvest = False
runeteachersafe = False
runebakersafe = False
passcheck = False
#routechecker
sheriffs_office = False
bakertalked = False
teachertalked = False
bakercheck = False
townehallinnerchek = False
townhallouterchek = False
teacherdead = False
bakerdead = False


def rollcheck():
    typewriter_effect("Rolling dice...")
    time.sleep(1)
    roll_result = random.randint(1, 20) 
    typewriter_effect ("You rolled a " + str(roll_result) + "!")
    return roll_result

def typewriter_effect(text,speed=0.001):
    for char in text:
        print(char, end='', flush=True )
        time.sleep(speed)
    print()

def intro_letter():
    typewriter_effect("The journey begins with you reading your letter to remind yourself of what you are doing, heading into such a small village such as this one.")
    typewriter_effect("Hello there!")
    typewriter_effect("My name is Howard Phillips, I’m the Mayor of the town of Redspring, just a ways from the Rhode Island harbour; you can’t miss it - unless you do, o’ course; we ain’t very big…")
    typewriter_effect("You see, me and the town need your help. There’s… things going on… strange things…")
    typewriter_effect("I think people are pretending not to see em and hoping they’ll go away, but… the kids have been going missing, and quite frankly; I don’t know what to do.")
    typewriter_effect("That’s where you come in; I hear from a colleague of yours at Swan Point University that you have an interest in particularly troublesome mysteries. So in exchange for you solving this mess, I’d like to offer you $200 and full room and board at the local hotel for as long as you need.")
    typewriter_effect("When you arrive, you’ll find me in my office in the town hall, I expect that if you come; you’ll see me right away. I fear that if we don’t get help soon, the town ain’t gonna last very long")
    typewriter_effect("Yours in fleeting hope,")
    typewriter_effect("Mayor Howard Phillips")

def choose_class():
    typewriter_effect("Welcome to the town")
    typewriter_effect("Choose your character and gain more knowledge of them:")
    typewriter_effect("1. Jackson MacAllister 'Ironclad' - Former star athlete.")
    typewriter_effect("2. Professor Evelyn Whitlock - A brilliant and enigmatic professor of archaeology.")
    typewriter_effect("3. Magnus Sinclair 'The Mountain' - A towering figure with a rugged demeanor.")

    while True:
        choice = input("Enter the number of your chosen character: ")

        if choice == "1":
            typewriter_effect("You've chosen to be Jackson 'Ironclad' MacAllister  Former star athlete, known for incredible speed and agility. Despite his athletic prowess he harbors a deep fascination with the occult, often delving into forbidden tomes in the university Library. Are you sure you want to proceed? (yes/no)")
            while True:
                confirmation = input().lower()
                if confirmation == "yes":
                    return "Jackson 'Ironclad' MacAllister"
                elif confirmation == "no":
                    break
                else:
                    typewriter_effect("Invalid input. Please enter 'yes' or 'no'.")
                    continue
        elif choice == "2":
            typewriter_effect("You've chosen to be Professor Evelyn Whitlock - A brilliant and enigmatic professor of archaeology and ancient languages at the university. Professor Whitlock is renowned for her groundbreaking research into ancient civilizations, particularly those with ties to eldritch lore. She possesses a keen intellect and an insatiable curiosity, often leading her on perilous expeditions in search of forbidden knowledge. Are you sure you want to proceed? (yes/no)")
            while True:
                confirmation = input().lower()
                if confirmation == "yes":
                    return "Professor Evelyn Whitlock"
                elif confirmation == "no":
                    break
                else:
                    typewriter_effect("Invalid input. Please enter 'yes' or 'no'.")
                    continue
        elif choice == "3":
            typewriter_effect("You've chosen to play as Magnus 'The Mountain' Sinclair Magnus Sinclair once served as the university's head groundskeeper and caretaker. Possessing immense strength and resilience, he was often called upon to deal with the more dangerous aspects of maintaining the university's sprawling campus. Despite his gruff exterior, Magnus has a deep understanding of the occult, passed down through generations of his family who have served the university for centuries. Are you sure you want to proceed? (yes/no)")
            while True:
                confirmation = input().lower()
                if confirmation == "yes":
                    return "Magnus 'The Mountain' Sinclair"
                elif confirmation == "no":
                    break
                else:
                    typewriter_effect("Invalid input. Please enter 'yes' or 'no'.")
                    continue
        else:
            typewriter_effect("Invalid choice. Please choose a number between 1 and 3.")
            continue

def mayor():
    global mayortalk
    global runemayortalk 
    global mayorcheck
    typewriter_effect("You ignore your distracting thoughts and head towards the Town Hall, putting aside any curiosity in odd parcels - you’re a university researcher, not a postal worker - and through an equal measure of dedication to your agreement, and a desire to get out of the rain; you push open the creaky wooden door to the Town Hall’s main foyer.")
    typewriter_effect("The interior of this hall is old, the design of the wooden furniture more reminiscent of a revolution-era gathering place than anything made in the last 50 years. The floorboards creak beneath your feet and signal your approach to anyone nearby.")
    typewriter_effect("You hear banging and scuffling as a portly old man wearing a battered grey suit and large wireframe glasses stands at the top of the stairs to your left. He smiles at you as he beckons you to the top of the stairs and into a moderately sized office, piled high with books and notes in all directions.")
    typewriter_effect("“It is good to see you,” says the man.")
    typewriter_effect("“I’m glad you got my letter and even more so that you decided to help; Professor van Buren seems to have great faith that you can solve what’s goin’ on.”")
    typewriter_effect("He reaches into a draw and pulls out a neatly folded piece of paper")
    typewriter_effect("“You see, we’ve known that kids go missin’ here and there; we were jus’ sure they were runnin’ off to the big city to chase wild dreams…”")
    typewriter_effect("The Mayor trails off, a sombre look grows on his face.")
    typewriter_effect("“Lotta kids here dream of making something o’ themselves in Arkham wasn’t til I heard from a driver bringing meats an such that he ain’t driven no-one to Arkham in three years, that I started wonderin’.")
    typewriter_effect("He unfolds the paper, an odd symbol is scrawled on it in a deep, maroon ink")
    print("     |      ")
    print("     |   *  ")
    print("     |      ")
    print("  ___|___   ")
    print(" |       |  ")
    print(" |       |  ")
    print(" |       |  ")
    typewriter_effect("“I been askin’ the sheriff to look into in for a while now, but he says ain’t nothin’ worth worrying about”")
    typewriter_effect("“So I looked into it myself, found this at the old tailors shop, where one o’ the first kids went missin’. Kid’s parents ran off to Arkham to look for her, so ain’t no use tryna’ find ‘em.”")
    typewriter_effect("“But we’re gonna have a town meetin’ tomorrow, let everyone know what you’re here for; and encourage ‘em to speak to you, not that you need to be there, but people round here tend to be ‘spicious of new faces, so might be easier if I introduce you.”")
    typewriter_effect("Can’t really blame them, you think to yourself.")
    typewriter_effect("“Course, you can walk around and talk to anyone you like; but you ain’t police, so if you start harassin’ folk, sheriff’ll have to take you in.”")
    typewriter_effect("“That said, most people are nice folk, jus’ a little cautious. Think you’ll find the baker most accommodating, Margaret Whateley, her name is. That said, you could always speak to the schoolmarm Miss Eleanor Greene, or our local vicar Father Raymond.”")
    typewriter_effect("A God fearing man in a place like this? Must be doing well for himself… ")
    typewriter_effect("“‘Course if you wanted to rest your head after your journey, the Hotel’s booked and ready for you, could sleep in there all day if you wanted. Course you’ll be wanting to investigate all the sooner, get your pay and get outta this place, right?”")
    typewriter_effect("Actually, a warm bath wouldn’t go amiss right about now.")
    typewriter_effect("“But here, take this; and I’ll let you go about your business; meeting’s tomorrow, feel free to join!”")
    typewriter_effect("You pick up the paper on the table and make your way out of the office, fearing that lingering any longer and you would’ve had to give a speech.")
    typewriter_effect("You exit the Town Hall into a lighter rain; the Sheriff’s office is opposite, the school down the road to the east, and you hear shouting coming from the path to the west.")
    runemayortalk = True
    mayortalk = True
    mayorcheck = True

def go_to_sheriffs_office():
    global sheriffs_office
    typewriter_effect("After a brief walk you make it to the sheriffs office, it seems empty, almost as if there had been no criminals brought here for a while.")
    typewriter_effect("You approach the sheriff’s office with a reprehensible look. Pondering your choices and what they might lead to. ")
    typewriter_effect("“Is the sheriff in?” you ask inquisitively to the young man who appeared to be the deputy sheriff. He gestured towards the back where a worn-down looking room could be seen.")
    typewriter_effect("You spot the sheriff, uniform raggedy from his years serving his town smoking a pipe of tobacco that gave the room a burning sensation when you walked in. ")
    typewriter_effect("“You must be the sheriff” you say, holding your breath so the smoke isn’t inhaled. It has a woody aroma to it yet sweet at the same time surprisingly.")
    typewriter_effect("“Must I? Those are  fighting words, buddy. You lookin for one?” the sheriff spat back at you")
    typewriter_effect("“Of course not, sheriff, just answers. Ones that you might have about the missing kids.”")
    typewriter_effect("You scan the sheriff curiously to see his reaction to your answer. He looks troubled by their disappearance and signals to the chair opposite his so you take a seat, observing your surroundings and making notes when you can.")
    typewriter_effect("“The kids were reported missin’ a week ago. There were no clues left behind by the kidnappers so they knew what they were doin’. Other than that, I got nothin’ for ya, pal. But best of luck to ya. Me an’ my deputy will help where we can alright. Just holler for us.”")
    typewriter_effect("You thanked the sheriff for his cooperation and took your leave. The deputy nodded as you left, the road bleak but potential leads were now in sight. They had to be a group of some sorts which was promising for the case.")
    time.sleep(2)
    sheriffs_office = True
    choice2split()
 
def go_to_sheriffs_office2():
    global sheriffs_office
    typewriter_effect("After a brief walk you make it to the sheriffs office, it seems empty, almost as if there had been no criminals brought here for a while.")
    typewriter_effect("You approach the sheriff’s office with a reprehensible look. Pondering your choices and what they might lead to. ")
    typewriter_effect("“Is the sheriff in?” you ask inquisitively to the young man who appeared to be the deputy sheriff. He gestured towards the back where a worn-down looking room could be seen.")
    typewriter_effect("You spot the sheriff, uniform raggedy from his years serving his town smoking a pipe of tobacco that gave the room a burning sensation when you walked in. ")
    typewriter_effect("“You must be the sheriff” you say, holding your breath so the smoke isn’t inhaled. It has a woody aroma to it yet sweet at the same time surprisingly.")
    typewriter_effect("“Must I? Those are  fighting words, buddy. You lookin for one?” the sheriff spat back at you")
    typewriter_effect("“Of course not, sheriff, just answers. Ones that you might have about the missing kids.”")
    typewriter_effect("You scan the sheriff curiously to see his reaction to your answer. He looks troubled by their disappearance and signals to the chair opposite his so you take a seat, observing your surroundings and making notes when you can.")
    typewriter_effect("“The kids were reported missin’ a week ago. There were no clues left behind by the kidnappers so they knew what they were doin’. Other than that, I got nothin’ for ya, pal. But best of luck to ya. Me an’ my deputy will help where we can alright. Just holler for us.”")
    typewriter_effect("You thanked the sheriff for his cooperation and took your leave. The deputy nodded as you left, the road bleak but potential leads were now in sight. They had to be a group of some sorts which was promising for the case.")
    sheriffs_office = True
    time.sleep(2)
    inn1()

def go_to_east_path():
    global bookinvestigate
    global bakertalked
    typewriter_effect("You make your way towards the bakery, the fragrance of fresh-baked pastries filling your lung as you approach.")
    typewriter_effect("The door swings open and a bell rings gleefully. “Hello there sir, how may I be of service?” asks the baker as she watches you enter her bakery. Her smile seems as warm and gentle as the bread she baked that morning.")
    typewriter_effect("“Good morning ma’am, you probably already know why I’m here don’t you?” you ask as she pulls up two chairs to seat you and herself. You take off your coat and drape it behind you on your chair, ready to proceed")
    typewriter_effect("“Yes I’ve been made aware, sir. It’s about the missing kids isn’t it? My own son was taken and I’m begging you to find him. He’s all I have left in this world” she pleads as she begins tearing up with memories of her son flooding her.")
    typewriter_effect("“Don’t worry ma’am, I’m going to find your son and the rest of the kids in no time. Do you know anything about where he was or when it happened? Anything at all would be great.”")
    if bookinvestigate == True:
        typewriter_effect("“Does this look at all familiar to you?” You take out the book, allowing the baker to examine it herself. She shakes her head confusedly, wondering where you found such a thing but can’t help you further.")
        typewriter_effect("“I’m sorry sir, nothing. If I did, you’d be the first person to know believe me.”")
        typewriter_effect("“That’s okay ma’am, you have a good day then.” You take your jacket and stand, shake the baker’s hand and tell her everything will be alright. You promptly leave, she wasn’t much help but now you’re more motivated than ever to find these kids.")
    typewriter_effect("You wander around town, fidgeting with the book and wondering what the rune inside could mean, if there’s any connection to the kids. If there is, you’ll make it and find them, that’s for damn sure. And you won’t rest till you do.")
    bakertalked = True
    time.sleep(2)
    choice2split()

def go_to_east_path2():
    global bookinvestigate
    global bakertalked
    
    typewriter_effect("You make your way towards the bakery, the fragrance of fresh-baked pastries filling your lung as you approach.")
    typewriter_effect("The door swings open and a bell rings gleefully. “Hello there sir, how may I be of service?” asks the baker as she watches you enter her bakery. Her smile seems as warm and gentle as the bread she baked that morning.")
    typewriter_effect("“Good morning ma’am, you probably already know why I’m here don’t you?” you ask as she pulls up two chairs to seat you and herself. You take off your coat and drape it behind you on your chair, ready to proceed")
    typewriter_effect("“Yes I’ve been made aware, sir. It’s about the missing kids isn’t it? My own son was taken and I’m begging you to find him. He’s all I have left in this world” she pleads as she begins tearing up with memories of her son flooding her.")
    typewriter_effect("“Don’t worry ma’am, I’m going to find your son and the rest of the kids in no time. Do you know anything about where he was or when it happened? Anything at all would be great.”")
    if bookinvestigate == True:
        typewriter_effect("“Does this look at all familiar to you?” You take out the book, allowing the baker to examine it herself. She shakes her head confusedly, wondering where you found such a thing but can’t help you further.")
        typewriter_effect("“I’m sorry sir, nothing. If I did, you’d be the first person to know believe me.”")
        typewriter_effect("“That’s okay ma’am, you have a good day then.” You take your jacket and stand, shake the baker’s hand and tell her everything will be alright. You promptly leave, she wasn’t much help but now you’re more motivated than ever to find these kids.")
    typewriter_effect("You wander around town, fidgeting with the book and wondering what the rune inside could mean, if there’s any connection to the kids. If there is, you’ll make it and find them, that’s for damn sure. And you won’t rest till you do.")
    typewriter_effect("You decide its about time to head back to the Inn.")
    bakertalked = True
    time.sleep(2)
    inn1()

def go_to_east_path3():
    global bookinvestigate
    global bakertalked
    
    typewriter_effect("You make your way towards the bakery, the fragrance of fresh-baked pastries filling your lung as you approach.")
    typewriter_effect("The door swings open and a bell rings gleefully. “Hello there sir, how may I be of service?” asks the baker as she watches you enter her bakery. Her smile seems as warm and gentle as the bread she baked that morning.")
    typewriter_effect("“Good morning ma’am, you probably already know why I’m here don’t you?” you ask as she pulls up two chairs to seat you and herself. You take off your coat and drape it behind you on your chair, ready to proceed")
    typewriter_effect("“Yes I’ve been made aware, sir. It’s about the missing kids isn’t it? My own son was taken and I’m begging you to find him. He’s all I have left in this world” she pleads as she begins tearing up with memories of her son flooding her.")
    typewriter_effect("“Don’t worry ma’am, I’m going to find your son and the rest of the kids in no time. Do you know anything about where he was or when it happened? Anything at all would be great.”")
    if bookinvestigate == True:
        typewriter_effect("“Does this look at all familiar to you?” You take out the book, allowing the baker to examine it herself. She shakes her head confusedly, wondering where you found such a thing but can’t help you further.")
    typewriter_effect("“I’m sorry sir, nothing. If I did, you’d be the first person to know believe me.”")
    typewriter_effect("“That’s okay ma’am, you have a good day then.” You take your jacket and stand, shake the baker’s hand and tell her everything will be alright. You promptly leave, she wasn’t much help but now you’re more motivated than ever to find these kids.")
    typewriter_effect("You wander around town, fidgeting with the book and wondering what the rune inside could mean, if there’s any connection to the kids. If there is, you’ll make it and find them, that’s for damn sure. And you won’t rest till you do.")
    typewriter_effect("You decide its about time to head back to the Inn.")
    bakertalked = True
    time.sleep(2)
    inn2()

def go_to_east_path4():
    global bookinvestigate
    global bakertalked
    
    typewriter_effect("You make your way towards the bakery, the fragrance of fresh-baked pastries filling your lung as you approach.")
    typewriter_effect("The door swings open and a bell rings gleefully. “Hello there sir, how may I be of service?” asks the baker as she watches you enter her bakery. Her smile seems as warm and gentle as the bread she baked that morning.")
    typewriter_effect("“Good morning ma’am, you probably already know why I’m here don’t you?” you ask as she pulls up two chairs to seat you and herself. You take off your coat and drape it behind you on your chair, ready to proceed")
    typewriter_effect("“Yes I’ve been made aware, sir. It’s about the missing kids isn’t it? My own son was taken and I’m begging you to find him. He’s all I have left in this world” she pleads as she begins tearing up with memories of her son flooding her.")
    typewriter_effect("“Don’t worry ma’am, I’m going to find your son and the rest of the kids in no time. Do you know anything about where he was or when it happened? Anything at all would be great.”")
    if bookinvestigate == True:
        typewriter_effect("“Does this look at all familiar to you?” You take out the book, allowing the baker to examine it herself. She shakes her head confusedly, wondering where you found such a thing but can’t help you further.")
    typewriter_effect("“I’m sorry sir, nothing. If I did, you’d be the first person to know believe me.”")
    typewriter_effect("“That’s okay ma’am, you have a good day then.” You take your jacket and stand, shake the baker’s hand and tell her everything will be alright. You promptly leave, she wasn’t much help but now you’re more motivated than ever to find these kids.")
    typewriter_effect("You wander around town, fidgeting with the book and wondering what the rune inside could mean, if there’s any connection to the kids. If there is, you’ll make it and find them, that’s for damn sure. And you won’t rest till you do.")
    typewriter_effect("You decide its about time to head back to the Inn.")
    bakertalked = True
    time.sleep(2)
    choice3split

def go_to_east_path5():
    global bookinvestigate
    global bakertalked
    
    typewriter_effect("You make your way towards the bakery, the fragrance of fresh-baked pastries filling your lung as you approach.")
    typewriter_effect("The door swings open and a bell rings gleefully. “Hello there sir, how may I be of service?” asks the baker as she watches you enter her bakery. Her smile seems as warm and gentle as the bread she baked that morning.")
    typewriter_effect("“Good morning ma’am, you probably already know why I’m here don’t you?” you ask as she pulls up two chairs to seat you and herself. You take off your coat and drape it behind you on your chair, ready to proceed")
    typewriter_effect("“Yes I’ve been made aware, sir. It’s about the missing kids isn’t it? My own son was taken and I’m begging you to find him. He’s all I have left in this world” she pleads as she begins tearing up with memories of her son flooding her.")
    typewriter_effect("“Don’t worry ma’am, I’m going to find your son and the rest of the kids in no time. Do you know anything about where he was or when it happened? Anything at all would be great.”")
    if bookinvestigate == True:
        typewriter_effect("“Does this look at all familiar to you?” You take out the book, allowing the baker to examine it herself. She shakes her head confusedly, wondering where you found such a thing but can’t help you further.")
    typewriter_effect("“I’m sorry sir, nothing. If I did, you’d be the first person to know believe me.”")
    typewriter_effect("“That’s okay ma’am, you have a good day then.” You take your jacket and stand, shake the baker’s hand and tell her everything will be alright. You promptly leave, she wasn’t much help but now you’re more motivated than ever to find these kids.")
    typewriter_effect("You wander around town, fidgeting with the book and wondering what the rune inside could mean, if there’s any connection to the kids. If there is, you’ll make it and find them, that’s for damn sure. And you won’t rest till you do.")
    typewriter_effect("You decide its about time to head back to the Inn.")
    bakertalked == True
    time.sleep(2)
    inn3()

def go_to_west_path():
    global runemayortalk
    global runebookinvest
    global sheriffs_office
    global bakertalked
    global teachertalked
    typewriter_effect("You manage to tear yourself away from the call of the mysterious cries from the west of town, and head towards the local school.")
    typewriter_effect("Weird decision, why would kids be there?")
    typewriter_effect("Anyway, you approach the front doors of the school, just in time to witness all the child going home for the day.")
    typewriter_effect("Yep, just one.")
    typewriter_effect("Recovering from the abundance of children you have seen today, you turn your attention to the Schoolmarm - a Miss Eleanor Greene - hair in tight curls, wearing small spectacles and a pleated skirt; she looks at you with a slight curiosity.")
    typewriter_effect("“I suppose you’re not here to learn to count to five…”")
    typewriter_effect("You smile, and reply “Unless you’re teaching up to ten, I’ll pass.”")
    typewriter_effect("She chuckles slightly, stands up from her desk, and meets you in the centre of the school building, which you now realise is just a singular room.")
    typewriter_effect("You introduce yourself, explain your investigation, and she raises a hand to stop you")
    typewriter_effect("“I’m aware of the situation, in case you haven’t noticed, I’m missing a good number of students.”")
    typewriter_effect("You inhale and straighten your back, slightly embarrassed, it should have been clear that she would know about the missing children, but you didn’t think of that, did you?")
    typewriter_effect("“Ah, yes… of course you would-” you begin.")
    typewriter_effect("“It wouldn’t be a problem, but it’s always the good students…” she muses.")
    typewriter_effect("You show her the piece of paper with the rune.")
    typewriter_effect("“This… I’ve seen something like this before, a few weeks ago…”")
    typewriter_effect("You look at her quizzically, and she takes the paper and walks back to her desk. She opens a drawer and pulls out a similarly folded piece of paper with a different symbol etched upon it, written in the same deep red ink.")
    if runebookinvest == True:
        typewriter_effect("“Well, you seem somewhat capable… maybe we’ll actually get to the bottom of this…”.")
    elif runemayortalk == True:
        typewriter_effect("“Well, if the Mayor gave this to you, then it’s good to know that someone at least seems interested in finding out what’s going on.”")
    typewriter_effect ("“The Mayor’s hosting-” you say")
    typewriter_effect ("“-a town meeting?” She rudely interrupts, “Nothing will happen, the Sheriff will tell everyone they’re overreacting, and they’ll start arguing about corn-yields instead.”")
    typewriter_effect ("You manage to hide your shock at the downright gall of her interrupting you, for long enough to utter, “Well, maybe someone doing something is better than no-one trying…” ")
    typewriter_effect ("In that moment, you can sense her belief in you… and you decide not to pursue a career as a motivational speaker.")
    typewriter_effect ("“I’ll go, but if the Sheriff is the same closed-minded yokel that he normally is, you’re investigating these with me.”")
    typewriter_effect ("Fair deal.")
    typewriter_effect ("You stand and approach the door.")
    typewriter_effect ("“Don’t make me wait” she calls after you, “I’m finding out one way or another.”")
    typewriter_effect ("You smile as you make your way back to the centre of town.")
    teachertalked = True
    time.sleep(2)
    choice2split()

def go_to_west_path2():
    global runemayortalk
    global runebookinvest
    global sheriffs_office
    global bakertalked
    global teachertalked
    typewriter_effect("You manage to tear yourself away from the call of the mysterious cries from the west of town, and head towards the local school.")
    typewriter_effect("Weird decision, why would kids be there?")
    typewriter_effect("Anyway, you approach the front doors of the school, just in time to witness all the child going home for the day.")
    typewriter_effect("Yep, just one.")
    typewriter_effect("Recovering from the abundance of children you have seen today, you turn your attention to the Schoolmarm - a Miss Eleanor Greene - hair in tight curls, wearing small spectacles and a pleated skirt; she looks at you with a slight curiosity.")
    typewriter_effect("“I suppose you’re not here to learn to count to five…”")
    typewriter_effect("You smile, and reply “Unless you’re teaching up to ten, I’ll pass.”")
    typewriter_effect("She chuckles slightly, stands up from her desk, and meets you in the centre of the school building, which you now realise is just a singular room.")
    typewriter_effect("You introduce yourself, explain your investigation, and she raises a hand to stop you")
    typewriter_effect("“I’m aware of the situation, in case you haven’t noticed, I’m missing a good number of students.”")
    typewriter_effect("You inhale and straighten your back, slightly embarrassed, it should have been clear that she would know about the missing children, but you didn’t think of that, did you?")
    typewriter_effect("“Ah, yes… of course you would-” you begin.")
    typewriter_effect("“It wouldn’t be a problem, but it’s always the good students…” she muses.")
    typewriter_effect("You show her the piece of paper with the rune.")
    typewriter_effect("“This… I’ve seen something like this before, a few weeks ago…”")
    typewriter_effect("You look at her quizzically, and she takes the paper and walks back to her desk. She opens a drawer and pulls out a similarly folded piece of paper with a different symbol etched upon it, written in the same deep red ink.")
    if runebookinvest == True:
        typewriter_effect("“Well, you seem somewhat capable… maybe we’ll actually get to the bottom of this…”.")
    elif runemayortalk == True:
        typewriter_effect("“Well, if the Mayor gave this to you, then it’s good to know that someone at least seems interested in finding out what’s going on.”")
    typewriter_effect ("“The Mayor’s hosting-” you say")
    typewriter_effect ("“-a town meeting?” She rudely interrupts, “Nothing will happen, the Sheriff will tell everyone they’re overreacting, and they’ll start arguing about corn-yields instead.”")
    typewriter_effect ("You manage to hide your shock at the downright gall of her interrupting you, for long enough to utter, “Well, maybe someone doing something is better than no-one trying…” ")
    typewriter_effect ("In that moment, you can sense her belief in you… and you decide not to pursue a career as a motivational speaker.")
    typewriter_effect ("“I’ll go, but if the Sheriff is the same closed-minded yokel that he normally is, you’re investigating these with me.”")
    typewriter_effect ("Fair deal.")
    typewriter_effect ("You stand and approach the door.")
    typewriter_effect ("“Don’t make me wait” she calls after you, “I’m finding out one way or another.”")
    typewriter_effect ("You smile as you make your way back to the centre of town.")
    teachertalked = True
    time.sleep(2)
    inn1()

def go_to_west_path3():
    global runemayortalk
    global runebookinvest
    global sheriffs_office
    global bakertalked
    global teachertalked
    typewriter_effect("You manage to tear yourself away from the call of the mysterious cries from the west of town, and head towards the local school.")
    typewriter_effect("Weird decision, why would kids be there?")
    typewriter_effect("Anyway, you approach the front doors of the school, just in time to witness all the child going home for the day.")
    typewriter_effect("Yep, just one.")
    typewriter_effect("Recovering from the abundance of children you have seen today, you turn your attention to the Schoolmarm - a Miss Eleanor Greene - hair in tight curls, wearing small spectacles and a pleated skirt; she looks at you with a slight curiosity.")
    typewriter_effect("“I suppose you’re not here to learn to count to five…”")
    typewriter_effect("You smile, and reply “Unless you’re teaching up to ten, I’ll pass.”")
    typewriter_effect("She chuckles slightly, stands up from her desk, and meets you in the centre of the school building, which you now realise is just a singular room.")
    typewriter_effect("You introduce yourself, explain your investigation, and she raises a hand to stop you")
    typewriter_effect("“I’m aware of the situation, in case you haven’t noticed, I’m missing a good number of students.”")
    typewriter_effect("You inhale and straighten your back, slightly embarrassed, it should have been clear that she would know about the missing children, but you didn’t think of that, did you?")
    typewriter_effect("“Ah, yes… of course you would-” you begin.")
    typewriter_effect("“It wouldn’t be a problem, but it’s always the good students…” she muses.")
    typewriter_effect("You show her the piece of paper with the rune.")
    typewriter_effect("“This… I’ve seen something like this before, a few weeks ago…”")
    typewriter_effect("You look at her quizzically, and she takes the paper and walks back to her desk. She opens a drawer and pulls out a similarly folded piece of paper with a different symbol etched upon it, written in the same deep red ink.")
    if runebookinvest == True:
        typewriter_effect("“Well, you seem somewhat capable… maybe we’ll actually get to the bottom of this…”.")
    elif runemayortalk == True:
        typewriter_effect("“Well, if the Mayor gave this to you, then it’s good to know that someone at least seems interested in finding out what’s going on.”")
    typewriter_effect ("“The Mayor’s hosting-” you say")
    typewriter_effect ("“-a town meeting?” She rudely interrupts, “Nothing will happen, the Sheriff will tell everyone they’re overreacting, and they’ll start arguing about corn-yields instead.”")
    typewriter_effect ("You manage to hide your shock at the downright gall of her interrupting you, for long enough to utter, “Well, maybe someone doing something is better than no-one trying…” ")
    typewriter_effect ("In that moment, you can sense her belief in you… and you decide not to pursue a career as a motivational speaker.")
    typewriter_effect ("“I’ll go, but if the Sheriff is the same closed-minded yokel that he normally is, you’re investigating these with me.”")
    typewriter_effect ("Fair deal.")
    typewriter_effect ("You stand and approach the door.")
    typewriter_effect ("“Don’t make me wait” she calls after you, “I’m finding out one way or another.”")
    typewriter_effect ("You smile as you make your way back to the centre of town.")
    teachertalked = True
    time.sleep(2)
    inn2()

def go_to_west_path4():
    global runemayortalk
    global runebookinvest
    global sheriffs_office
    global bakertalked
    global teachertalked
    typewriter_effect("You manage to tear yourself away from the call of the mysterious cries from the west of town, and head towards the local school.")
    typewriter_effect("Weird decision, why would kids be there?")
    typewriter_effect("Anyway, you approach the front doors of the school, just in time to witness all the child going home for the day.")
    typewriter_effect("Yep, just one.")
    typewriter_effect("Recovering from the abundance of children you have seen today, you turn your attention to the Schoolmarm - a Miss Eleanor Greene - hair in tight curls, wearing small spectacles and a pleated skirt; she looks at you with a slight curiosity.")
    typewriter_effect("“I suppose you’re not here to learn to count to five…”")
    typewriter_effect("You smile, and reply “Unless you’re teaching up to ten, I’ll pass.”")
    typewriter_effect("She chuckles slightly, stands up from her desk, and meets you in the centre of the school building, which you now realise is just a singular room.")
    typewriter_effect("You introduce yourself, explain your investigation, and she raises a hand to stop you")
    typewriter_effect("“I’m aware of the situation, in case you haven’t noticed, I’m missing a good number of students.”")
    typewriter_effect("You inhale and straighten your back, slightly embarrassed, it should have been clear that she would know about the missing children, but you didn’t think of that, did you?")
    typewriter_effect("“Ah, yes… of course you would-” you begin.")
    typewriter_effect("“It wouldn’t be a problem, but it’s always the good students…” she muses.")
    typewriter_effect("You show her the piece of paper with the rune.")
    typewriter_effect("“This… I’ve seen something like this before, a few weeks ago…”")
    typewriter_effect("You look at her quizzically, and she takes the paper and walks back to her desk. She opens a drawer and pulls out a similarly folded piece of paper with a different symbol etched upon it, written in the same deep red ink.")
    if runebookinvest == True:
        typewriter_effect("“Well, you seem somewhat capable… maybe we’ll actually get to the bottom of this…”.")
    elif runemayortalk == True:
        typewriter_effect("“Well, if the Mayor gave this to you, then it’s good to know that someone at least seems interested in finding out what’s going on.”")
    typewriter_effect ("“The Mayor’s hosting-” you say")
    typewriter_effect ("“-a town meeting?” She rudely interrupts, “Nothing will happen, the Sheriff will tell everyone they’re overreacting, and they’ll start arguing about corn-yields instead.”")
    typewriter_effect ("You manage to hide your shock at the downright gall of her interrupting you, for long enough to utter, “Well, maybe someone doing something is better than no-one trying…” ")
    typewriter_effect ("In that moment, you can sense her belief in you… and you decide not to pursue a career as a motivational speaker.")
    typewriter_effect ("“I’ll go, but if the Sheriff is the same closed-minded yokel that he normally is, you’re investigating these with me.”")
    typewriter_effect ("Fair deal.")
    typewriter_effect ("You stand and approach the door.")
    typewriter_effect ("“Don’t make me wait” she calls after you, “I’m finding out one way or another.”")
    typewriter_effect ("You smile as you make your way back to the centre of town.")
    teachertalked = True
    time.sleep(2)
    choice3split()

def go_to_west_path5():
    global runemayortalk
    global runebookinvest
    global sheriffs_office
    global bakertalked
    global teachertalked
    typewriter_effect("You manage to tear yourself away from the call of the mysterious cries from the west of town, and head towards the local school.")
    typewriter_effect("Weird decision, why would kids be there?")
    typewriter_effect("Anyway, you approach the front doors of the school, just in time to witness all the child going home for the day.")
    typewriter_effect("Yep, just one.")
    typewriter_effect("Recovering from the abundance of children you have seen today, you turn your attention to the Schoolmarm - a Miss Eleanor Greene - hair in tight curls, wearing small spectacles and a pleated skirt; she looks at you with a slight curiosity.")
    typewriter_effect("“I suppose you’re not here to learn to count to five…”")
    typewriter_effect("You smile, and reply “Unless you’re teaching up to ten, I’ll pass.”")
    typewriter_effect("She chuckles slightly, stands up from her desk, and meets you in the centre of the school building, which you now realise is just a singular room.")
    typewriter_effect("You introduce yourself, explain your investigation, and she raises a hand to stop you")
    typewriter_effect("“I’m aware of the situation, in case you haven’t noticed, I’m missing a good number of students.”")
    typewriter_effect("You inhale and straighten your back, slightly embarrassed, it should have been clear that she would know about the missing children, but you didn’t think of that, did you?")
    typewriter_effect("“Ah, yes… of course you would-” you begin.")
    typewriter_effect("“It wouldn’t be a problem, but it’s always the good students…” she muses.")
    typewriter_effect("You show her the piece of paper with the rune.")
    typewriter_effect("“This… I’ve seen something like this before, a few weeks ago…”")
    typewriter_effect("You look at her quizzically, and she takes the paper and walks back to her desk. She opens a drawer and pulls out a similarly folded piece of paper with a different symbol etched upon it, written in the same deep red ink.")
    if runebookinvest == True:
        typewriter_effect("“Well, you seem somewhat capable… maybe we’ll actually get to the bottom of this…”.")
    elif runemayortalk == True:
        typewriter_effect("“Well, if the Mayor gave this to you, then it’s good to know that someone at least seems interested in finding out what’s going on.”")
    typewriter_effect ("“The Mayor’s hosting-” you say")
    typewriter_effect ("“-a town meeting?” She rudely interrupts, “Nothing will happen, the Sheriff will tell everyone they’re overreacting, and they’ll start arguing about corn-yields instead.”")
    typewriter_effect ("You manage to hide your shock at the downright gall of her interrupting you, for long enough to utter, “Well, maybe someone doing something is better than no-one trying…” ")
    typewriter_effect ("In that moment, you can sense her belief in you… and you decide not to pursue a career as a motivational speaker.")
    typewriter_effect ("“I’ll go, but if the Sheriff is the same closed-minded yokel that he normally is, you’re investigating these with me.”")
    typewriter_effect ("Fair deal.")
    typewriter_effect ("You stand and approach the door.")
    typewriter_effect ("“Don’t make me wait” she calls after you, “I’m finding out one way or another.”")
    typewriter_effect ("You smile as you make your way back to the centre of town.")
    teachertalked = True
    time.sleep(2)
    inn3()

def book():
    global bookinvestigate
    global runebookinvest
    typewriter_effect("You decide that the mayor can wait, this tightly wrapped parcel seems to have piqued your interest, you wander over to it. Straying away from the path towards the Towne Hall.")
    typewriter_effect("You get to the parcel, its wrapping now damp and muddy, you make out from the weight of it that it must be a book or journal of sorts")
    typewriter_effect("Upon removing the packaging you discover a book with the list of the children that have gone missing in Redspring, where they were taken from, how they were taken but not why. That information is not listed, as if to protect or hide that reason.")
    typewriter_effect("The names include:")
    typewriter_effect("Sally Silversmith - Behind the blacksmith, lured with sounds of a cat. Snatched with a bag early morning")
    typewriter_effect("-REDACTED-")
    typewriter_effect("Ezra Whateley - On the road heading towards the school, Lured with a “Broken Carriage”. Knocked out and thrown into chains into the carriage. (May have been witnessed by Oliver Kingsport)")
    typewriter_effect("Adelaide Dunwich - Outside the cemetery, was visiting her late mother, who she visits late at night as she believes it is the best time to commune with lost relatives. Easy snatch and grab, late night. In the cover of darkness.")
    typewriter_effect("Oliver Kingsport - In the alleyway behind the Lawmens office, believed to have been enroute to report the kidnapping of “Ezra Whateley”. Bag over head. Disposed of in front of the others, to show what happens if they try to escape or talk about what happened.")
    typewriter_effect("You sit reading the book, contemplating who would have been sloppy enough to write the information down. Someone who believes themselves too competent and possibly overestimates their self worth. The book you notice is an expensive book, the pages are not cheap nor shoddy. They are expertly crafted, only someone with spare expenses could have procured such a book. You decide to keep an eye out in the future for someone matching this description.")
    typewriter_effect("You get to the last page and there is some sort of odd symbol is scrawled on it in a deep, maroon ink.")
    print("  _______")
    print(" |       |")
    print(" |       |")
    print(" |   *   |")
    print(" |       |")
    print(" |_______|")
    typewriter_effect("You realise that you’ve spent a good amount of time on this book, maybe too much. You should head back to town and try to find the mayor and explain yourself and why you’re so late.")
    time.sleep(2)
    bookinvestigate = True
    runebookinvest = True
    
def town_intro():
    typewriter_effect("August 20th, 1928.")
    typewriter_effect("You are now an initiate researcher at Miskatonic University, Arkham, Massachusetts. Your hunger for knowledge and mystery has taken you to a respectable position at the university, aided by the connections and guidance of your mentor; Professor Winfield van Buren.")
    typewriter_effect("It is because of the good professor that you find yourself here now; standing half-drenched with cold feet on a dirt road that leads to the small town of Redspring. You look around at the greyness of the world you now find yourself in: the sky - grey, the buildings - grey, somehow, even the people themselves have a greyish hue to them.")
    typewriter_effect("You clutch in your arms a small bag of clothes you know won’t last for a full week, and a letter from the mayor of Redspring, asking for your help and requesting that you head to the town hall to meet with him upon your arrival.")
    typewriter_effect("As you take a breath and walk forward, a cart trundles past you and something falls out of the back, it appears to be a tightly wrapped parcel - potentially quite valuable you think - you notice a light flicker in a window on the second floor of the building marked “TOWNE HALL”... it seems that someone knows you’ve arrived.")

    while True:
        choice1 = input("Please input what you would like to do: Investigate the parcel (parcel) or speak to the mayor (mayor): ").strip().lower()
        
        if choice1 == "mayor":
            mayor()
            break
        elif choice1 == "parcel":
            book()
            break
        else:
            typewriter_effect("Invalid choice. Please enter 'parcel' to investigate the parcel or 'mayor' to speak to the mayor.")

def choice1split():
    global bookinvestigate
    global mayortalk
    global mayorcheck
    
    if bookinvestigate == True:
        typewriter_effect("The mayor approached with a dire face and spoke abruptly: “Where d’you think yer going, partner?” Taken aback, you begin searching for a reason as to why you were missing, coming up with any excuse you can think of while concealing the book on your person.You look around frantically while a million ideas rush around your head and calculating what would work best on the mayor.")
        typewriter_effect("What have you been doing? What is that? Explain yourself! I'm paying you what is left of the towne budget just to get you here! So you have no excuse")
        typewriter_effect("Roll a D20 to try to persuade the mayor why you were right to investigate the book")
        time.sleep(1)
        player_roll = rollcheck()
        if player_roll >= 10:
            typewriter_effect("Well i guess you got lucky then, good job. we have a town meeting tomorrow, maybe you can learn something there. for now ")
            typewriter_effect("the Sheriff’s office is just infront opposite the Towne Hall you never made it to, the school is down the road to the east. You think to yourself, maybe you can go and investigate there since you have the missing kids list. and finally you hear shouting coming from the path to the west. Maybe you should investigate that? What will you do")
            mayorcheck = True
        elif player_roll <= 1:
            typewriter_effect("You're one of them aren't you! i know it!, the mayor plunges a knife into your throat thinking you are part of the cult, killing you.")
            dead()
        else:
            typewriter_effect("“Never mind, I wanna discuss sum’ urgent with ya. Now good?” You nod enthusiastically, hoping to shift the conversation away as soon as possible before focusing on the new conversation at hand. “It’s gotta do with th’ children ya see. We need ya help in returnin’  em to their families safe n sound while gettin to the bottom of who’s behind this and why. Can yer do that for me?” You agree, shaking hands and parting ways at once so the investigation can begin, contemplating where you can begin and what to do once there.")
            typewriter_effect("the Sheriff’s office is just infront opposite the Towne Hall you never made it to, the school is down the road to the east. You think to yourself, maybe you can go and investigate there since you have the missing kids list. and finally you hear shouting coming from the path to the west. Maybe you should investigate that? What will you do")
            mayorcheck = False
    
    elif mayortalk == True:
        typewriter_effect("Where will you go? Sheriff’s Office, The East Path or The West Path ")
    
    while True:
        choice = input("Enter your choice (Sheriff's Office / East Path / West Path): ").strip().lower()

        if choice == "sheriff's office":
            typewriter_effect("You decide to head towards the Sheriff's Office.")
            go_to_sheriffs_office()
            break  # Exit the loop after a valid choice is made
        elif choice == "east path":
            typewriter_effect("You decide to take the East Path.")
            go_to_east_path()
            break  # Exit the loop after a valid choice is made
        elif choice == "west path":
            typewriter_effect("You decide to take the West Path.")
            go_to_west_path()
            break  # Exit the loop after a valid choice is made
        else:
            typewriter_effect("Invalid choice. Please choose either Sheriff's Office, East Path, or West Path.")

def choice2split():
    global sheriffs_office
    global bakertalked
    global teachertalked
    
    typewriter_effect("You feel as though you have enough time to head to one of the places you didn't head to before.")
    
    while True:
        if teachertalked == True:
            choice = input("Enter your choice (Sheriff's Office / East Path): ").strip().lower()

            if choice == "sheriff's office":
                typewriter_effect("You decide to head towards the Sheriff's Office.")
                go_to_sheriffs_office2()
                break
            elif choice == "east path":
                typewriter_effect("You decide to take the East Path.")
                go_to_east_path2()
                break
            else:
                typewriter_effect("Invalid choice. Please choose either Sheriff's Office or East Path")

        elif bakertalked == True:
            choice = input("Enter your choice (Sheriff's Office / West Path): ").strip().lower()

            if choice == "sheriff's office":
                typewriter_effect("You decide to head towards the Sheriff's Office.")
                go_to_sheriffs_office2()
                break
            elif choice == "west path":
                typewriter_effect("You decide to take the West Path.")
                go_to_west_path2()
                break
            else:
                typewriter_effect("Invalid choice. Please choose either Sheriff's Office or West Path")

        elif sheriffs_office == True:
            choice = input("Enter your choice (East Path / West Path): ").strip().lower()

            if choice == "west path":
                typewriter_effect("You decide to head towards the West Path.")
                go_to_west_path2()
                break
            elif choice == "east path":
                typewriter_effect("You decide to take the East Path.")
                go_to_east_path2()
                break
            else:
                typewriter_effect("Invalid choice. Please choose either West Path or East Path")

def inn1():
    global mayortalk
    global bookinvestigate
    typewriter_effect("Reaching the end of your first, long day in Redspring; you walk towards the town’s Hotel, an unimpressive wooden affair in the eastern side of town.")
    typewriter_effect("The windows are few and far between, the front door creaks as you enter, and the face that looks at you from the front desk appears either honestly uninterested in your arrival, or smugly nonchalant in the face of what your arrival means.")
    typewriter_effect("The Innkeeper is a tall man, notably over 6 feet tall, with short, cropped hair and a light stubble. He wears a cream coloured thick sweater over a well-ironed shirt, tie, and black trousers; he appears to be reading the local newspaper - the Arkham Advertiser - as you approach.")
    typewriter_effect("“I know why you’re here, stranger.” The Innkeeper says, “Mayor already filled me in,”")
    typewriter_effect("You breathe a sigh, comfortable in the knowledge that you wouldn’t have to defend your purpose here to someone else.")
    typewriter_effect("“‘Course I think it’s a bad idea.”")
    typewriter_effect("Well, that didn’t last long…")
    typewriter_effect("“Your room’s upstairs, first door on your left.”")
    typewriter_effect("He holds out a key; not looking up from the paper.")

    if mayortalk == True:
        typewriter_effect("You feel as if you could press him for more information, but he may not like that. ")
        while True:
            choice = input("Enter 1 to press for more information or 2 to take the key: ")
            if choice == '1':
                typewriter_effect("[Press him for more info]")
                typewriter_effect("You decide to press this man for more information; unsatisfied with the simple notion of ‘it’s a bad idea’.")
                typewriter_effect("The innkeeper glances at you.")
                typewriter_effect("“Look, anyone with half a mind could tell you something strange is going on here.”")
                typewriter_effect("Kids going missing, uninterested Sheriff, weird symbols… strange doesn’t begin to cover it")
                typewriter_effect("“But from what I hear, you say you’re an expert in what’s going on. Which is funny, cause I’m pretty sure if I understood more than I do, I’d have left a long time ago.”")
                typewriter_effect("He puts the paper down and hands you a familiar bag of not nearly enough clothes.")
                typewriter_effect("“Forgive my scepticism, but the first thing I look for in an expert; is not to leave their bag in the mayor’s office.”")
                typewriter_effect("Ah. That’s rather embarrassing…")
                typewriter_effect("You decide to take the key and your bag upstairs.")
                break
            elif choice == '2':
                typewriter_effect("[Take the key and go upstairs]") # This line was missing parentheses
                typewriter_effect("“Hang on, got a present for you from the Mayor.”")
                typewriter_effect("Without taking his eyes off the paper, the Innkeeper reaches behind the desk and hands you a familiar looking bag containing not enough clothes.")
                typewriter_effect("“You can leave it in your room if you like, but if you take it out again; keep an eye on it.”")
                typewriter_effect("You decide to take the key and your bag upstairs.")
                break
            else:
                typewriter_effect("Invalid input. Please enter either '1' or '2'.")
    elif bookinvestigate == True:
        typewriter_effect("You feel as if you could press him for more information, but he may not like that. ")
        while True:
            choice = input("Enter 1 to press for more information or 2 to take the key: ")
            if choice == '1':
                typewriter_effect("You decide to press this man for more information; unsatisfied with the simple notion of ‘it’s a bad idea’.")
                typewriter_effect("The innkeeper glances at you")
                typewriter_effect("“Look, anyone with half a mind could tell you something strange is going on here.")
                typewriter_effect("Kids going missing, uninterested Sheriff, weird symbols… strange doesn’t begin to cover it.")
                typewriter_effect("“But from what I hear, you say you’re an expert in what’s going on. Which is funny, cause I’m pretty sure if I understood more than I do, I’d have left a long time ago.”")
                typewriter_effect("Confident in your expert knowledge that you don’t want to annoy this man for as long as you’re staying here; You grab the key, and take your possessions upstairs.")
                break
            elif choice == '2':
                typewriter_effect("[Take the key and go upstairs]") # This line was missing parentheses
                typewriter_effect("“If I were you, I’d be on the wagon that’s leaving here in the morning”")
                typewriter_effect("You look at him quizzically.")
                typewriter_effect("“Wagon leaves every morning for Arkham, good to keep in mind when things get… strange…”")
                typewriter_effect("Well convinced of the strangeness of both the situation, and the man opposite you; you collect your key and take your things and yourself upstairs.")
                break
            else:
                typewriter_effect("Invalid input. Please enter either '1' or '2'.")

    typewriter_effect("The room that greets you as you turn the handle of the first door on the left is quite pleasant, all things considered. The walls are covered with deep brown wooden panels, and there appears to be a small table next to the single bed. ")
    typewriter_effect("The electric lights are a comforting luxury you didn’t expect, though after a quick visit to the bathroom down the hall, the lack of a shower makes you miss your home near the university.")
    typewriter_effect("Well aware that this may be the calmest day you experience in Redspring, you quickly settle into the bed for as much sleep as your body will allow.")
    typewriter_effect("You fade off into a slumber...")
    time.sleep(2)
    nightmareseq1()

def nightmareseq1():
    typewriter_effect("In the middle of the night, you hear faint whispers around your room. The air is cold and stale and you can see bated breath lingering in the air. An eerie presence could be felt when a gush of wind blasted the windows open, the wind howling in the moonlit backdrop. A shadowy figure could be seen off in the distance before you jolted awake, unaware whether this was simply a nightmare or a tale of events yet to come…")
    day2intro()
def day2intro():
    time.sleep(2)
    typewriter_effect("The second day began with the shriek of a rooster at dawn and a gentle warmth entering the town. The sun beamed from above, illuminating the surrounding area with an orange glow of daylight serenity. You try to cast away the events of last night from your mind and proceed to get ready for the new day.")
    typewriter_effect("You leave the inn, ready to take what this dingy little town throws at you today. As you walk around, you greet any unfamiliar faces around town and make small talk along your walk to your next destination. You spot the mayor in the distance, reminiscing on yesterday’s conversation and how it ended.")
    if mayortalk == True:
        typewriter_effect("“Hi there, thank ya for meeting with me yesterday. I’m glad we got that conversation down so you can save em kids. Now run along n see what you can find. I’ll be waitin to hear from ya.")
        typewriter_effect("After that short yet sweet conversation, you make your way into town to follow up on your leads. You have an uneasy feeling about this case but you took it and now you must see it through til the end. You notice the town is livelier than usual and notice that there’s a meeting at the town hall, the lights are beaming and the hum of chatter and excitement fill the air. ")
        townehallinner()
    elif mayorcheck == True:
        typewriter_effect("“”You again kid? I’m glad I ran into ya. Make sure you get to lookin for them kids ya hear? I’ll see  ya later then.”")
        typewriter_effect("After that short yet sweet conversation, you make your way into town to follow up on your leads. You have an uneasy feeling about this case but you took it and now you must see it through til the end. You notice the town is livelier than usual and notice that there’s a meeting at the town hall, the lights are beaming and the hum of chatter and excitement fill the air.")
        townehallinner()
    elif mayorcheck == False:
        typewriter_effect("“Well, well, well, look who it is. I don’t trust ya very much but I’m stuck with ya so I’ll hafta deal with it. You better get to findin’  them kids before you find yerself at the bottom of a ditch, ya hear? No scram, get outta my sight. You got work to do, so dont come to the town meeting.")
        townhall_outer()

def townehallinner():
    global townehallinnerchek
    typewriter_effect("You follow the Mayor into the hall, a dozen of the townsfolk await you inside with bated breath, all seated around a wooden table.")
    typewriter_effect("A man in a black shirt and a white collar smiles warmly at you; and a rather portly looking man in a white suit that struggles to contain him strides up to you the moment you enter:")
    typewriter_effect("“Ah yes, the stranger; I’ve heard a lot about you.” The portly man says.")
    typewriter_effect("You’re pretty sure you haven’t heard a lot about you, so it’s odd that this man has.")
    typewriter_effect("“Earnest Olmstead, local socialite and philanthrope, pleased to make my acquaintance, I’m sure.” ")
    typewriter_effect("Oh good, the rich are here…")
    typewriter_effect("“If there’s anything about the town you need to know, I’m sure I could be of service.")
    typewriter_effect("Especially to a university academic such as yourself,” He chuckles as if he’s said something funny; you’re fairly convinced he’s never said anything funny in his life.")
    typewriter_effect("“Probably… the wrong audience for that one, eh?” Olmstead says.")
    typewriter_effect("“Now, now; settle down ev’rybody! Don’t crowd the guest,” the Mayor proclaims, saving everyone from this awkward conversation.")
    typewriter_effect("“We gots some problems, kids goin’ missin’, foul airs waftin’ through town, and nothin’ seems doing ‘bout it!”")
    typewriter_effect("The congregation gathered here harrumphs in agreement.")
    typewriter_effect("“Now the reason our guest is here, is to look into these missin’ kids and to try to find them; so chances are they might have questions for some of you, I trust that you’ll be as respectful with them, as you would with me.”")
    typewriter_effect("You begin to wonder exactly how respectful the townsfolk are with the Mayor, before your thoughts are cut off by an old, shrill, man’s voice.")
    typewriter_effect("“RESPECTFUL? OF WHAT?”")
    typewriter_effect("You see an older man than you ever thought possible stand up, and raise one leg onto the table.")
    typewriter_effect("He is wearing a Sheriff’s badge, you hope against all hope that he isn’t the Sheriff.")
    typewriter_effect("“SOME STRANGER COMIN’ INTO OUR TOWN AND TELLIN’ US THAT WE AIN’T DOIN RIGHT BY OUR KIDS?” The Sheriff continues.")
    typewriter_effect("“APOLOGIES TO OUR ‘ESTEEMED’ UNIVERSITY GUEST, BUT WE KNOW WHAT’S HAPP’NIN’ WITH THESE KIDS, THEY’S ALL RUNNIN’ OFF TO ARKHAM, TO CHASE STUPID DREAMS OF FORTUNE AND FAME!”")
    typewriter_effect("“Excuse me?” A woman interjects, you recognise her as the baker, Margaret Whateley.")
    typewriter_effect("“My Ezra is 8 years old, and you think he’s running off with some big city dreams? Are you three sandwiches short of a picnic, Sheriff?”")
    typewriter_effect("“THAT’S WHAT THESE KIDS DO NOWADAYS, THEY GET TO SIX AND THEY THINK THEY KNOW EVERYTHIN’; THEY SHOULDA’ DONE WHAT I DONE DID AND WAITED TIL THEY WERE SEVEN TO WORK IN THE HELIUM MINES!”")
    typewriter_effect("You’re fairly certain there’s no such thing, but it would explain the Sheriff’s voice and wild energy.")
    typewriter_effect("“Alright folks, I think it’s only fair we hear from someone else now,” the Mayor somewhat calms the situation.")
    typewriter_effect("“Maybe our Sheriff can continue later with his findin’s once he’s remembered the volume at which we speaks these meetin’s.”")
    typewriter_effect("“I think we’ve been afforded a good opportunity to learn what’s going on, we should take advantage of having an expert among us while we can.” a young woman notes.")
    typewriter_effect("“Thank you, miss Eleanor,” the Mayor replies.")
    typewriter_effect("“Well o’course she wants the stranger to run aroun’ makin’ false accusations, she’s prob’ly teachin’ those kids to run off to the city for some insane, foreign purposes!” The Sheriff blurts out, not quite quietly enough.”")
    typewriter_effect("'It’s all that readin’, it poisons the mind!'")
    typewriter_effect("“Well I think we’ve learned everything we need to know about the Sheriff’s opinion,” Eleanor calmly responds.")
    typewriter_effect("“Well you ain’t exactly local neither, are you girl?” The Sheriff spits out, menacingly “Who's to say you ain’t takin’ those kids yerself?”")
    typewriter_effect("Eleanor goes red in the face, as she tries to steady her breathing.")
    typewriter_effect("“Interestin’ how you don’t got a family o’ yer own, then all these kids go missin’, what’s a sheriff to think about that?”")
    typewriter_effect("Eleanor stands and quickly leaves, tears welling up in her eyes. The room is silent for a moment.")
    typewriter_effect("“I think…” the Mayor cautiously begins “that maybe we move onto what we might need from our guest, and how we feel we can help them, before anyone else is accused.”")
    typewriter_effect("The Sheriff grumbles and settles down.")
    typewriter_effect("In the following hour you are introduced again to Earnest Olmstead, whose family has been in this town since the revolution, and has owned a great deal of land around the town.")
    typewriter_effect("You hear from Father Raymond, an older man of slight frame; who seems pleasant enough, and welcomes you to confession and evening service at the Church, though appears to be somewhat uninformed when it comes to your current investigation.")
    typewriter_effect("A number of others speak up and tell you everything they think is important, though you begin to realise that for many of them, a town meeting is just where they share gossip about whose houses are painted strangely, and who ate meat on a Friday, even though God apparently doesn’t like that.")
    typewriter_effect("As the meeting packs up and people begin to leave, Margaret Whately walks up to you.")
    typewriter_effect("“She didn’t take him.”")
    typewriter_effect("You look at her, slightly confused.")
    typewriter_effect("""Miss Eleanor, my Ezra thought… thinks the world of her. I know she wouldn’t take him.""")
    typewriter_effect("Lots of people around here don’t like her cause they think she’s gonna ruin the town by making all the kids too smart so they move away, but she wants the best for those kids.”")
    typewriter_effect("You agree with her, but wonder how you’d be able to prove that.")
    typewriter_effect("“I don’t trust the Sheriff and the others to find my Ezra, but I think you might have a chance, if you’re everything the Mayor thinks you are.""")
    typewriter_effect("""You should come by the shop sometime, don’t know how much help I’ll be, but a friendly face has gotta be better than nothing.""")
    typewriter_effect("You’re pleased at the prospect of seeing a welcoming face, and her being so close to the investigation could provide some unique insight.")
    typewriter_effect("As you leave the town hall in the wake of the chaos that has just ensued, you take a deep breath and assess your options for the remainder of the day.")
    typewriter_effect("Eleanor walks off, as people begin to file out of the Town Hall, it appears that you have a few options available to you:")
    typewriter_effect("")
    typewriter_effect("1. Head to the schoolhouse")
    typewriter_effect("2. Visit the Baker")
    townehallinnerchek = True
    choice = input("Enter your choice (1/2): ")

    while True:
        if choice == "1":
            global teachertalked
            if teachertalked == True:
                teacher2()
            else:
                go_to_west_path()
            # link to teacher1
            break
        elif choice == "2":
            global bakertalked
            if bakertalked == True:
                bakershack()
            else:
                go_to_west_path()
            # link to baker1
            break
        else: 
            typewriter_effect("Invalid input, please try inputting 1 or 2.")

def townhall_outer():
    global townhallouterchek
    typewriter_effect("Well…")
    typewriter_effect("")
    typewriter_effect("It seems that the vast majority of the people that are worth speaking to are in the town meeting.")
    typewriter_effect("")
    typewriter_effect("That you were just uninvited from.")
    typewriter_effect("")
    typewriter_effect("What was it about first impressions that Professor van Buren was always telling you? If you could remember it you’d probably be in the town meeting right now.")
    typewriter_effect("")
    typewriter_effect("You spend a few minutes allowing thoughts to run around your head, until you are rudely interrupted by someone leaving the Town Hall in what seems to be a state of distress.")
    typewriter_effect("")
    typewriter_effect("The young woman - a Miss Eleanor Greene - takes a moment to straighten out her dress and looks over to you.")
    typewriter_effect("")
    typewriter_effect("“Well, at least there’s someone in this town who is smart enough to know not to go to a town meeting that’s just going to turn into a witch hunt.”")
    typewriter_effect("")
    typewriter_effect("You look at her sympathetically, “Honestly, I wasn’t invited; seems like I upset the Mayor” you say.")
    typewriter_effect("")
    typewriter_effect("“Well, I wouldn’t worry; he’s almost as unwelcome around here as we are. Only arrived here five-ish years ago” she replies.")
    typewriter_effect("")
    typewriter_effect("You shoot her a confused look.")
    typewriter_effect("")
    typewriter_effect("“What got you uninvited to the town meeting anyway?”")
    typewriter_effect("")
    typewriter_effect("You show her the book you found the day before.")
    typewriter_effect("")
    typewriter_effect("“Mind if I open it?” she inquires.")
    typewriter_effect("")
    typewriter_effect("You pull the book back, not entirely sure of her intentions; but sure that if she isn’t involved, she’s probably better off not knowing what’s in there.")
    typewriter_effect("")
    typewriter_effect("“Fair enough, suppose we don’t really know anything about each other, and that kind of trust takes time… I’d be the same if I thought that book was the key to everything…”")
    typewriter_effect("")
    typewriter_effect("She seems disappointed, but understands your tentativeness.")
    typewriter_effect("")
    typewriter_effect("“If you ever decide you’re willing to take a risk on trusting someone, I’ll be at the schoolhouse, there aren’t too many kids left, so lessons are a lot shorter.”")
    typewriter_effect("")
    typewriter_effect("Eleanor walks off, as people begin to file out of the Town Hall, it appears that you have a few options available to you:")
    typewriter_effect("")
    typewriter_effect("1. Head to the schoolhouse")
    typewriter_effect("2. Visit the Baker")
    townhallouterchek = True
    choice = input("Enter your choice (1/2): ")
    while True:
        if choice == "1":
            global teachertalked
            if teachertalked == True:
                teacher2()
            else:
                go_to_west_path4()
            # link to teacher1
            break
        elif choice == "2":
            global bakertalked
            if bakertalked == True:
                bakershack()
            else:
                go_to_east_path3()
            # link to baker1
            break
        else: 
            typewriter_effect("Invalid input, please try inputting 1 or 2.")

def teacher2():
    global passcheck
    global runeteachersafe
    global teacherdead
    typewriter_effect("You decide to check in on the teacher, Eleanor Greene; concerned that if you don’t, she may pursue a dangerous investigation of her own. ")
    typewriter_effect("You find her in the schoolhouse, furiously reading a large scroll of paper. Wondering what kind of literature could make someone so mad, you walk over and ask what she is reading.")
    typewriter_effect("“The paper you showed me before” she says, barely acknowledging your existence. “Let me see it again.”")
    typewriter_effect("Fully understanding her current mood - as well as the dangers of untreated papercuts - you hand over the rune you showed her before.")
    typewriter_effect("“I knew it, they’re everywhere. Look, it’s like an alphabet!”")
    typewriter_effect("She points you to the paper she is reading, it’s the Town Charter, your attention pans over the old script to a series of small drawings around the borders of the Charter, seemingly innocent designs at first around the outside of the text, quite pretty to look at in the style of whoever wrote this; but to your eye, very clearly sigils like you’ve found before.")
    typewriter_effect("“There appear to be eight different runes in total, but I’m unfamiliar with most of them; and nothing I can find would point to any kind of pronunciation, so I don’t think they’re used in any spoken language.”")
    choice = input("Would you like to try and investigate the rune and figure out what it is? yes/no ").strip().lower()
    if choice == "yes":
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            typewriter_effect("You stare at these glyphs and wonder, why would they be written down so freely here, and then kept as some form of secret when written on the folded paper?")
            typewriter_effect("You hold the runic paper in your hands and look down at the symbol in red ink.")
            typewriter_effect("You have an inkling.")
            typewriter_effect("You taste the ink.")
            typewriter_effect("Metallic, dry.")
            typewriter_effect("While you don’t make a habit of tasting ink, you are immediately aware that this is not it.")
            typewriter_effect("And whatever the purpose of these papers is, you know why they are secret.")
            typewriter_effect("They hold power, because they are written in blood.")
        elif roll == 1:
            typewriter_effect("You’ve read detective novels, you know what you’re doing.")
            typewriter_effect("You confidently lick the paper, and then swallow it.")
            typewriter_effect("Actually, it’s not going down")
            typewriter_effect("You’re choking, on the paper.")
            typewriter_effect("That you put in your mouth.")
            typewriter_effect("What are you? Five?")
            typewriter_effect("You choke, and die.")
            dead()

        else:
            typewriter_effect("You glare down at the runes before you, trying to divine their meaning. A headache begins to form and the images swim before your eyes. Whatever their purpose is or was, there’s no way you’re figuring it out now. ")
            typewriter_effect("The Teacher looks at you with her trademark patented disappointment.") 
            typewriter_effect("I’ll just have to figure it out on my own.” She says, brushing past you as you clutch at your head.")
            typewriter_effect("Maybe you should go lie down.")
    else: 
        typewriter_effect("You think that you wont figure out what the rune is and that you don't have time to mess around and stare at a piece of paper for a lengthy amount of time and move on")

    
    typewriter_effect("As you ponder the information you have been presented with, Eleanor pulls you over to a map of the town on the wall; she has made markings on it, 5 (x)s on different parts of the map.")
    typewriter_effect("“The School, The Church, The Town Hall, The Olmstead Manor, Providence Hill.” she says.")
    typewriter_effect("“Each of these buildings has its own copy of the Town Charter, apart from Providence Hill.”")
    typewriter_effect("So why would she mark it?")
    typewriter_effect("“I marked it because it’s where the Charter was originally signed, back in 1752.”")
    typewriter_effect("Oh… fair enough then.")
    typewriter_effect("“My theory is that whatever is going on, has something to do with that Hill.”")
    typewriter_effect("She begins to leave.")
    typewriter_effect("“Are you coming?”")
    typewriter_effect("You follow her along the path that leads northward out of the town, towards an old forest that completely surrounds an open-topped hill. As you climb up the hill’s sides you begin to notice large stones on top of it, stacked in some seemingly practised or religious manner.")
    typewriter_effect("“It’s a henge, possibly used by the original settlers as a landmark” Eleanor notes.")
    typewriter_effect("“A kind of… stone… henge?” you quip.")
    typewriter_effect("“All henges are made of stone, it’d be like calling it a ‘stone-stone-structure’.” she flatly responds.")
    typewriter_effect("You take a moment to question how fun she is, while she takes a moment to question your employment at a university")
    typewriter_effect("As you arrive within the stone circle, you each take a look around, and note markings on each stone.")
    typewriter_effect("Eight stones.")
    typewriter_effect("Eight symbols")
    typewriter_effect("Each inert… for now")
    typewriter_effect("You remain lost in thought for a few seconds more before hearing a quiet conversation behind you. Someone is coming, and both of you could be in danger.")
    typewriter_effect("You feel like you have to do something.")
    while True:
        typewriter_effect("1. Throw rocks at it!")
        typewriter_effect("2. HIDE!")
        typewriter_effect("3. Talk your way out of it")
        choice2 = input("What will you do? ")

        if choice2 == "1":
            typewriter_effect("You decide to throw rocks at your problems")
            typewriter_effect("Rolling a D20")
            roll = rollcheck()
            if roll >= 12:
                passcheck = True
                typewriter_effect("You summon all the strength you can muster and push the nearest rock down the hill and towards the voices. You hear shouts as you and Eleanor run down the hill in the opposite direction. Bad news, they know someone was here. Good news, they don’t know for certain that it was you.")
                break
            elif roll == 1:
                typewriter_effect("Oh dear a nat 1")
                typewriter_effect("You push the rock, and it rolls down the hill towards the voices. YES. Then you hear a cry as Father Raymond is crushed by the rock. SIGNIFICANTLY LESS YES. The Sheriff turns to the top of the hill to see you and Eleanor looking down, stunned. AH. He pulls out his pistol and fires at Eleanor. NO. As she falls to the floor, the Sheriff turns his pistol on you. SIGNIFICANTLY MORE N-")
                dead()
            else:
                typewriter_effect("You summon all the strength you can muster… which turns out to not be a lot, you look very odd as the two figures reach the top of the hill. Bad news, at best they think you’re weird. Worse news, they might think you’re trying to destroy a town monument.")
                break
        elif choice2 =="2":
            typewriter_effect("You decide to hide")
            typewriter_effect("Rolling a D20")
            roll = rollcheck()
            if roll >= 12:
                passcheck = True
                typewriter_effect("Light as a cat on your feet, you spring to attention, grab Eleanor’s arm, and hide behind one of the stones. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
                typewriter_effect("“That stranger’ll bring nothing but trouble.” you hear the Sheriff say.")
                typewriter_effect("“Ah my friend, remember; judge not, for all will be judged by our lord when he returns to us. It is not our place to make assumptions of others, rather to welcome them and hope they reciprocate.” Father Raymond replies.")
                typewriter_effect("“Well… I suppose… I’m still not happy about it. What if they show up and ruin everything?”  the Sheriff utters.")
                typewriter_effect("The Priest replies “I think it’s high time you stopped doubting his will, and placed your faith in him. Sit with me, pray.”")
                typewriter_effect("You and Eleanor remain still for a moment, until you are confident that the two are focused enough on silent prayer that you can go.")
                typewriter_effect("The two of you slink away silently")
                break
            elif roll == 1:
                typewriter_effect("Oh dear a nat 1")
                typewriter_effect("Channelling agility you never knew you possessed, you leap to the top of the tallest rock. You feel the sun shine on your face as you are imbued with the power of the Gods, and seeing these cultists reach the hill, you smite them down. You then use your newly acquired Godly powers to free the children, cure disease, fix the economy, and you and Eleanor marry, living a wonderful life teaching the children at the schoolhouse")
                typewriter_effect("Of course, none of this ACTUALLY happens. You shattered your skull trying to backflip over a rock and are currently hallucinating in your final moments.")
                typewriter_effect("Still, a nice image.")
                dead()
                break
            else:
                typewriter_effect("Light as a brick on your feet, you try to push Eleanor behind a rock and instead clatter into her, and then into the rock you attempted to hide behind. You are now dazed, confused, and being looked upon by an equally confused Sheriff and Father Raymond.")
                break
        elif choice2 =="3":
            typewriter_effect("You decide to talk and convince them you're no trouble")
            typewriter_effect("Rolling a D20")
            roll = rollcheck()
            if roll >= 12:
             passcheck = True
             typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
             typewriter_effect("“That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
             typewriter_effect("You greet them both warmly, expressing your academic interest in anthropological architecture, specifically potential historical landmarks and worship sites. The Sheriff looks embarrassed as you treat him with a kindness far greater than he has afforded you. Father Raymond is especially impressed by your knowledge that a henge is made of stone, so calling it a ‘stonehenge’ is equivalent to calling it a ‘stone-stone-structure’, though Eleanor seems ever so slightly miffed at your plagiarism.")
             typewriter_effect("After a rather pleasant afternoon speaking with these two, you and Eleanor make your excuses to leave, and head back to the schoolhouse, fairly convinced that no one is suspicious of you.")
            break
        elif roll == 1:
             typewriter_effect("Oh dear a nat 1")
             typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
             typewriter_effect("“That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
             typewriter_effect("You look down at them confidently, you are prepared for the greatest bluff in the history of mankind.")
             typewriter_effect("“FOOLISH EVILDOERS, I KNOW OF YOUR PLANS. I WILL STOP YOU, FOR WHAT YOU ARE NOT YET AWARE OF IS THAT I-” ")
             typewriter_effect("You are shot mid sentence")
             typewriter_effect("As the Sheriff shoots Eleanor, you begin to wonder if your bluff may not have been the best choice. ")
             typewriter_effect("Ah well, at least it doesn’t matter now.")
             dead()
             break
        else:
             typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you")
             typewriter_effect("That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
             typewriter_effect("“What are you doing here?” Father Raymond asks.")
             typewriter_effect("“What are you doing here?” You parrot back")
             typewriter_effect("“I asked you first.” Raymond replies.")
             typewriter_effect("Damn… he makes a good point; he has won this war of words")
             break
    else:
         typewriter_effect("Invalid choice. Please select 1, 2, or 3.")
 
    if passcheck == True:
        runeteachersafe = True
        teacherdead = False
        typewriter_effect("You and Eleanor rush back to the school, confident that what you have learned will be key in solving the mystery of this town.")
        typewriter_effect("You inform her of the carts leaving town each morning, and suggest that if things take a turn for the worst she should probably be on one of them.")
        typewriter_effect("“You’re right, but at least I can provide another helping hand before I leave,” she says.")
        typewriter_effect("She hands you a piece of paper, covered in dirt, but neatly folded, perfectly preserved, and within, another rune written in blood.")
        print("  _______")
        print(" |       |")
        print(" |_______|")
        print("     |   ")
        print("   __|  * ")
        inn2()
    elif passcheck == False:
        teacherdead = True
        runeteachersafe = False
        typewriter_effect("You are looked upon with great confusion by the Sheriff, Father Raymond, and Eleanor - who it appears has lost some respect for you - as you try to recover from your frankly awkward decision.")
        typewriter_effect("“I think it’s best that the two of you leave,” the sheriff say")
        typewriter_effect("You and Eleanor agree and awkwardly stumble away, having not only been caught by the two town authority figures who already didn’t like you; but also having likely aroused suspicion in your motives.")
        typewriter_effect("As you arrive back at the schoolhouse, Eleanor shuts the doors to the school in your face, and you are left in the rain. Cold, wet, and slightly stupid.")
        inn2()

def teacher3():
    global passcheck
    global runeteachersafe
    global teacherdead
    typewriter_effect("You decide to check in on the teacher, Eleanor Greene; concerned that if you don’t, she may pursue a dangerous investigation of her own. ")
    typewriter_effect("You find her in the schoolhouse, furiously reading a large scroll of paper. Wondering what kind of literature could make someone so mad, you walk over and ask what she is reading.")
    typewriter_effect("“The paper you showed me before” she says, barely acknowledging your existence. “Let me see it again.”")
    typewriter_effect("Fully understanding her current mood - as well as the dangers of untreated papercuts - you hand over the rune you showed her before.")
    typewriter_effect("“I knew it, they’re everywhere. Look, it’s like an alphabet!”")
    typewriter_effect("She points you to the paper she is reading, it’s the Town Charter, your attention pans over the old script to a series of small drawings around the borders of the Charter, seemingly innocent designs at first around the outside of the text, quite pretty to look at in the style of whoever wrote this; but to your eye, very clearly sigils like you’ve found before.")
    typewriter_effect("“There appear to be eight different runes in total, but I’m unfamiliar with most of them; and nothing I can find would point to any kind of pronunciation, so I don’t think they’re used in any spoken language.”")
    choice = input("Would you like to try and investigate the rune and figure out what it is? yes/no ").strip().lower()
    if choice == "yes":
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            typewriter_effect("You stare at these glyphs and wonder, why would they be written down so freely here, and then kept as some form of secret when written on the folded paper?")
            typewriter_effect("You hold the runic paper in your hands and look down at the symbol in red ink.")
            typewriter_effect("You have an inkling.")
            typewriter_effect("You taste the ink.")
            typewriter_effect("Metallic, dry.")
            typewriter_effect("While you don’t make a habit of tasting ink, you are immediately aware that this is not it.")
            typewriter_effect("And whatever the purpose of these papers is, you know why they are secret.")
            typewriter_effect("They hold power, because they are written in blood.")
        elif roll == 1:
            typewriter_effect("You’ve read detective novels, you know what you’re doing.")
            typewriter_effect("You confidently lick the paper, and then swallow it.")
            typewriter_effect("Actually, it’s not going down")
            typewriter_effect("You’re choking, on the paper.")
            typewriter_effect("That you put in your mouth.")
            typewriter_effect("What are you? Five?")
            typewriter_effect("You choke, and die.")
            dead()

        else:
            typewriter_effect("You glare down at the runes before you, trying to divine their meaning. A headache begins to form and the images swim before your eyes. Whatever their purpose is or was, there’s no way you’re figuring it out now. ")
            typewriter_effect("The Teacher looks at you with her trademark patented disappointment.") 
            typewriter_effect("I’ll just have to figure it out on my own.” She says, brushing past you as you clutch at your head.")
            typewriter_effect("Maybe you should go lie down.")
    else: 
        typewriter_effect("You think that you wont figure out what the rune is and that you don't have time to mess around and stare at a piece of paper for a lengthy amount of time and move on")

    
    typewriter_effect("As you ponder the information you have been presented with, Eleanor pulls you over to a map of the town on the wall; she has made markings on it, 5 (x)s on different parts of the map.")
    typewriter_effect("“The School, The Church, The Town Hall, The Olmstead Manor, Providence Hill.” she says.")
    typewriter_effect("“Each of these buildings has its own copy of the Town Charter, apart from Providence Hill.”")
    typewriter_effect("So why would she mark it?")
    typewriter_effect("“I marked it because it’s where the Charter was originally signed, back in 1752.”")
    typewriter_effect("Oh… fair enough then.")
    typewriter_effect("“My theory is that whatever is going on, has something to do with that Hill.”")
    typewriter_effect("She begins to leave.")
    typewriter_effect("“Are you coming?”")
    typewriter_effect("You follow her along the path that leads northward out of the town, towards an old forest that completely surrounds an open-topped hill. As you climb up the hill’s sides you begin to notice large stones on top of it, stacked in some seemingly practised or religious manner.")
    typewriter_effect("“It’s a henge, possibly used by the original settlers as a landmark” Eleanor notes.")
    typewriter_effect("“A kind of… stone… henge?” you quip.")
    typewriter_effect("“All henges are made of stone, it’d be like calling it a ‘stone-stone-structure’.” she flatly responds.")
    typewriter_effect("You take a moment to question how fun she is, while she takes a moment to question your employment at a university")
    typewriter_effect("As you arrive within the stone circle, you each take a look around, and note markings on each stone.")
    typewriter_effect("Eight stones.")
    typewriter_effect("Eight symbols")
    typewriter_effect("Each inert… for now")
    typewriter_effect("You remain lost in thought for a few seconds more before hearing a quiet conversation behind you. Someone is coming, and both of you could be in danger.")
    typewriter_effect("You feel like you have to do something.")
    typewriter_effect("1. Throw rocks at it!")
    typewriter_effect("2. HIDE!")
    typewriter_effect("3. Talk your way out of it")
    choice2 = input("What will you do?")
    if choice2 == "1":
        typewriter_effect("You decide to throw rocks at your problems")
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            passcheck = True
            typewriter_effect("You summon all the strength you can muster and push the nearest rock down the hill and towards the voices. You hear shouts as you and Eleanor run down the hill in the opposite direction. Bad news, they know someone was here. Good news, they don’t know for certain that it was you.")
        elif roll == 1:
            typewriter_effect("Oh dear a nat 1")
            typewriter_effect("You push the rock, and it rolls down the hill towards the voices. YES. Then you hear a cry as Father Raymond is crushed by the rock. SIGNIFICANTLY LESS YES. The Sheriff turns to the top of the hill to see you and Eleanor looking down, stunned. AH. He pulls out his pistol and fires at Eleanor. NO. As she falls to the floor, the Sheriff turns his pistol on you. SIGNIFICANTLY MORE N-")
            dead()
        else:
            typewriter_effect("You summon all the strength you can muster… which turns out to not be a lot, you look very odd as the two figures reach the top of the hill. Bad news, at best they think you’re weird. Worse news, they might think you’re trying to destroy a town monument.")
    elif choice2 =="2":
        typewriter_effect("You decide to hide")
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            passcheck = True
            typewriter_effect("Light as a cat on your feet, you spring to attention, grab Eleanor’s arm, and hide behind one of the stones. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
            typewriter_effect("“That stranger’ll bring nothing but trouble.” you hear the Sheriff say.")
            typewriter_effect("“Ah my friend, remember; judge not, for all will be judged by our lord when he returns to us. It is not our place to make assumptions of others, rather to welcome them and hope they reciprocate.” Father Raymond replies.")
            typewriter_effect("“Well… I suppose… I’m still not happy about it. What if they show up and ruin everything?”  the Sheriff utters.")
            typewriter_effect("The Priest replies “I think it’s high time you stopped doubting his will, and placed your faith in him. Sit with me, pray.”")
            typewriter_effect("You and Eleanor remain still for a moment, until you are confident that the two are focused enough on silent prayer that you can go.")
            typewriter_effect("The two of you slink away silently")
        elif roll == 1:
            typewriter_effect("Oh dear a nat 1")
            typewriter_effect("Channelling agility you never knew you possessed, you leap to the top of the tallest rock. You feel the sun shine on your face as you are imbued with the power of the Gods, and seeing these cultists reach the hill, you smite them down. You then use your newly acquired Godly powers to free the children, cure disease, fix the economy, and you and Eleanor marry, living a wonderful life teaching the children at the schoolhouse")
            typewriter_effect("Of course, none of this ACTUALLY happens. You shattered your skull trying to backflip over a rock and are currently hallucinating in your final moments.")
            typewriter_effect("Still, a nice image.")
            dead()
        else:
            typewriter_effect("Light as a brick on your feet, you try to push Eleanor behind a rock and instead clatter into her, and then into the rock you attempted to hide behind. You are now dazed, confused, and being looked upon by an equally confused Sheriff and Father Raymond.")
    elif choice2 =="3":
        typewriter_effect("You decide to talk and convince them you're no trouble")
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            passcheck = True
            typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
            typewriter_effect("“That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
            typewriter_effect("You greet them both warmly, expressing your academic interest in anthropological architecture, specifically potential historical landmarks and worship sites. The Sheriff looks embarrassed as you treat him with a kindness far greater than he has afforded you. Father Raymond is especially impressed by your knowledge that a henge is made of stone, so calling it a ‘stonehenge’ is equivalent to calling it a ‘stone-stone-structure’, though Eleanor seems ever so slightly miffed at your plagiarism.")
            typewriter_effect("After a rather pleasant afternoon speaking with these two, you and Eleanor make your excuses to leave, and head back to the schoolhouse, fairly convinced that no one is suspicious of you.")
        elif roll == 1:
            typewriter_effect("Oh dear a nat 1")
            typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
            typewriter_effect("“That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
            typewriter_effect("You look down at them confidently, you are prepared for the greatest bluff in the history of mankind.")
            typewriter_effect("“FOOLISH EVILDOERS, I KNOW OF YOUR PLANS. I WILL STOP YOU, FOR WHAT YOU ARE NOT YET AWARE OF IS THAT I-” ")
            typewriter_effect("You are shot mid sentence")
            typewriter_effect("As the Sheriff shoots Eleanor, you begin to wonder if your bluff may not have been the best choice. ")
            typewriter_effect("Ah well, at least it doesn’t matter now.")
            dead()
        else:
            typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you")
            typewriter_effect("That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
            typewriter_effect("“What are you doing here?” Father Raymond asks.")
            typewriter_effect("“What are you doing here?” You parrot back")
            typewriter_effect("“I asked you first.” Raymond replies.")
            typewriter_effect("Damn… he makes a good point; he has won this war of words")
       
    if passcheck == True:
        runeteachersafe = True
        typewriter_effect("You and Eleanor rush back to the school, confident that what you have learned will be key in solving the mystery of this town.")
        typewriter_effect("You inform her of the carts leaving town each morning, and suggest that if things take a turn for the worst she should probably be on one of them.")
        typewriter_effect("“You’re right, but at least I can provide another helping hand before I leave,” she says.")
        typewriter_effect("She hands you a piece of paper, covered in dirt, but neatly folded, perfectly preserved, and within, another rune written in blood.")
        print("  _______")
        print(" |       |")
        print(" |_______|")
        print("     |   ")
        print("   __|  * ")
        inn2()
    elif passcheck == False:
        teacherdead = False
        runeteachersafe = False
        typewriter_effect("You are looked upon with great confusion by the Sheriff, Father Raymond, and Eleanor - who it appears has lost some respect for you - as you try to recover from your frankly awkward decision.")
        typewriter_effect("“I think it’s best that the two of you leave,” the sheriff say")
        typewriter_effect("You and Eleanor agree and awkwardly stumble away, having not only been caught by the two town authority figures who already didn’t like you; but also having likely aroused suspicion in your motives.")
        typewriter_effect("As you arrive back at the schoolhouse, Eleanor shuts the doors to the school in your face, and you are left in the rain. Cold, wet, and slightly stupid.")
        choice3split()

def teacher4():
    global passcheck
    global runeteachersafe
    global teacherdead
    typewriter_effect("You decide to check in on the teacher, Eleanor Greene; concerned that if you don’t, she may pursue a dangerous investigation of her own. ")
    typewriter_effect("You find her in the schoolhouse, furiously reading a large scroll of paper. Wondering what kind of literature could make someone so mad, you walk over and ask what she is reading.")
    typewriter_effect("“The paper you showed me before” she says, barely acknowledging your existence. “Let me see it again.”")
    typewriter_effect("Fully understanding her current mood - as well as the dangers of untreated papercuts - you hand over the rune you showed her before.")
    typewriter_effect("“I knew it, they’re everywhere. Look, it’s like an alphabet!”")
    typewriter_effect("She points you to the paper she is reading, it’s the Town Charter, your attention pans over the old script to a series of small drawings around the borders of the Charter, seemingly innocent designs at first around the outside of the text, quite pretty to look at in the style of whoever wrote this; but to your eye, very clearly sigils like you’ve found before.")
    typewriter_effect("“There appear to be eight different runes in total, but I’m unfamiliar with most of them; and nothing I can find would point to any kind of pronunciation, so I don’t think they’re used in any spoken language.”")
    choice = input("Would you like to try and investigate the rune and figure out what it is? yes/no ").strip().lower()
    if choice == "yes":
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            typewriter_effect("You stare at these glyphs and wonder, why would they be written down so freely here, and then kept as some form of secret when written on the folded paper?")
            typewriter_effect("You hold the runic paper in your hands and look down at the symbol in red ink.")
            typewriter_effect("You have an inkling.")
            typewriter_effect("You taste the ink.")
            typewriter_effect("Metallic, dry.")
            typewriter_effect("While you don’t make a habit of tasting ink, you are immediately aware that this is not it.")
            typewriter_effect("And whatever the purpose of these papers is, you know why they are secret.")
            typewriter_effect("They hold power, because they are written in blood.")
        elif roll == 1:
            typewriter_effect("You’ve read detective novels, you know what you’re doing.")
            typewriter_effect("You confidently lick the paper, and then swallow it.")
            typewriter_effect("Actually, it’s not going down")
            typewriter_effect("You’re choking, on the paper.")
            typewriter_effect("That you put in your mouth.")
            typewriter_effect("What are you? Five?")
            typewriter_effect("You choke, and die.")
            dead()

        else:
            typewriter_effect("You glare down at the runes before you, trying to divine their meaning. A headache begins to form and the images swim before your eyes. Whatever their purpose is or was, there’s no way you’re figuring it out now. ")
            typewriter_effect("The Teacher looks at you with her trademark patented disappointment.") 
            typewriter_effect("I’ll just have to figure it out on my own.” She says, brushing past you as you clutch at your head.")
            typewriter_effect("Maybe you should go lie down.")
    else: 
        typewriter_effect("You think that you wont figure out what the rune is and that you don't have time to mess around and stare at a piece of paper for a lengthy amount of time and move on")

    
    typewriter_effect("As you ponder the information you have been presented with, Eleanor pulls you over to a map of the town on the wall; she has made markings on it, 5 (x)s on different parts of the map.")
    typewriter_effect("“The School, The Church, The Town Hall, The Olmstead Manor, Providence Hill.” she says.")
    typewriter_effect("“Each of these buildings has its own copy of the Town Charter, apart from Providence Hill.”")
    typewriter_effect("So why would she mark it?")
    typewriter_effect("“I marked it because it’s where the Charter was originally signed, back in 1752.”")
    typewriter_effect("Oh… fair enough then.")
    typewriter_effect("“My theory is that whatever is going on, has something to do with that Hill.”")
    typewriter_effect("She begins to leave.")
    typewriter_effect("“Are you coming?”")
    typewriter_effect("You follow her along the path that leads northward out of the town, towards an old forest that completely surrounds an open-topped hill. As you climb up the hill’s sides you begin to notice large stones on top of it, stacked in some seemingly practised or religious manner.")
    typewriter_effect("“It’s a henge, possibly used by the original settlers as a landmark” Eleanor notes.")
    typewriter_effect("“A kind of… stone… henge?” you quip.")
    typewriter_effect("“All henges are made of stone, it’d be like calling it a ‘stone-stone-structure’.” she flatly responds.")
    typewriter_effect("You take a moment to question how fun she is, while she takes a moment to question your employment at a university")
    typewriter_effect("As you arrive within the stone circle, you each take a look around, and note markings on each stone.")
    typewriter_effect("Eight stones.")
    typewriter_effect("Eight symbols")
    typewriter_effect("Each inert… for now")
    typewriter_effect("You remain lost in thought for a few seconds more before hearing a quiet conversation behind you. Someone is coming, and both of you could be in danger.")
    typewriter_effect("You feel like you have to do something.")
    typewriter_effect("1. Throw rocks at it!")
    typewriter_effect("2. HIDE!")
    typewriter_effect("3. Talk your way out of it")
    choice2 = input("What will you do?")
    if choice2 == "1":
        typewriter_effect("You decide to throw rocks at your problems")
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            passcheck = True
            typewriter_effect("You summon all the strength you can muster and push the nearest rock down the hill and towards the voices. You hear shouts as you and Eleanor run down the hill in the opposite direction. Bad news, they know someone was here. Good news, they don’t know for certain that it was you.")
        elif roll == 1:
            typewriter_effect("Oh dear a nat 1")
            typewriter_effect("You push the rock, and it rolls down the hill towards the voices. YES. Then you hear a cry as Father Raymond is crushed by the rock. SIGNIFICANTLY LESS YES. The Sheriff turns to the top of the hill to see you and Eleanor looking down, stunned. AH. He pulls out his pistol and fires at Eleanor. NO. As she falls to the floor, the Sheriff turns his pistol on you. SIGNIFICANTLY MORE N-")
            dead()
        else:
            typewriter_effect("You summon all the strength you can muster… which turns out to not be a lot, you look very odd as the two figures reach the top of the hill. Bad news, at best they think you’re weird. Worse news, they might think you’re trying to destroy a town monument.")
    elif choice2 =="2":
        typewriter_effect("You decide to hide")
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            passcheck = True
            typewriter_effect("Light as a cat on your feet, you spring to attention, grab Eleanor’s arm, and hide behind one of the stones. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
            typewriter_effect("“That stranger’ll bring nothing but trouble.” you hear the Sheriff say.")
            typewriter_effect("“Ah my friend, remember; judge not, for all will be judged by our lord when he returns to us. It is not our place to make assumptions of others, rather to welcome them and hope they reciprocate.” Father Raymond replies.")
            typewriter_effect("“Well… I suppose… I’m still not happy about it. What if they show up and ruin everything?”  the Sheriff utters.")
            typewriter_effect("The Priest replies “I think it’s high time you stopped doubting his will, and placed your faith in him. Sit with me, pray.”")
            typewriter_effect("You and Eleanor remain still for a moment, until you are confident that the two are focused enough on silent prayer that you can go.")
            typewriter_effect("The two of you slink away silently")
        elif roll == 1:
            typewriter_effect("Oh dear a nat 1")
            typewriter_effect("Channelling agility you never knew you possessed, you leap to the top of the tallest rock. You feel the sun shine on your face as you are imbued with the power of the Gods, and seeing these cultists reach the hill, you smite them down. You then use your newly acquired Godly powers to free the children, cure disease, fix the economy, and you and Eleanor marry, living a wonderful life teaching the children at the schoolhouse")
            typewriter_effect("Of course, none of this ACTUALLY happens. You shattered your skull trying to backflip over a rock and are currently hallucinating in your final moments.")
            typewriter_effect("Still, a nice image.")
            dead()
        else:
            typewriter_effect("Light as a brick on your feet, you try to push Eleanor behind a rock and instead clatter into her, and then into the rock you attempted to hide behind. You are now dazed, confused, and being looked upon by an equally confused Sheriff and Father Raymond.")
    elif choice2 =="3":
        typewriter_effect("You decide to talk and convince them you're no trouble")
        typewriter_effect("Rolling a D20")
        roll = rollcheck()
        if roll >= 12:
            passcheck = True
            typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
            typewriter_effect("“That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
            typewriter_effect("You greet them both warmly, expressing your academic interest in anthropological architecture, specifically potential historical landmarks and worship sites. The Sheriff looks embarrassed as you treat him with a kindness far greater than he has afforded you. Father Raymond is especially impressed by your knowledge that a henge is made of stone, so calling it a ‘stonehenge’ is equivalent to calling it a ‘stone-stone-structure’, though Eleanor seems ever so slightly miffed at your plagiarism.")
            typewriter_effect("After a rather pleasant afternoon speaking with these two, you and Eleanor make your excuses to leave, and head back to the schoolhouse, fairly convinced that no one is suspicious of you.")
        elif roll == 1:
            typewriter_effect("Oh dear a nat 1")
            typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you.")
            typewriter_effect("“That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
            typewriter_effect("You look down at them confidently, you are prepared for the greatest bluff in the history of mankind.")
            typewriter_effect("“FOOLISH EVILDOERS, I KNOW OF YOUR PLANS. I WILL STOP YOU, FOR WHAT YOU ARE NOT YET AWARE OF IS THAT I-” ")
            typewriter_effect("You are shot mid sentence")
            typewriter_effect("As the Sheriff shoots Eleanor, you begin to wonder if your bluff may not have been the best choice. ")
            typewriter_effect("Ah well, at least it doesn’t matter now.")
            dead()
        else:
            typewriter_effect("You stand calmly, waiting for the two individuals to arrive. As you wait you hear the voices of Father Raymond and the Sheriff, each talking about you")
            typewriter_effect("That stranger’ll bring nothing but troub-.” the Sheriff stops as he sees you.")
            typewriter_effect("“What are you doing here?” Father Raymond asks.")
            typewriter_effect("“What are you doing here?” You parrot back")
            typewriter_effect("“I asked you first.” Raymond replies.")
            typewriter_effect("Damn… he makes a good point; he has won this war of words")
       
    if passcheck == True:
        runeteachersafe = True
        typewriter_effect("You and Eleanor rush back to the school, confident that what you have learned will be key in solving the mystery of this town.")
        typewriter_effect("You inform her of the carts leaving town each morning, and suggest that if things take a turn for the worst she should probably be on one of them.")
        typewriter_effect("“You’re right, but at least I can provide another helping hand before I leave,” she says.")
        typewriter_effect("She hands you a piece of paper, covered in dirt, but neatly folded, perfectly preserved, and within, another rune written in blood.")
        print("  _______")
        print(" |       |")
        print(" |_______|")
        print("     |   ")
        print("   __|  * ")
        inn3()
    elif passcheck == False:
        runeteachersafe = False
        teacherdead = True
        typewriter_effect("You are looked upon with great confusion by the Sheriff, Father Raymond, and Eleanor - who it appears has lost some respect for you - as you try to recover from your frankly awkward decision.")
        typewriter_effect("“I think it’s best that the two of you leave,” the sheriff say")
        typewriter_effect("You and Eleanor agree and awkwardly stumble away, having not only been caught by the two town authority figures who already didn’t like you; but also having likely aroused suspicion in your motives.")
        typewriter_effect("As you arrive back at the schoolhouse, Eleanor shuts the doors to the school in your face, and you are left in the rain. Cold, wet, and slightly stupid.")
        inn3()

def bakershack():
    global townehallinnerchek
    global townhallouterchek
    global bakercheck
    global runebakersafe
    global bakerdead
    if townhallouterchek == True:
        typewriter_effect("You quickly catch up to the Baker as she charges off into the town.")
        typewriter_effect("She begins to speak as if to ward off your attempts of stopping her but you cut her off, offering your assistance in the search. ")
        typewriter_effect("Her eyes gleam wetly for a moment before she nods curtly and begins marching determinedly towards the nearest neighbour, you following after.")
    elif townehallinnerchek == True:
        typewriter_effect("The next hours are spent fruitlessly searching from building to building, asking all who you come across if they have seen the child but to no luck.")
        typewriter_effect("As the evening wanes, you reach the edge of the tree line and spot a run-down shack.")
        typewriter_effect("You gesture at the building and ask if it’s possible the child could be hiding within.")
        typewriter_effect("She says that it’s been abandoned for as long as anyone could remember but you could try.")
        typewriter_effect("You approach the shack carefully, dodging broken nails and floorboards as you mount the porch and try the door.")
        typewriter_effect("It creaks open, permitting the stench of mildew, damp, mould, and the great unwashed.")
        typewriter_effect("The floor has clearly been used in the past as a squatting ground for the local unhoused population, spotting the random bloodstains and empty bottles that litter the area.")
        typewriter_effect("As one particularly loud board gives a permissive squeak, you suddenly notice a whimpering sound begin from across the room, behind the only door in the shack.")
        typewriter_effect("Margaret calls out to the noise and it quickly turns into a child’s breathless begging.")
        typewriter_effect("“EZRA!” Margaret cries, “That’s him!”")
        typewriter_effect("You both charge over to the door only to find it locked up tight.")
        typewriter_effect("After trying the handle a few times, frustration takes over as Margaret slams a fist helplessly against the door and the child’s pleading twists into screams of agony as some sort of glyph begins glowing beneath her hand.")
        typewriter_effect("There is a desperate smell of burning.")
        typewriter_effect("Burning flesh.")
        while True:
            choice = input("What will you do? 1. Break open the door. 2. Try to pick the lock. 3. Try to find the key.  ")
            time.sleep(1)
            player_roll = rollcheck()
            if choice == "1" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You yell for the Baker to move and take a running shoulder to the door.")
                typewriter_effect("The wood breaks inward but remains intact.")
                typewriter_effect("You slam it again and finally smash through, splinters piercing into your flesh.")
                
            elif choice == "1" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You take a running shoulder into the door… but it doesn’t budge.")
                typewriter_effect("Your shoulder screams in pain, dislocated?")
                typewriter_effect("In desperation, you start kicking the door below the lock, again and again.")
                typewriter_effect("The Baker joins your attempt, screaming for her child as she batters the door with bloodied knuckles.")
                
            elif choice == "2" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You quickly pull out your set of lockpicks and get to work on the door.")
                typewriter_effect("The screams rattle your brain as you try to find the tumbler, painfully aware of how long this is taking.")
                typewriter_effect("If you could just…there!")
                typewriter_effect("It juts into place and you scramble into the room.")
                 
            elif choice == "2" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You pull out your lockpicks and attack the door with vigour.")
                typewriter_effect("There has to be a correct angle, something you’re missing-")
                typewriter_effect("SNAP")
                typewriter_effect("Your lockpick breaks inside the lock, NO… not now, anytime but now!")
                typewriter_effect("You pull out another, but the remains of the first are still in the tumbler and -it’s hopeless.")
                typewriter_effect("You are suddenly filled with a sense of loss as you stare at the door.")
                
            elif choice == "3" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You desperately scan the room for the key, knocking over what little furniture and decor there is.")
                typewriter_effect("An empty chest, a broken table… a strangely familiar book sat on a shelf.")
                typewriter_effect("You grab the book and, sure enough, there is a depression within holding a rusted looking key.")
                typewriter_effect("It easily slots into the lock.")
                
            elif choice == "3" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You hunt around the room frantically.")
                typewriter_effect("Tables are thrown, shelving tipped over… but no key.")
                typewriter_effect("You run outside and try to find maybe a window or a broken bit of wall to slip through.")
                typewriter_effect("Nothing.")
                typewriter_effect("Despondent, you return to the door and watch the Baker slam herself against it.")
                
            elif player_roll <= 1 :
                typewriter_effect("You rush around, mind racing… whatever you were going to try, whatever brilliant and heroic idea you had; it’s gone, and all that remains in its place is smoke, regret, and pain. ")
                typewriter_effect("CRACK.")
                typewriter_effect("You hear the sound of some supports in the old shack snapping, this building is coming down, and there’s no time to save Margaret, Ezra, or even yours-")
                dead()
            else:
                typewriter_effect("Invalid input. Please enter either '1' or '2'.")
            if bakercheck == True:
                runebakersafe = True
                typewriter_effect("The body of a child sits, roiling in flame, inside a blackened sigil.")
                typewriter_effect("You swiftly pull the child from the room and use your jacket to pat down the flames.")
                typewriter_effect("The smell of burning hair and flesh is sickening.")
                typewriter_effect("The Baker weeps as she gathers the faintly breathing child to her and cradles him in her arms, rocking slowly.")
                typewriter_effect("You begin to leave to find the doctor; the small child in Margaret’s arms lets out a small noise, and as you turn around, hands you something.")
                typewriter_effect("Neatly folded, completely untouched by flames, and as unsettling as all the others: a piece of paper, with a sigil, in blood red ink.")
                print("    |   ")
                print("   _|_")
                print("  |   |")
                print("  | * |")
                print("  |___|")
                print("    |   ")
                print("    |   ")
                inn2()
                
            else:
                runebakersafe = False
                bakerdead = True
                typewriter_effect("Soon the sense of heat emanates from behind the door.")
                typewriter_effect("You begin to sweat even harder.")
                typewriter_effect("The screams have stopped.")
                typewriter_effect("Flames lick from underneath the door.")
                typewriter_effect("The room is filling with smoke.")
                typewriter_effect("You call out to Margaret, the building is quickly losing integrity and will fall down soon.")
                typewriter_effect("No response.")
                typewriter_effect("She’s slumped against the door, her eyes empty as she stares out across the room.")
                typewriter_effect("You have no choice but to run out as the supports begin to fail.")
                typewriter_effect("The shack burns.")
                inn2()

def bakershack2():
    global townehallinnerchek
    global townhallouterchek
    global bakercheck
    global runebakersafe
    global bakerdead
    if townhallouterchek == True:
        typewriter_effect("You quickly catch up to the Baker as she charges off into the town.")
        typewriter_effect("She begins to speak as if to ward off your attempts of stopping her but you cut her off, offering your assistance in the search. ")
        typewriter_effect("Her eyes gleam wetly for a moment before she nods curtly and begins marching determinedly towards the nearest neighbour, you following after.")
    elif townehallinnerchek == True:
        typewriter_effect("The next hours are spent fruitlessly searching from building to building, asking all who you come across if they have seen the child but to no luck.")
        typewriter_effect("As the evening wanes, you reach the edge of the tree line and spot a run-down shack.")
        typewriter_effect("You gesture at the building and ask if it’s possible the child could be hiding within.")
        typewriter_effect("She says that it’s been abandoned for as long as anyone could remember but you could try.")
        typewriter_effect("You approach the shack carefully, dodging broken nails and floorboards as you mount the porch and try the door.")
        typewriter_effect("It creaks open, permitting the stench of mildew, damp, mould, and the great unwashed.")
        typewriter_effect("The floor has clearly been used in the past as a squatting ground for the local unhoused population, spotting the random bloodstains and empty bottles that litter the area.")
        typewriter_effect("As one particularly loud board gives a permissive squeak, you suddenly notice a whimpering sound begin from across the room, behind the only door in the shack.")
        typewriter_effect("Margaret calls out to the noise and it quickly turns into a child’s breathless begging.")
        typewriter_effect("“EZRA!” Margaret cries, “That’s him!”")
        typewriter_effect("You both charge over to the door only to find it locked up tight.")
        typewriter_effect("After trying the handle a few times, frustration takes over as Margaret slams a fist helplessly against the door and the child’s pleading twists into screams of agony as some sort of glyph begins glowing beneath her hand.")
        typewriter_effect("There is a desperate smell of burning.")
        typewriter_effect("Burning flesh.")
        while True:
            choice = input("What will you do? 1. Break open the door. 2. Try to pick the lock. 3. Try to find the key.  ")
            time.sleep(1)
            player_roll = rollcheck()
            if choice == "1" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You yell for the Baker to move and take a running shoulder to the door.")
                typewriter_effect("The wood breaks inward but remains intact.")
                typewriter_effect("You slam it again and finally smash through, splinters piercing into your flesh.")
                
            elif choice == "1" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You take a running shoulder into the door… but it doesn’t budge.")
                typewriter_effect("Your shoulder screams in pain, dislocated?")
                typewriter_effect("In desperation, you start kicking the door below the lock, again and again.")
                typewriter_effect("The Baker joins your attempt, screaming for her child as she batters the door with bloodied knuckles.")
                
            elif choice == "2" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You quickly pull out your set of lockpicks and get to work on the door.")
                typewriter_effect("The screams rattle your brain as you try to find the tumbler, painfully aware of how long this is taking.")
                typewriter_effect("If you could just…there!")
                typewriter_effect("It juts into place and you scramble into the room.")
                
            elif choice == "2" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You pull out your lockpicks and attack the door with vigour.")
                typewriter_effect("There has to be a correct angle, something you’re missing-")
                typewriter_effect("SNAP")
                typewriter_effect("Your lockpick breaks inside the lock, NO… not now, anytime but now!")
                typewriter_effect("You pull out another, but the remains of the first are still in the tumbler and -it’s hopeless.")
                typewriter_effect("You are suddenly filled with a sense of loss as you stare at the door.")
                
            elif choice == "3" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You desperately scan the room for the key, knocking over what little furniture and decor there is.")
                typewriter_effect("An empty chest, a broken table… a strangely familiar book sat on a shelf.")
                typewriter_effect("You grab the book and, sure enough, there is a depression within holding a rusted looking key.")
                typewriter_effect("It easily slots into the lock.")
                
            elif choice == "3" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You hunt around the room frantically.")
                typewriter_effect("Tables are thrown, shelving tipped over… but no key.")
                typewriter_effect("You run outside and try to find maybe a window or a broken bit of wall to slip through.")
                typewriter_effect("Nothing.")
                typewriter_effect("Despondent, you return to the door and watch the Baker slam herself against it.")
                
            elif player_roll <= 1 :
                typewriter_effect("You rush around, mind racing… whatever you were going to try, whatever brilliant and heroic idea you had; it’s gone, and all that remains in its place is smoke, regret, and pain. ")
                typewriter_effect("CRACK.")
                typewriter_effect("You hear the sound of some supports in the old shack snapping, this building is coming down, and there’s no time to save Margaret, Ezra, or even yours-")
                dead()
            else:
                typewriter_effect("Invalid input. Please enter either '1' or '2'.")
            if bakercheck == True:
                runebakersafe = True
                typewriter_effect("The body of a child sits, roiling in flame, inside a blackened sigil.")
                typewriter_effect("You swiftly pull the child from the room and use your jacket to pat down the flames.")
                typewriter_effect("The smell of burning hair and flesh is sickening.")
                typewriter_effect("The Baker weeps as she gathers the faintly breathing child to her and cradles him in her arms, rocking slowly.")
                typewriter_effect("You begin to leave to find the doctor; the small child in Margaret’s arms lets out a small noise, and as you turn around, hands you something.")
                typewriter_effect("Neatly folded, completely untouched by flames, and as unsettling as all the others: a piece of paper, with a sigil, in blood red ink.")
                print("    |   ")
                print("   _|_")
                print("  |   |")
                print("  | * |")
                print("  |___|")
                print("    |   ")
                print("    |   ")
                choice3split()
                
            else:
                runebakersafe = False
                bakerdead = True
                typewriter_effect("Soon the sense of heat emanates from behind the door.")
                typewriter_effect("You begin to sweat even harder.")
                typewriter_effect("The screams have stopped.")
                typewriter_effect("Flames lick from underneath the door.")
                typewriter_effect("The room is filling with smoke.")
                typewriter_effect("You call out to Margaret, the building is quickly losing integrity and will fall down soon.")
                typewriter_effect("No response.")
                typewriter_effect("She’s slumped against the door, her eyes empty as she stares out across the room.")
                typewriter_effect("You have no choice but to run out as the supports begin to fail.")
                typewriter_effect("The shack burns.")
                choice3split()

def bakershack3():
    global townehallinnerchek
    global townhallouterchek
    global bakercheck
    global runebakersafe
    global bakerdead
    if townhallouterchek == True:
        typewriter_effect("You quickly catch up to the Baker as she charges off into the town.")
        typewriter_effect("She begins to speak as if to ward off your attempts of stopping her but you cut her off, offering your assistance in the search. ")
        typewriter_effect("Her eyes gleam wetly for a moment before she nods curtly and begins marching determinedly towards the nearest neighbour, you following after.")
    elif townehallinnerchek == True:
        typewriter_effect("The next hours are spent fruitlessly searching from building to building, asking all who you come across if they have seen the child but to no luck.")
        typewriter_effect("As the evening wanes, you reach the edge of the tree line and spot a run-down shack.")
        typewriter_effect("You gesture at the building and ask if it’s possible the child could be hiding within.")
        typewriter_effect("She says that it’s been abandoned for as long as anyone could remember but you could try.")
        typewriter_effect("You approach the shack carefully, dodging broken nails and floorboards as you mount the porch and try the door.")
        typewriter_effect("It creaks open, permitting the stench of mildew, damp, mould, and the great unwashed.")
        typewriter_effect("The floor has clearly been used in the past as a squatting ground for the local unhoused population, spotting the random bloodstains and empty bottles that litter the area.")
        typewriter_effect("As one particularly loud board gives a permissive squeak, you suddenly notice a whimpering sound begin from across the room, behind the only door in the shack.")
        typewriter_effect("Margaret calls out to the noise and it quickly turns into a child’s breathless begging.")
        typewriter_effect("“EZRA!” Margaret cries, “That’s him!”")
        typewriter_effect("You both charge over to the door only to find it locked up tight.")
        typewriter_effect("After trying the handle a few times, frustration takes over as Margaret slams a fist helplessly against the door and the child’s pleading twists into screams of agony as some sort of glyph begins glowing beneath her hand.")
        typewriter_effect("There is a desperate smell of burning.")
        typewriter_effect("Burning flesh.")
        while True:
            choice = input("What will you do? 1. Break open the door. 2. Try to pick the lock. 3. Try to find the key.  ")
            time.sleep(1)
            player_roll = rollcheck()
            if choice == "1" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You yell for the Baker to move and take a running shoulder to the door.")
                typewriter_effect("The wood breaks inward but remains intact.")
                typewriter_effect("You slam it again and finally smash through, splinters piercing into your flesh.")
                
            elif choice == "1" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You take a running shoulder into the door… but it doesn’t budge.")
                typewriter_effect("Your shoulder screams in pain, dislocated?")
                typewriter_effect("In desperation, you start kicking the door below the lock, again and again.")
                typewriter_effect("The Baker joins your attempt, screaming for her child as she batters the door with bloodied knuckles.")
                
            elif choice == "2" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You quickly pull out your set of lockpicks and get to work on the door.")
                typewriter_effect("The screams rattle your brain as you try to find the tumbler, painfully aware of how long this is taking.")
                typewriter_effect("If you could just…there!")
                typewriter_effect("It juts into place and you scramble into the room.")
                
            elif choice == "2" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You pull out your lockpicks and attack the door with vigour.")
                typewriter_effect("There has to be a correct angle, something you’re missing-")
                typewriter_effect("SNAP")
                typewriter_effect("Your lockpick breaks inside the lock, NO… not now, anytime but now!")
                typewriter_effect("You pull out another, but the remains of the first are still in the tumbler and -it’s hopeless.")
                typewriter_effect("You are suddenly filled with a sense of loss as you stare at the door.")
                
            elif choice == "3" and player_roll >= 10:
                bakercheck=True
                typewriter_effect("You desperately scan the room for the key, knocking over what little furniture and decor there is.")
                typewriter_effect("An empty chest, a broken table… a strangely familiar book sat on a shelf.")
                typewriter_effect("You grab the book and, sure enough, there is a depression within holding a rusted looking key.")
                typewriter_effect("It easily slots into the lock.")
                
            elif choice == "3" and player_roll < 10:
                bakercheck=False
                typewriter_effect("You hunt around the room frantically.")
                typewriter_effect("Tables are thrown, shelving tipped over… but no key.")
                typewriter_effect("You run outside and try to find maybe a window or a broken bit of wall to slip through.")
                typewriter_effect("Nothing.")
                typewriter_effect("Despondent, you return to the door and watch the Baker slam herself against it.")
                
            elif player_roll <= 1 :
                typewriter_effect("You rush around, mind racing… whatever you were going to try, whatever brilliant and heroic idea you had; it’s gone, and all that remains in its place is smoke, regret, and pain. ")
                typewriter_effect("CRACK.")
                typewriter_effect("You hear the sound of some supports in the old shack snapping, this building is coming down, and there’s no time to save Margaret, Ezra, or even yours-")
                dead()
            else:
                typewriter_effect("Invalid input. Please enter either '1' or '2'.")
            if bakercheck == True:
                runebakersafe = True
                typewriter_effect("The body of a child sits, roiling in flame, inside a blackened sigil.")
                typewriter_effect("You swiftly pull the child from the room and use your jacket to pat down the flames.")
                typewriter_effect("The smell of burning hair and flesh is sickening.")
                typewriter_effect("The Baker weeps as she gathers the faintly breathing child to her and cradles him in her arms, rocking slowly.")
                typewriter_effect("You begin to leave to find the doctor; the small child in Margaret’s arms lets out a small noise, and as you turn around, hands you something.")
                typewriter_effect("Neatly folded, completely untouched by flames, and as unsettling as all the others: a piece of paper, with a sigil, in blood red ink.")
                print("    |   ")
                print("   _|_")
                print("  |   |")
                print("  | * |")
                print("  |___|")
                print("    |   ")
                print("    |   ")
                inn3()
                
            else:
                runebakersafe = False
                bakerdead = True
                typewriter_effect("Soon the sense of heat emanates from behind the door.")
                typewriter_effect("You begin to sweat even harder.")
                typewriter_effect("The screams have stopped.")
                typewriter_effect("Flames lick from underneath the door.")
                typewriter_effect("The room is filling with smoke.")
                typewriter_effect("You call out to Margaret, the building is quickly losing integrity and will fall down soon.")
                typewriter_effect("No response.")
                typewriter_effect("She’s slumped against the door, her eyes empty as she stares out across the room.")
                typewriter_effect("You have no choice but to run out as the supports begin to fail.")
                typewriter_effect("The shack burns.")
                inn3()

def dead():
    typewriter_effect("Oh dear, you are dead.")
    sys.exit()
def inn2():
    typewriter_effect("After a long day you head back to the inn, slouch down and start to fall asleep onto your bed, the days events bouncing around your head.")
    nightmareseq2()
def nightmareseq2():
    typewriter_effect("As night approached, you lay in your bed looking back on the day’s events, fatigued from your efforts. TIredness overwhelmed you, and you drifted off soon after. The clock struck midnight, when the nightmare from the night before resumed itself. The shadowy figure returned, the dread and disdain emanating from his visage. A faint whisper could be heard: “Time is running out: beware.” Unable to move, sweat beading from your face, you woke up dazed, unsure how long these nightmares would last and why. ")
    day3()
def day3():
    global runebakersafe
    global runeteachersafe
    global teachertalked
    global bakertalked
    global teacherdead
    global bakerdead
    typewriter_effect("The morning begins sullen and dreadful. Time is running out, and you must do what’s necessary to save these kids before you lose yourself in the process.The pieces of the puzzle are coming together and it’s up to you to fit them into a completed picture and solve this case once and for all. You leave the inn and prepare for the coming day’s events, not knowing who or what it may bring. The air has a dulling effect on your senses, making you question everything you see and hear now. Before long, this mysterious atmosphere follows you with your investigation, casting judgement on anything remotely connected to the case.It’s time to get to work, because someone has to solve this and that someone is you.")
    if runebakersafe == True:
        typewriter_effect("Since you managed to save the baker you decide to head towards finding out whats going on with the school teacher")
        teacher4()
        if teacherdead== True:
            choice3split()
        elif teachertalked == True:
            teacher4()
        elif teachertalked == False:
            go_to_west_path4()
    elif runeteachersafe == True:
        typewriter_effect("Since you managed to save the teacher you decide to head towards finding out whats going on with the baker")
        bakershack3()
        if bakerdead== True:
            choice3split()
        elif bakertalked == True:
            bakershack3
        else:
            go_to_east_path4
    

    else:
        if teacherdead == True:
            ("After the events with the teacher you decide to head towards finding out whats going on with the baker")
            bakershack3()
        elif bakerdead == True:
            ("After the events with the baker you decide to head towards finding out whats going on with the teacher")
            teacher4()
        else: 
            typewriter_effect("Where would you like to head?")
            typewriter_effect("1. Head to the schoolhouse")
            typewriter_effect("2. Visit the Baker")
            townhallouterchek == True
            choice = input("Enter your choice (1/2): ")
            while True:
                if choice == "1":
                    if teachertalked == True:
                        teacher4()
                    else:
                        go_to_west_path5()
            # link to teacher1
                    break
                elif choice == "2":
                    if bakertalked == True:
                        bakershack3()
                    else:
                        go_to_east_path5()
                # link to baker1
                    break
                else: 
                 typewriter_effect("Invalid input, please try inputting 1 or 2.")
                 break
def choice3split():
    global runebakersafe
    global runeteachersafe
    global teachertalked
    global bakertalked
    global teacherdead
    global bakerdead
    typewriter_effect("The events of the morning have drained you mentally and physically. Yet there’s no time to rest: much more awaits you to complete. There can be no more breaks as you head into the last spurt of this investigation. The end goal is in sight and it’s up to you to reach it. The sun begins setting on the town, with the feeling of despair and disdain cloaking it once more. You dread the nights now but where there’s darkness, there’s light and that’s sufficient motivation to banish the darkness from this town and return its light once more. ")
    if runebakersafe == True:
        typewriter_effect("Since you managed to save the baker you decide to head towards finding out whats going on with the school teacher")
        teacher4()
        if teacherdead== True:
            choice3split()
        elif teachertalked == True:
            teacher4()
        elif teachertalked == False:
            go_to_west_path4()
    elif runeteachersafe == True:
        typewriter_effect("Since you managed to save the teacher you decide to head towards finding out whats going on with the baker")
        bakershack3()
        if bakerdead== True:
            choice3split()
        elif bakertalked == True:
            bakershack3
        else:
            go_to_east_path4
    inn3()

def inn3():
    typewriter_effect("Time to head to the inn. It’s been an eventful day to say the least but damn, are you glad it’s over. You enter your room drowsy and dazed, unsure if everything that happened today really did or if it was all just a fever dream. The bed stares at you, warm and inviting in a way you can’t resist, prompting you to change into your night garments before burying yourself under the duvet for another night’s rest. This time, fearful of what the night may have in store for you…")
    nightmareseq3()
def nightmareseq3():
    typewriter_effect("Your dreams are not yours.")
    typewriter_effect("They are the playthings of creatures beyond imagining.")
    typewriter_effect("They distort, bend, are they glimpses, possibilities of events?")
    typewriter_effect("Did you, or someone that looks a lot like you, really allow these things to happen?")
    typewriter_effect("They rush past, you’re barely able to process them before they’re swept away into a different but very distinct horror.")
    print("")
    typewriter_effect("The Teacher’s lifeless eyes stare up at you from the forest floor, accusation clear, a bullet hole through the chest steadily streaming blood into the soil and feeding the nearby roots of a red-leafed tree.")
    typewriter_effect("Dark silhouettes stand over the body, chanting.")
    typewriter_effect("The tree creaks and bends like a living thing.") 
    print("")
    typewriter_effect("You see the bodies of the Baker and her child writhing in flames, screaming out your name in pure hatred as you have no other choice than to stare at them helplessly as the flesh burns away, eyes melting like candle wax and pouring down their faces.")
    typewriter_effect("Until all that is left are burnt husks of the people you knew, petrified forever in their terror.")
    typewriter_effect("")
    typewriter_effect("The gaunt faces of the missing children stare at you, expectantly, as a forest grows around all of you, the children approach you, roots sprouting from their fingers.")
    typewriter_effect("They dig the roots into you wherever they can find purchase, spreading through your nostrils, down your throat, into your ears, and through the corners of your eyes... the children take root... and begin to drain.")
    print("")
    typewriter_effect("You gasp awake, clutching at your mouth, half expecting the roots to be there, but instead; you find only a tightly folded piece of paper, with a rune emblazoned upon it in blood.")
    print("")
    print("    *   /  ")
    print("     * /__ __")
    print("   *  /   ")
    print("    */__ __ __ ")
    print("*   /  *")
    print(" * / ")
    print("  /")
    typewriter_effect("The first rays of dawn glitter through the windowpane.")
    typewriter_effect("It awaits.")
    final_day()
def final_day():
    typewriter_effect("You walk downstairs into the lobby of the inn, aware that today may be the last day you and the rest of Redspring ever see. Your chest tightens with anxiety and fear yet you remain steadfast in your conviction. This is for the kids, you repeat in your head; over and over, your mantra is set.")
    if runebakersafe == True and runeteachersafe == True:
        typewriter_effect("You see Eleanor and Margaret arrive; Margaret holds her son in her arms.")
        typewriter_effect("“It’s bad out there.” Margaret states the obvious.")
        typewriter_effect("Eleanor looks at you, “We’ve spoken, we can stay and help-” ")
        typewriter_effect("“No”")
        typewriter_effect("Your response is flat and non-argumentative. You make it clear in one word that this is not up for debate, the two of them nod, as the Innkeeper looks over.")
        typewriter_effect("“Wagon’s off in ten minutes, sure we can’t bring you along?” he requests, already knowing your answer.")
        typewriter_effect("You shake your head “Take them to the Miskatonic in Arkham, find van Buren. They’ll be well looked after until I arrive.”")
        typewriter_effect("The Innkeeper looks through you, “And if you don’t?”")
        typewriter_effect("“Then they’ll be looked after until they don’t need it.”")
        typewriter_effect("The Innkeeper nods and opens the front door.")
        typewriter_effect("“Give ‘em hell.”")
        typewriter_effect("You smile and nod as you take the most important step of your life.")
        the_ritual()
    elif runebakersafe == True and runeteachersafe == False:
        typewriter_effect("Margaret walks in through the Inn door, holding her son in her arms, the wind howling behind her,")
        typewriter_effect("“It’s bad out there.” Margaret states the obvious.")
        typewriter_effect("“It’s about to get worse.” you reply, “The wagon is out back, you should be heading off, get to Miskatonic; you’ll be safe there.”")
        typewriter_effect("“You’re a better person than most of the people here.”")
        typewriter_effect("You smile sadly.")
        typewriter_effect("“Anyway, there’s a fresh loaf of bread waiting for you when I open a shop in Arkham, so don’t go dying before that, okay?")
        typewriter_effect("You approach the Inn door, “I’ll keep it in mind”, and you step out.")
        the_ritual()
    elif runebakersafe == False and runeteachersafe == True:
        typewriter_effect("Eleanor arrives, determination in her eyes.")
        typewriter_effect("You begin to speak, “The wagon is out back, the driver will collect you in five minutes. Get to the Miskatonic.”")
        typewriter_effect("“I’m not going.” She insists, “You can’t take on everything all alone, it’s not right.")
        typewriter_effect("You remain silent as you move towards the door.")
        typewriter_effect("“You’re taking me with you, you need my help.” Eleanor continues to press as you take the key out of the door.")
        typewriter_effect("“I’ll be more worried if you’re there, I won’t be able to focus” You say.")
        typewriter_effect("“Don’t you dare, you wouldn’t have come nearly this far if not for me. Don’t dare say that I have to let you run off to die alone!” Eleanor starts to cry.")
        typewriter_effect("“You’re right,” you say with resignation, “Okay, just grab that bag from behind the desk and we’ll go.”")
        typewriter_effect("As she reaches over the desk, you walk out of the Inn door and lock it behind you.")
        typewriter_effect("She’ll probably be furious with you when she sees you again, but at least she’ll be alive.")
        the_ritual()
    elif runebakersafe == False and runeteachersafe == False:
        typewriter_effect("The lobby of the hotel is quiet.")
        typewriter_effect("You feel as though this could be different.")
        typewriter_effect("Maybe lots of things could’ve been.")
        typewriter_effect("You sigh, look around, and leave to face the inevitable… Alone.")
        the_ritual()


    pass
def the_ritual():
    typewriter_effect("You exit the Hotel, you hear chanting in the distance, and you feel a chill creep up your spine as you look in the direction of Providence Hill.")
    typewriter_effect("Armed with all the knowledge you have gathered throughout your investigation, and aware that the time is running out, you run north towards the forest… a red forest.")
    typewriter_effect("The ominous glow of torches ahead of you prompts you to slow; as you approach the hill, the chanting grows cacophonous:")
    typewriter_effect("“PHA NO MHEBB’ITHTRA”")
    print()
    typewriter_effect("“PHA NO MHEBB’ITHTRA”")
    print()
    typewriter_effect("“PHA NO MHEBB’ITHTRA”")
    print()
    typewriter_effect("You pad towards the figures through the trees, it feels as though the closer you get, the harder it is to keep moving forward.")
    typewriter_effect(" The trees grasp at you, red leaves and vines twisting around your arms and legs, not strong enough to hold you back, but making movement difficult enough.")
    typewriter_effect("You stumble forward, and for a second you freeze, convinced that you’ll be caught and killed by the cultists.")
    typewriter_effect("But you just hear the chanting.")
    typewriter_effect("You look around, and none of the cultists have moved.")
    typewriter_effect("Each is caught in a trance, looking at the three robed figures on top of the hill.")
    typewriter_effect("They look upon the stone circle, now glowing with ancient, evil power.")
    typewriter_effect("The children that were previously unaccounted for are lying in the centre; each still alive, but rail thin, emaciated.")
    typewriter_effect("You feel the bile rise in your throat as you move up the hill, sickened by the image but grateful that the cultists appear distracted.")
    typewriter_effect("You reach the top of the hill as the first of the three leaders enters the circle.")
    typewriter_effect("He lowers his hood:")
    typewriter_effect("“We call upon thee our lord, to free us from reliance on the cruelty of man!” Father Raymond cries as he stands over one of the children, raising a knife.")
    typewriter_effect("The second follows suit:")
    typewriter_effect("“Give us eternal prosperity under your watchful eyes, so that we may continue to serve you throughout all time!” Shouts Earnest Olmstead, doing the same.")
    typewriter_effect("The final figure rears up to an astounding height, The Sheriff, lowering his hood, stands at nearly seven feet tall, no longer hunching, and looking more young and aware than you have ever seen him.")
    typewriter_effect("“WE CALL UPON THE MHEBB’ITHTRA: THE RED SPRING; TAKE THESE CHILDREN INTO YOUR ARMS AS THEY BECOME ONE WITH YOUR FOREST, AND OUR BLOOD AND SOULS BECOME ONE WITH THEM!” The Sheriff proclaims, in a clear, booming voice the likes of which you have never heard.")
    typewriter_effect("Before you have time to react, the three plunge their knives into their chests and slump.")
    typewriter_effect("They each remain standing, held aloft by a power which is not their own, as the blood drains from them onto the children in the circle.")
    typewriter_effect("You run forwards, attempting to enter the circle, but are stopped by an unseen force.")
    typewriter_effect("The trees in the area seem to scream at you as you try to interfere with this ancient and powerful ritual.")
    typewriter_effect("You look at the children in the circle, roots have grown from the chests of the three head cultists and have begun to take root under the skin of the kids, draining them.")
    typewriter_effect("You see the children begin to age, as the bodies of the three cultists appear to grow younger, with each second that passes, months of life are stolen from the children and given to these wicked men.")
    typewriter_effect("You look around for something… anything to do; and you see the symbols upon the stones.")
    typewriter_effect("You quickly pull the pieces of paper from your pockets, as this ritual occurs, the symbols seem to pulse red, and for each one there is a pull, as if each piece of paper is about to fly off towards a different stone.")
    typewriter_effect("You let go of all the runes you have gathered, you see them get sucked into the circle, and then land, face down, over the corresponding symbol on the stones.")
    typewriter_effect("You didn’t have time to collect them all, you wonder if it would even have been possible to do it had you known, but it’s too late for that now, you can simply wait, and hope.")
    print()
    player_roll = rollcheck()
    if runeteachersafe == False and runebakersafe == False and player_roll >= 15:
         typewriter_effect("You feel the power of the runes reverberate throughout the circle; the vibrations and chanting are so loud now that you feel as though your head may split open.")
         typewriter_effect("You see the stones shake, faster, and faster… until they shatter.")
         typewriter_effect("The forest and cultists scream all as one as the ritual is reversed, the life being drained from the children is returned to them tenfold.")
         typewriter_effect("As the storm dies down, each child looks as healthy and well fed as they could ever wish to be.")
         typewriter_effect("The cult leaders look at you, each an image of death embodied; skin pale as paper, hollow eyes and thin lips, you look at their eyes and see no recognition, and in the final moments before they turn to dust in the wind, each breathes a sigh of resignation.")
         typewriter_effect("The world is quiet for a moment as the forest slowly returns to green, you feel exhausted and slump to the ground.")
         typewriter_effect("The remaining cultists, realising that their eldritch god may no longer exist, awkwardly slink away as you collect the children and begin to make your way down the hill.")
         typewriter_effect("")
         typewriter_effect("The children are safe.")
         print("")
         typewriter_effect("The town is safe.")
         if runebakersafe == True:
             typewriter_effect("Margaret and her son are safe.") 
         elif runeteachersafe == True:
             typewriter_effect("Eleanor is safe.")
         elif runebakersafe == True and runeteachersafe == True:
             typewriter_effect("Even the strange innkeeper, yeah, he’s safe too, you guess.")
             typewriter_effect("")
         typewriter_effect("You are safe.")
         print("")
         typewriter_effect("For now.")
    elif runebakersafe == True and runeteachersafe == True and player_roll >= 5:
        typewriter_effect("You feel the power of the runes reverberate throughout the circle; the vibrations and chanting are so loud now that you feel as though your head may split open.")
        typewriter_effect("You see the stones shake, faster, and faster… until they shatter.")
        typewriter_effect("The forest and cultists scream all as one as the ritual is reversed, the life being drained from the children is returned to them tenfold.")
        typewriter_effect("As the storm dies down, each child looks as healthy and well fed as they could ever wish to be.")
        typewriter_effect("The cult leaders look at you, each an image of death embodied; skin pale as paper, hollow eyes and thin lips, you look at their eyes and see no recognition, and in the final moments before they turn to dust in the wind, each breathes a sigh of resignation.")
        typewriter_effect("The world is quiet for a moment as the forest slowly returns to green, you feel exhausted and slump to the ground.")
        typewriter_effect("The remaining cultists, realising that their eldritch god may no longer exist, awkwardly slink away as you collect the children and begin to make your way down the hill.")
        typewriter_effect("")
        typewriter_effect("The children are safe.")
        print("")
        typewriter_effect("The town is safe.")
        if runebakersafe == True:
             typewriter_effect("Margaret and her son are safe.") 
        elif runeteachersafe == True:
             typewriter_effect("Eleanor is safe.")
        elif runebakersafe == True and runeteachersafe == True:
             typewriter_effect("Even the strange innkeeper, yeah, he’s safe too, you guess.")
             typewriter_effect("")
        typewriter_effect("You are safe.")
        print("")
        typewriter_effect("For now.")
    elif runebakersafe == True or runeteachersafe == True and player_roll >= 10: 
            typewriter_effect("You feel the power of the runes reverberate throughout the circle; the vibrations and chanting are so loud now that you feel as though your head may split open.")
            typewriter_effect("You see the stones shake, faster, and faster… until they shatter.")
            typewriter_effect("The forest and cultists scream all as one as the ritual is reversed, the life being drained from the children is returned to them tenfold.")
            typewriter_effect("As the storm dies down, each child looks as healthy and well fed as they could ever wish to be.")
            typewriter_effect("The cult leaders look at you, each an image of death embodied; skin pale as paper, hollow eyes and thin lips, you look at their eyes and see no recognition, and in the final moments before they turn to dust in the wind, each breathes a sigh of resignation.")
            typewriter_effect("The world is quiet for a moment as the forest slowly returns to green, you feel exhausted and slump to the ground.")
            typewriter_effect("The remaining cultists, realising that their eldritch god may no longer exist, awkwardly slink away as you collect the children and begin to make your way down the hill.")
            typewriter_effect("")
            typewriter_effect("The children are safe.")
            print("")
            typewriter_effect("The town is safe.")
            if runebakersafe == True:
                 typewriter_effect("Margaret and her son are safe.") 
            elif runeteachersafe == True:
                 typewriter_effect("Eleanor is safe.")
            elif runebakersafe == True and runeteachersafe == True:
                 typewriter_effect("Even the strange innkeeper, yeah, he’s safe too, you guess.")
                 typewriter_effect("")
            typewriter_effect("You are safe.")
            print("")
            typewriter_effect("For now.")


    else:
         typewriter_effect("You feel the power of the runes reverberate throughout the circle; the vibrations and chanting are so loud now that you feel as though your head may split open.")
         typewriter_effect("You see the stones shake, faster, and faster…")
         print("")
         typewriter_effect("And then they stop.")
         typewriter_effect("The paper falls away from each, useless.")
         typewriter_effect("If only you’d found all the runes, if only you’d had more time!")
         typewriter_effect("If only the children had more time!")
         typewriter_effect("The time that you don’t have slips away.")
         typewriter_effect("The time that the children had is drained from them.")
         typewriter_effect("The time that wasn’t the cultists is now theirs, young and vibrant, they would have used it.")
         typewriter_effect("The cultists would have celebrated.")
         typewriter_effect("You would have felt regret.")
         typewriter_effect("Had none of you looked down.")
         typewriter_effect("Looked at the hill open.")
         typewriter_effect("Looked at the hill blink.")
         typewriter_effect("And saw the eye that you once thought was a hill…")
         typewriter_effect("...look back.")
    thank_you()
def thank_you():
    typewriter_effect("Thank you for playing The Red Spring, Created by Laurence, Caitlin, Mohammed and Chris")
    sys.exit()
player_class = choose_class()
intro_letter()
time.sleep(2)
town_intro()
choice1split()
time.sleep(2)





