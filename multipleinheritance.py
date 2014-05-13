__author__ = 'anthonybeyal'
class Animal(object):
    """
    Base class for all other animals
    """

    def __init__(self, name):
        self.name = name

    def talk(self):
        print "You shouldn't be calling this directly!"  # We'll learn about exceptions this week


class Human(Animal):
    def talk(self):
        print "I am a human!"


class Horse(Animal):
    def __init__(self, name, legs):
        super(Horse, self).__init__(name)
        self.legs = legs

    def talk(self):
        print "Neigh!"


class Centaur(Human, Horse):
    pass

cent = Centaur('All-star', 4)
cent.talk()
print cent.legs
