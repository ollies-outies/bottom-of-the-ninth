
define c = Character("Casey")
define b = Character("Aldric")
define l = Character("Cileren")
define f = Character("Dandy")
define z = Character("Diver")
define du = Character("Dusk")
define r = Character("Father Robin")
define o = Character("Ock")
define s = Character("Shaw")
define a = Character("Ock and Shaw")
define p = Character("Scylla")
define t = Character("Trouble Comings")
define w = Character("Whippy")
define i = Character("Bratherford Hatherford")
define v = Character("Victor")

label start:

    scene bg market
    call AldricMarket
    call CilerenMarket
    call DandyMarket
    call DiverMarket
    call DuskMarket
    call FatherRobinMarket
    call OckShawMarket
    call ScyllaMarket
    call TroubleMarket
    call WhippyMarket

    scene bg stadium
    call AldricStadium
    call CilerenStadium
    call DandyStadium
    call DiverStadium
    call DuskStadium
    call FatherRobinStadium
    call OckShawStadium
    call ScyllaStadium
    call TroubleStadium
    call WhippyStadium

return
