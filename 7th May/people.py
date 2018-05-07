class person:
    def __init(self):
        pass
    def show(self):
        print("this is person")
class married(person):
    def __init(self,child):
        self.child=child

    def show(self):
        print("this is married class")

    def noofchild(self):
        print(self.child)

class single(person):
    def __init(self):
        pass

    def show(self):
        print("this is married class")

class divorced(single,married):   # hybrid inheritance person->(married,single)->snake
    def __init__(self,ch):
        self.ch=ch
    def show(self):
        print("this is divorced class")

d=divorced(5)
print(d.ch)
