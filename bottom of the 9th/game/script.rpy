define c = Character("Casey")
define w = Character("Whippy")
define r = Character("Father Robin")
define o = Character("Ock")
define s = Character("Shaw")
define a = Character("Ock and Shaw")
define t = Character("Trouble")

label start:

    scene bg smoke

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    "It was the 5th anniversary."

    show casey
    
    " "
    "It's been a hard few years since then, but I'd imagine, it was harder for him."
    
    "The years hadn't dulled the pain, but it had offered insight. Insight into what people were put here to do."
    "For some, they get busy living. For others, they caught dying."
    "How horrible, to be somewhere inbetween."

    c " "
    c "I realize that you probably can't hear this, V, but... this is for me."
    c "I'm sorry."
    
    "My name is Casey Conway Fisk. I'm a ex-professional ball player, living out in the boonies, in a little town called Katabas."
    "And I've got a story to tell."
 
    scene bg katabisstadium

    "The name of the game was, and still is, Wizardball."
    "Everyone in the Trikingdom Area knows about it. Even some of the fools in the underworld know about it."
    "It's fast, unique, and has enough leniancy in the rules that anything and anyone can work."
    "Course, the few rules they have can't be broken, under any circumstances. Otherwise..."
    "Well, otherwise your sponsor's stop calling you, and you're forced to skip town, lay low for a while."
    "I was the biggest star the field's ever seen, ya know. The mighty C.C., up on the mound. Had my face on quite a number of breakfast foods."
    "But of course, the bigger you are, yada yada."
    "Maybe it's that desire to be big and important again, or maybe it's the nagging feeling in my heart, since I was asked to leave."
    "I still love the game, simply put. I love everything about it, from the feeling of dirt pulling at your feet, to the roar of the crowd, as someone lands a Fireball."
    "And as much as I tried, I couldn't live without it."
    "See, in those 5 years, I'd realized something. Something stronger than any one of us, something bigger."
    "Fate."
    "Fate's what brought me to the game in the first place. Fate's what put V in the wrong place, at the wrong time. Fate's the player, and we're all just pawns."
    "So... Why fight it?"
    "Fate'll bring what fate'll bring. All we can do is play with what's been given."
    # show cardpack
    "And, in this case, it's a pack of Coven brand ''Minor League's Up & Coming Rookie'' cards."
    "Complete, of course, with a stick of Gerblin Green Chewing Gum, which was as stale as a rock."
    "See, I couldn't play in the Major leagues. Board wouldn't let me. Still won't, in fact."
    "But I could gather a team."
    "Hand picked, by none other than the swaing hand of fate, I could amass a group of players that were never given the chance to go big, and finally let 'em."
    "I was done worrying about the fall. I was done letting what could happen prevent me from focusing on what has happened."
    "Let's see what fate had up first." 

    scene bg market

    "I walked into the center of Katabas, the bustling market area, and pulled the first card from the pack."

    scene bg park

    # show whippy_card

    "Jordan Redslide. ''Whippy'', to friends and admirers."
    "This little birdy has a big secret. Namely, the kid's god an arcane reserve the size of the ocean."
    "Issue is, he's also got no spell control in the slightest. He's a constantly charging dynamo, with no real place to discharge."
    "And eventually, the dam as got to burst."
    "This sometimes comes out as arcane bursts, explosions of pure force, which, while spectactular, are not regulation, and did get him kicked off the Rasko Stonemasons."
    "Or now, due to runes etched into his uniform, pure strength."
    "He's a powerhouse in the truest sense of the word..."
    
    show whippy_panic
    
    "He's just also a bit... unpredictable."
    "I ran into him, after he had, seemingly singlehandedly, leveled a food stall."
    "Or, what used to be one, at the very least."
    "I say it was him, not because I saw him do it, but because he was standing over it, biting his feathers, panicing."
    "Plus, my first words that I heard him say were..."
    w "Oh gods, not another one!"
    "I'm no private dick, but you don't have to be one to put two and two together."
    c "You alright, son?"
    "He turned so quick, I swore I heard something crack. There was a panic in his eyes that I had never seen before."
    "He was spiraling quick. I needed to put him at ease somehow."

    menu: 
            "So I told him..."

            "You're that demolishion crew I ordered, right?": 
             jump whippy_A1

            "Hey, it's okay. It's okay. Breathe. Breathe.": 
             jump whippy_A2


    label whippy_A1:
    "He looked at me, more confused than panicked."
    c "To destroy my old stall, right? I talked to someone yesterday, but the reception was kinda hazy. I thought they said there'd be at least a ''third man'' coming to help."
    c "I realize what she ment now. It's incredible, that you were able to do this by yourself!"
    c "And here I was, worried I'd have to split the money three ways."
    "I gave a chuckle. I hadn't lied that hard since grade school, but it was working. Whippy was calming down."
    c "Here, why don't you wait over there? I've some quick paperwork, to finish up the ol' girl."
    "I point to a nearby bench, under a tree. Whippy hesitates, then nods and walks over."
    "I quickly pull out my pen and paper and write a hastily written ''I O U x 1. STALL. SORRY, C.C.'' and place it on the rubble, before turning back to Whippy."
    jump whippy_A3

    label whippy_A2:
    "He, stiffling tears, tried to say,"
    w "I d-didn't... m-mean t-..."
    c "Course not, course not! You're fine. No one was hurt, no one was hurt, it was just stuff."
    c "Stuff can get replaced. Take some deep breaths. Are you okay? "
    "He seemed surprised at the question, but complied. Breathing in, holding for a few seconds, breathing out."
    w "Yeah, I'm... I'm fine."
    c "Here, sit down. We're gonna get through this." 
    "I gestured to a bench, nearby, where he walked over and cautuously took a seat."
    jump whippy_A3


    label whippy_A3:
    "I sat down next to him."
    c "You have a gift, kiddo. Like it or not, fate's given you this crazy power, and the best thing you can do is try to use it for good."
    "I offerd him my hand."
    c "I'm starting a pro Wizardball team, here in town. If you'd like, I'd love to have you with us."
    w "You sure you want m-me? After everything?"
    c "What, after showing me your skills, or after being a great player?" 
    "He looked at me, slightly dumbfounded, and gingerly took my hand. I smiled, cocky glint in my eye."
    c "Go ahead, I can take it."
    "He gave a glint back, and shook my hand, fully and wholeheartedly." 
    "I damn near dislocated my arm."
    c "Meet us at Hell Valley Stadium, in a few days." 
    "He nodded, almost excited." 
    w "I'll see you there!"
   
