import random
import spellEffects
import art


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def cls():
    print('\r\n' * 100)
def wait():
    input('\r\nPress ENTER to continue\r\n')
    cls()
cls()
print('*** Welcome to WitchRace! ***')
print('You are a rabble-rousing upstart running for local office in medieval Iceland. Use guile, cunning, and black magic to outdo your opponents and become a big fish in a little frozen pond!')
wait()


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
game.timeLeft = len(opponents) + 1

sep = '********************************'

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

def loser():
    all = opponents + [me]
    l = opponents[0]
    for a in all:
        if scoreAppeal(a) < scoreAppeal(l):
            l = a
    return l
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
def heify(msg):
    msg = msg.replace('Your', 'His')
    msg = msg.replace('your', 'his')
    msg = msg.replace('You','He')
    msg = msg.replace('you','he')
    return msg
def youify(msg):
    msg = msg.replace('His','Your')
    msg = msg.replace('his','your')
    msg = msg.replace('He','You')
    msg = msg.replace('he','you')
    msg = msg.replace('him','you')
    return msg

def turn():
    while True:
        while game.timeLeft > 0:
            def checkForEnd():
                if me.health <= 0:
                    print(sep)
                    print('You are DEAD. Better luck next time!')
                    print(sep)
                    exit()
                if len(opponents) < 1:
                    print(
                        'All your opponents have been eliminated. The people crown you as their new king in a ceremonial feast of the men who did not make it. Their bones are later fashioned into a comode that empties onto a mass grave containing their family and possessions, as is tradition.')
                    print('Hooray for you!')
                    print('KING YOU')
                    print()
                    print('THE END!')
                    exit()

            names = ''
            for o in opponents:
                names += o.name + ', '
            print('\n\nIt is a new day! There are only ' + str(game.timeLeft) + ' days till the next run-off vote, when the candidate with the fewest votes gets eliminated! The candidates remaining: ' + names + 'and you.')
            print()
            print(sep)
            print('You are feeling ' + healthAdj(me.health) + '.')
            slaveMoney = random.choice(range(me.slaves + 1))
            me.wealth += slaveMoney
            print('Farmland worked by your slaves netted you ' + str(slaveMoney) + ' gold today. So you have ' + str(me.wealth) + ' gold in your pocket.')
            print('Word on the street is that you are ' + fameAdj(me.fame) + '. The front-runner appears to be ' + leader().name + ' today!')
            for eff in me.effects:
                print(describe(me))
            print(sep)
            choice = None
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
            cls()
            if choice == '2':
                print(eat(me)[0])
            if choice == '1':
                print(kiss(me)[0])
            if choice == '3':
                print(raid(me)[0])
            if choice == '4':
                print(cast(me)[0])
            if choice == '5':
                print(buy(me)[0])
            wait()

            checkForEnd()

            for o in opponents[0:]:
                if o.health < 1:
                    print(o.name + ' could not take the heat and dropped out of the race!')
                    opponents.remove(o)
                else:
                    actions = [(eat, 'eat a slave'), (kiss, 'kiss some babies'), (raid, 'raid Flammerhammerborgensteinerdingerlinger'), (cast, 'cast a spell'), (buy, 'buy a slave')]
                    random.shuffle(actions)
                    print (o.name + ' decided to ' + actions[0][1] + ' today.')
                    print(actions[0][0](o)[1])
                    print(sep)
            wait()
            checkForEnd()

            game.timeLeft -= 1

        # runoff time!
        print(sep + '\r\nElection day is here!\r\n' + sep)
        print('The people eagerly gather in the square to exercise their collective voice, as determined by a small group of property-owning white men.')
        print('As the sun drops below the horizon, the candidates wait nervously while the votes are tallied.')
        wait()
        print('And the loser is. . .')
        wait()
        print(loser().name + '!')
        if loser() == me:
            cls()
            print('The people have spoken, and you have been eliminated in the run-off election!')
            print('Please sort your affairs and return to the great hall for division of your property and limbs.')
            print('GAME OVER')
            wait()
            exit()
        print('The guards lower their spears toward ' + loser().name + ' and herd him toward the great hall, where he will be force-fed toads and peet in preparation for the eventual coronation. As is tradition.')
        wait()
        opponents.remove(loser())
        checkForEnd()
        game.timeLeft = len(opponents) + 1

def buy(who):
    if who.wealth < 2:
        return ['You wasted the whole day trying to haggle with a guy whose ears were full of tallow.', 'He did not have the funds to purchase even the weakest, sickliest, former yes-man in middle management. The day was a total bust.']
    who.wealth -= 2
    who.slaves += 1
    return ['You picked up a chubby grump who was exiled from his tribe for mixing Skittles and M&Ms.', 'He brought home a bewildered Dutchman who used to sell snake oil to the elderly.']

def eat(who):
    if who.slaves < 1:
        return ['The day was wasted as you searched the slave pen for someone to eat, then realized nobody was left.', 'He forgot that before one may eat a slave, one must first own a slave. What a goofball.']
    who.slaves -= 1
    who.health += 2
    return ['You feel better after a good meal.', 'He looks a bit healthier now.']
def kiss(who):
    who.fame += 1
    who.wealth += 1
    return ['You drooled on an infant and everybody thinks you are a little cooler now. Somebody dropped a coin in your cup on your way home.', 'He slobbered on some stray kids and animals. Everyone agrees he is a nice enough guy but they decided to give him a gold to go home.']
def cast(who):
    if who.wealth < 1:
        return ['You are too poor to afford the components for a spell.', 'He could not afford the ingredients, and returned home somewhat embarrassed.']
    print(who.name + ' pays a gold to cast a spell!')
    who.wealth -= 1
    opps = opponents + [me]
    # opps.remove(who) # let's try making yourself a potential target, that sounds fun  :D
    # print('opponents to cast against are ' + str([o.name for o in opps]))
    random.shuffle(opps)
    target = opps[0]
    msg = ['Your spell affects ' + target.name + '.', 'His spell affects ' + target.name + '.']
    eff = spellEffects.useRandomSpell(target)
    msg[0] += eff
    if target == me:
        msg[1] += youify(eff)
    else:
        msg[1] += eff
    return msg

def raid(who):
    if who == me:
        print(art.barbarian() + '\r\n')
    who.fame += 1
    who.wealth += 1
    who.slaves += 1
    who.health -= 2
    if who.health < 0:
        who.health = 0
        return ['The Hammerflammerwhatever people cut you into pieces, burn the pieces, piss on your ashes, and use them to stuff dummies for testing new sled designs.', 'The Hammerflammerdingerflingers put so many arrows into him that he bled to death standing on his boat. He is remembered in verse as The Porcupine Prince.']
    return ['You made it home with some money, a slave, and a couple fewer teeth.', 'He survived, with a slave and some gold. He will never stop bringing this up at parties.']


turn()