
label TeamSelection:

menu:

    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        jump secondpick


    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        jump secondpick


    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        jump secondpick


    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        jump secondpick


    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        jump secondpick


    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        jump secondpick


    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        jump secondpick


    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        jump secondpick


    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        jump secondpick


    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        jump secondpick

label secondpick:
    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        jump thirdpick

    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        jump thirdpick

    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        jump thirdpick

    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        jump thirdpick

    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        jump thirdpick

    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        jump thirdpick

    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        jump thirdpick

    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        jump thirdpick


    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        jump thirdpick

    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        jump thirdpick

label thirdpick:

    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        jump fourthpick

    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        jump fourthpick

    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        jump fourthpick

    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        jump fourthpick


    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        jump fourthpick

    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        jump fourthpick


    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        jump fourthpick


    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        jump fourthpick

    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        jump fourthpick


    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        jump fourthpick

label fourthpick:

    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        jump DoneSelection


    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        jump DoneSelection

    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        jump DoneSelection


    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        jump DoneSelection


    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        jump DoneSelection

    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        jump DoneSelection


    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        jump DoneSelection

    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        jump DoneSelection

    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        jump DoneSelection

    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        jump DoneSelection

jump DoneSelection