label start:


    scene bg market

    
  

    show O&S_Card

    "Ock and Shaw. Siblings, of the highest caliber."
    "See, back in Aught Six, there was a massive hullabaloo about a Gorgon in the Major League."
    "The opponent’s team argued that since each snake on the Gorgon's head was alive, they had to count each as a player, and thus, the Gorgon should be disqualified, due to an overstaffed team."
    "This then led to the creation of Euryales Law, named after the Gorgon, wherein any multiminded player, so long as all minds present and accounted for are working as a unit, instead of on multiple strategies at once, could be registered as one player."
    "While this was mostly a good thing, there were a few people who tried to use it to their advantage. Some hydras, an odd cerberus or two, but none were as effective, or out of left field as Ock and Shaw."
    "Fitting, considering that's where they'd usually play from. Ock and Shaw weren't joined at the hip, but it felt like they were one mind in two bodies."
    "Shaw, the running man, would control movement, while Ock, the arms, would be the one in charge of spell slinging and ball catching."
    "This was a terrifyingly effective strategy, when they worked together."

    # show Ock angry
    # show Shaw angry

    "But back then, it was quite difficult to actually see."
    o "No, YOU listen! I gave you HALF our funds, told you to spend it on FOOD, and what do you come back with?"
    s "You didn't specify what kind! You said FOOD, and I bought us food!"
    o "You bought us a CARRIAGE, a LITERAL HORSE DRAWN CARRIAGE, OF EXCLUSIVELY EGGS."
    s "THEY WERE ON SALE, OCK. I WOULD HAVE LOST MONEY NOT BUYING THEM."
    s "Plus, now we have a cart! And a horse! That's the bargain of a lifetime!"
    o "Do you even LIKE eggs?"
    s "I WILL LEARN TO LIKE EGGS."
    "See, there were rumors that the Ornsburrogh Sidewinders were interested in picking up Ock, and exclusively Ock, for their next season."
    "Combine that with the fact that siblings already argue like cats over string, and that both of them are in arguably the most demanding sport currently allowed to see overworld play..."
    "Well, tensions were high. They were a powder keg, simply waiting to explode."
    "And I figured, I ought to put out the fuse before it does."

