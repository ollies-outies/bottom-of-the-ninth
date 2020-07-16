# Define du = character("Dusk")
# Define c = character("Casey")

label DuskMarket:
    $ HasDusk = True

    show carddusk

    c "They say curiosity killed the cat, but when it came to Dusk Darkness, curiosity made them more powerful than they ever could've imagined."

    c "Delving into the arts of necromancy at a very young age, Dusk soon became quite accustomed with all things dead, and mostly deadly."

    c "Necromancers were few and far between in the Wizardball minor league circuit, allowing Dusk to make a name for their feline self out on the field."

    c "Unfortunately, skills in dealing with the dead don't always translate into skills when dealing with the living."

    c "This was undoubtedly gonna be a tough one."

    hide carddusk

    show dusk

    du "HEY! PUNKOSAURUS!"

    du "N'you staring n'yat me or somethin'?!?"

    c "My apologies, I simply recognized you. You're a Wizardball player, right? Used to play for the Danderville Scruff-Necks?"

    du "Maybe n'yi did! Maybe n'yi didn't! what's it to n'you!?"

    menu:
    
    "I was already off to a less than ideal start, so I dropped any grand argument I had planned on weaving and simply said:"

        "I'll give you some salmon if you hear me out.":
            du "N'you tryna patronise me just cause N'yi'm fuzzy?! N'yi'll have n'you know n'yim n'yalergic to salmon!"
            c "I didn't get a single word of that. Anyways, don't you miss being able to pummel your enemies into the dust?"

        "I'm starting a Wizardball team, you in? or are you out?":
            du "Well... what would be n'yin it for me?"
            c "You'll get to cause severe bodily harm to an enemy team member."
            
        after_menu:
            
    du "I do like hurting things…"
    
    du "But N'yi don't need to be n'yon n'ya wizardball team to do that!
    
    menu:
    
    "I was loosing ground."
    
        "Dusk, I'm pretty sure thats called a felony."
            du "Well... N'yi don't know what that means so, take that!"
            
        "That's... technically true dusk, but why just hurt people when you can hurt people and get a sport trophy about it.
            du "Trophies N'yare N'ya capitalist monolith designed to quantify meningless actions N'yin N'yorder to sate the masses just N'yenougn to keep them complacent! N'yor N'yat least that's what N'yit said N'yin the book N'yi N'ate last week...
            
      after_menu:
      
      c "I'm frightened but admitantly a little impressed."
    
        
    

    c "(They got the world record two seasons ago for most red cards earned in a single game. I need their ferocity on my team.)"

    du "N'you know what?! N'yive done some thinking and…"

    du "N'yi wanna do it! Get me on your team!"
    
    hide dusk
    return

