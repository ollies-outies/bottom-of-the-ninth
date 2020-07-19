# define c = Character("Casey")
# define o = Character("Ock")
# define a = Character("Ock and Shaw")
# define s = Character("Shaw")

label OckShawStadium:
    $ HasOckShaw = True

    show cardockshaw
    
    "Ock and Shaw. Two twins, but, legally, one player." 
    "See, back in aught six, there was a massive hullabaloo about a Gorgon in the Major League."
    "The opponent’s team argued that since each snake on the Gorgon's head was alive, they had to count each as a player, and thus the Gorgon should be disqualified, due to an overstaffed team."
    "This then led to the creation of Euryales Law, named after the Gorgon, wherein any multiminded player, so long as all minds present and accounted for are working as a unit, instead of on multiple strategies at once, could be registered as one player."
    "While this was mostly a good thing, there were a few people who tried to use it to their advantage. Some hydras, an odd cerberus or two, but none were as effective, or out of left field as Ock and Shaw."
    "Most people didn't even realize that something fishy was going on, until they were ''Brutally Bisected'' during one of their games."
    "In reality, they just finally got knocked off each other's shoulders."
    "They're two peas in a pod. Two sides of a coin. And so on."
    "'course, when I found em up in the bleachers, you could hardly tell."
    
    hide cardockshaw
    show ockshaw apart
    
    
    s "It's always about you, isn't it, huh? Just cause you're the face, you think you're better than me?"
    o "Think?! I don't think anything, shortie, I KNOW."
    s "You're about to know the fuckin' PAVEMENT if you don't apologize."
    o "Oh, is that a threat? Are you threatening your own flesh and blood?"
    "There was a rumor going around that Shaw wanted out. That after being pushed around for too long, they wanted to turn heel."
    "One-sided coins don't exist for a reason. It only makes sense that they'd be fighting."
    "Ock doesn't want to be left in the dirt, arms, but no legs, and Shaw's the exact opposite."
    "I figured I ought to try my hand at helping."
    c "'scuse me, gents, I-"
    "They stopped bickering to turn to me, and before I can make a suggestion, Shaw starts up."
    s "Oh thank the gods, an outside judge. This shit was going NOWHERE, we can agree there."
    o "You got me there."
    a "You got me there." 
    "The twins nodded at each other, then approached."
    s "Okay, stand here, and tell us which one."
    "They pushed me into a seat, and stood back to back, both obviously wriggling to straighten themselves out more."
    a "C'mon, tell us! Which one of us is taller?"
    "Obviously, whoever was stretching the longest was the tallest, if only for a moment, but all things considered... To say that they were identical twins would answer the question."
    "But something told me they weren't looking for something neutral. So, I bit the bullet, and just chose one at random."
    menu:
        c "The one who's taller is..."

        "Ock":
            jump oands_B1

        "Shaw":
            jump oands_B2

    label oands_B1:
    o "HA!" 
    s "Man, alright."
    jump oands_B3

    label oands_B2:
    s "HA!"
    o "Man, alright."
    jump oands_B3

    label oands_B3:
    "The two swapped headbands, then took their trademark position, the previous green Headband wearer now on the bottom."

    show ockshaw together

    a "Thanks for that, pal. Solved this for sure."
    s "Yeah, at least until my next growth spurt."
    o "Oh! You think you're gonna get FED? After that RUDENESS?" 
    "And just like that, they were bickering again. I... I thanked fate me and my sister weren't like this. I couldn't help but laugh."
    c "Oh, gods, you had me genuinely worried there. I heard that Ock had... No, Shaw was... One of you wanted to leave."
    a "Can you really not tell us apart?"
    c "... Can you?"
    "We shared a thousand yard stare for a moment."
    a "... I think I was Shaw, starting out."
    a "No, that was me! God, you would, huh?!"
    c "Hey, hey. Shut up for a second."
    "They surprisingly do, rather quickly."
    c "I approached you when I thought you were fighting 'cause I wanted to solve that sitch by offering you a place on the Katabas Comedians."
    "They let the offer sink in, then practically throw each other away, and strike dramatic poses."

    show ockshaw apart

    o "Oh, I could never work with you again! You villain, cad, bully and thief!"
    s "Well, my good fucker, you will find that you are glue, and I... I am rubber!"
    c "Okay, if you keep this up, I'm taking my offer back."
    "And just like that, back on each other's shoulders."

    show ockshaw together

    a "We'll behave."
    c "Here's hoping. First game's in Hell Valley Stadium in a few days. Don't be late."

    hide ockshaw together

    "As I turned to walk away, I could faintly hear insults and shouting."
    "... I ought to call my Sister."
    "Next up..."

    return