menu: 
            "Pardon me, sorry to intrude, but..."

            "Do I happen to know you two from anywhere?": 
             jump oands_A1

            "Do you know where someone might be able to pick up several thousand eggs?": 
             jump oands_A2

           
label after_menu:
          

    label oands_A1:
    #Show shaw surprise
    #Show ock surprise
    "They acted stunned, taken aback, and slightly insulted."
    "Of course, I'd known who they were from the second I saw them, but I figured I'd play dumb to get 'em talking."
    o "Well, you probably don't recognize us apart."
    s "Of course, if we were in formation, you'd recognize us from a mile away."
    c "Oh? And what ''formation'' would that be?"
    #show shaw smile
    #show ock smile
    "The two shared a smile, that was wider than they were tall."
    o "Well, imagine if I were... about  three feet taller."
    s "Long coat, pinstripes, number 15...? Ringing any bells?"
    c "Mm... It's starting to get there… Have you guys done anything noteworthy?"
    "People love to talk about themselves, especially their accomplishments. "
    "And, it just so happened that with these two, talking about their accomplishments directly includes the other."
    s "We won the fourth annual Derby Day Tournament, practically by ourselves."
    s "The Pyre on the Spire? Any of this?"
    o "God, Pyre on the Spire... that was a damn good game, honestly."
    s "Wasn't it? That was the one where I tackled that guy right at the end, right?"
    "Ock turned to face Shaw, practically bouncing with excitement."
    o "Yeah, yeah! I snagged the ball while you kept him locked down with a Minor Paralysis..." 
    a "And we brought him and the ball to the goal posts!"
    "They let out a quick, but hearty laugh. Sounded like a good play, but it didn't seem funny... but I guess I had to have been there."
    "They were laughing, arm over shoulder, about past victories and triumphs, like the family and team they should be. I finally let the facade down."
    c "Wait, I think... I think I'm starting to recall. You're those wizardball players, right?"
    s "Yeah, you're finally getting it! Only took you an hour."
    "They laugh a bit harder."
    c "The ones who brought home over three Pennants, four Medals, and a Trophy for Fine Excellence in Sportsmanship and Good Conduct?"
    o "The very same! The two and only."
    c "The defining twins, that shake the very field they're on whenever and wherever they dare step foot?"
    s "Ooh, so apt. So apt and accurate. That is undoubtibly us, without question!" 
    c "Then I might have a proposal for you."
    a "And what is that, my well educated stranger?"
    jump oands_A3 

    label oands_A2:
    #show shaw happy
    #show ock happy
    "A mischievous glint appeared in both of their eyes, almost instantly." 
    "I've been around magic my entire life. My mother was a sorcerer, and my father worked with artifacts. I spent the majority of my adult life studying and practicing different strategies for a sport that literally has ''wizard'' in its title."
    "I have never seen something as magical as two twins forming a coherent plan to scam someone into the ground, exclusively in glances and nods over the course of maybe two seconds."
    s "Well, as luck would have it, we're actually a pair of traveling egg vendors!"
    o "Just come into town today, to sell our freshly gathered, free-range egg collection."
    s "Collected from all over the world, from coast to coast, and preserved perfectly in pristine condition, in our Carriage-Du-Omelette."
    a "Care to take a look, friend?"
    "I closed my eyes, and gave a slight laugh. The kind a grandparent might have."
    c "There's no need to look, I trust your kind faces, and wonderful synchronization. I'm thinking about taking the whole lot, for... Oh, I don't know, how much do houses sell for, nowadays?"
    "The two's grins widened."
    a "Why thank you! We aim to please!"
    c "But, I worry... this is simply too many eggs, isn't it? Just too many for one old geezer to carry."
    o "No, no, not to worry, my good and wealthy individual! As previously stated, we are equipped with a top of the line Egg-carriage."
    s "And a horse!"
    o "And a horse too, thank you, also a horse. We are more than happy, nay, more than willing, NAY, MORE than INSISTING that we deliver these for you, sir!"
    a "Just tell us where to go!"
    "I stifled a laugh, as my grin finally got as wide as theirs."
    c "Hell Valley Stadium. And bring your gear, too. We're gonna be taking down the Tophets with a few other jokers."
    #show shaw surprised
    #show ock surprised
    o "..."
    s "..."
    a "What?"
    jump oands_A3

    label oands_A3:
    c "I realize I've yet to introduce myself, and that was rude of me. My name is Casey Conrad Fisk. It's a pleasure to make your acquaintance." 
    c "I'm starting a Major League team, here in Katabas. The Comedians. Something tells me you two will fit right in."
    c "I'm offering a spot for both of you, and I've got as many boons and goodies as it'll take to get you to say yes."
    c "So. What'll it be?"
    "They let the offer sink in, before turning in a quick huddle, to discus their options."
    "I sat there and listened to their vaguely incomprehensible chatter for quite some time. Pondered the meaning of life, and what it was I was going to eat for lunch."
    "I hate to admit it, but I had a hankering for eggs."
    "I thought about fate, how something greater than us, uncontrolable, seemingly controls our every whim, of an infinte question, and a few fairly stand out answers."
    "But in that moment, only one answer stood out, more than any others."
    #show oands
    " "
    a "We're in."

