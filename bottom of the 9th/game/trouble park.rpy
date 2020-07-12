

define c = Character("Casey")
define t = Character("Trouble Commings")



label TroublePark:

$ HasTrouble = True
$ Magic += 2
$ Might += 3
$ Movement += 1


    scene bg stadium

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show trouble_card
 
    "Trouble Commings. An ex-reciever for the Reinbachs, over in Joshua Tree."
    "Everyone knows he could've gone major. He was a brilliant shot, and a wiz with a sword, pun partially intended."
    "Issue is, trouble comes often for Trouble Commings."
    "His parents up and bounced on him, his younger sister, and his two younger brothers, to pursue the adventuring life."
    "Leaving him in charge of not only the family bounty hunting buisness, but also three hungry children, and a list of debts longer than the span of a thousand wizardball fields."
    
    show trouble_sad

    "So to see him here, lamenting the shitty deal that fate's decided to deal him... It only made sense."
    "He was sitting on the railing, looking into the field. No doubt, imagining himself running, ball tucked in one hand, blade in the other."
    "'course, when I snuck up behind him and asked him,"
    c "Do you wanna join my new team, kid?"
    "He damn near fell off his seat."
    "Never was a dexterous one, that Trouble Commings."
    
    show trouble_surprised 

    t "C-Casey Conrad??"
    t "I thought you had to retire after the whole uh-"
    c "I did, kid. But fate seems to want me back in the game."
    "Casey made a face. Concerned, but curious."
    t "Are you joining the minor league...? Or playing in, like, a secret underground ring?"
    c "... Kind of that second one, actually." 
    "Trouble actually did fall after that one. Towards me, thankfully, so he didn't have to climb up the wall to the stands."
    c "Let me explain, Trouble. See, I-"
    show trouble_happy
    t "YOU KNOW MY NAME?"
    c "'course, kid! You're one the best in the minor league! Hell, I prefer to watch Minor to Major. Way more creative strategies than what those egghead coaches think up."
    c "Anyway! I've decided to be an egghead coach. We're centralized right here in Katabas!"
    t "Uhh?! This is way too good to be true. What's the catch?"
    c "Our first game is in Hell, in less than a week."
    show trouble_nervous
    t "AH. YEAH THAT'S A BIG ONE ISN'T IT."
    c "What's the matter, scared?"
    t "No, no, it's just..." 
    show trouble_sad
    "Trouble sighed, and sat back down on the railing, back to the field. He looked conflicted."
    t "I don't know. I finally get a good thing going with the hunting, and now I'm hooked right back in. I love the game, don't get me wrong, it's just..."
    t "I love my family more. And the idea of putting them at risk for a chance at glory, it feels weird." 
    "Kid had a point. Joining the Major Leagues meant having that as your Full Time Job, and dropped everything else. It was part of the process of registration."
    "I sat next to him, facing towards the field, my legs over the railing."
    c "Kid, I'm not gonna make you choose. I wanted to put the option there, if you wanted to take it. I understand putting family before personal gain. I can relate."
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
    c "'course, this was before the advancements we've made in medicinal magic, and at the time, it was uncurable."
    "He turned his head to listen as I continued, staring down at the field." 
    c "She was hooked up to gods only know how many tubes, pumping this that and another. We had healers making house calls around the clock."
    c "And my dad, he was an artifact guy, see? He turned to his work, dedicating all of his time to finding something that would make her better."
    c "Never could."
    c "I still remember how she looked when she finally passed. The worst part was that Scarlet Fever wasn't contagious, so we all could watch."
    c "She had a stare that went for a thousand miles, and a smile."
    c "I'm glad, at least, she was able to go with her family by her side."
    c "But... that dedication my dad had. He threw everything else aside, even his own buisness, to try and save her."
    c "... But he couldn't."
    "I wiped my eyes, and caught my breath. I'm glad I was facing away from Trouble, but I think he saw the mask slip anyway."
    jump trouble_b3
    
    label trouble_b2: 
    c "My sister. When we were both going into college... around your age, actually, we had something bad happen to a family member of ours."
    t "If you don't mind me asking, what?"
    c "... Suffice it to say, someone died of something that should have been preventable."
    c "And... it radicalized her, I guess." 
    c "She did nothing for years and years but study, and research, and learn."
    c "Graduated, went back, graduated AGAIN, went abroad to learn what they had there, and then came back to start teaching it."
    t "Wow."
    c "Yeah. I wish I could've been like her, but instead..."
    "I raised my hands, to gesture out towards the field."
    c "This."
    c "But I think we're two sides of the same coin, me and her."
    c "See, beyond her dedication, there was passion. There was a goal to achieve, sure, but she found out she enjoyed doing it."
    c "She enjoyed learning, and helping people. In the same way, I found out I enjoy entertaining, and playing the game."
    c "I know I'm no physician, or a revolutionary... But I'd like to think that me being on the field helped someone grow, even just a little."
    t "... I know it helped me."
    "We shared a companionable silence for a small bit of time."
    jump trouble_b3

    label trouble_b3:
    c "Anyway... I get it."
    c "It's difficult to convince yourself that the happy route is the correct one."
    c "But... for what it's worth."
    c "I personally promise that you and your siblings will be looked after."
    c "I can't guarantee it'll be hillside villas and champagne, but it'll be decent."
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
    t "I'll... I'll see you there, Coach."
    "I smiled."
    c "Glad to hear it."

    return
