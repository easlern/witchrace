# opening the file
def read(filename):
    all = ''
    with open('art/' + filename,'r') as text:
       # reading the file by using a for loop
       for line in text:
          # stripping the newline character from the line
          all += line
    return all

def barbarian():
    return read('barbarian.txt')
def market():
    return read('market.txt')
def baby():
    return read('baby.txt')
def burger():
    return read('burger.txt')
def witch():
    return read('witch.txt')
def cover():
    return read('cover.txt')
def sunrise():
    return read('sunrise.txt')
def ai():
    return read('ai.txt')
def king():
    return read('king.txt')
def death():
    return read('death.txt')
def village():
    return read('village.txt')
def soldier():
    return read('soldier.txt')
def prisoner():
    return read('prisoner.txt')