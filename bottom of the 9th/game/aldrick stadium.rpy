# Define b = character("Aldric")
# Define c = character("Casey")

label AldricStadium:
    $ HasAldric = True

    scene bg stadium
    show cardaldric

    "Alric Bohan. The Trikingdom's favorite hero. And, at that point, it seemed like fate's favorite, too."
    "Even in the Minor Leagues, he was bigger than some of the Major players. Interviews, guest appearences, and most importantly to him, quests."
    "He's what some might call ''A Chosen One''. Few are made every year, they're people who are destined for greatness, should nothing stop them."
    "That was the issue with Aldric; His ego had too big for his own good. He had the skills he needed to go further, but was alright being stagnant. To him, he had peaked. No point trying to go any higher."
    hide cardaldric
    show aldric
    "That's what they said about him, anyway. I found him in the Katabas home field, standing in the entryway. Looking up at the pennants and banners that decorated it, signifying glory."
    "He gave a quick glance my way, and stopped me, saying in a booming and boisterous voice..."
    b "HAIL, FAIR CITIZEN!"
    c "Uh... Hail. Currently hailing."
    b "And thank you for doing so! I do hope you can forgive me for stopping you, as you clearly seem to be in some form of hurry, but I must insist you stop a moment."
    c "Not an issue. In fact-"
    b "Tell me, citizen, do you know why I asked you to do such a thing?"
    
    menu:
        "He turned and waited for an answer. I felt like I needed to humor him, so I said..."
    
        "Uh... I was was about to slip on a banana peel and you were saving me from such an embarrassing, albeit comedic fate?":
            jump aldric_b1
    
        "Uh... You mistook me for a long lost lover and wanted one last chance to reconcile an old spark?":
            jump aldric_b2
    
    
    label aldric_b1:
    "He gave a hearty guffaw, and shook his head."
    b "Oh, that would have been humorous. You would have surely taken a tumble!"
    b "Ah, but at your apparent age, that would've resulted something significantly not funny."
    b "No, it was something grander than just preventing your sudden descent, at the hands of a potassium container."
    jump aldric_b3
    
    label aldric_b2:
    "He gave a hearty chuckle, and wagged his finger."
    b "Ha! No, not that. You do resemble someone, that I once shared a night with in the Quintopelle Mountains, but alas."
    b "Even if you were them, our time has passed. While it was fun, it was not ment to be."
    b "And besides, you're not even them! You'd need to be at least 10 years younger, at least. No, that wasns't it."
    jump aldric_b3
    
       
    label alric_b3:
    "He gestured to the stadium broadly, with both arms, his armor clanking as he did"
    b "The reason that I stopped you, fellow traveler, is this, right here."
    b "As adventurers, I feel like we hardly take time to appreciate the stillness, the silence of it all. The beauty that lies in what is at our front door."
    b "As gratifying as slamming a battleaxe into the head of a giant snake may be, it lacks that sort of beautifully melancholic air moments like this hold, standing on the threshold to something great."
    "I was taken aback. Wanderlust was what defined adventurers, right behind bloodlust. But this was a side of Aldric that the papers seemed to neglect to mention."
    b "Anyways, you seemed worried, and worse for wear. I assumed you might enjoy a chance to appreciate this moment with me. If I am stopping you on your journey, then my apologies."
    c "Ah, it's no issue. You are stopping me, but not how you'd think."
    "He looked confused, so I continued."
    c "See, I'm on a quest. Putting together a pro-league team, right here in this stadium. Our first game's outta town, but after we win that, we'll be able to settle down, and bring glory back with us."
    "I figured he'd like that last part. Nothing gets an adventurers heart pumping quite like the promise of glory, I've found out."
    b "... Could I still galavant, from time to time?"
    c "Not fully, but we'd be traveling for games occasionally, and on the off seasons, sure, I don't see why not."
    b "Then tell me, brave coach of this team, where do I sign up?"
    "I grinned, and walked him through the process. And after we registered him, next up was..."
    
    hide aldric
return
