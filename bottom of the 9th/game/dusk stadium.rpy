# Define y = character("Dusk")
# Define c = character("Casey")

label DuskStadium:
    $ HasDusk = True

    show carddusk
    
    "They say curiosity killed the cat, but when it came to Dusk D'arcnes, curiosity made them more powerful than they ever could've imagined."
    "Delving into the arts of necromancy at a very young age, Dusk soon became quite accustomed with all things dead, and mostly deadly."
    "Necromancers were few and far between in the Wizardball minor league circuit, allowing Dusk to make a name for their feline self out on the field."
    "Unfortunately, skills in dealing with the dead don't always translate into skills when dealing with the living."
    "This was undoubtedly gonna be a tough one."
    
    hide carddusk
    
    show dusk
    
    y "N'YOUT OF THE WAY, N'YUMBSKULL!"
    "I found them sitting, front row, looking out at the empty Wizardball field."
    c "I beg your pardon but, what are you doing?"
    y "Watchin'..."
    "Their eyes squinted with the intent of a predator staking out their prey from afar."
    c "And... what might you be watching?"
    y "The GAME, dummy! The n'yone that you're blocking my view n'yof!"
    c "But… There's no game going on right now."
    y "Uhm, YEAH, n'yi know that? But what if there WAS!?"
    y "Then n'youd be the piss-baby-spinach-brain blocking it!"
    c "...I mean you're technically not wrong but-"
    y "COURSE I'M N'YOT WRONG! N'yow beat it!"
    "They sat deeper in their seat, and tried to look around me. This was going well so far."
    c "Listen, my name is Casey Conrad Fisk, and I’m forming a pro Wizball team. I came here to recruit you. So, you wanna join up?"
    y "Why, in n'ya world would I DO somethin' like THAT?!"
    y "FIRSTMOST, I'ven't played in like, two years."
    y "N'yand SECONDMOST, n'yor team uniforms are probably stinky!"
    "I waited for a thirdmost that never came. They sat, intently staring at me, waiting for a rebuttal."
    menu:
       "So, I feebly said..."
 
        "Why in the world is scent something that came to mind? We can clean things, you know.":
            jump dusk_B4 
      

        "You'd be missing out on all the fame and adoration of the roaring crowd if you didn't join.":
            jump dusk_B5 
         
    label dusk_B4:
    y "Why in nya world're you, the dumbest Wizardball coach who ever coached Wizardball, huh?! You moronic, rock-eatin' coach!"
    y "Do you have n'yany idea how supremely sensitive and exacting a feline’s sense of smell is? Do you? Of course not, n’you brainless mound of steaming worm dung."
    c "Right, sure, but what are you basing the assumption on?"
    y "Oh, jeez, I dunno, maybe th'team's coach, who n'yapproached me smelling like, n'and I repeat myself, A BRAINLESS MOUND OF STEAMING WORM DUNG."
    jump dusk_B6
    
    label dusk_B5:
    y "N'yi couldn't give a rat's ass what the crowd thought of me."
    c "I seriously doubt that. We all say we don’t need the roar of the cheering fans, but you must admit, every cat loves to be loved."
    y "N’you got that back-assward, chump! N’yeveryone wants to be a cat. N’yain’t you ever heard that before, or are n'ya just a n'yimrod?"
    
    label dusk_B6:
    c "Fine, fine, but that aside, don't you miss the excitement of the game? The feeling of absolutely trampling the enemy team on your way to victory?"
    y "N'yi am a fan of trampling them fools, what n’yeed trampling... buuuut, n'yI've got a nap scheduled for the n'yext, oh I dunno... year and a half so... n'yi don't think I'll be able to fit n'your little team n’yinto my schedule."
    "I sighed, and put my hand to my face, rubbing my temples."
    c "You know, at this point I'm not even surprised."
    y "N’y’know, if n'yi were as washed-up as you, n'yi would feel the exact same way!"
    c "Hey now. I'm the one taking the initiative to put a team together. The Katabas Comedians."
    y "Hey, don’t you fret! N'you don't need to make excuses for yourself, n'yow."
    c "I don't even know why I'm here talking to you. This is going nowhere, and fast."
    "I knew that I needed to get them on the team, or else whatever Fate's plan was would fall apart, but my gods, it couldn't've been worse than this, and it was starting to get to me."
    "I hopped the fence, and started to walk the field, desperate at an attempt to calm down somewhat, before diving headfirst back into Dusktown."
    y "HEY! WASHUP! N'YOU GONN'YA MOVE OR WHAT? N'YOU'RE GETTIN' IN TH'WAY N'YOF THE GAME, HERE!"
    "That one hit harder than the other insults, for whatever reason. Maybe it was because an empty field was preferred viewing to one with me on it, or the fact that I had some deeply repressed feelings being back on the green that Dusk brought forward, but either way..."
    "I turned around, ready to lay into them, but nothing came out."
    "No witty retort, no denial. Just... nothing."
    "I wasn't a washup. I was making a whole-ass team, guided by the strongest Force in the world, and we were gonna change the face of Wizardball."
    "But it wasn't that, was it? That wasn't the goal. There was no conquest to overcome. There wasn't a dragon to slay. There was no quest, no fanfare."
    "Just a sad, lonely attempt at bringing something back that I missed."
    c "...I really am just grasping at something I don't have, aren't I? Just a... A greedy old bastard, not ready to give up glory."
    y "Hey, n'you said it, n'yot me."
    "I looked at the ground, avoiding Dusk's gaze."
    y "Which, n'yisn't to say, that that's a bad thing, necessarily."
    y "It's hard ownin'yup to somethin', let alone somethin' of that particular m'yagnitude."
    y "Wantin' somethin' you don't got is the first step in'yobtainin' that purrticular somethin'."
    y "And ackn'yoliging your shortcomings is the only way to overcome 'em, I say."
    y "So... Maybe you ownin'yup to how n'your feeling about this'll help you more than'nything else."
    "Shocked isn't the right word. I was surprised, and a bit taken aback by how astute Dusk was. The words that I had wanted to say to Dusk when I first turned made their way forward, much stranger and different than what I expected."
    c "I.. I’m a washup."
    y "Hnm? What was that?"
    c "I'm a washup!"
    y "N'you bet your ass you are!"
    c "HELL YEAH I AM. I'M A WASHUP!"
    y "N'YAND WHAT N'IS THIS TIRED OLD WASHUP GONNA DO?!"
    c "FORM THE BEST GODS-BE-DAMNED TEAM EVER!"
    y "N'YAND WHAT N'YARE THEY GONNA DO WITH THAT TEAM?!"
    c "WIN SOME GODS-BE-DAMNED WIZARDBALL!"
    "I breathed a sigh of sweet relief after my outcry. The words still rich on my tongue, echoing through the stadium. I'd thought them before, sure, but it was this moment I wanted them realized."
    c "Shit... you were right. That was... cathartic."
    y "Good. Oh, and for n'your information, n’yI made up my mind about 5 minutes ago."
    c "What are you talking about?"
    y "The team, n’you thundering simpleminded cretin! N'yI wanted to play on'yer team from the moment n'you actually pitched it to me."
    "I wasn't even mad. I laughed a little at the absurd awfulness of it and then asked..."
    c "If you already wanted to play, why did you give me such a damned hard time?"
    y "N’I'll let you decide if it was because n'yI could tell th'you were down in the dumps'nd n'yeeded a little help, or because n'yI like to create problems to see how they eventually resolve themselves. Like fire, for n'yinstance."
    "I wracked my brain for some clever retort but in this moment, I just sighed and took in my revelations."
    c "Welcome to the team, Dusk"
    "I filled them in on the details, and after some promises of logo alterations and alternative forms of payment, namely any corpses accumulated, they promised to meet me at the stadium."

    hide dusk

    "That was one obligation done. Here's hoping Fate knew what it was doing. Next up, was..."


return


