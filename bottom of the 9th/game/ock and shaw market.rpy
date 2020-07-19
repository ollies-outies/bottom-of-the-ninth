
# define c = Character("Casey")
# define o = Character("Ock")
# define s = Character("Shaw")
# define a = Character("Ock and Shaw")

label OckShawMarket:
    $ HasOckShaw = True

    show cardockshaw

    "Ock and Shaw. Siblings, of the highest caliber."
    "See, back in Aught Six, there was a massive hullabaloo about a Gorgon in the Major League."
    "The opponent’s team argued that since each snake on the Gorgon's head was alive, they had to count each as a player, and thus, the Gorgon should be disqualified, due to an overstaffed team."
    "This then led to the creation of Euryales Law, named after the Gorgon, wherein any multiminded player, so long as all minds present and accounted for are working as a unit, instead of on multiple strategies at once, could be registered as one player."
    "While this was mostly a good thing, there were a few people who tried to use it to their advantage. Some hydras, an odd cerberus or two, but none were as effective, or out of left field as Ock and Shaw."
    "Fitting, considering that's where they'd usually play from. Ock and Shaw weren't joined at the hip, but it felt like they were one mind in two bodies."
    "Shaw, the running man, would control movement, while Ock, the arms, would be the one in charge of spell slinging and ball catching."
    "This was a terrifyingly effective strategy, when they worked together."

    hide cardockshaw
    show ockshaw apart
  

    "But back then, that was quite difficult to actually see."
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

           
label oands_A1:
  
    "They acted stunned, taken aback, and slightly insulted."
    "Of course, I'd known who they were from the second I saw them, but I figured I'd play dumb to get 'em talking."
    o "Well, you probably don't recognize us apart."
    s "Of course, if we were in formation, you'd recognize us from a mile away."
    c "Oh? And what ''formation'' would that be?"
   
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
    
    show ockshaw together

    " "
    a "We're in."

    hide ockshaw together

    "Let's see... Next was..."

    return