label start:

    scene bg park
    show robin_card

    "Robin Fairweather. A mountain of a man, with a deeper knowledge of the internal workings of spellcasting that could put Merlin to shame."
    "Robin played for the Keetsity Roundabouts, primarily, where he served as one of their defensive agressors."
    "But, ball was never Robin's passion, you see."
    "Inbetween the cheering and uproars, Robin heard a higher calling; that of some deity, calling him to care for the weak."
    "And so, he left the game. No one faulted him for it. It was a shame, but it was what he needed to do."
    "He started up an orphanage, here in Katabas. Lived a quaint and quiet life for some time. Raised cattle. A flock, some might call it."
    "But inbetween visits to the town square, and running market stalls to sell various beadworks and blessings..."
    show robin_Neutral
    "I could recognize a man struggling to survive."
    
   
 
    "He'd never admit it, of course. Faithful men never like admitting that the path they're on is the wrong one."
    "And, that's partially because it wasn't."
    "Fate'd lead him here, but it was mans inhumanity to man that shafted him in the end."
    r "Beads for sale. Individualized, prayer beads. Each, hand blessed. Certain to bring fortune."
    "His shill wasn't loud, but it was insistant. He wasn't trying to catch attention, he was talking as if someone was already listening, and already interested."
    "Down the row, there were several children at various stands, selling Holy Water and Lemon, or various panphlets of scripture."
    "I could tell that this cost more than it would've brought in, for certain. It would have been that way, even without people actively avoiding them, and dodging their glances."
    "I, however, caught his glance wholeheartedly."

    menu: 
            c "Hey pal..."

            "Are these beads really blessed?": 
             jump robin_A1

            "Is this the best field trip you could offer?": 
             jump robin_A2


    label robin_A1:
    "He looked up, a knowing glint in his eye."
    r "Each, individual one. I would know, I've done it myself."
    "I hold one of the charms, a masterpiece in its own right."
    c "You made each bead?" 
    r "... I blessed each bead."
    c "But the beads themself?"
    r "More than likely made by hand, by someone, somewhere else."
    c "Ah. A classic."
    "I give a quick glance down the way, to the rest of the stalls. The kids running them look ragged, but happy."
    c "It's a good thing you're doing, Robin. These kids needed something like this."
    r "It is... what is right. It's unfortunate, that they've been forced to do something like this to simply survive, but I want what's best for them."
    "I looked at Robin, his eyes focused on his flock. He was more ragged than ever. What was once a tall mountain of a man was mined thin, through hardships and strife."
    c "Yeah, I get where you're coming from."
    "I put the beads down."
    c "That's why I wanted to find you, actually."
    jump robin_A3

    label robin_A2:
    "He looked up, with concern, more than anger, in his glare."
    r "It's... not much, but... I think that it cultivates strength."
    r "Each child is given their own chance to flourish, if just for a moment."
    r "Some, choose to band together. Others, try to strike it on their own."
    r "It's something... defining."
    c "Builds character?"
    "He nods."
    r "Something like that."
    "He intently focuses on the children. The ones selling holy lemonade decided to close up shop. They brought cups full of the stuff to the other kids."
    c "Teamwork, even at a young age. Incredible, huh Robin?"
    "He nods again, slower this time."
    c "Robin, I wanted to ask you something."
    jump robin_A3


    label robin_A3:
    c "I'm starting a team. Based here, in Katabas. You wouldn't have to leave your flock, and the extra income might help them."
    "I put a hand on his shoulder."
    c "It might help you."
    r "... I'm retired, Casey."
    c "I know, Robin. I'm sorry for asking you, like this. But fate brought me to you."
    "His eyes perked up."
    r "What do you know about fate, Casey Conrad?"
    c "More than you'd think, and less than I'd like."
    r "... Hm."
    "He sits in silence, and considers his thoughts for a moment."
    c "...  The first game is in a few days. Hell Valley Stadium."
    c "I understand if you can't but... I'd love to see you there."
    "I let go, picking up a charm as I do."
    c "If not for me, or you... then for them."
    "I paid the asking price, twice over. If this was gonna work, I wouldn't mind something swaying fate more in my favor."
    "Both, for the team, and for landing Robin."

    # show Trouble Card

    "Trouble Comings. A bright young upstart in the minor leagues. Used to play for the Reinbachs, over in Joshua Tree. Best shot in the game, and a damn fine receiver too. He had a bright future ahead of him, all things considered." 
    "Except for one nagging issue, that is. See, Trouble had a massive debt to pay, thanks to his mom and pop bouncing out of he and his three siblings' lives the first chance they got."
    "Left poor Trouble to foot the bill of two lifetimes' worth of gambling and drinking, plus three hungry mouths to feed."
    "So, he did what any responsible person would do in that situation: Quit his passion, to continue the business his folks left behind."
    "Which just so happens to be based primarily in the hunting of men."

    # show Trouble Angry

    T "God damn it! Which way did she go?"
    "I ran into him in the middle of a hunt, ya see. Some fool had made the mistake of pissing off the wrong person with the right amount of cash, which left a target on their back, the size of a barnyard door. "
    "And, as I previously mentioned, Trouble was a great shot. "
    "Issue was, Trouble was never the quickest kid in the park. Meaning anyone more fleet-footed than him could be out and away, just like that. "
    "What he needed was a Team. What he got was an entree plate of bad luck with a side order of bullshit. "
    "So, I decided to fill the niche."
    C "Trouble Comings, right? Need any help?"

    # show Trouble Confused 
    "Trouble gave me a look over, not quite sure what I meant, before realizing who was offering their service."
    # show Trouble Neutral
    T "Casey Conway?! I thought you’d curled up and died somewhere! D-uh, no offence."
    C "Well, I did move permanently into this backwater, so... you’re half right."  

