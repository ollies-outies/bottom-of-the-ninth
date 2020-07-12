
label TeamSelection:

menu:

    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        $ HasAldrick = False
        jump secondpick


    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        $ HasCiliren = False
        jump secondpick


    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        $ HasDandy = False
        jump secondpick


    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        $ HasDiver = False
        jump secondpick


    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        $ HasDusk = False
        jump secondpick


    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        $ HasFatherRobin = False
        jump secondpick


    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        $ HasOckShaw = False
        jump secondpick


    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        $ HasScylla = False
        jump secondpick


    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        $ HasTrouble = False
        jump secondpick


    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        $ HasWhippy = False
        jump secondpick

label secondpick:
    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        $ HasAldrick = False
        jump thirdpick

    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        $ HasCiliren = False
        jump thirdpick

    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        $ HasDandy = False
        jump thirdpick

    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        $ HasDiver = False
        jump thirdpick

    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        $ HasDusk = False
        jump thirdpick

    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        $ HasFatherRobin = False
        jump thirdpick

    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        $ HasOckShaw = False
        jump thirdpick

    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        $ HasScylla = False
        jump thirdpick


    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        $ HasTrouble = False
        jump thirdpick

    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        $ HasWhippy = False
        jump thirdpick

label thirdpick:

    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        $ HasAldrick = False
        jump fourthpick

    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        $ HasCiliren = False
        jump fourthpick

    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        $ HasDandy = False
        jump fourthpick

    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        $ HasDiver = False
        jump fourthpick


    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        $ HasDusk = False
        jump fourthpick

    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        $ HasFatherRobin = False
        jump fourthpick


    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        $ HasOckShaw = False
        jump fourthpick


    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        $ HasScylla = False
        jump fourthpick

    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        $ HasTrouble = False
        jump fourthpick


    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        $ HasWhippy = False
        jump fourthpick

label fourthpick:

    "Aldrick. 3 Might, 1 Magic, 2 Movement" if HasAldrick == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        $ HasAldrick = False
        jump DoneSelection


    "Ciliren. 2 Might, 2 Magic, 2 Movement" if HasCiliren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        $ HasCiliren = False
        jump DoneSelection

    "Dandy. 2 Might, 1 Magic, 3 Movement" if HasDandy == True:
        $ Magic += 1
        $ Might += 2
        $ Movement += 3
        $ HasDandy = False
        jump DoneSelection


    "Diver. 1 Might, 4 Magic, 1 Movement" if HasDiver == True:
        $ Magic += 4
        $ Might += 1
        $ Movement += 1
        $ HasDiver = False
        jump DoneSelection


    "Dusk. 1 Might, 3 Magic, 2 Movement" if HasDusk == True:
        $ Magic += 3
        $ Might += 1
        $ Movement += 2
        $ HasDusk = False
        jump DoneSelection

    "Father Robin. 2 Might, 3 Magic, 1 Movement" if HasFatherRobin == True:
        $ Magic += 3
        $ Might += 2
        $ Movement += 1
        $ HasFatherRobin = False
        jump DoneSelection


    "Ock and Shaw. 1 Might, 2 Magic, 3 Movement" if HasOckShaw == True:
        $ Magic += 2
        $ Might += 1
        $ Movement += 3
        $ HasOckShaw = False
        jump DoneSelection

    "Scylla. 1 Might, 1 Magic, 4 Movement" if HasScylla == True:
        $ Magic += 1
        $ Might += 1
        $ Movement += 4
        $ HasScylla = False
        jump DoneSelection

    "Trouble. 3 Might, 2 Magic, 1 Movement" if HasTrouble == True:
        $ Magic += 2
        $ Might += 3
        $ Movement += 1
        $ HasTrouble = False
        jump DoneSelection

    "Whippy. 4 Might, 1 Magic, 1 Movement" if HasWhippy == True:
        $ Magic += 1
        $ Might += 4
        $ Movement += 1
        $ HasWhippy = False
        jump DoneSelection

jump DoneSelection