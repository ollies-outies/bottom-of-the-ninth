# Define w = character("Dusk")
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

    w "HEY! PUNKOSAURUS!"
    w "N'you staring n'yat me or somethin'?!?"
    c "Oh, uh... My apologies, I just recognized you. You're a Wizardball player, right? Used to play for the Danderville Scruff-Necks?"
    w "Maybe n'yi did! Maybe n'yi didn't! what's it to n'you!?"
    "I was already off to a less than ideal start, so I dropped any grand argument I had planned on weaving and simply said:"
    c "I'll give you some salmon if you hear me out.":
    w "N'you tryna patronise me just cause N'yi'm fuzzy?! N'yi'll have n'you know n'yim n'yalergic to salmon!"
    c "I didn't get a single word of that. Anyways, I'm starting a Wizardball team, you in? or are you out?"
    w "Well... what would be n'yin it for me?"
    c "You'll get to cause severe bodily harm to an enemy team member. Don't you miss being able to pummel your enemies into the dust out on the field"
    w "N'yi mean that was fun 'n n'yall but why would n'yi want to go back to playing when n'yi can harm whatever n'yi want whenever n'yi want?"
    c "Dusk, I'm pretty sure that's a felony
    w "Well... N'yi don't know what that means so, take that! Besides wizardball has n'yall those dumb-stinky rules n'you need to worry n'yabout."
    c "That's... technically true dusk, but why just hurt people when you can hurt people and get a sport trophy about it.
    w "Trophies N'yare N'ya capitalist monolith designed to quantify meningless n'yactions N'yin N'yorder to sate the masses just N'yenougn to keep them complacent! N'yor N'yat least that's what N'yit said N'yin the book N'yi N'ate last week..."
    c "I'm frightened but admitantly a little impressed."
    w "Purrcicely what N'yi was going for!"
    menu: 
      
          "[LAUGH]"
           jump dusk_B1
  
          
          "[DON'T LAUGH]"
           jump dusk_B2
              
          
    label dusk_B1:
    "I saw Dusk glare at me with the silent rage of a courpse hearing people talk shit at their open-casket funeral."
    c "Dusk, I don't really have all day to talk about this with you."
    w "N'i'm n'yaware!"
    jump dusk_B3
      
    label dusk_B2:
    "I knew the dangers of angering this fickle feline and did not wan't to test them."
    w "Do n'you have n'yanything n'yelse to say n'yor n'yar n'you just gonna stand there like 'n'ya big dumb pile n'yof slugs?
    c "I feel like I should take offense to that but honestly I just don't have it in me right now."
    w "N'yoh n'yis that SO?! Dumb little slug pile wanna n'yeat some rocks n'yor something? Slugpile headass"
    jump dusk_B3
      
              
    dusk_B3
    "This conversation was going nowhere faster than a gravy train."
    c "Work with me here. You don't want your claws going dull do you?"
    c "All time without practice is gonna put quite the damper on your skills."
    w "N'you know what?! N'yive done some thinking and…"
    w "N'yi wanna do it! Get me on your team!"
    c "Alright!"
    w "N'yon N'yone condition."
    c "Fuck."
    w "N'yi get to be the team MASCOT! N'yincluding but not limited to: 50 percent n'yof n'yall team n'yearnings, t-shirts with me n'yon them doing something cool like breaking someones legs n'yor something, N'YAAAAAND, N'yif we win n'yi get to take the team to my favorite place to n'yeat n'yafterwords."
    w "SPOILER: N'yit's very cozy.
    w "SPOILER-SPOILER: N'yit's the sewer.
    c "So what you're putting down is if we do all that you'll play for the team?
    w "Make n'yit 70 percent n'yof n'all n'yearnings n'yinstead n'yof 60 n'yand n'you got n'ya deal"
    c "Now now, wait just a very long second! Why did you go all the way up to 70?!"
    w "Consider n'yit colateral."
    c "Do you even know what that means, Dusk?"
    w "Well... no. But N'yi won't need to worry n'yabout that with n'yall the prize money n'yimma have!"
    c "How about we negotiate this a little, partner."
    w "N'ylright! How's 85 percent sound..."
    c "O-kay that's not really how negotiating is supposed to work but uhhh..."
    c "What do you say to the prize money getting divided up equally, and I'll pay the tab on that post game dinner?"
    w "They don't have TABS n'yin the sewer idiot! But N'yi'm in!"
    c "Wonderful! We'll be playing at Hell Valley Stadium in a few days. I'll keep you updated."
    "They may have been stubborn as all hell but I was hoping that would be a price worth paying in the grand scheme of the game. Next up was..."
    
    hide dusk
    return
          
