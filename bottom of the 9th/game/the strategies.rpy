
# define c = Character("Casey")
# define i = Character("Bratherford Hatherford")
# define v = Character("Victor")

label TheStrats:

    scene bg demonstadium
    # show finalteam

    c "With all of these strategies, we need two people in the back, defending our goal post, no matter what."
    c "What that means is that we should think about this in groups of four."
    "Four people to enact whatever we decide. I had to think about their strengths and weaknesses, and, for one more time, I turned to the cards."
    "This time, not for fate. But for that wonderful thing that makes fate managable."
    "Statistics."
    "Each card comes with a Potential Power Rating on it."
    "These are measures of the individual's potency in each of three categories:"
    "Might, Movement, and Magic."
    "If we want this to work, we're gonna have to rely on the folks over at Coven Card and Chewing Gum to be right."
    

    c "This first one, I'm calling the Maneuver."
    c "It's an all-out physical assault. Ramming through, throwing people to the side, etc. There's not a thing subtle about this."
    c "We'd be treating this more like a bloodsport than it already is."
    "I'd estimate we'd need... at least 10 Might in a group to have this work."
   
    c "This next one, I've dubbed the Scheme."
    c "We're gonna be moving so fast, I don't even think they'll have time to follow us. It'll be a cup and ball game, at mach speed."
    c "They can't hit what they can't see, after all."
    "For something like this... We'd definetly need at least 10 Movement in the group."

    c "Next up, the Plot." 
    c "This might get a bit hazy, so I've drawn you all diagrams. It's a lotta creative casting, and it's all timing based."
    c "Thing is, if we can land it, it'll guarantee us the win for certain."
    "We would definitly need at least - at LEAST - 10 Magic in the group to even try this."

    c "After that, we got the Technique."
    c "This is a classic, with a little focus on everything. It's a lot of fundamentals, but it's a lot of subversions too."
    c "We're gonna be playing it old school with this, and playing it right."
    "When I did this back in the day, I had to have a group with at least 6 in each stat."

    c "Then finally, the Dream."
    c "This... this might sound faulty, but I had this vision, of a play so convoluted it was impossible to follow, and impossible to counter."
    c "I... I don't have anything backing this up that it'll even work, but I just know that it will."
    "... We would need a group with a total stat count of, like, 24 for this to even POTENTIALLY work."


    "Now, it was time to pick my four. But who to pick?"
 
    jump TeamSelection