menu: 
            "I said to him..."

            "You look like you need help, Comings.": 
             jump trouble_A1

            "Carrying on the family legacy, are ya know?": 
             jump trouble_A2

label after_menu:

label trouble_A1:
    # Show Trouble Happy
    "He cracked a faint smile." 
    T "I certainly wouldn’t turn it down, sir."
    C "It’s hard work, what you do. I might slow you down, with how well you’re doin’ it."
    "His smile faded, slightly."
    T "Thanks, C.C., but you know that this isn’t what I wanna do with the rest of my life." 
    C "You know, that reminds me..."
    jump trouble_A3

label trouble_A2:
    # Show Trouble 
    "He ruffled his brow, and gave me a curious look."
    T "Some of us gotta work to live, pal. Not all of us have boxes of cereal with our faces on them."
    "I raised my hands, shaking my head."
    C "I told my manager that brand deal was a bad play, but he insisted." 
    C "Worst part of it all is that I got none of the residuals. It all goes to my old team."
    C "Which, reminds me."
    jump trouble_A3

label trouble_A3:
    C "I’m starting a new team, based here in Katabas. Calling ourselves the Comedians, because people seem to think it’s a joke. If you’re available, we’d love to have you play with us." 
    "Trouble's eyes lit up, and he almost tripped, standing still. He hadn’t upped his footwork in the slightest, clearly."
    # Show trouble Neutral
    T "Uh? Yeah I?? Guess???"
    # Show trouble Confused
    T "... wait, is it paid?" 
    C "It is paid, yes. Quite well, actually."
    # Show trouble Happy
    T "Then yeah!? I’d- well I would need to finish this first, but I still want to play on your team after, can we do that? God, I’m sorry this is important, and we already signed a contract for this, so I would need to finish the hunt before I had any free time, and I don’t think that I can just leave on this, and oh god what am I gonna tell Strife I’m so sorry this is all just so much all of a sudden, I’m babbling and I’m just-"
    C "Kid." 
    # Show trouble neutral
    "Trouble stops." 
    C "Let’s finish the hunt you’re doing, then get you signed up."
    # Show trouble happy
    "He smiled, big and wholeheartedly." 
    T "Hell yeah!! Hell!! Yeah!!!"
    "We talked strategy for a moment. It feels good to be working out the metaphorical strategic muscles before the big game."
    "Fate is a big decider in everything, but it’s strategies that make fate manageable."
    "'Course, that doesn’t mean that fate can’t just occasionally give you a boon, like, say, the target tripping in a nearby alleyway, making a racket and alerting you and your new companion that they are 1. prone and 2. Extremely nearby."
    "Without talking, Trouble leapt at them."
    "There was a small skirmish, but Trouble handily defeated the foe, finishing by tying them up. He then quickly popped back out."
    T "Hey, I’m gonna handle this, but where should I meet up with you?"
    C "We’re meeting the rest of the team in a few days, at Hell Valley Stadium."
    "Trouble’s face changes."
    # Show Trouble Angry
    T "Hell Valley? But I thought we were settled here. Why not in Katabas Park?"
    C "First game is an out of town one."
    T "We're gonna play our first game without any practice?!"
    C "If you don’t wanna come, that’s totally understandable, and the offer still stands, if'n we aren’t destroyed."
    # Show trouble neutral
    T "No, no, it’s fine. I’ll be there."
    "He looked refreshed, more steadied, and eager for the future." 
    T "I... Thank you for this, Coach. Really."
    # Remove trouble
    "He walked into the alley, grabbing the hogtied schmuck. He sent up a wave with his free hand, and I waved back"
    "Course, Trouble’s back is turned when I did, but the schmuck saw it. He waved with his hands tied, giving a jazz hand / spirit finger combo."

