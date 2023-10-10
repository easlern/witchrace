import random

print('*** Welcome to WitchRace! ***')
print('You are a rabble-rousing upstart running for local office in medieval Iceland. Use guile, cunning, and black magic to outdo your opponents and become a big fish in a little frozen pond!')


class Obj:
    def __init__(self):
        pass

def spawn(name):
    who = Obj()
    who.health = 3
    who.fame = 0
    who.wealth = 1
    who.slaves = 1
    who.name = name
    who.effects = []
    return who

flurgl = spawn('Flurgl')
herzl = spawn('Herzl')
geeg = spawn('Geeg')
opponents = [flurgl, herzl, geeg]
me = spawn('you')
game = Obj()
game.timeLeft = 5

def scoreAppeal(who):
    return who.health * who.fame * who.wealth
def fix(v):
    return max(0,min(4,v))
def healthAdj(h):
    h = fix(h)
    return ['dead', 'near death', 'sick', 'healthy', 'hale as a horse'][h]
def fameAdj(f):
    f = fix(f)
    return ['unknown', 'somewhat notable', 'locally famous', 'the subject of epic poetry', 'god-like'][f]
def wealthAdj(w):
    w = fix(w)
    return ['broke', 'poor', 'well-off', 'rich', 'swimming in gold'][w]

def leader():
    all = opponents + [me]
    l = me
    for a in all:
        if scoreAppeal(a) > scoreAppeal(l):
            l = a
    return l
def describe(who):
    msg = who.name + ' is ' + healthAdj(who.health) + '.'
    msg += '\nAround here, he is ' + fameAdj(who.fame) + '.'
    msg += '\nWord is that ' + who.name + ' is also ' + wealthAdj(who.wealth) + '.'
    for e in who.effects:
        msg += '\nHe ' + e + '.'
    return msg

def turn():
    while game.timeLeft > 0:
        names = ''
        for o in opponents:
            names += o.name + ', '
        print('\n\nIt is a new day! There are only ' + str(game.timeLeft) + ' days till the next run-off vote, when the candidate with the fewest votes gets eliminated! The candidates remaining: ' + names + 'and you.')
        print('You are feeling ' + healthAdj(me.health) + '.')
        slaveMoney = random.choice(range(me.slaves + 1))
        me.wealth += slaveMoney
        print('Farmland worked by your slaves netted you ' + str(slaveMoney) + ' gold today. So you have ' + str(me.wealth) + ' gold in your pocket.')
        print('Word on the street is that you are ' + fameAdj(me.fame) + '. The front-runner appears to be ' + leader().name + ' today!')
        choice = None
        sep = '********************************'
        while choice not in ['1','2','3','4','5']:
            print('\n\nWhat is your plan for the day?')
            print('1) Kiss a baby')
            print('2) Eat a slave (' + str(me.slaves) + ' left)')
            print('3) Raid Flammerhammerborgensteinerdingerlinger')
            print('4) Cast a spell')
            print('5) Buy a slave for 2 gold')
            print('6) Learn about your opponents')
            choice = input('Choice: ')
            if choice == '6':
                for o in opponents:
                    print(sep)
                    print(describe(o))
                    print(sep)
        print(sep)
        if choice == '2':
            print(eat(me))
        if choice == '1':
            print(kiss(me))
        if choice == '3':
            print(raid(me))
        if choice == '4':
            print(cast(me))
        if choice == '5':
            print(buy(me))
        print(sep)

        for o in opponents:
            if o.health < 1:
                print(o.name + ' could not take the heat and dropped out of the race!')
                opponents.remove(o)
            else:
                actions = [(eat, 'eat a slave'), (kiss, 'kiss some babies'), (raid, 'raid Flammerhammerborgensteinerdingerlinger'), (cast, 'cast a spell'), (buy, 'buy a slave')]
                random.shuffle(actions)
                print (o.name + ' decided to ' + actions[0][1] + ' today.')
                actions[0][0](o)

        game.timeLeft -= 1

def buy(who):
    if who.wealth < 2:
        return 'You wasted the whole day trying to haggle with a guy whose ears were full of tallow.'
    who.wealth -= 2
    who.slaves += 1
def eat(who):
    if who.slaves < 1:
        return 'The day was wasted as you searched the slave pen for someone to eat, then realized nobody was left.'
    who.slaves -= 1
    who.health += 2
    return 'You feel better after a good meal.'
def kiss(who):
    who.fame += 1
    who.wealth += 1
    return 'You drooled on an infant and everybody thinks you are a little cooler now. Somebody dropped a coin in your cup on your way home.'
def cast(who):
    if who.wealth < 1:
        return 'You are too poor to afford the components for a spell.'
    who.wealth -= 1
    opps = opponents + [me]
    opps.remove(who)
    print('opponents to cast against are ' + str([o.name for o in opps]))
    random.shuffle(opps)
    target = opps[0]
    msg = 'Your spell affects ' + target.name + '.'
    def wealthInc():
        target.wealth += 1
    def wealthDec():
        target.wealth = max(0, target.wealth - 1)
    def healthInc():
        target.health = min(4, target.healht + 1)
    def healthDec():
        target.health = max(0, target.health - 1)
    def fameDec():
        target.fame = max(0, target.fame - 1)
    def slaveDec():
        target.slaves = max(0, target.slaves - 1)
    effects = []
    effects += [('While singing his own praises in the street, his nuts expand to the size of grapefruits and explode. This is detrimental to his groin and to his esteem.', 'has no nuts', [healthDec, fameDec])]
    effects += [('At a fundraising dinner with some hoity-toity types, he is suddenly struck with the inability to correctly pronounce quinoa. His fame suffers.', 'can not pronounce quinoa', [fameDec])]
    effects += [('Once a day at an unpredictable moment, a bird swoops over and deposits a sloppy poop on his head. People agree it is kind of yucky.', 'has bird poop hair', [fameDec])]
    effects += [('One of his slaves was lifted into the air while carrying his umbrella, and was swept all the way back to their home in Hammerflammer town or whatever it was called.', 'lost a slave on a windy day', [slaveDec])]
    effects += [('A chicken bone became lodged in his throat while eating dinner and now he lays a large, painful egg every day or so.', 'lays eggs', [healthDec])]
    effects += [('He woke up today to find that every third toe on his feet had turned to gold. They sold for a decent amount to some guy with a really weirdly intense interest in feet.', 'is missing a third of his toes', [healthDec, wealthInc])]
    effects += [('A hole appeared in his pocket while sitting on the john. Despite saving a couple coins, some of his gold remains buried in a morass of excreted beer and pretzels.', 'has poopy fingers', [fameDec, wealthDec])]
    effects += [('A horse wearing a tophat spoke to him in a dream, and now he eats from a feedbag attached to his face.', 'looks ridiculous', [fameDec])]
    effects += [('His slaves built a catapult from discarded firewood and launched the stinkiest among them into the sun.', 'had a slave fly too close to the sun', [slaveDec])]
    random.shuffle(effects)
    effect = effects[0]
    msg += '\n' + effect[0]
    target.effects += [effect[1]]
    for f in effect[2]:
        f()
    return msg

def raid(who):
    who.fame += 1
    who.wealth += 1
    who.slaves += 1
    who.health -= 2
    if who.health < 0:
        who.health = 0
        return 'The Hammerflammerwhatever people cut you into pieces, burn the pieces, piss on your ashes, and use them to stuff dummies for testing new sled designs.'
    return 'You made it home with some money, a slave, and a couple fewer teeth.'


turn()