Class Store():
    def __init__(self):
        self.



Class Customer():
    def __init__(self,nt,nd,id):
        self.NumOfTools = nt
        self.NumOfDays = nd
        self.CustomerID = id


Class CasualCustomer(Customer):
    def __init__(self, id):
        super()._init_([1,2],[1,2],id)

    def getNumOfDays(self):
        return self.NumOfDays

    def getNumOfTools(self):
        return self.NumOfTools

Class BusinessCustomer(Customer):
    def __init__(self, id):
        super()._init_([3],[7],id)

    def getNumOfDays(self):
        return self.NumOfDays

    def getNumOfTools(self):
        return self.NumOfTools

Class RegularCustomer(Customer):
    def __init__(self, id):
        super()._init_([1,2,3],[3,4,5],id)

    def getNumOfDays(self):
        return self.NumOfDays

    def getNumOfTools(self):

        return self.NumOfTools

Class Tool():
    def __init__(self,ppd):
        self.PricePerDay = ppd
