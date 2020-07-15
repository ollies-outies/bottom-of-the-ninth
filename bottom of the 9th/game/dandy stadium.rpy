# Define f = Character("Dandy")
# Define c = Character ("Casey")

label DandyStadium:
    $ HasDandy = True

Scene bg stadium
Show carddandy

    "Alouicious Dupris. ''Dandy'', to her fans. So, I called her Dandy."
    "Dandy was everything that made wizardball great, in it's hayday. A true sportswoman, she played fair, and always hit above the belt, so to say."
    "But as time went on, she went from classic to tacky. New rules were added, that she didn't play around. New magic was discovered, that she didn't learn."
    "New blood came into the game, and brought new skills and abilities, and she never adapted to it."
    "Fundamentals, she knew, but it was what the game brought with time that made people think she was stagnant."
    "Course, anyone who knew her would say that was a load of-"
    f "POPPYCOCK!"
    
    hide carddandy
    show dandy
    
    "I found her in the halls of the Katabas stadium, pounding on the bar of some conscession stand."
    f "NO ONE IN THEIR RIGHT MIGHT WOULD SPEND THAT MUCH FOR A HOTTED DOG, BALLPARK OR NOT! WHY, I COULD BUY MY OWN MEAT GRINDER AND HOG ANUS FOR THAT PRICE!"
    "No one was at the stall, so it seemed she was just yelling for the sake of being loud."
    f "DO YOU COAT YOUR NACHOS IN GOLD? IS THAT WHY I'D HAVE TO TAKE OUT A MORGAGE TO BUY A BASKET?"
    f "WHAT ABSOLUTE HORSE HOCKY!!"
    "She knocked over a stack of large disposable cups, and started to stomp off."
    "She then turned around, restacked the cups as they were, then turned back to continue her huff."
    "Course, that's when she ran into me."
    f "Oh my- Casey Conrad? Is that you? I'd've heard you took one last dirt nap, and shimmied off this mortal coil! But, ha! In the flesh, more or less!"
    c "It's good to see you too, Dandy. You uh... looking to get some food?"
    "She turned back to the stand, ashamed."
    f "Well, ah, you see... I... How much did you see?"
    c "Just the tail end. Speaking of which, I had no idea you knew the going price of hog anus. I've got to say, I'm impressed."
    "She sighed, and made her way to a nearby bench, opposite from the stall. I took a seat next to her as she started."
    f "It's just... Well, it's hard to put into words without sounding too crotchety, I suppose."
    c "Go ahead, I won't judge."
    f "... This whole stadium's changed so much. The... trophies are so much bigger, now."
    "She looked like she was going to continue, but she stopped herself. We sat in companionable silence for a moment, my mind thinking back to when I was a kid."
    c "... This used to be a sideshow, right? This stall?"
    "She perked up when I mentioned it."
    f "Ah! Ah! Yes, yes it was! Full of, ''Antiquities and Curiosities''!"
    c "Right, right! When I was a kid, and I would watch games... Well, that was back when the game was still turn based, right? So, during those long charge rounds, I'd sneak out of the bleachers, and make my way down here."
    f "Truth be told, whelp, so did I. Whenever I was benchwarming, I'd try to mosey down here, and grab a candy floss."
    c "Oh, those were the best. And the uh... The Dancing Automaton? Was that was it was called?"
    f "You got it in one! You could feed it change, and it would cut a rug like nothing else."
    c "Didn't it gain sentience a few years in?"
    f "Joined the league, iffin I recall correctly. Played for the New Throughfare Candlestick-makers. Handguard."
    c "Right, right. Good times."
    "We were reduced back to silence, for a moment."
    f "... I'm getting old, C.C.. Far too old for my liking."
    f "I wouldn't mind the shakier joints, but it feels like everything else is getting younger."
    f "Shinier, sleaker. Better off. And, in a sentimental way, I'm proud. I'm happy, even."
    f "I just wish that I could still be a part of it."
    "She sat for a moment, gathering her thoughts again."
    f "I know I'm just a relic of a woman, now. Some novelty that people keep on their shelves, to oggle and gaze at, and to go ''How quaint!'' before moving on to the next curiosity."
    f "I guess, I'm just worried that the game's outgrown me, or I've outgrown the game. That my appeal'll stop, and I'll be replaced, by... by some..."
    "She gestures to the food stand."
    f "I don't want to be remembered as simply, what came before."
    "She had finally broken through, and I just sat there, not knowing what to say. I wish I had some words of wisdom, some pep talk that could sway her away from her thoghts. But, nothing was coming."
    "So, I just changed the topic, and told her..."
    c "I'm starting a Major League team based outta here, and I think you should be on it."
    "She gave a tired smile, and looked at me."
    f "Why do you think that, child? I'ven't played the game in an odd 20 years, and the last thing I was thinking about doing was playing again."
    "I needed to convince her, once and for all, that she deserved to play."
    menu:
    
    "So, I asked her to join the team..."
    
    "For my sake":
    jump dandy_b1
    
    "For her sake":
    jump dandy_b2
    
    label dandy_b1
    "I sighed, and got ready for an introspection of my own."
    c "Growing up, it was you, and your love of the game that sparked mine."
    c "And as I'm sure you know, a lifetime spent loving the game is a lifetime well spent."
    c "I was forbidden from ever playing again, but fate's given me this chance to try it again, from a different angle."
    c "And... As foolish as it is, I've been hoping that it all falls together."
    c "That, this whole cockinany scheme pulls through. All of it, to..."
    "I think to V, and my throat freezes up. I clear it."
    c "To do right by someone.":
    jump dandy_b3
    
    label dandy_b2
    "I shifted myself on the bench, so I was looking directly at her."
    c "Dandy, when I was 10, I saw you on the screen for the first time. I can recall the exact end score, each play by play, the entire game's been on loop in my mind, since I was in grade school."
    c "To say that you inspired me is an understatement. You defined me."
    c "You defined an entire generation, Alouicious Dupris."
    c "So, please trust me when I say that you are nowhere near done. There's a hundred thousand kids out there, each locked to their screen, who've... who've only just seen this as a food stall."
    c "There's gotta be someone, to tell them about back when it was still a fair, or else they'll never know."
    c "And once they know... they might want to see, for themselves."
    jump dandy_b3
    
    label dandy_b3
    "I tried to think of more words, but stopped, turning to face the ceiling. Her gaze had never left the floor, but her expression changed."
    "It went from something soft, something abandoned, to something determined. Something rigid, and prepared."
    "She stood up from the bench, then, hands in fists. She wanted to say something, I could tell."
    "Something, profound. Something that told me that everything would be better, now. Something that meant the start of something new, while remembering the old. Something, that signalled the creation of a new classic."
    "What she finally decided to say, was"
    f "Lets kick some ass."
    "Which, I think worked even better."
    hide dandy
    "After Dandy, there was..."
    
