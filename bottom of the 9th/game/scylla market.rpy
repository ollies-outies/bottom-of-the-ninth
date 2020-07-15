# Define p = character("Scylla")
# Define c = character("Casey")

label ScyllaMarket:
    $ HasScylla = True

    show cardscylla

    "One of the factors that differentiates Wizardball from your average everyday bloodsport is the chaos. The fluidity of it all. And no one shows that off better than Scylla."
    "No one truly knows just exactly how she broke into playing on the Minor league circuit. Story goes she just showed up to the tryouts of the Capacian Breakerss and filled her name in, on the team wall as if she had already been accepted."
    "Manager was pissed, obviously, but Scylla wasn't having it. Challenged the entire newbie gang to a game. No one else on her team, just her."
    "Course, you've heard of these kinds of stories. Singlehandedly showed them all up, ended before they got a single point. She moved so quick, threw so fast that it was like she didn't even need a team."
    "And that was the issue, as it turns out. She didn't. She was a garbage team player and a ball hog, who was constantly going on week-long drinking benders before and after matches."
    "She'd get the results, when she'd actually turn up. But, after missing a championship game that would've sent the Breakers to stardom, she was found piss drunk in a ditch a few towns over. She was let go after that."
    "I didn't find her in a ditch, but it was damn close to looking like I might've. She was outdrinking an entire bar stall, and running quite a tab."

    hide cardscylla
    show scylla

    p "And ANOTHER THING! Just because you might OWN the place doesn't mean you can treat me like this. That is RUDE! You hear me? RUDE!!"
    "Seems the bartender cut her off, 'cause he learned she didn't intend on footing the bill."
    p "Hey, hey you! In the hat."
    "She flagged me down. Walking up, the scent of bad booze hit me like a brick."
    p "Listen, I hate to impose like this, but THAT asshole over there has put me into a bit of a predicament."
    p "The old ''You aren't allowed to buy anything unless you can pay for it'' routine. Turns out, not having on hand money is suddenly an issue, and tabs mean nothing."
    p "You wouldn't happen to be a generous benefactor that I could squeeze a few dubloons out of, would you?"
    "I sat down next to her at the bar."
    c "Not for free, at least. I've a proposition for you, regarding Wizardball."
    p "Oh, let me guess, a fan? Well, autographs normally are fiveteen per signing, with a 50%% gratuity charge, but I suppose I could make an exception, iffin you get me another drink."
    "I flagged down the bartener, and signalled for 2 brews."
    c "Actually, I was interested in something else. I’m building a team, and I need players. What say you to getting back in the game? Getting to feel the rush of it all one more time?"
    "She damn near fell out of her seat laughing."
    p "HA! HAHAHA! OH, oh, gods above, that got me."
    "She turned to me, and saw my deadpan expression."
    p "Oh fuck, you're serious."
    "The ale finally arrived, served in big metal tankards. She grabbed for both of them, and started nursing the first."
    p "Look, I hate to break it to you but sometimes it’s best to just let dreams die. Painfully and slowly. You get over it eventually!"
    "She shot back the rest of the drink, and gave a whistful glare to the bottom of the mug, seeing her reflection, and more importantly, the lack of booze."
    c "Looks like you've adapted just swimmingly to post-wizardball living. Don’t you want a chance to take back control of your life?"
    p "Control is for chumps. Uncertainty, that's where it's at."
    c "Well you more than anyone would probably have an intimate knowledge of just how uncertain and wild those games can get."
    "She started to down the beer I had ordered for myself. I kept at it."
    c "You’ve got talent, Scylla. Talent that no one's seen for years, and if you don't get back in, they might never see again."
    c "I know it's difficult, but I know you miss it too. Believe me, I've been there."
    "She slammed the mug down, spilling it's precious liquid courage over the counter, stopping me in my tracks. Her face was long, and angry."
    p "Oh, I'm sure you do. I'm sure you know how it feels to let down everyone, time and time again, to be the laughing stock of an entire game. To be the bottom of the barrel, in a league made entirely of the losers who couldn't go big."
    p "Why should I trust you? Why do you CARE? Why do you suddenly show up, thinking you know who I am, how I feel? Why the fuck do you think you can bring up what I left behind?"
    "I was caught off guard, and her questions hit home. But, this was what I needed. She opened her shell, for just a second. If I didn't land this now, there'd be no way I could land it after. I'd need to tell her about something important."
    
    menu:
        "So, I told her about..."
    
        "V.":
            jump scylla_a1
   
        "My mother.":
            jump scylla_a2
    
    label scylla_a1:
    "It still hurt to talk about it, but I needed to let her in on what I was doing, or nothing would change. So, I gingerly approached the topic."
    c "Because I've been hurt too. I've fallen so far, I'm surprised I'm still standing."
    c "I was a pro-player. It was everything to me, Scylla. The game, it made me who I was."
    c "And it was taken from me, because of something I did."
    "I took the flaggon she had slammed on the bar, and took a sip."
    c "I... I lost a friend. And in losing them, I lost everything else."
    c "The game, the supporters, my team... My own father turned his nose up at me."
    c "I was forced to stay a hermit for years, to punish me for what I did. For everything I caused."
    c "And the worst part of it all, years later, is that I still don't feel like it was enough."
    c "I still feel like shit, every day, and that will never go away, because there's no way to undo what I've done."
    jump scylla_a3
   
    
    
    label scylla_a2:
    "My mind went to my mother, and what I couldn't do for her. I refused to let that happen again."
    c "Because I've lived in uncertainty before. It was my mother."
    c "She was a brilliant mind, and a sorcereess like no one else. Revolutionized the field of modern connective magic, for the better."
    c "And she came down with a case of Scarlet Plague."
    "I took the flaggon she had slammed on the bar, and took a sip."
    c "The entire time she was dying, my father was working non-stop, to try and save her. He was an artificer."
    c "Every day, he'd come up with something. Some ancient potion recipe, or some blessed amulet. Something that was sure to work, this time, it had to work."
    c "It never did."
    c "Every day, we'd build up hope, only to have it come crashing down. Over, and over again. When she finally moved on, I remember thinking..."
    c "At least it's finally over. At least we know that it's over, and we can stop."
    p "Holy shit."
    c "It radicalized me, Scylla. Fate's a bitch, and we're just trying to deal with it screwing us over."
    jump scylla_a3
   
    label scylla_a3:
    c "So you want to know why I care?"
    c "It's because I know a downward spiral better than anyone, and I refuse to let it happen to someone that I can do something about."
    c "You were a champion, Scylla. You still are a champion. And I am going to do everything in my power to make sure you remember that."
    "We sat in relative silence for a few moments. The rest of the patrons and the barkeeper kept their distance, nonchalantly doing other things, but were keeping their ears out for the response. And finally..."
    p "... What're the details."
    c "The first game's in a few days, down in Hell. We can talk salary privately, but it's not bad."
    p "... Fuck it. But I'm letting you know, I'm not playing sober."
    c "I'll have an open bar set up for you in the locker room."
    "There was a cheer from the bar, and I set down the tankard I had ordered. Scylla looked at it for a moment, still morose, took a deep breath, and grabbed it, letting out a cheer as she did."
    p "THE NEXT ROUNDS ON ME, GENTS!"
    "There was another cheer, barkeeper included, who then sharped up, and started to fuss with her, as she downed the last of the tankard."
    hide scylla
    "I could still hear the carousing, as I looked at what was next."

  
return