label DoneSelection:

    c "You two're gonna play defense. You four're the offense. Now, listen up." 

    menu: 
    
        c "What we're gonna do is..."
  
        "The Maneuver.":
            jump strat1

        "The Scheme.":
            jump strat2

        "The Plot":
            jump strat3

        "The Technique":
            jump strat4

        "The Dream":
            jump strat5


    label strat1:
    c "Yeah, the Maneuver."
    c "Okay, everyone. You get one personal item, so make it count. I recommend something good for hitting, like a sword or a particularly good rock."
    c "Oh, and go easy on the ghost, wouldja?"
    "I watched them as they went into the field, the crowd so loud you could barely hear yourself think."
    "It was out of my hands, now. All I could do is watch them flourish, hope, and listen to the announcements."
    i "LADIES, GENTLEMEN, INDIVIDUALS OF ALL VARIETIES, ARE YOU READY TO CAAAAAST?"
    i "YOU'RE LISTENING TO THE ONE AND ONLY BRATHERFORD HATHERFORD, GIVING YOU THE PLAY-BY-PLAY."
    i "WE'RE COMING AT YOU LIVE FROM BEAUTIFUL DOWNTOWN JUDECCA, BROADCASTING THROUGH THE AETHER THE HOTTEST GAME IN WIZARDBALL!"
    i "And I DO mean that literally, folks! The ninth circle of Hell has many constantly roaring fires, that give heck that notoriously famous look, and lighting!"
    i "No doubt the players of tonight's game are feeling the heat, as they step onto the field!" 
    i "And if you can't stand the heat, then get out of Hell's kitchen, AM I RIGHT FOLKS?"
    i "Tonight's game is between the Hell Valley Tophets and the Katabas Comedians!"
    i "And the coach must BE a comedian themself, look at this team! Nothing but rookies, from all sorts of teams."
    i "There's gonna be a miracle in Hell if they take home the win, everyone, especially considering the lineup that the Tophets seem to have!"
    i "Butch Stanley, Tony Squatthrust, Dingo Fleshripper... And that's not even considering the floating apparition centerfield!"
    i "Folks, I've got to be honest, I have NO idea who that is, but if it's on the Tophets' side, it's gotta be a force to be reckoned with."
    i "AND WITH THAT, BOTH TEAMS HAVE REACHED THEIR MARKS! THE GAME IS ON WHEN THE BALL IS CAST FIRST. WHO'S GOT THE COUNTER READY?"
    i "AND THEY'RE OFF! WITH A BOLT, THE BALL FALLS INTO BUTCH'S FIRM BUT SOFT HANDS, AND-"
    i "OH, ONE OF THE ROOKIES WITH AN INTERCEPTION! Grabs the ball RIGHT from Butch's grasp!"
    i "Wait, no! Butch is still holding the ball!"
    i "The Rookie just TORE BUTCH'S ARM OFF, AND IS TRAVELING WITH IT AS A MAKESHIFT SHIELD!"
    i "A brutal maneuver, but technically allowed, after players finally were included in the list of 'approved envronmental hazards'."
    i "AND THE FIRST POINT GOES TO THE COMEDIANS, WITH A BRUTAL SWING! The rookie's thrown the arm to a child, who will no doubt hang it from their wall!"
    i "I think we all love little trophies from game day like that. I remember my first game, I-"
    i "AND WE'RE BACK! THE BALL IS THROWN, THE ROOKIE FROM THE COMEDIANS GETS THE BALL!"
    i "The OTHER rookie, I should've said, the OTHER rookie gets the ball!"
    i "I really should have looked into what these jokers' names were, but I'm gonna be honest folks, I didn't expect them to get a single point-"
    i "OH, LET ALONE TWO?! THE ROOKIE WITH THE BALL WAS SURROUNDED BY THEIR TEAMMATES, AND FORMED AN OFFENSIVE PHALANX THAT RAMMED THROUGH THE TOPHETS' LONE DEFENSIVE PLAYER!"
    i "He's laying on the ground now, I think that's Tony Squatthrust on the ground, devastated by the might these jesters are packing!"
    i "The teams take their spots, Tony still on the floor, as the third ball of the night is delivered, sky high."
    i "Oh, and the apparition has the ball! It's gone over the Comedians' heads, like an inside joke with new friends, as these newbies watch the oldest trick in the book!"
    i "BOOM SHAKKALAKKA, LADIES AND GENTS, THE GHOST HAS PERFORMED A SLAM DUNK. GOD I LOVE THIS SPORT."
    i "Oh, and now it looks like Tony's back on his feet! Folks, we're seeing what not skipping leg day can do!"
    i "He's rushing down the Comedians, and - I don't believe it! They're going for AN IMMEDIATE FOLLOW-UP DUNK??"
    i "THE COMEDIANS GO FOR THE BLOCK, BUT THE EFFORT IS WASTED, TONY'S GOT JUMPS FOR DAYS!" 
    i "BOOM GOES THE DYNAMITE! TWO POINTS ON BOTH SIDES, AS TONY GETS IT OFF THE REBOUND!"
    i "The score's tied, and both teams are looking tired. One of them doesn't have an arm, just a reminder, Butch is still without an arm."
    i "The ball is cast, and there's-!"
    i "I don't believe it! For you folks at home, there's a rumble in the center of the ring, as both teams have a player gripping the ball with all their might!"
    i "THE REST OF THE TEAM RUSHES TO THEIR AID, GRIPPING THEM FROM THE WAIST, PULLING WITH ALL THEIR STRENGTH!"
    i "Due to Shimadzu's Law, in a case like this, the entire game suddenly gets put in the balance!"
    i "For those who are unaware, in tug-of-war situations, each player engaged in the war becomes a point, should the opposing side score!"
    i "With both teams on all hands on deck, the Nuclear Option is activated, and whoever gets this next point gets the game!!"
    i "This is it, folks. Do the Tophets singlehandly win the game? Or can the Comedians deliver their final punchline?"
    i "OH, AND WITH A CLOUD OF SMOKE, THE TEAMS HAVE SLIPPED FORWARD! THIS IS NAIL BITING. AND WHEN THE DUST CLEARS..."
    if Might >= 10:
        i "THE COMEDIANS STAND, BALL IN HAND! THE COMEDIANS WIN! THE COMEDIANS WIN!"
        jump teamWin
    else:
        i "THE TOPHETS STAND, BALL IN HAND! THE TOPHETS WIN! THE TOPHETS WIN!"
        jump teamLoss


    label strat2:
    c "Yeah, the Scheme."
    c "Okay everyone, don't forget: the bleachers are technically legal playing ground, so long as legal playing ground is on them." 
    c "Kick some dirt up, see what you can do. You got this."
    "I watched them as they went into the field, the crowd so loud you could barely hear yourself think."
    "It was out of my hands, now. All I could do is watch them flourish, hope, and listen to the announcements."
    i "LADIES, GENTLEMEN, INDIVIDUALS OF ALL VARIETIES, ARE YOU READY TO CAAAAAST?"
    i "YOU'RE LISTENING TO THE ONE AND ONLY BRATHERFORD HATHERFORD, GIVING YOU THE PLAY-BY-PLAY."
    i "WE'RE COMING AT YOU LIVE FROM BEAUTIFUL DOWNTOWN JUDECCA, BROADCASTING THROUGH THE AETHER THE HOTTEST GAME IN WIZARDBALL!"
    i "And I DO mean that literally, folks! The ninth circle of Hell has many constantly roaring fires, that give heck that notoriously famous look, and lighting!"
    i "No doubt the players of tonight's game are feeling the heat as they step onto the field!" 
    i "And if you can't stand the heat, then get out of Hell's kitchen, AM I RIGHT FOLKS?"
    i "Tonight's game is between the Hell Valley Tophets and the Katabas Comedians!"
    i "And the coach must BE a comedian themself, look at this team! Nothing but rookies, from all sorts of teams."
    i "There's gonna be a miracle in Hell if they take home the win, everyone, especially considering the lineup that the Tophets seem to have!"
    i "Vash Vanderquick, Rudy Equire, Thunder Rolling... And that's not even considering the floating apparition centerfield!"
    i "Folks, I've got to be honest, I have NO idea who that is, but if it's on the Tophets' side, it's gotta be a force to be reckoned with." 
    i "AND WITH THAT, BOTH TEAMS HAVE REACHED THEIR MARKS! THE GAME IS ON WHEN THE BALL IS CAST FIRST. WHO'S GOT THE COUNTER READY?"
    i "OH, AND WITHIN MOMENTS OF THE BALL GETTING LAUNCHED, ONE OF THE COMEDIANS HAS GRABBED IT! THEY'RE RUSHING TO THE GOAL, RECKLESS ABANDON FLOWING LIKE THE WIND IN THEIR EYES!"
    i "A formation of Tophets assemble to block the runner, they GET the pin, and th-"
    i "THE RUNNER DIDN'T HAVE THE BALL?! The Tophets scramble to their feet, looking around for the rest of the rookies, who, believe it or not, have all seemed to disappear!"
    i "The field is still registering them as in-game, though, so where could - OH!" 
    i "EMERGING FROM THE DEPTHS BELOW THE GOALPOST, A HAND HOLDING THE BALL! COMEDIANS GET FIRST POINT, WITH A CLASSIC REVERSE WHACK-A-MOLE!"
    i "They return to their marks, marking new paths as they do! They're flicking the dirt into the crowd, into the stands, onto the roof!"
    i "This is a risky play, folks, as both sides can use these newly-formed dirt roads. The crowd seems entirely enthused by the inclusions, and have begun to spread the dirt even further!"
    i "This once beautiful field is getting turned into a wizardball megahighway, folks, and it's purely wonderful. The marks are taken again, and-"
    i "OH WHAT'S THIS?! A TOPHET HAS ALREADY SCORED A POINT! VASH VANDERQUICK, SIGHT UNSEEN, HAS MOVED HIS OWN MARK TO BEHIND THE GOALPOAST!"
    i "While technically legal, Mark Mismanagement IS viewed as a dick move in the professional community, but everyone loves a heel, now don't they?"
    i "The next ball is cast, and it's already gone? And-"
    i "Well I-..."
    i "Folks, I don't know how to tell you this, but none of the players are visible to the naked eye."
    i "Not to worry, though! This announcer came prepared, with a pair of Energy Following Goggles. Whether invisible or well-disguised, we will soon learn the- WHAT IN THE BLAZES?!"
    i "IT'S PURE SPEED! THEY'RE MOVING SO FAST, I-I-I CAN BARELY KEEP UP! RUDY TOSSES IT TO THE GHOST, NO, THE GHOST WAS AN AFTER-IMAGE OF A COMEDIAN, WHO CATCHES IT, BUT IT'S STOLEN BY-"
    i "THE THIEF IS GO- INTERCEPTION BY TH- REBOUND CATCH FROM V- BUT THE- AND THEN- I- I'M SORRY FOLKS, I KNOW THIS DOESN'T MAKE FOR GOOD RADIO, BUT I'M CALLING IT LIKE I SEE IT!"
    i "And... folks, everyone just stopped dead in the tracks!"
    i "I don't have ears down there, but it looks like someone was keeping track of the score, and someone's ALREADY WON!" 
    i "This is unprecedented. Let me get down there, talk to a referee. Folks, I'll be right back."
    i "..." 
    i "....."
    i "FOLKS, I'VE GOT THE RESULTS IN FROM THE OFFICIAL FIELDSIDE REFEREE, who, by the way, lets give a hand to for keeping up with that, FOR THE FINAL TALLY."
    if Movement >= 10:
        i "TOPHETS 91,"
        i "COMEDIANS 99."
        i "COMEDIANS TAKE THE GAME! COMEDIANS WIN!"
        jump teamWin
    else:
        i "COMEDIANS 91,"
        i "TOPHETS 99."
        i "TOPHETS TAKE THE GAME! TOPHETS WIN!"
        jump teamLoss

    label strat3:
    c "Yeah, the Plot."
    c "Okay everyone, remember that if you hold hands and believe in the power of friendship, it's been proven to make your Lightning Bolts 80% more vicious." 
    c "Kick ass, have fun, and take names!"
    "It was out of my hands, now. All I could do is watch them flourish, hope, and listen to the announcements."
    i "LADIES, GENTLEMEN, INDIVIDUALS OF ALL VARIETIES, ARE YOU READY TO CAAAAAST?"
    i "YOU'RE LISTENING TO THE ONE AND ONLY BRATHERFORD HATHERFORD, GIVING YOU THE PLAY-BY-PLAY."
    i "WE'RE COMING AT YOU LIVE FROM BEAUTIFUL DOWNTOWN JUDECCA, BROADCASTING THROUGH THE AETHER THE HOTTEST GAME IN WIZARDBALL!"
    i "And I DO mean that literally, folks! The ninth circle of Hell has many constantly roaring fires, that give heck that notoriously famous look, and lighting!"
    i "No doubt the players of tonight's game are feeling the heat, as they step onto the field!" 
    i "And if you can't stand the heat, then get out of Hell's kitchen, AM I RIGHT FOLKS?"
    i "Tonight's game is between the Hell Valley Tophets and the Katabas Comedians!"
    i "And the coach must BE a comedian themself, look at this team! Nothing but rookies, from all sorts of teams."
    i "There's gonna be a miracle in Hell if they take home the win, everyone, especially considering the lineup that the Tophets seem to have!"
    i "Zyrtzes the Great, Thrunbungus the Magnificent, Michel... And that's not even considering the floating apparition centerfield!"
    i "Folks, I've got to be honest, I have NO idea who that is, but if it's on the Tophets' side, it's gotta be a force to be reckoned with."
    i "AND WITH THAT, BOTH TEAMS HAVE REACHED THEIR MARKS! THE GAME IS ON WHEN THE BALL IS CAST FIRST. WHO'S GOT THE COUNTER READY?"
    i "STARTING THINGS OFF, A SPECTRAL HAND HAS APPEARED FROM THE COMEDIANS' SIDE! Classic first move, almost guarantees the ball."
    i "WHICH IS WHY THE TOPHETS GO FOR IT TOO! The hands now appear to be going for a Ro Sham Bo gambit, lets see if it pays off."
    i "OH AND COMEDIANS GET THE CRUSH WITH A ROCK! NOTHING BEATS ROCK, FOLKS! The ball goes to the Comedians, and then the lot of them..."
    i "Assume a cheer pyramid? Is this to try and throw the groove of the Tophets off? I've heard of charm builds, but none like th-HWHOAH!"
    i "WITH A SONIC BOOM, THE BALL GOES STRAIGHT INTO THE TOPHETS' POST, LEAVING A DENT WHERE IT LANDS! I've heard of Magic Missiles, but this is RIDICULOUS!"
    i "But the pyramid was a risky play! An Icy Patch directly under the two rookies playing land development causes them to go TOPPLING, LEAVING JUST THE GOALIES!"
    i "A Mirror Self is tried, to make the goal seem fully guarded, but balls don't care about illusions, folks! It soars directly on, getting the Tophets a point!"
    i "The ball is cast once again, and the receiver on the Tophets' end goes for it- but stops dead in his tracks, giggling!"
    i "Zyrtzes the Great is ON HIS BACK, IN HYSTERICS! Looks like the Comedians finally got to him, in more ways than one. The ball falls EASILY into the rookies, who-"
    i "OH, A CIRCLE HAS BEEN DRAWN IN CHALK! THE COMEDIANS HAVE BROUGHT CHALK IN, AND ARE NOW PERFOMING SOME KIND OF RITUAL? THEY'RE CHANTING IN A LANGUAGE I-I SIMPLY DON'T UNDERSTAND, FOLKS."
    i "THE TOPHETS ARE BEING INFECTED BY SOME KINDA HYSTERIA, ALL OF THEM EXCEPT THE GHOST! Guess the joke went right over his head!"
    i "And into... what looks like row G, seat 310? Unless that lady there is just getting her jollies from watching the ritual."
    i "Which, the apparition appears to want to break up! He crosses the threshold, and places his hand on one of t-"
    i "OH MY GOODNESS! THERE WAS AN EXPLOSION, LADIES AND GENTLEMEN, AND BOTH TEAMS ARE SEEMINGLY OUT FOR THE COUNT!"
    i "BUT THE BALL ITSELF IS FLOATING, AND... GLOWING A COLOR I CAN ONLY DESCRIBE AS A LIGHT INCANDESCENT... PURPLISH YELLOW?"
    i "IT'S... IT'S MOVING THROUGH THE AIR! LADIES AND GENTLEMEN, WHILE THIS IS A MAGIC GAME AND THINGS FLY OFTEN, VERY RARELY DO WE SEE WHAT APPEARS TO BE A BALL GAIN SENTIENCE!"
    i "IT'S STILL LEGALLY IN PLAY, AS IT'S YET TO LEAVE THE AIR! WHO WILL THIS BALL DECIDE TO SIDE WITH? HAS THE RITUAL BEEN A SUCCESS?"
    i "I'M ON THE EDGE OF MY SEAT, LADIES AND GENTS, IT IS FLYING TO A POST, AND ONCE IT'S THERE, IT WILL STAY THERE, EFFECTIVELY GENERATING INFINTE POINTS."
    if Magic >= 10:
        i "IT IS GOING... TO THE TOPHET'S POST!!! COMEDIANS WIN, A MILLION TO ONE! JUST LIKE THEIR CHANCE OF ACTUALLY PULLING THIS OFF, THEY'VE WON, A MILLION TO ONE!"
        jump teamWin
    else:
        i "IT IS GOING... TO THE GHOST!!! THE ALLIANCE HAS BEEN MADE, SPECTRAL TO SPECTRAL, AND THE COMEDIANS' POST IS ASSAULTED BY THE BALL! JUST LIKE THEIR CHANCES OF PULLING THIS OFF, THEY LOST A BILLION TO ONE!"
        i "Oh god, I'm gonna have to get an interview with that ball after this."
        jump teamLoss

    label strat4:
    c "Yeah, the Technique."
    c "Okay gang. This might seem like it's old tech, but that's because it is. I want you to get out there, and funk out those fundamentals."
    c "Those funkdamentals."
    c "Okay, pretend I didn't say that, and go win this thing!"
    "I watched them as they went into the field, the crowd so loud you could barely hear yourself think."
    "It was out of my hands, now. All I could do is watch them flourish, hope, and listen to the announcements."
    i "LADIES, GENTLEMEN, INDIVIDUALS OF ALL VARIETIES, ARE YOU READY TO CAAAAAST?"
    i "YOU'RE LISTENING TO THE ONE AND ONLY BRATHERFORD HATHERFORD, GIVING YOU THE PLAY-BY-PLAY."
    i "WE'RE COMING AT YOU LIVE FROM BEAUTIFUL DOWNTOWN JUDECCA, BROADCASTING THROUGH THE AETHER THE HOTTEST GAME IN WIZARDBALL!"
    i "And I DO mean that literally, folks! The ninth circle of Hell has many constantly roaring fires, that give heck that notoriously famous look, and lighting!"
    i "No doubt the players of tonight's game are feeling the heat, as they step onto the field!" 
    i "And if you can't stand the heat, then get out of Hell's kitchen, AM I RIGHT FOLKS?"
    i "Tonight's game is between the Hell Valley Tophets and the Katabas Comedians!"
    i "And the coach must BE a comedian themself, look at this team! Nothing but rookies, from all sorts of teams."
    i "There's gonna be a miracle in Hell if they take home the win, everyone, especially considering the lineup that the Tophets seem to have!"
    i "Sleve Mcdichael, Raul Chamgerlain, Glenallen Mixon, Bobson Dugnut... And that's not even considering the floating apparition centerfield!"
    i "Folks, I've got to be honest, I have NO idea who that is, but if it's on the Tophets' side, it's gotta be a force to be reckoned with."
    i "AND WITH THAT, BOTH TEAMS HAVE REACHED THEIR MARKS! THE GAME IS ON WHEN THE BALL IS CAST FIRST. WHO'S GOT THE COUNTER READY?"
    i "The cast is made, and with a HEARTY SWING, the Tophets knock it dead into Comedians' territory! The rookie playing second reciever grabs it and tucks, then makes a straight shot for center field!"
    i "Looks like there's a blocksquad set up, but the Comedian goes for- is that a Greased Nosedive??"
    i "Holy crap, it absolutely is! With the support from their teammate, the ground under the rookie's been slicked, and they slide under the blockers ENTIRELY!"
    i "That takes out those two playing Forward Defence, but that leaves the Hardknocker still, and Bobson's a hell of a Hardknocker! He takes the rookie down, with a PATENTED Dugnut Special!"
    i "Oh, but the reciever gets a hand free, and throws it to the Comedians' Handguard, who takes off like a BULLET! Looks like they're going for the leftmost route." 
    i "Smart tactic from the rookie Handguard, everyone knows that the Tophets' weakest link is Kevin Nogilney, Left-Center Outfielder for the Tophets. Sidebar, I'm surprised the spirit replaced Mike Truk instead of him, to be honest."
    i "The handguard plows through, and... holds their hand above their head? W-wait, is this-? People at home, please avert your childrens' eyes, because the rule of Sudden Death has just been called!"
    i "We've been tunnelvisioned on the Handguard, we didn't even notice that the rest of the Comedians have taken their spots at all the cardinal directions, letting the sole Reciever pinned in the middle assume the title of Ultimate Center Fielder!"
    i "This is unbelievable. This is unbelievable. The Comedians have a single shot, taken with all the interuptions the Tophets can throw at them, to win the game."
    i "Such a risky maneuver, and on their first game?! This is something even VETERANS are scared to do!"
    i "AND AT 0/0??!"
    i "The ball is fired to the U.C.F., who lines it up...! The Tophets are coming from every angle, charging like a pack of wild animals, but they're too late! The ball is cast, and...!"
    if Magic >= 6 && Might >= 6 && Movement >=6:
        i "SCORES, FOR THE COMEDIANS, THE ONLY SCORE THEY'D NEED, AND JUST LIKE THAT, THEY'VE SECURED THE GAME, FOLKS! YOU HEARD IT HERE FIRST, THESE COMEDIANS WON THEIR FIRST GAME WITH A GOD DAMN SUDDEN DEATH SHOT!"
        jump teamWin
    else:
        i "MISSES ENTIRELY!!! THE COMEDIANS LOSE, BUT WHAT A HELL OF A SHOW! WHAT A SHOW, FOLKS!"
        jump teamLoss

    label strat5:
    c "Yeah. The Dream."
    c "If we're gonna wanna take this, we're gonna have to do the Dream. But I know, if anyone can do it... It's you guys."
    c "Give 'em hell."
    "I watched them as they went into the field, the crowd so loud you could barely hear yourself think."
    "It was out of my hands, now. All I could do is watch them flourish, hope, and listen to the announcements."
    i "LADIES, GENTLEMEN, INDIVIDUALS OF ALL VARIETIES, ARE YOU READY TO CAAAAAST?"
    i "YOU'RE LISTENING TO THE ONE AND ONLY BRATHERFORD HATHERFORD, GIVING YOU THE PLAY-BY-PLAY."
    i "WE'RE COMING AT YOU LIVE FROM BEAUTIFUL DOWNTOWN JUDECCA, BROADCASTING THROUGH THE AETHER THE HOTTEST GAME IN WIZARDBALL!"
    i "And I DO mean that literally, folks! The ninth circle of Hell has many constantly roaring fires, that give heck that notoriously famous look, and lighting!"
    i "No doubt the players of tonight's game are feeling the heat, as they step onto the field!" 
    i "And if you can't stand the heat, then get out of Hell's kitchen, AM I RIGHT FOLKS?"
    i "Tonight's game is between the Hell Valley Tophets and the Katabas Comedians!"
    i "And the coach must BE a comedian themself, look at this team! Nothing but rookies, from all sorts of teams."
    i "There's gonna be a miracle in Hell if they take home the win, everyone, especially considering the lineup that the Tophets seem to have!"
    i "Devin Odinson, Laura McFarkus... and that's not even considering the floating apparition centerfield."
    i "Folks, I've got to be honest, I have NO idea who that is, but if it's on the Tophets' side, it's gotta be a force to be reckoned with." 
    i "AND WITH THAT, BOTH TEAMS HAVE REACHED THEIR MARKS! THE GAME IS ON WHEN THE BALL IS CAST FIRST. WHO'S GOT THE COUNTER READY?"
    i "THE BALL IS CAST, AND WITH A SWIPE THE COMEDIANS HAVE THE BALL TUCKED AND READY!"
    i "But the Tophets are closing in from all sides, sparks surging from their fingers as they do! A FIGHT'S A-BREWIN'!"
    i "With a zap, the first spell of the night's cast, with an Ice Bolt from the Tophets' reciever! A few Comedians send back spells of their own, but they all miss!"
    i "The rookie Handguard soaks the full blast of the well-aimed Ice Bolt, and sends back a terrifying Skeletal Grasp that manages to hit! It lands squarely, giving their bone structure a squeezing they're sure to remember!"
    i "But bones aren't the only thing getting squeezed, as the Tophets' Hardknocker gets the rookie holding the ball in a patent pending UNDERWORLD HEADLOCK!" 
    i "Somehow, the rookie seemed? Prepared for this? They're let go, as a teammate's Poison Splash that seemed to go wide hits the Hardknocker squarely in the back of the head!"
    i "This is followed up by just a GARBAGE AIRBALL by the rookie, nowhere near the Tophets' post! Well, there's a reason that these are still rookies, an-DWHAA?"
    i "LADIES AND GENTS, THE BALL HAS BEEN HIT BY THREE CASTS AT ONCE! FROM EVERY DIRECTION, THE SPELLS THAT HAD MISSED COLLIDED, BREAKING THE BALL INTO PIECES!"
    i "THE TOPHETS GO TO RESET, BUT THE COMEDIANS ARE STILL PLAYING AS IF THE BALL IS ACTIVE? OH- AND MY RULES CHECKER HAS JUST TOLD ME THAT'S BECAUSE IT STILL TECHNICALLY IS!!!"
    i "AS THE COLLISION HAPPENED MIDAIR, THE BALL HAS YET TO HIT THE GROUND, MEANING IT'S STILL IN PLAY! THE ONLY TOPHET WHO'S SEEMED TO NOTICE IS THE APPARITION, WHO..."
    i "From up here in this box, folks at home, it seems as though he's HESITATING! I swear, there is something strangely familiar about that ghost. OH!"
    i "THE TOPHETS FINALLY REALIZE WHAT WAS WRONG, BUT IT'S TOO LATE! VICTOR'S LAW MEANS THE GAME IS STILL AFOOT, AND THE COMEDIANS HAVE ALREADY REACHED THE GOALPOST!"
    i "EACH SEGMENT IS COUNTED INDIVIDUALLY! EACH CONTACT IS A POINT! THERE MUST HAVE BEEN A BILLION PIECES, AT LEAST! LADIES AND GENTLEMEN, THESE BALLS ARE MADE OF MARBLE!"
    i "COMEDIANS WIN! COMEDIANS WIN! IN A TWIST OF FATE NO ONE SAW COMING, THE COMEDIANS FUCKING WIN!"
    #there is no way to lose the dream scenario, so there is only a wincon


    i "Oh, good golly Miss MOLLY. That was one of, if not THE, tightest games I've ever seen."
    i "My name's been Bratherfurd Hatherfurd, and you will HEAR me... Next time."

 
