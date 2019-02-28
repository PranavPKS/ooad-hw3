import random

Class Store():
    def __init__(self,tools):
        self.Tools = set(tools)
        self.active_transactions = []
        self.completed_transactions = []

    def SortandUpdate(self,day_num):
        self.active_transactions.sort(key = lambda x:x[4])

        j=0
        for i in range(len(self.active_transactions)):
            if self.active_transactions[i][4] == day_num:
                j += 1
            if self.active_transactions[i][4] > day_num:
                break

        ret  = self.active_transactions[:j]
        self.completed_transactions.append(self.active_transactions[:j])
        self.active_transactions = self.active_transactions[j+1:]

        return ret


    def ReturnAvailTools(self):
        return list(set(Tools))

    def GetInventoryStock(self):
        return len(self.Tools)

    def checkCurrentTools(cid):
        count = 0
        for t in active_transactions:
            if t[1] == cid:
                count + = len(t[2])

    def createRental(self,trans_id,day_num,customer,req_tools,num_nights):


        c_id = customer.getCustomerID()

        return_day = day_num + num_nights
        total_price = 0
        t_ids = []

        for tool in req_tools:
            total_price += tool.GetPricePerDay() * num_nights
            t_ids.append(tool.GetID())

        self.active_transactions.append([trans_id,c_id,t_ids,day_num,return_day,total_price])


Class DaysSimulator():



Class Customer():
    def __init__(self,nt,nd,id):
        self.NumOfTools = nt
        self.NumOfDays = nd
        self.CustomerID = id

    def getCustomerID(self):
        return self.CustomerID

    def getNumOfDays(self):
        return self.NumOfDays

    def getNumOfTools(self):
        return self.NumOfTools


Class CasualCustomer(Customer):
    def __init__(self, id):
        super()._init_([1,2],[1,2],id)


Class BusinessCustomer(Customer):
    def __init__(self, id):
        super()._init_([3],[7],id)


Class RegularCustomer(Customer):
    def __init__(self, id):
        super()._init_([1,2,3],[3,4,5],id)




Class Tool():
    def __init__(self,ppd,id,t):
        self.PricePerDay = ppd
        self.ID=id
        self.type = t

    def GetID(self):
        return self.ID

    def GetPricePerDay(self):
        return self.PricePerDay

Class PaintingTool(Tool):
    def __init__(self,id):
        super()._init_(7,id,'painting')

Class ConcreteTool(Tool):
    def __init__(self,id):
        super()._init_(3,id,'concrete')

Class PlumbingTool(Tool):
    def __init__(self,id):
        super()._init_(8,id,'plumbing')

Class WoodworkTool(Tool):
    def __init__(self,id):
        super()._init_(4,id,'woodwork')

Class YardworkTool(Tool):
    def __init__(self,id):
        super()._init_(5,id,'yardwork')



def createCustomer(type,id):
    if type=1:
        return CasualCustomer(id)
    if type=2:
        return BusinessCustomer(id)
    if type=3:
        return RegularCustomer(id)


if __name__ == '__main__':

    tools = []

    for i in range(1,21):
        if i in [1,2,3,4]:
            tools.append(PaintingTool(i))
        if i in [5,6,7,8]:
            tools.append(ConcreteTool(i))
        if i in [9,10,11,12]:
            tools.append(PlumbingTool(i))
        if i in [13,14,15,16]:
            tools.append(WoodworkTool(i))
        if i in [17,18,19,20]:
            tools.append(YardworkTool(i))

    customers = []

    for i in range(10):
        customers.append(createCustomer(random.choice([1,2,3])))




    while(

    random.choice(list(range(10)))
