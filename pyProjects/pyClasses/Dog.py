class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

class Bulldog(Dog):

    def __init__(self, name, words):
        self.name = name
        self.words = words

    def bark(self):
        print(self.words)

