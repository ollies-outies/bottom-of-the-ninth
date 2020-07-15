
# define c = Character("Casey")
# define t = Character("Trouble Comings")

label TroubleMarket:
    $ HasTrouble = True

    show cardtrouble

    "Trouble Comings. A bright young upstart in the minor leagues. Used to play for the Reinbachs, over in Joshua Tree. Best shot in the game, and a damn fine receiver too. He had a bright future ahead of him, all things considered." 
    "Except for one nagging issue, that is. See, Trouble had a massive debt to pay, thanks to his mom and pop bouncing out of he and his three siblings' lives the first chance they got."
    "Left poor Trouble to foot the bill of two lifetimes' worth of gambling and drinking, plus three hungry mouths to feed."
    "So, he did what any responsible person would do in that situation: Quit his passion, to continue the business his folks left behind."
    "Which just so happens to be based primarily in the hunting of men."

    hide cardtrouble
    show trouble

    t "God damn it! Which way did she go?"
    "I ran into him in the middle of a hunt, ya see. Some fool had made the mistake of pissing off the wrong person with the right amount of cash, which left a target on their back, the size of a barnyard door. "
    "And, as I previously mentioned, Trouble was a great shot. "
    "Issue was, Trouble was never the quickest kid in the park. Meaning anyone more fleet-footed than him could be out and away, just like that. "
    "What he needed was a Team. What he got was an entree plate of bad luck with a side order of bullshit. "
    "So, I decided to fill the niche."
    c "Trouble Comings, right? Need any help?"

   
    "Trouble gave me a look over, not quite sure what I meant, before realizing who was offering their service."
   
    t "Casey Conway?! I thought you’d curled up and died somewhere! Oh, d-uh... no offence."
    c "Well, I did move permanently into this backwater, so... you’re half right."  

menu: 
            "I said to him..."

            "You look like you need help, Comings.": 
             jump trouble_A1

            "Carrying on the family legacy, are ya know?": 
             jump trouble_A2

label trouble_A1:
    
    "He cracked a faint smile." 
    t "I certainly wouldn’t turn it down."
    c "It’s hard work, what you do. I might slow you down, with how well you’re doin’ it."
    "His smile faded, slightly."
    t "Thanks, C.C., but you know that this isn’t what I wanna do with the rest of my life." 
    c "You know, that reminds me..."
    jump trouble_A3

label trouble_A2:
    
    "He ruffled his brow, and gave me a curious look."
    t "Some of us gotta work to live, pal. Not all of us have boxes of cereal with our faces on them."
    "I raised my hands, shaking my head, giving a slight laugh."
    c "You know, I told my manager that brand deal was a bad play, but he insisted. No one wants clam flavored cereal, endorcement or not!" 
    c "Worst part of it all is that I got none of the residuals. It all goes to my old team."
    c "Which, reminds me."
    jump trouble_A3

label trouble_A3:
    c "I’m starting a new team, based here in Katabas. Calling ourselves the Comedians, due to uh... circumstances. Look, if you’re available, we’d love to have you play with us." 
    "Trouble's eyes lit up, and he almost toppled over, standing still. He hadn’t upped his footwork in the slightest, clearly."
    
    t "Uh? Yeah I?? Guess???"
   
    t "... wait, is it paid?" 
    c "It is paid, yes. Quite well, actually."
    
    t "Then yeah!? I’d- well I would need to finish this first, but I still want to play on your team after, can we do that? God, I’m sorry this is important, and we already signed a contract for this, so I would need to finish the hunt before I had any free time, and I don’t think that I can just leave on this, and oh god what am I gonna tell Strife I’m so sorry this is all just so much all of a sudden, I’m babbling and I’m just-"
    c "Kid." 
    
    "Trouble stops." 
    c "Let’s finish the hunt you’re doing, then get you signed up."
    
    "He smiled, big and wholeheartedly." 
    t "Hell yeah!! Hell!! Yeah!!!"
    "We talked strategy for a moment. It feels good to be working out the metaphorical strategic muscles before the big game."
    "Fate is a big decider in everything, but it’s strategies that make fate manageable."
    "'Course, that doesn’t mean that fate can’t just occasionally give you a boon, like, say, the target tripping in a nearby alleyway, making a racket and alerting you and your new companion that they are 1. prone and 2. Extremely nearby."
    "Without talking, Trouble leapt at them."
    "There was a small skirmish, but Trouble handily defeated the foe, finishing by tying them up. He then quickly popped back out."
    t "Hey, I’m gonna handle this, but where should I meet up with you?"
    c "We’re meeting the rest of the team in a few days, at Hell Valley Stadium."
    "Trouble’s face changes."
    
    t "Hell Valley? But I thought we were settled here. Why not in Katabas Park?"
    c "First game is an out of town one."
    t "We're gonna play our first game without any practice?!"
    c "If you don’t wanna come, that’s totally understandable, and the offer still stands, if'n we aren’t destroyed."
    # Show trouble neutral
    t "No, no, it’s fine. I’ll be there."
    "He looked refreshed, more steadied, and eager for the future." 
    t "I... Thank you for this, Coach. Really."
    hide trouble
    "He walked into the alley, grabbing the hogtied schmuck. He sent up a wave with his free hand, and I waved back"
    "Course, Trouble’s back is turned when I did, but the schmuck saw it. He waved with his hands tied, giving a jazz hand / spirit finger combo."
    "After that, of course..."

    return