label teamWin:    
    scene bg smoke
    "So, after that, the Comedians became a household name in a moment."
    "We won a bunch more, and I'll be fair, we did also lose a few."
    "But more than that, we made something of ourselves. We let anyone who doubted us know exactly who we were, and exactly what we've done."
    "And, more surprising, I think, than us actually doing well for ourselves... was that that skuzbag Ordog went through with his side of the deal."
    "After the game in Hell Valley, he relinquished control. I didn't get my position back as a player, but I think that's for the best, huh?"
    v "Yeah, honestly. You're looking older every day. Was I really gone that long?"
    c "Hey, you'd be surprised what five years of being locked inside will do to you."
    v "I'm sure that the ''Being Inside'' is what gave you all those crowsfeet."
    c "Hey, I saved your ass from Hell! A little respect please?"
    v "Thank you for, unintentionally, being in the right place to save me from Hell."
    c "Did you not get ANY of that story? FATE brought me there!" 
    v "Yeah, yeah."
    v "... Genuinely, thanks, C.C.. I uh... I'm glad to be back."
    c "... Happy to help, V."
    "I could say something more, about fate guiding people together. Or, maybe its uncontrollable nature."
    "How a story could be told a thousand times, and each time be something completely different, based on the whims of fate deciding it should be."
    "But I think we know this all already." 
    "Sometimes, I think it's better to just let what's been said... be said,"
    c "Happy to help."
    jump endLoss

label teamLoss:   
    scene bg smoke
    "It's funny, isn't it? All that, to be shafted in the end. Fate's a sucker, like that."
    "..."
    "Honstly, I feel worse for those kids. They just got a taste of fame, and..."
    "Eh. All we can do is that my bad fate doesn't rub off on them."
    "..."
    "Maybe, after that big game, some major league manager saw them, and put their faces on a boxsa Corn Puffs. You remember those?"
    "..." 
    "Yeah, they weren't the best, but they weren't the worst neither. Kinda like me, in a way, huh?"
    "..."
    "I.. I'm used to being locked indoors, alone. Did it for five years after all. It's just... a bit hotter this time"
    "And besides, this time I'm not alone."
    c "Huh, bud?"
    v "..."
    c "Yeah, that's okay. I'll do enough talking for both of us."
    v "..."
    c "... Do you wanna hear it again? I'll change it up this time, make it more interesting, I promise."
    v "..." 
    c "Alright. Here we go."
    scene bg black
    c "It was the fifth anniversary."
label endLoss:
    


return