label start:


    scene bg smoke


    show casey

    "Market was a big hit, it turned out. Lots of friendly faces, lots of new pals."

    "But fate still had it in for me, ya see? So I let fate guide my footfalls, for a while."
    "Let my mind wander, and had my body following after it."
    "I thought about where I was now. How this whole thing was coming together."
    "The Comedians. That's what V always said he wanted his team to be called. I never got V, but he was a good friend."
    "Figured, I ought to pay respects, judging by what I did."
    "It still hurts to think about that day, just 5 years ago."
    "I was getting older, ya know. Not as spry and magic as I was in my prime."
    "See, even though Wizardball is named that, it only takes 1 spell to get you in."
    "Fire Ball. A classic, honestly."
    "So there were always players who knew the minimum, learned as a kid, and just used their wit and skill to make it through."
    "Powerful warriors, stealthy assassins... there were even some who tried to charm their way into wins."
    "But for me, it was all about the Spells."
    "I was a mastermind when it came to creative tactics. Was, I suppose, being the opperative word."
    "See, as I got older, my tactics still would work, just not with me. I couldn't keep up."
    "That's when I met Ordog."
    
    show ordog

    "A demon, notorious around the underworld circut. Purveyer of the best stimulants in the game."
    "And, as fate would have it, we shared a dinner table, after some victorious game."
    "He offered me a potion. Superior Mana, he called it. Said to boost your slots, and fill your meters, satisfaction Guarenteed."
    "And like a fool, I took it."
    "See, my issue wasn't needing to refill. My capacity was just getting lower."
    "So when my dumbass drank it..."
    "I surged."
    "Wizardball encourages stimulants. It's part of the fun, seeing just how crazy far you can take something."
    "They even encourage injury! There's a full staff of healers waiting by the sidelines, to rush to people who had their arms ripped off, or their guts spilled..."
    "Regeneration spells are amazing, and can fix almost anything."
    "But they can't fix permadeath."
    "After downing the pot, I turned to Victor. My teammate, Victor, who I had been through over 20 years of hardships with..."
    "And instead of a Fire Ball for a pass..."
    "A Finger of Death came out." 
    "No medics. No Greater Healing Touches."
    "Just the cold, departed body of my friend, and a game stuck in stalemate."
    "It was on this field. This same one."
    
    scene bg stadium

    "And somehow, I keep getting pulled back here."
    "This is what I think fate's telling me. That's why I started the Commedians. To honor him, and to finally anchor me here. To live with what I did, and to move on."
    "I can't argue with where fate's guiding me. All I can do is adapt and thrive."
    "And in order to do that, I have to meet..." 

    scene bg stadium

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show trouble_card
 
    "Trouble Commings. An ex-reciever for the Reinbachs, over in Joshua Tree."
    "Everyone knows he could've gone major. He was a brilliant shot, and a wiz with a sword, pun partially intended."
    "Issue is, trouble comes often for Trouble Commings."
    "His parrents up and bounced on him, his younger sister, and his two younger brothers, to pursue the adventuring life."
    "Leaving him in charge of not only the family bounty hunting buisness, but also three hungry children, and a list of debts longer than the span of a thousand wizardball fields."
    
    show trouble_sad

    "So to see him here, lamenting the shitty deal that fate's decided to deal him... It only made sense."
    "He was sitting on the railing, looking into the field. No doubt, imagining himself running, ball tucked in one hand, blade in the other."
    "Course, when I snuck up behind him and asked him,"
    c "Do you wanna join my new team, kid?"
    "He damn near fell off his seat."
    "Never was the dexterous one, that Trouble Commings."
    
    show trouble_surprised 

    t "C-Casey Conrad??"
    t "I thought you had to retire after the whole uh-"
    c "I did, kid. But fate seems to want me back in the game."
    "Casey made a face. Concerned, but curious."
    t "Are you joining the minor league...? Or, playing in, like, a secret underground ring?"
    c "... Kind of that second one, actually." 
    "Trouble actually did fall after that one. Towards me, thankfully, so he didn't have to climb up the wall to the stands."
    c "Let me explain, Trouble. See, I-"
    show trouble_happy
    t "YOU KNOW MY NAME?"
    c "Course, kid! You're one the best in the minor league! Hell, I prefer to watch Minor to Major. Way more creative strategies that what those egghead coaches think up."
    c "Anyway! I've decided to be an egghead coach. We're centralized right here in Katabas!"
    t "Uhh?! This is way too good to be true. What's the catch?"
    c "Our first game is in Hell, in less than a week."
    show trouble_nervous
    t "AH. YEAH THAT'S A BIG ONE ISN'T IT."
    c "What's the matter, scared?"
    t "No, no, it's just..." 
    show trouble_sad
    "Trouble sighed, and sat back down on the railing, back to the field. He looked conflicted."
    t "I don't know. I finally get a good thing going, with the hunting, and now I'm hooked right back in. I love the game, don't get me wrong, it's just..."
    t "I love my family more. And the idea of putting them at risk for a chance at glory, it feels weird." 
    "Kid had a point. Joining the Major Leagues meant having that as your Full Time Job, and dropped everything else. It was part of the process of registration."
    "I sat next to him, facing towards the field, my legs over the riling."
    c "Kid, I'm not gonna make you choose. I wanted to put the option there, if you wanted to take it. I understand putting family before personal gain, I can relate."
    "He looked up, confused."
    t "You? How?"
    menu: 
            "I told him about..."

            "My mother.": 
             jump trouble_b1

            "My sister.": 
             jump trouble_b2
    
    
    label trouble_b1:
    c "My mom. When I was younger... around your age actually, she caught a case of the Scarlet Plague."
    c "Course, this was before the advancements we've made in medicinal magic, and at the time, it was uncurable."
    "He turned his head to listen, as I continued, staring down at the field." 
    c "She was hooked up to gods only know how many tubes, pumping this that and another. We had healers making house calls around the clock."
    c "And my dad, he was an artifact guy, see? He turned to his work, dedicating all of his time to finding something that would make her better."
    c "Never could."
    c "I still remember how she looked when she finally passed. The worst part was that Scarlet Fever wasn't contagious, so we all could watch."
    c "She had a stare, that went for a thousand miles, and a smile."
    c "I'm glad, at least, she was able to go with her family by her side."
    c "But... that dedication, my dad had. He threw everything else aside, even his own buisness, to try and save her."
    c "... But he couldn't."
    "I wiped my eyes, and caught my breath. I'm glad I was facing away from Trouble, but I think he saw let the mask slip anyway."
    jump trouble_b3
    
    label trouble_b2: 
    c "My sister. When we were both going into college... around your age, actually, we had something bad happen to a family member of ours."
    t "If you don't mind me asking, what?"
    c "... Suffice it to say, someone died of something that should have been preventable."
    c "And... it radicalized her, I guess." 
    c "She did nothing for years and years, but study, and research, and learn."
    c "Graduated, went back, graduated AGAIN, went abroad to learn what they had there, and then came back to start teaching it."
    t "Wow."
    c "Yeah. I wish I could've been like her, but instead..."
    "I raised my hands, to gesture out towards the field."
    c "This."
    c "But, I think we're two sides of the same coin, me and her."
    c "See, beyond her dedication, there was passion. There was a goal to achieve, sure, but she found out she enjoyed doing it."
    c "She enjoyed learning, and helping people. In the same way, I found out I enjoy entertaining, and playing the game."
    c "I know I'm no physician, or a revolutionary... But I'd like to think that, me being on the field, helped someone grow, even just a little."
    t "... I know it helped me."
    "We shared a companionable silence, for a small bit of time."
    jump trouble_b3

    label trouble_b3:
    c "Anyway... I get it."
    c "It's difficult to convince yourself that the happy route is the correct one."
    c "But... for what it's worth."
    c "I personally promise that you and your siblings will be looked after."
    c "I can't guarentee it'll be hillside villas and champagne, but it'll be decent."
    "He turned on the railing, now facing towards the field."
    t "... It's been so long, though. What if I've forgotten? What if I go for it, and I fail?"
    "The words hit home."
    c "Then, I suppose... We'll have to start over."
    c "We'll take what we learned, and try again."
    c "But failure is always an option, Trouble. That's the thing. You could fail your job now."
    c "Some target might be too tough to handle, and you..."
    "An uncomfortable beat."
    c "... Lets stick with fail. You fail." 
    c "The risk is still there, either path you take."
    c "So, I would go for the one that makes you happy."
    c "And there's no way you've forgotten. Wizardball's like a tricycle. No wrong way to do it."
    t "... I can actualy think of a couple of wrong ways to ride a tricycle."
    c "Yeah, so can I. Pretend I said a good metaphor instead."
    "There's another beat. Both our eyes examine the homefield, the stands, empty, sure, but we could hear the cheering still. It echoed through our ears, both."
    show Trouble_happy
    t "Yeah."
    c "Yeah?"
    t "I'll... I'll see you there, coach."
    "I smiled."
    c "Glad to hear it."



    return



