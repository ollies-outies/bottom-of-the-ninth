# Define y = character("Dusk")
# Define c = character("Casey")

label DuskMarket:
    $ HasDusk = True

    show carddusk

    "They say curiosity killed the cat, but when it came to Dusk D'arcnes, curiosity made them more powerful than they ever could've imagined."
    "Delving into the arts of necromancy at a very young age, Dusk soon became quite accustomed with all things dead, and mostly deadly."
    "Necromancers were few and far between in the Wizardball Minor League circuit, allowing Dusk to make a name for their feline self out on the field."
    "Unfortunately, skills in dealing with the dead don't always translate into skills when dealing with the living."
    "This was undoubtedly gonna be a tough one."

    hide carddusk

    show dusk

    y "HEY! PUNKOSAURUS!"
    "Dusk was the one to find me in the square. They're an extremely iconic individual, despite their height, and my search for them was nothing close to subtle."
    y "N'you staring at me or somethin'?!? What's yer DEAL?!?"
    c "Oh, uh... My apologies, I just recognized you. You're a Wizardball player, right? Used to play for the Danderville Scruff-Necks?"
    y "N'aybe I did! N'aybe I didn't! What's it to you, n'you stalker!?"
    "Dusk was surprisingly intimidating, so I tried a strategy that used to work on my old pet."
    c "Well, I'll uh... give you some salmon if you hear me out?"
    y "N'you tryin t' patronize me just cause I'm fuzzy?! N'yI'll have you kn'yow that I'm allergic to salmon!"
    c "Fine, right, sorry, no salmon. Should've just said that I'm starting a pro-team in Katabas and I'd like to have you on it."
    y "Sure, joining a stranger’s team! Someon'ye who's seemingly been n'yactively STALKING me, while I buy my groceries!!" 
    c "... Yeah, that's accurate. You in?"
    "For the first time since I ran into them, they calmed down."
    y "... What would be in'yit for me?"
    c "You'll uh... get to cause severe bodily harm to an enemy team-member, if not the entire enemy team?"
    

    y "Nnn... I mean that was funnin'yall but WHY would I want to go back to playing some dumb game when n'yi can just go pummeling fooligans, wherever n' WHEN'YEVER I want?"
    c "Dusk, that's a... that's a felony. You know that's a felony, right?"
    y "N'yot if I don’t get caught! Besides, Wizardball has all those dumb-stinky rules n'that you need to worry about."
    c "That's... technically true, Dusk, but why just hurt people... when you can hurt people and then get a shiny trophy for it?"
    y "Trophies are n'yothin butta capitalist monolith designed to quantify meaningless n'yactions in order to sate the masses just enough to keep 'em complacent! N'yor at least that's what it said in that book that I ate last week..."
    "I stood back a bit and thought about the implications of that. Less about the meanings behind trophies, and more about how Dusk ate a book."
    c "I'm frightened but, admittedly, a little impressed."
    y "Purrcicely what n’yI was going for!"
    "They stood proudly, and smugly, and more importantly, expectantly. Was this a joke? Was that a joke?"
    menu: 
    "I realized I should do something, so I..."
  
          "Laughed.":
              jump dusk_B1
  
          
          "Stayed quiet.":
              jump dusk_B2
              
          
    label dusk_B1:
    "I saw Dusk glare at me with the silent rage of a corpse hearing people talk shit at their open-casket funeral."
    "That was not a joke, apparently. I wondered if it was hardback or not."
    c "Dusk, I- Look, not that I'm not enjoying this, but I don't really have all day to talk about this with you."
    y "Oh, look who's suddenly too BUSY to stalk me, ya bogbreathy smellfungus!"
    jump dusk_B3
      
    label dusk_B2:
    "I knew the dangers of angering this fickle feline and did not want to test them."
    y "Do you n'yot have anythin'yelse to say or are you just gonn'ya stand there like a big dumb pile of slugs?"
    c "I... I feel like I should take offense to that but, honestly I-"
    y "N'yis that SO?! Dumb little slug pile, wanna go eat some rocks 'er something? Slugpile! SLUGPILE!"
    jump dusk_B3
      
              
    label dusk_B3:
    "This conversation was going nowhere faster than a midnight gravy train."
    c "Alright, Dusk, the name-calling isn't doing anyone any favors. Listen, level with me. You don't want your claws going dull, do you?"
    c "All this time without playing is gonna put quite the damper on your skills, magical or otherwise."
    y "What part've assault n'battery didja not get?!"
    c "It being genuine, I suppose?! You're very hard to get a read on, pal."
    "Dusk fluffed up, making them seem like a whopping 4 feet instead of their ususal 3'10''"
    y "WHO'RE YOU CALLIN' PAL? I STILL DON'T KN'YOW WHO YOU ARE!"
    c "Have I seriously still not introduced myself?! Casey Conrad Fisk. Coach of the Katabas Comedians. Look, what'll it take to get you on the team? I'd really rather not have another deranged necromancer on the streets, especially when I can do something about it."
    "They turned around for a moment, and muttered to themselves, for a bit. I probably could have listened in, but I was preoccupied with thinking about how painful paper cuts in your stomach would be. Eventually, they turned back around, with a small list prepared."
    y "N'alright, got my demands. They are limited to n'yot just the following, but include, at BARE MINIMUM!"
    y "1. I get to be the team MASCOT! Including but once again, n'yot limited to: 50 percent of all team merchandise earnings, t-shirts with me onn'em doing something cool like, breaking someone’s legs'r something, commemorative Dusk smoke lighters to celebrate me, and, uh..."
    y "Oh yeah, and if we win, then'ya gotta let me take the team to my favorite place to get grub t'eat n'yafterwards."
    y "SPOILER: it's very cozy."
    y "SPOILER-SPOILER: it's the sewer."
    "I waited for more."
    c "Wait, so- Is that your entire list?"
    y "LIMITED TO N'YOT JUST TH'FOLLOWING, BUT INCLUDE AT BARE MINIMUM! Were you not listening?!"
    c "You just numbered it, so I thought- If there was- But... Whatever. Look, what you're saying is that if we do that, you'll play?"
    y "Make it 70 percent instead of the 60 you suggested, an'you got a deal."
    c "Seventy?! Wha-where did-"
    c "Look, how 'bout we negotiate this a little, partner?"
    y "N'ylright! How's 85 percent sound..."
    c "O-kay that's- not really how negotiating regularly works, but I'm willing to improvise."
    c "What do you say about... the prize money, getting divided up equally among the team members, and I'll pay the tab on that post game dinner?"
    y "They don't have TABS in the sewer, idiot! You'd think you've never gone. But, fine. N'yi'm in. Still think th'n'you should do the t-shirt thing."
    c "Good, cool. I will... uh, keep that in mind, with the shirt thing. We'll be playing at Hell Valley Stadium in a few days, I'll see you then."
    hide dusk
    "I turn around and start to walk, to hear Dusk get in some argument about weather a peach was worth the same price as a pear. Whatever side they were taking, it was very loud."
    "That cat may have been stubborn as a mule, but I was hoping that would be a price worth paying in the grand scheme of the game. Next up was..."
    
   
    return
          

