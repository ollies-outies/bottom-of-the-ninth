# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Casey")
define r = Character("Father Robin")

# The game starts here.

label start:

    scene bg Park
    show cardrobin
   
    "Robin Fairweather. The size of a whale, with a heart as big as one, too. One of the best spell slingers in the minor leagues."
    "Before he retired, there were rumors of him going pro. He used to be the Hardknocker for the Keensity Roundabouts, and with his size, there's no question why."
    "But, like I said, he retired, early. Some might even say before his prime."
    "To those who know why he left, though, they thought a different tune."
    "He retired in Katabas, ya see. Heard a calling from a higher power, supposedly, who told him that what he needed to do was care for those who couldn't care for themselves."
    "And so, the Fairweather Orphanage was started. Tended farms, raised cattle, all to supply those kids starving on the street with food and shelter."
    "He was a noble man, in the truest sense of the word. I felt bad, seeing fate guide me to him."
    "That was, until I actually ran into him."
     
     hide cardrobin
     show robin

    "Robin himself wasn't doing too bad. He was looking at the trophies that lined the walls inside the stadium."
    "It was the gaggle of children, skin and bones, torn rags and sacks sewn lovingly to make clothes, running loose alongside him."
    "They were transfixed by the paintings and statues of players come and gone. They hadn't made one for me, yet, but something told me I wouldn't be around to see if, if they did."
    "I turned my gaze back at Robin. He was staring at the trophies from aught one. That was the year he had retired."
    "I tried something simple."
    c "You know, it's not too late."
    "He looked up, and smiled, seeing me."
    r "Ah, Casey Conrad. Brash as ever, I see."
    c "You got me down to rights. How's the flock?"
    "He turned to the kids."
    r "I'm... assuming you mean the children, and not... my actual flock of sheep."
    c "Once again, accurate."
    "He forced a smile. It wasn't disengenuine, it was just for something else."
    r "They're making it through."
    r "And how've you been keeping, old timer?"
    c "Aside from finally stretching my legs? I'm pretty good. Got a new hobby, actually."
    "He took a step back.
    r "The mighty Casey Conway Fisk, doing something other than Wizardball?"
    c "No, no, I didn't say that. For the first time this conversation, you missed. I'm coaching a pro-team now. Stationed up here in Katabas, actually. Same stadium."
    "He let the information sit for a moment, and then let out a hearty laugh."
    r "Oh, I should have expected! No way that C.C. Fisk would ever get off their grassy hill. I was a fool to think otherwise."
    c "Yeah, yeah. Yukk it up. It's only fitting, honestly. New team's called ''The Comedians''."
    "He stopped laughing, then turned, serious and sudden.
    r "You're here to ask me to join your team, aren't you?"
    c "... I gotta say, when you're right, you're right. You can stay in town most days, and have enough money to help the kids out."
    r "Casey Conway... are you a good person?"
    "He caught me off guard with that one. Morality was the centerpoint of his schtick, so I thought it might've been a test."
    "But... The question kinda rang through my head for a while. Am I?"
    "Do I think I'm doing this for me, or for someone else? Am I really here to help him, or am I using his disadvantage for my own gain?"
    "Does that make me a bad person, if that's true? Does any of this? What does bad and good even mean?"
    "I stood there for probably half a minute, just thinking. Robin just... stood, patiently waiting."
    menu: 
            "Until, I eventually broke the silence, when I said simply,"

            "Yes.": 
             jump robin_B1

            "No.": 
             jump robin_B1

    "He nodded, quietly and susinctly." 
    r "I... will join your team, Casey Conrad."
    c "I should also mention, first game IS in Hell. They're the only fools who'll take newcomers."
    "He thumped my head with the bottom of his fist. It hurt, but I deserved it for pulling a fast one like that."
    c "... See you there in a few days?"
    r "... See you there, C.C.." 
    hide robin
    "My head still hurting, next was..."   

    return
