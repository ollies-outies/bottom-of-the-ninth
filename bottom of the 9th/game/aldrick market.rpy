﻿
# Define b = character("Aldric")
# Define c = character("Casey")

label AldricMarket:
    $ HasAldric = True

    show cardaldric

    "Aldric Bohan. If you want to talk about someone favored by Fate, then there's no one better than Aldric."
    "Naturally gifted athlete, traditionally attractive, and a member of Gallant Monthly's 25 under 25 list."
    "Everyone in the game expected him to go to the Majors years ago, but he suffered from what is commonly described as ''The Adventurer’s Spirit''."
    "Which, isn't some spelunker’s ghost poltergeisting things around. It's a lust, both for wander, and for blood. Combine that with an ego the size of a whale..."
    "Well, overconfidence can be deadly, I should know. Big egos and lack of focus kill potential more than anything else. It's honestly worse than death! Because, to be fair, some of the best players in the game back then were undead."
    "But the kid had skill, I couldn't deny that, and a sense of honor that's still rare to see today. If the cards said I needed that, then who was I to argue? Just had to find him."
    b "HOW QUAINT!"
    hide cardaldric
    show aldric
    "Or, maybe his better fate could make him find me."
    b "Your hands! Oh, I’d recognize the hands of a future Wizardball player anywhere and my oh my, do you have them, my dear friend! Have you considered playing? Age is not an issue, you know!"
    "I would've liked to tear into him for calling me old, but that would imply I had a moment to speak."
    b "I know there's a new team that's starting here in town, I wonder if we can talk to their coach and see if they'd accept someone off the street! That's why I'm here, actually. Oh, friend, you'll love the game."
    "He then proceeded to explain the rules of the game I’d played for the majority of my life. I tried toning it out until I had an opportunity to talk, but it looked like it wasn't coming."
   
    b "... Oh, and that's when Yurtle’s Law was introduced! See, due to a curse put on the concept of the game, there must be a shelled animal, or, animal adjacent being, present at all Wizardball games, or else one of the players gets a sickly pox in a fortnight!"
    "I will admit, Yurtle’s Law made schoolyard games very worrying, growing up. It did cause the snail to become a very popular pet, though. I mean, I had one."
    "But, remembering youth wasn't getting me closer to assembling a team, and Aldric was starting to do the unthinkable; switch topics."
    b "You know, I love the smell of the market in the morning. Katabas is wonderful, especially this time of year. That reminds me of this one QUEST I went on to the southern Valleys, near Brauns? If you haven't been, it is just LOVELY..."
    "Obviously Aldric wanted to join the team, or at least check the option out. But how to subtly ease the conversation back to the topic?"
    
    menu:
        "I finally interrupted, loudly saying..."
        
        "ADVENTURER, THERE'S A QUEST THAT NEEDS CONQUERING, AND YOU'RE THE ONLY ONE WHO CAN DO IT!":
            jump aldric_A1
        
        "WOULD YOU PLEASE SHUT YOUR CHIZZLED JAW LINE FOR ONE MINUTE, AND LET ME INTRODUCE MYSELF?":
            jump aldric_A1
        
        
    label aldric_A1:
    "He stopped yapping after I said that, stunned into silence to listen. I took a deep breath, and started."
    c "My name's Casey Conrad Fisk, and I have Wizardballer hands because I'm a Wizardballer. I'm also the coach you'd like to talk to, and on a quest from Fate to get a team of rookies together in a few days, to then go to Hell to play our first game."
    c "There will be no practices before we go, there will more than likely be bloodshed because the game is in Hell and they like to play dirty down there, I'm not old; you’re just young, and Yurtle’s is a hex not a pox. Curses can't do disease, you were thinking of Miasmas."
    c "So. Are you in?"
    "He kept sitting, not answering."
    c "... I'm finished."
    b "Ah. Thank you. I didn't want to interrupt; interrupting's rude."
    "He raised a fist to the sky and let out an enthusiastic Hurrah, startling several stall owners."
    b "BRAVE VETERAN CASEY CONRAD FISK, I ACCEPT YOUR CHALLENGE! CONSIDER ME A MEMBER OF THE..."
    "His eyes glazed for a second."
    c "The Comedians. We're the Comedians."
    b "A MEMBER OF THE COMEDIANS! How JOVIAL! Oh, recruitment. This is just like my last quest, over in Quinthorp, when I-"
    c "Hey, that's really great, man. Love to hear about it. But gotta run, call to action, much to do, Fate's hand, you know how it is, I'm sure. See you in Hell Valley, champ!"
    "I left before he could start another story. Interesting story or not, I was on a time limit, and still had a few cards left in the pack."
    
    
        

hide aldric
return

