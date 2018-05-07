class high:
    def __init__(self):
        self.student = ["raj", "rabi", "akash", "atul"]
        self.__teachers = ["prema", "thiruchirapalli", "vinci", "vinod"]
        self.__principal=["ashok age 54 height 6'1"]
        self.__staffmembers=["raj", "rabi", "akash", "atul"]
        pass
    def getteachersrecord(self):
        return(self.__teachers)

    def getstudentsrecord(self):
        return(self.student)

    def getprincipalsrecord(self):
        return (self.__principal)
    def getstaffrecord(self):
        return (self.__staffmembers)



class principal(high):
    def __init__(self):
        super().__init__()
        self.t_record=super().getteachersrecord()
        self.s_record=super().getstudentsrecord()
        self.stf = super().getstaffrecord()
        self.p_record=super().getprincipalsrecord()

    def getallrecords(self):
        print(self.t_record,self.s_record,self.stf,self.p_record)


class staff(high):
    def __init__(self,name):
        super().__init__()
        self.s_record = super().getstaffrecord()
    def getallrecords(self):
        print(self.s_record)

class teacher(high):
    def __init__(self):
        super().__init__()
        self.s_record = super().getstudentsrecord()
    def getallrecords(self):
        print(self.s_record)



p=principal()
p.getallrecords()

t=teacher()
t.getallrecords()

stafff=staff("rajeev")
stafff.getallrecords()











