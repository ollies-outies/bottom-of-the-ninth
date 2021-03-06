﻿# Define z = Character("Diver")
# Define c = Character("Casey")

label DiverStadium:
    $ HasDiver = True

    show carddiver
    " "
    "The first thing that stuck out to me was the suit."
    "Diver. I'd heard of them before. Some unthinkable horror, stuck inside some long forgotten diving suit, decided to come up and play."
    "I was intimidated, to say the least, trying to find them. I'd never interacted with them, and most games they were in ended up a bit non-euclidean."
    "But, rules have changed. Ever since Yharnum's law, Eldritch entities are actually more welcomed. Turns out, tentacles make for great slingers."
    "So when I saw that dripping suit, standing along the rows of chairs, watching the field in the stadium..."
    hide carddiver
    show diver
    "I figured, I'd take my shot in the dark."
    c "Ah, pardon me, pal. Don’t mean to pry by asking this but... Wouldn't you get a better view of the, uh... nothing, if you had front row seats?"
    "They turned quick to me, and in a voice that was much lighter than what I had expected, said-"
    z "I-I'm sorry, are... you talking to me?"
    c "... No, I'm talking to the other tentacle filled bathy-suit up here."
    "They actually turned to look for another one."
    c "Sorry, sorry. I was being sarcastic. Yeah, I'm talking to you, bud."
    z "Ah! W-well, I'm doing this for safety. I've gotta keep my distance, or-"
    "They must have realized I was standing next to them, and let out a scream I can still hear in my nightmares."
    z "P-p-p-pardon me!! You'd better get out of here as fast as you can!! If you don't you’ll probably just wind up getting hurt or something..."
    "They clammed up further, and I let out a laugh."
    c "You know, not to be rude or anything, but I hardly feel threatened right now."
    "There was a moment, and they unfolded, looking up at me."
    z "...Really?"
    c "Really really. Now, seriously. What are you doing up here?"
    "I sat down in the chair next to them, as they started to explain."
    z "W-well, I was born in the fifth house of empty sorrow within the vast eldritch nothingness of the cosmos."
    c "Of course. Classic."
    z "Both my parents are elder-gods, which is... r-really cool, and I love them very much."
    z "But, it means the very sight of my be-tentacled self can drive mortals to insanity."
    c "Not so cool."
    "They nodded."
    z "Normally, I wear my suit to help people be able to see me, but..."
    "They sighed, or at least did something that looked like sighing."
    z "I was playing a game of Wizardball today, back in the city, but a quarter through, my helmet got knocked off."
    z "Half the other team were transported to the 8th Nowhere, which was embarrassing, and the other half made fun of me for my tentacles!"
    c "Which was more embarrassing."
    "They nodded, rapidly. I sunk a little further in my seat, just thinking about what it took me in my heyday to instantly take out half of the enemy team."
    "They did it accidentally, and were embarrassed about it."
    c "Jeez. Sounds like that really got to you."
    z "The worst part is, I had just started getting confident about my appearance."
    z "I would look in the mirror at that writhing mass of tentacles and actually feel happy. Like I had looks I could be proud of! Or-or at least be okay with. That would be enough. But then they went and tore it all down..."
    z "Son of a... gosh, people can just be so mean sometimes."
    c "Amen to that, pal o’mine. Amen to that."
    "They turned to me, insides wriggling as they did."
    z "Hey, you seem pretty cool. What would you have done in my shoes?"
    
    menu:
        "I thought for a bit, and told them..."
    
        "I'd beat the snot outta them, for thinkin' they had the right.":
            jump diver_b1
    
        "I'd tone 'em out, focus on what actually mattered- the game.":
            jump diver_b2
    
    label diver_b1:
    "They looked at their hands, one glove missing."
    z "I'm not very strong, though..."
    c "But that's why you have your team with you! People who're there for you, thick and thin, to make up for what you lack."
    c "And when then they hear that you've been made fun of, they should be there to tell you what a great person you are, and to kick the everloving shit outta anyone who says otherwise."
    z "R-really?"
    c "Well sure, that's what I used to do."
    "They looked down, clamming up."
    z "T-tell you the truth, my team are scared of me too."
    z "I hear them calling me names, and they never invite me out with them when they celebrate."
    "I damn near broke the chair, I slammed my fist down so hard. Diver bolted up."
    c "That's bullshit! You're the MVP, they should be buying you dinner every day!"
    c "What you need, pal, is a support system. And I think I know just where to get you one."
    jump diver_b3
    
    label diver_b2:
    "They looked at their hands, one glove missing."
    z "I... I suppose. I do love the game, and all."
    z "I just... their words still hurt, you know? And no matter how good I play, they're still going to look at me like I'm something weird, to be feared."
    z "Even my own team treats me weird."
    "We sat in the bleachers for a while, looking out at the grassy field. I eventually sighed, and said..."
    c "Sorry, pal. I was kinda goin’ for a whole big uplifting speech thing but it kinda fell short."
    z "That’s okay, hehe. I’m really bad at speeches too."
    c "You know what, maybe the whole idea that we have to be feeling amazing at every moment is eight kinds of wack. Sometimes, you just feel okay, and that's absolutely fine."
    z "Yeah... Yeah, I get that. I-it makes the happy days seem even happier-er than they did before, in a way."
    c "That being said, your team treat you weird?"
    z "O-oh, yeah. They make fun of me, for being so... wiggly, and they never invite me with them when they do things."
    c "I hope you don't mind me saying, but that's bullshit."
    c "Teams are supposed to look out for each other, and be there when they need each other. And instead, here you are."
    c "Stuck with me, up in these bleachers."
    c "That being said, actually, that does remind me."
    jump diver_b3
    
    label diver_b3:
    c "I'm starting up a team, here. We've got a game down in Hell coming up, and fittingly, a hell of a line up so far. We'd love to have you join us."
    "They looked at me, rather calmly, but I could tell from the squirming under the suit that they were excited about the idea."
    z "M-m-major league? A-are you sure you'd want me?"
    c "100 percent positive. There's no one like you in a million miles, kid."
    z "Wow, I... I guess you're right."
    "I extended my hand."
    c "Name’s Casey, by the by."
    z "Oh, I'm Y’gthangsogy’rislil-Aiuevh'icn'kris-Mhymbrerc-Graodrross-Aiuectaiothr'endu-Abhaodhrexz-Ngiogr'gnish-Ctheg'itros-Iuvh'iolda-Oshyjh'thin."
    z "But my friends call me Diver!"
    "I blinked, my ears slightly ringing. I'm fairly certain my nose was bleeding, as well."
    c "It's... a pleasure to meet you, Diver."
    hide diver
    "After shaking that true name from my head, I had..."
    
return

