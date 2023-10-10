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