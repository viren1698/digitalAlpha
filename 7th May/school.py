class animals:
    def __init__(self):
        pass
    def type(self):
        print("this is animal class")

class pets(animals):        ##normal inheritance
    def __init__(self):
        pass
    def type(self):
        print("this is pets class")

class wild(animals):       ##normal inheritance
    def __init__(self):
        pass
    def type(self):
        print("this is wild animals class")

class dog(pets):   ##multilevel inheritance   animals->pets->dog
    def __init__(self):
        pass
    def type(self):
        print("this is dog class")
    def nooflegs(self):
        print("4 legs")

class tiger(wild):  ##multilevel inheritance   animals->wild->tiger
    def __init__(self):
        pass

    def type(self):
        print("this is tiger class")

    def nooflegs(self):
        print("4 legs")

class snake(wild,pets):  ##multiple inheritance  (pets,wild)->snake     hybrid inheritance animals->(pets,wild)->snake
    def __init__(self):
        pass

    def type(self):
        print("snake can be wild as well as pets")

a=animals()
a.type()
s=snake()
s.type()
d=dog()
d.type()






