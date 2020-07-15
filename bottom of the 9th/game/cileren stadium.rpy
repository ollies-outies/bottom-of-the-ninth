# Define l = character("Cileren")
# Define c = character("Casey")

label CilerenStadium:
    $ HasCileren = True
    scene bg stadium
    show cardcileren

    "Oh, fates be praised. Cileren Naezeros."
    "Cileren was a huge potential wizardball star, from the college circuit."
    "She was born into a family with more money than most city states, and she was raised with the best wizardball tutors that money could buy."
    "Myself included, actually."
    "She was shaping up to be the next big name, but fell in with what is commonly known as ''The Wrong Crowd.''"
    "Started missing games to be at parties, started ignoring tutilage, and kind of just fell from grace."
    hide cardcileren
    show cileren
    "I found her in one of the dugouts in the stadium, partaking of a pipe of Old Toby."
    c "Hey, pardon me kid, but you used to be Cileren Naezieros, right?"
    l "Why, who wants to know? You a narc?"
    c "Gods no. I promise, I just wanna talk, maybe make an offer."
    l "Not a nark, huh? Wanna toke up to prove it? I, uh... Wouldn't mind having someone to talk to, right now."
    
    menu:
    
        "Nah, I don't smoke anymore.":
            jump cileren_b1
    
        "Yeah, let me hit that.":
            jump cileren_b2
    
    label cileren_b1:
    l "That's chill, man. Peer pressure is lame-ass anyway, you do you."
    jump cileren_b3
    
    label cileren_b2:
    "I took a drag. Smooth, sweet. Much better than I anticipated a college drop-out to have. But, that's money for you. I passed the pipe back."
    jump cileren_b3
    
    label cileren_b3:
    "I found a spot in the dugout. It was the away team one, so it was a bit less than optimal, but it still had a nice bench, that I laid down on. Cileren was already sprawled out on the floor."
    c "So, what're you doing here, kid? I thought you quit the game."
    "Cileren took a long hit from her pipe, and blew out a ring of smoke."
    l "Alrighty Brosephina, You ready for some real home grown moody existential hours shit?"
    l "Sometimes, I’m not really all about that ''Fr@-Lyfe''TM. All the kickass parties and all-nighters... It can leave a bro kinda... overwhelmed, if you feel me. And anyways, most of the time I just do it so I’ll get into trouble."
    l "Seems like the only way I can get my parents to notice me, but it's pretty draining. When I was playing, no matter how good I was doing, never got anything from them. The second I mess up, though, they're on me like icing on a cake."
    c "... Shit, man. That's actually way heavier a revelation than I expected from this chat."
    l "And we're still in it, bro. Shit can be fun, don't get me wrong, parties may still MEGA smack in the best ways possible, but it all can just get so..."
    "She raised her hands, gesturing to nothing."
    c "Exhausting?"
    l "Yeah, man. Life can really be too much to handle for its own good, sometimes."
    l "Sometimes, I just need to vibe. And this place always reminds me of my days playing Wizardball. Most of my happiest memories are from back then, so... I vibe here."
    "I got partially up, enough so that I was looking at her."
    c "Do you ever wissh you could go back to your Wizardball days?"
    l "Maybe. Like, a lil bit, on the DL, you know?"
    c "Well, maybe it's better to talk about this when you're sober, but I'm putting a team together. Major League. We could use a player with your skills."
    l "Bro... do you really mean that?"
    c "Cross my heart. You in?"
    l "Might just be the pipeweed talking, but I am so fucking down for this, bro."
    c "Then welcome to the team, Cileren Naezeros."
    "She stood up, and saluted me, which seemed odd, but I saluted back. I told her about the first game, where it was gonna be played, and what to bring."
    l "I won't be late, man, pinky swear."
    c "Glad to hear it, kid. Keep vibing, yeah?"
    l "CAN DO, COACH."
    hide cileran
    "She's a good kid, going through some shitty times. Honestly, aren't we all, though?"
    "After vibing for a bit, there was..."

return   