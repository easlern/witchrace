import random

def wealthInc(target):
    target.wealth += 1
def wealthDec(target):
    target.wealth = max(0, target.wealth - 1)
def healthInc(target):
    target.health = min(4, target.health + 1)
def healthDec(target):
    target.health = max(0, target.health - 1)
def fameDec(target):
    target.fame = max(0, target.fame - 1)
def slaveDec(target):
    target.slaves = max(0, target.slaves - 1)

global effects
effects = []
effects += [('While singing his own praises in the street, his nuts expand to the size of grapefruits and explode. This is detrimental to his groin and to his esteem.', 'has no nuts', [healthDec, fameDec])]
effects += [('At a fundraising dinner with some hoity-toity types, he is suddenly struck with the inability to correctly pronounce quinoa. His fame suffers.', 'can not pronounce quinoa', [fameDec])]
effects += [('Once a day at an unpredictable moment, a bird swoops over and deposits a sloppy poop on his head. People agree it is kind of yucky.', 'has bird poop hair', [fameDec])]
effects += [('One of his slaves was lifted into the air while carrying his umbrella, and was swept all the way back to their home in Hammerflammer town or whatever it was called.', 'lost a slave on a windy day', [slaveDec])]
effects += [('A chicken bone became lodged in his throat while eating dinner and now he lays a large, painful egg every day or so.', 'lays eggs', [healthDec])]
effects += [('He woke up today to find that every third toe on his feet had turned to gold. The toes sold for a decent amount to some guy with a weirdly intense interest in feet.', 'is missing a third of his toes', [healthDec, wealthInc])]
effects += [('A hole appeared in his pocket while sitting on the john. Despite saving a couple coins, some of his gold remains buried in a morass of excreted beer and pretzels.', 'has poopy fingers', [fameDec, wealthDec])]
effects += [('A horse wearing a tophat spoke to him in a dream, and now he eats from a feedbag attached to his face.', 'looks ridiculous', [fameDec])]
effects += [('His slaves built a catapult from discarded firewood and launched the stinkiest among them into the sun.', 'had a slave fly too close to the sun', [slaveDec])]

def useRandomSpell(target):
    random.shuffle(effects)
    effect = effects[0]
    msg = '\n' + effect[0]
    target.effects += [effect[1]]
    for f in effect[2]:
        f(target)
    effects.remove(effect)
    return msg