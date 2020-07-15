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

        "I'll give you some salmon if you hear me out.":
            du "N'you tryna patronise me just cause N'yi'm fuzzy?! N'yi'll have n'you know n'yim n'yalergic to salmon!"
            c "I didn't get a single word of that. Anyways, don't you miss being able to pummel your enemies into the dust?"

        "I'm starting a Wizardball team, you in? or are you out?":
            du "Well... what would be n'yin it for me?"
            c "You'll get to cause severe bodily harm to an enemy team member."

    du "I do like hurting things…"

    c "(They got the world record two seasons ago for most red cards earned in a single game. I need their ferocity on my team.)"

    du "N'you know what?! N'yive done some thinking and…"

    du "N'yi wanna do it! Get me on your team!"
    
    hide dusk
    return

