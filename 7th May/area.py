class tri():
    def __init__(self,a,b,c):
        super().__init__()
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        p=(self.a+self.b+self.c)/2
        ar=(((p)*(p-self.a)*(p-self.b)*(p-self.c))**.5)
        print(ar)


class circle():
    def __init__(self,r):
        self.r=r
    def area(self):
        print(3.1415*self.r**2)


class rec():
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print(self.l*self.b)






t=tri(3,4,5)
c=circle(3)
r=rec(2,4)

t.area()
c.area()
r.area()
