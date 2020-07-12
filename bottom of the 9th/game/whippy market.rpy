define c = ("Casey")
define w = ("Whippy")


label WhippyMarket:


$ HasWhippy = True
$ Magic += 1
$ Might += 4
$ Movement += 1

    scene bg market
    show cardwhippy

    "Jordan Redslide. ''Whippy'', to friends and admirers."
    "This little birdy has a big secret. Namely, the kid's got an arcane reserve the size of the ocean."
    "Issue is, he's also got no spell control in the slightest. He's a constantly charging dynamo, with no real place to discharge."
    "And eventually, the dam as got to burst."
    "This sometimes comes out as arcane bursts, explosions of pure force, which, while spectactular, are not regulation, and did get him kicked off the Rasko Stonemasons."
    "Or now, due to runes etched into his uniform, pure strength."
    "He's a powerhouse in the truest sense of the word..."
    
    hide cardwhippy
    show whippy
    
    "He's just also a bit... unpredictable."
    "I ran into him, after he had, seemingly singlehandedly, leveled a food stall."
    "Or, what used to be one, at the very least."
    "I say it was him, not because I saw him do it, but because he was standing over it, biting his feathers, panicking."
    "Plus, my first words that I heard him say were..."
    w "Oh gods, not another one!"
    "I'm no private dick, but you don't have to be one to put two and two together."
    c "You alright, son?"
    "He turned so quick, I swore I heard something crack. There was a panic in his eyes that I had never seen before."
    "He was spiraling quick. I needed to put him at ease somehow."

    menu: 
            "So I told him..."

            "Oh, thank goodness! Someone broke it down!": 
             jump whippy_A1

            "Hey, it's okay. It's okay. Breathe. Breathe.": 
             jump whippy_A2


    label whippy_A1:
    "He looked at me, now more confused than panicked."
    c "That old thing was a safety hazard. City said so. So, they were fining me to have it destroyed."
    c "And here I was, worried I'd have to find someone to do it... When, clearly, you're all I needed! You're my hero, little fella."
    c "Now, I can start my second buisness; Staring a Wizardball team!"
    "I gave a chuckle. I hadn't lied that hard since grade school, but it was working. Whippy was calming down, and more importantly, buying it."
    c "Here, why don't you wait over there? I've got some quick paperwork, to finish up the ol' girl."
    "I point to a nearby bench, under a tree. Whippy hesitates, then nods and walks over."
    "I quickly pull out my pen and paper and write a hastily written ''I O U x 1. STALL. SORRY MY BAD, C.C.'' and place it on the rubble, before turning back to Whippy."
    jump whippy_A3

    label whippy_A2:
    "He, stifling tears, tried to say,"
    w "I d-didn't... m-mean t-..."
    c "'course not, 'course not! You're fine. No one was hurt, no one was hurt, it was just stuff."
    c "Stuff can get replaced. Take some deep breaths. Are you okay? "
    "He seemed surprised at the question, but complied. Breathing in, holding for a few seconds, breathing out."
    w "Yeah, I'm... I'm fine."
    c "Here, sit down. We're gonna get through this." 
    "I gestured to a nearby bench, where he walked over and cautiously took a seat."
    jump whippy_A3


    label whippy_A3:
    "I sat down next to him."
    c "You have a gift, kiddo. Like it or not, fate's given you this crazy power, and the best thing you can do is try to use it for good."
    "I offerd him my hand."
    c "I'm starting a pro Wizardball team, here in town. If you'd like, I'd love to have you with us."
    w "You sure you want m-me? After everything?"
    c "What, after showing me your skills, or after being a great player? I've seen you on the field, young man." 
    "He looked at me, slightly dumbfounded, and gingerly took my hand. I smiled, a cocky glint in my eye."
    c "Go ahead, I can take it."
    "He gave a glint back, and shook my hand, fully and wholeheartedly." 
    "I damn near dislocated my arm."
    c "Meet us at Hell Valley Stadium in a few days." 
    "He nodded, almost excited." 
    w "I'll see you there!"
    
    hide whippy
    
    "Lets see, after Whippy..."
   
return
