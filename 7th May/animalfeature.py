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
    def __init__(self,h):
        self.h=h

    def type(self):
        print("this is dog class")
    def nooflegs(self):
        print("4 legs")

    def showheight(self):
        print(self.h)

    def sound(self):
        print("bark")

class tiger(wild):  ##multilevel inheritance   animals->wild->tiger
    def __init__(self):
        pass

    def type(self):
        print("this is tiger class")

    def nooflegs(self):
        print("4 legs")

    def sound(self):
        print("roar")


class snake(wild,pets):  ##multiple inheritance  (pets,wild)->snake     hybrid inheritance animals->(pets,wild)->snake
    def __init__(self,l):
        self.l=l

    def type(self):
        print("snake can be wild as well as pets")

    def showlen(self):
        print(self.l)

a=animals()
a.type()
s=snake(40)
s.type()
d=dog(14)
d.type()
d.showheight()
s.showlen()







