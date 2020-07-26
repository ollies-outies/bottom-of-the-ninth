default HasAldric = False
default HasCileren = False
default HasDandy = False
default HasDiver = False
default HasDusk = False
default HasFatherRobin = False
default HasOckShaw = False
default HasScylla = False
default HasTrouble = False
default HasWhippy = False

default Magic = 0
default Might = 0
default Movement = 0
default characterlist = ["Aldric", "Cileren", "Dandy", "Diver", "Dusk", "FatherRobin", "OckShaw", "Scylla", "Trouble", "Whippy"]


define c = Character("Casey")
define b = Character("Aldric")
define l = Character("Cileren")
define f = Character("Dandy")
define z = Character("Diver")
define y = Character("Dusk")
define r = Character("Father Robin")
define o = Character("Ock")
define s = Character("Shaw")
define a = Character("Ock and Shaw")
define p = Character("Scylla")
define t = Character("Trouble Comings")
define w = Character("Whippy")
define q = Character("Ordog")
define i = Character("Bratherford Hatherford")
define v = Character("Victor")


label start:

    $ renpy.random.shuffle(characterlist)
    $ encounter1 = characterlist[0] + "Market"
    $ encounter2 = characterlist[1] + "Market"
    $ encounter3 = characterlist[2] + "Market"
    $ encounter4 = characterlist[3] + "Stadium"
    $ encounter5 = characterlist[4] + "Stadium"
    $ encounter6 = characterlist[5] + "Stadium"

    scene bg smoke
    
    "It was the fifth anniversary."
    
   
    "It's been a hard few years since then, but I'd imagine it was harder for him."
    
    "The years hadn't dulled the pain, but they had offered insight. Insight into what people were put here to do."
    "For some, they get busy living. For others, they get caught dying."
    "How horrible, to be somewhere in between."
    
    show casey
    
    c " "
    c "I realize that you probably can't hear this, Vic, but... I mean it."
    c "I'm sorry."
    
    "My name is Casey Conway Fisk. I'm a ex-professional Wizardball player, living out in the boonies, in a little town called Katabas."
    "And I've got a story to tell."
 
    scene bg stadium

    "The name of the game was, and still is, Wizardball."
    "Everyone in the Tri-kingdom area knows about it. Even those damned fools in the underworld know about it."
    "It's fast, unique, and has enough leniency in the rules that anything and anyone can work."
    "'Course, the rules they actually do have can't be broken, under any circumstances. Otherwise..."
    "Well, otherwise your sponsors stop calling you, and you're forced into house arrest for a few years."
    "I was the biggest star the field's ever seen, ya know. The mighty C.C., up on the mound. Had my face on quite a number of breakfast foods."
    "But of course, the bigger you are, the harder you fall."
    "Maybe it's that desire to be big and important again, or maybe it's the nagging feeling in my heart since I was asked to leave."
    "I still love the game, simply put. I love everything about it, from the feeling of dirt pulling at your feet, to the roar of the crowd as someone lands a Fire Bolt."
    "And as much as I tried, I couldn't live without it."
    
    scene bg smoke
    
    "See, in those five years, I'd realized something. Something stronger than any one of us, something bigger."
    "Fate."
    "Fate's what brought me to the game in the first place. Fate's what put my best friend Vic in the wrong place, at the wrong time. Fate's the player, and we're all just pawns."
    "So... why fight it?"
    "Fate'll bring what Fate'll bring. All we can do is play with what's been given."
    "And, in this case, I've been given a pack of Coven brand ''Minor League's Up & Coming Rookie'' cards."
    "Complete, of course, with a stick of Gerblin Green Chewing Gum, which was as stale as a rock."
    "Each card in a pack of 6 comes complete with assessment values of the 3 things that matter in Wizardball- Might, Magic, and Movement."
    "Aside from the pack being a wonderful collector’s item, and coming with what can arguably be described as a piece of candy, it also shows what the next big team might be. Wizardball is played in teams of six, of course – just like a pack of Coven Cards."
    "See, I could no longer play on the field. The game’s Executive Board wouldn't let me. Still won't, in fact."
    "But I could gather a team, and play Coach, from the backlines."
    "Hand picked, by none other than the swaying hand of Fate, I could amass a group of players that were never given the chance to go big, and finally let 'em."
    "I was done worrying about the fall. I was done letting what could happen prevent me from focusing on what has happened."
    
    "I had a first game already scheduled, down in the underworld in Judecca. I had a team name, The Comedians, and a lifetime worth of strategies. All I needed were the players to do it with."
    "Let's see what Fate had up her sleeve first." 
    
    hide casey
    
    scene bg market

    "I walked into the center of Katabas, the bustling market area, and pulled the first card from the pack."

    $ renpy.call(encounter1)

    $ renpy.call(encounter2)

    $ renpy.call(encounter3)

    jump PostMarket
