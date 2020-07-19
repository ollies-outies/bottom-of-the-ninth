define xpick = 3

label TeamSelection:

menu:

    "Might: [Might] \nMagic: [Magic] \nMovement: [Movement]"

    "Aldric. 3 Might, 1 Magic, 2 Movement" if HasAldric == True:
        $ Magic += 1
        $ Might += 3
        $ Movement += 2
        $ HasAldric = False
        jump secondpick


    "Cileren. 2 Might, 2 Magic, 2 Movement" if HasCileren == True:
        $ Magic += 2
        $ Might += 2
        $ Movement += 2
        $ HasCileren = False
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
$ xpick -= 1
if xpick >=0:
    jump TeamSelection

jump DoneSelection