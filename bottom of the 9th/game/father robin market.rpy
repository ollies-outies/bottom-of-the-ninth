define c = ("Casey")
define r = ("Father Robin")

label FatherRobinMarket:

$ HasTrouble = True
$ Magic += 2
$ Might += 3
$ Movement += 1

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

return
   
    