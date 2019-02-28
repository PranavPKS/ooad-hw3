import random

Class Store():
    def __init__(self,tools):
        self.Tools = set(tools)
        self.active_transactions = []
        self.completed_transactions = []

    def getTool():
        tool = random.choice(list(self.Tools))
        self.Tools.remove(tool)

        return tool

    def SortandUpdate(self,day_num):

        ret = {}
        if (day_num == 0):
            return ret

        self.active_transactions.sort(key = lambda x:x[4])

        j=0
        for i in range(len(self.active_transactions)):
            if self.active_transactions[i][4] == day_num:
                j += 1
            if self.active_transactions[i][4] > day_num:
                break

        completed_returns  = self.active_transactions[:j]


        for row in completed_returns:
            ret[row[1]] = row[2]

        self.completed_transactions.extend(completed_returns)
        self.active_transactions = self.active_transactions[j+1:]

        return ret


    def ReturnAvailTools(self):
        return list(set(Tools))

    def GetInventoryStock(self):
        return len(self.Tools)


    def createRental(self,trans_id,day_num,customer,req_tools,num_nights):


        c_id = customer.getCustomerID()
        return_day = day_num + num_nights
        total_price = 0
        t_ids = []


        for tool in req_tools:
            total_price += tool.GetPricePerDay() * num_nights
            t_ids.append(tool.GetID())

        self.active_transactions.append([trans_id,c_id,t_ids,day_num,return_day,total_price])


def DaysSimulator(customers,tools):

    cust_track = {c.getCustomerID():[] for c in customers}
    curr_trans_id = 0
    hw_rental = Store(tools)
    for day in range(1, 36):
        #check if inventory is not empty
        tools_returned = hw_rental.SortandUpdate(day)

        for key,value in tools_returned.items():
            for t in value:
                cust_track[key].remove(t)

        while(hw_rental.GetInventoryStock() > 0):

            try:
                if (hw_rental.GetInventoryStock() >2):
                    customer = random.choice([c for c in customers if len(cust_track[c.getCustomerID()]) < 3 ])
                else:
                    customer = random.choice([c for c in customers if c.getType()!=2])

            except:
                break

            cid = customer.getCustomerID()
            num_tools = random.choice(list(range(1,min(max(customer.getNumOfTools()),max(customer.getNumOfTools())-len(cust_track[cid]),hw_rental.GetInventoryStock())+1)))

            tools = []
            for j in range(num_tools):
                tool = hw_rental.getTool()
                tools.append(tool)
                cust_track[cid].append(tool)

            curr_trans_id += 1
            hw_rental.createRental(curr_trans_id,day,customer,tools, random.choice(customer.getNumOfDays()))





Class Customer():
    def __init__(self,nt,nd,id,t):
        self.NumOfTools = nt
        self.NumOfDays = nd
        self.CustomerID = id
        self.Type = t

    def getCustomerID(self):
        return self.CustomerID

    def getNumOfDays(self):
        return self.NumOfDays

    def getNumOfTools(self):
        return self.NumOfTools

    def getType(self):
        return self.Type


Class CasualCustomer(Customer):
    def __init__(self, id):
        super()._init_([1,2],[1,2],id,1)


Class BusinessCustomer(Customer):
    def __init__(self, id):
        super()._init_([3],[7],id,2)


Class RegularCustomer(Customer):
    def __init__(self, id):
        super()._init_([1,2,3],[3,4,5],id,3)




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

    for i in range(11):
        if i in [1,2,3,4]:
            customers.append(createCustomer(1,i))
        if i in [5,6,7]:
            customers.append(createCustomer(2,i))
        if i in [8,9,10]:
            customers.append(createCustomer(3,i))


    DaysSimulator(customers,tools)
    
