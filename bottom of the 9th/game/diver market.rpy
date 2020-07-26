# Define z = Character("Diver")
# Define c = Character("Casey")

label DiverMarket:
    $ HasDiver = True

    show carddiver
    " "
    "The first thing that stuck out to me was the suit."
    "I'd heard about Diver before. Some fisherman scooped up something unknowable from the bottom of the ocean, off the Varicinian Coast."
    "Damn near lost his mind, but the thing scuttled into a nearby bathy-suit, and walked the fisherman through therapeutic breathing exercises."
    "Since then, thing's been on land, trying to deal with society. And because of Fate's funny hand, it ended up in the minor circuit."
    
    hide carddiver
    show diver
    
    "And, in the Katabas market square, trying out free samples of various pastries from a local bakery stall."
    "I approached them, snagging a bitesized croissant as I did, and took a shot in the dark."  
    c "Say, pal. You wouldn't want to be in the Major Leagues for Wizardball, would you?"
    "They didn't react, until they noticed that the baker wasn't taking me up on the offer. Slowly, they turned to me, and, in a voice that I did not in any anticipate this monster having, said"
    z "A-a-are you t-talking to me?"
    "Like a fourth grader, reading a book report. I was stunned for a moment, and then eventually followed up with..."
    c "Yep. I figure, a big strong body like that, you'd be a shoo-in, and I would know."
    z "Oh, oh no, this isn't strong. Look!"
    "They wiggled the entirety of their insides. While it seemed humanoid, there wasn't a bone in that entire suit."
    z "I-it's an easy mistake to make, I think. S-see, I was born in fifth house of empty sorrow within the vast eternal last nothingness of the cosmos."
    "I nodded."
    c "Of course, that makes sense."
    z "S-so the fact remains that no mortal entity can fully comprehend my grim v-visage without going mad... hence Suit."
    "I nodded again."
    c "This is some very specific verbiage you're using, pal."
    z "M-my therapist told me it makes understanding easier if I use words like that."
    c "Ah. Well, still, allow me to make my acquaintance! Name’s Casey. And you are...?"
    z "Oh, well, my name makes people's ears bleed if they hear it."
    z "B-but my friends call me Diver."
    c "Pleased to meet you, Diver. So, like I asked earlier, you wouldn't want to be in the Major Leagues of Wizardball, would you?"
    "They wriggled, for a moment, then stopped."
    z "O-oh, well, I mean... I'd love to, but I'm not so sure about... the safety of it."
    c "How so, bud?"
    z "Well, m-my last game, I was playing great. Blocked well, got a point in..."
    z "B-but after one of their Handguards rushed me, they knocked my helmet off."
    z "T-they're still trying to find the audience members that were sent to the 8th Non-euclidean Nightmare Zone."
    z "A-and those that didn't get sent there made FUN of me, for my weird shaped head!"
    z "I would be so embarrassed if something like that happens again..."
    "I've been in those kinds of situations before. I think we all have."
    menu:
        "And when I was that down in the dumps, what I wanted to hear was.."
    
        "Don't worry! If anybody makes fun of you we can beat the living shit out of them, as a team!":
            jump diver_a1
    
        "What they say about you doesn’t matter. You’re a beautiful tentacle monster and you shouldn’t let anyone tell you otherwise.":
            jump diver_a2
    
    label diver_a1:
    "They perked up, when I said that."
    z "R-really?! You would do that for me?!"
    c "Course! The whole team would. We look out for each other, you know?"
    z "Wow... I’ve never had someone promise to beat the living shit out of people for me!"
    jump diver_a3
    
    
    label diver_a2:
    "I saw that two spots near where their cheeks would be were heating up and glowing a bright red. I took that for their approximation of blushing through a brass helmet."
    z "Oh... Oh my gosh... I've never had someone tell me that before..."
    z "Do you really mean that?"
    c "I am saying this with 100 percent sincerity, that you are without out a doubt, the coolest, cutest, best tentacle monster in a diving suit that I've seen in my entire life."
    z "Wow... I've never had someone say something that sincere to me!"
    jump diver_a3
    
    label diver_a3:
    z "D-d'you really think I'm good enough for the team?"
    c "I wouldn't be asking if you weren't. And if you're still worried about hurting someone, we'll get you a new suit, with a better latched helmet."
    "They were wriggling non-stop, now."
    z "Then yes! I'll do it! I'll join your team, Coach!"
    c "Fantastic. I'll see you in a few days, in Hell Valley Stadium for our first game."
    z "See you then!"
    hide diver
    "I snagged another croissant bite, as I turned to walk away."
    "Next up was..."
   
return


