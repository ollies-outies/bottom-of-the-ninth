
# define c = Character("Casey")
# define w = Character("Whippy")

label WhippyStadium:
    $ HasWhippy = True

    show whippycard

    "Jordan ''Whippy'' Redslide. The unsung hulk of the minor leagues. Depending on how you look at it, fate either loves or hates Whippy."
    "He was blessed from birth with an unusually high capacity for mana, which meant unusually high-potency spells. Love."
    "He was also blessed with as much spell control as a fish has lung capacity. Namely, zilch. Hate."
    "When he was found by the minor leagues, his high energy levels meant he was able to swing with the big boys, with little to no actual muscle density. Love."
    "He's too strong, to the point of leveling buildings by brushing into them, and destroying arms with high fives. Hate."
    "I think that the prevailing idea that you have to choose between either hate or love is shortsighted. Whippy is living proof both can coexist."
    "Which is why, when I found him practicing his swing on the field itself, I think I knew what was running through his mind."
     
    show whippy

    "There was a pile of broken bats next to him, and another pile around his ankles of broken granite wizballs."
    "We typically trained with granite. Overdoing it on weight and density makes it easier to handle the official marble ones in-game."
    "'course, the fact he was breaking them wasn't a good sign. I watched him take one from a bucket nearby, toss it up, and turn it to powder. He sighed a deep sigh."
    c "Hey, kid. You look like you need a pitcher."
    "He looked up, surprised someone was talking to him, and sad that the person was trying to help."
    w "No, that's alright. I'm just trying to get this right."
    "Another in the air, another shower of powder."
    c "Look. I insist. You barely have enough time to grip your bat with two hands."
    "He looked almost insulted. I could tell from his glare, he wanted to say ''You're seeing what I'm doing with one hand, why the hell would I want to use two?'', but he didn't. Instead, he said,"
    w "Oh, uh. Alright."
    "I took the field again. Stood on my mark again. I won't lie, that alone felt good. But this wasn't for me right now."
    "Grabbed his bucket of balls, and he found a fresh bat. Stances were taken, and the cast was made."
    "He hit the ball square on, and it, to no one's surprise, exploded into shrapnel. He drooped the bat and dropped his stance."
    w "It's worse, I think, when I use two."
    "I shook my head."
    c "Kid, when you're only using one hand, it's all the bat's weight, and none of your control that you bring with your arms. The forces add together, but with none of the benefits."
    c "I want you to try to hit the ball with the butt of the bat. I'm gonna throw it low, okay? Keep the rest of it unmoving, and try to hit the ball I throw with the butt, alright?"
    "Whippy grumbled, but took his position. I threw, and he hit it square on, a ball that's been clocked at 102 MpH, with something the size of a bottlecap."
    "It exploded, nonetheless, but that precision is exactly what I was looking for on the Comedians. I chucked a bit."
    c "Hey, nice hit! Okay, one more thing, then I promise I'll be out of your feathers."
    w "... Alright. What?"
    c "I want you to do that exact same swing. I'm gonna pitch it high, but still act like you were hitting low, okay? The exact motion."
    "He stood, then took his stance, and I did exactly what I said. I aimed for the slow-moving, controlled sweet spot."
    "And the ball went sailing through the sky, just like a dream."
    "Whippy and I watched as it flew across the entire span of field and slammed smack into the goalpost. If this were a real game, that distance would've gotten us at least three points."
    c "Nice shot, kid."
    w "... I... How did that..."
    c "Well, a promise is a promise. I'll leave you be, pal."
    "I turned back into the entryway, and Whippy damn near ran me over trying to get me to stop."
    w "How did you- m-make me do that? How did I...? Do that how did you...?"
    c "I'm a professional, kid. You've got potential for the majors. Keep it up, alright?"
    "He stomped his foot, and damn near sent a crack through the vomitorium."
    w "Teach me, please."
    "What else could I say? The kid said please."
    c "Alright, sport, you're on the team. We'll meet up with the others at Hell Valley Stadium in a few days."
    "He stood in silence, before breaking out into sweat. I didn't know birds could sweat."
    w "T-te-t-t-TEAM?"
    c "Yeah, of course. The best way to learn is to play, and with arms like yours, we need to do that where there's medics on standby."
    c "Welcome to the Major League, kid."
    "I turned arond again, to walk back indoors, when he shouted one last thing."
    w "HEY!"
    w "DO I KNOW YOU FROM SOMEWHERE?"
    menu: 
            "..."

            "Yeah, I was pretty famous a while ago.": 
             jump whippy_B1

            "Nah. I'm a no one, nowadays.": 
             jump whippy_B1
    
    label whippy_B1:
    "I gave my answer, and waited for a response that never came."
    "Whatever Whippy was thinking was enough. And what I was thinking..."
    "Was how much I enjoyed getting back on the field."
    "Everything about it."
    "And, how much I enjoyed teaching someone a new way how to play."

    return
