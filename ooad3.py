#Python version : 3.5
import random
#A lot of randomizations are involved to simulate all the natural choices taken in the program

class Store():
    '''
    A class that represents a Rental Store
    with its own functionalities to handle transactions for rentals,
    maintain an Inventory and generate reports
    '''
    def __init__(self,tools):
        self.Tools = set(tools)  #The inventory of available tools
        self.active_transactions = []  #list of currently active transactions
        self.completed_transactions = [] #All previously completed transactions

    def getTool(self):
        '''Returns a random available tool from the Inventory'''
        tool = random.choice(list(self.Tools))
        self.Tools.remove(tool)
        return tool

    def GetInventoryStock(self):
        return len(self.Tools)

    def SortandUpdate(self,day_num):
        '''Sort and move all the active transactions that are completed for the day
        to the completed transactions database'''
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

        completed_returns  = self.active_transactions[:j+1]

        for row in completed_returns:
            ret[row[1]] = row[2]
            for t in row[2]:
                self.Tools.add(t)

        self.completed_transactions.extend(completed_returns)
        self.active_transactions = self.active_transactions[j+1:]

        return ret

    def createRental(self,trans_id,day_num,customer,req_tools,num_nights):
        '''Add a transaction to store a current Rental'''
        c_id = customer.getCustomerID()
        return_day = day_num + num_nights
        total_price = 0
        tools = []

        for tool in req_tools:
            total_price += tool.GetPricePerDay() * num_nights
            tools.append(tool)

        self.active_transactions.append([trans_id,c_id,tools,day_num,return_day,total_price])

    def generateReport(self):
        '''
        A function to generate a final report of the completed and active rentals.
        '''
        print("\nNumber of tools currently available: ", len(self.Tools))
        for t in self.Tools:
            print(t.getType() + str(t.GetID()))
        total_price = 0
        for a in self.active_transactions:
            total_price += a[5]
        for c in self.completed_transactions:
            total_price += c[5]
        print("\nAmount of money they store made in 35 days: ", total_price)

        print("\nCompleted Rentals: ")
        for c in self.completed_transactions:
            print("\nCustomer ID: ", c[1],"| Tools Rented: ", [t.getType() + str(t.GetID()) for t in c[2]],"| Number of days rented: ", c[4]-c[3],"| Total amount : ", c[5])

        print("\n------------------------------------------------------------------------")
        print("\nActive Rentals: ")
        for c in self.active_transactions:
            print("\nCustomer ID: ", c[1],"| Tools Rented: ", [t.getType() + str(t.GetID()) for t in c[2]],"| Number of days rented: ", c[4]-c[3],"| Total amount : ", c[5])


class Customer():
    '''
    The abstract class that represents a customer
    with their Tools Capacity, Renting Days range, ID and their behavior type
    '''
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

#All three Customer as Subclasses
class CasualCustomer(Customer):
    def __init__(self, id):
        super().__init__([1,2],[1,2],id,1)

class BusinessCustomer(Customer):
    def __init__(self, id):
        super().__init__([3],[7],id,2)

class RegularCustomer(Customer):
    def __init__(self, id):
        super().__init__([1,2,3],[3,4,5],id,3)


class Tool():
    '''
    The abstract class that represents a tool
    with its price per day, tool_id and its category
    '''
    def __init__(self,ppd,id,t):
        self.PricePerDay = ppd
        self.ID=id
        self.Type = t

    def GetID(self):
        return self.ID

    def GetPricePerDay(self):
        return self.PricePerDay

    def getType(self):
        return self.Type

#All five Tools as Subclasses
class PaintingTool(Tool):
    def __init__(self,id):
        super().__init__(7,id,'painting')

class ConcreteTool(Tool):
    def __init__(self,id):
        super().__init__(3,id,'concrete')

class PlumbingTool(Tool):
    def __init__(self,id):
        super().__init__(8,id,'plumbing')

class WoodworkTool(Tool):
    def __init__(self,id):
        super().__init__(4,id,'woodwork')

class YardworkTool(Tool):
    def __init__(self,id):
        super().__init__(5,id,'yardwork')


def DaysSimulator(customers,tools,days):
    '''
    A function that simulates the Hardware Rental Store's general
    flow of rentals for 35 days
    '''
    cust_track = {c.getCustomerID():[] for c in customers} #All customers are mapper to their list of rented tools
    curr_trans_id = 0
    hw_rental = Store(tools)
    #Simulating the Days
    for day in range(1, days+1):
        #Every morning update the database of the completed Rentals and return back from the Customers holdings
        tools_returned = hw_rental.SortandUpdate(day)

        for key,value in tools_returned.items():
            for t in value:
                cust_track[key].remove(t)
        #Only if there is any stock in the Inventory the Rentals occur
        while(hw_rental.GetInventoryStock() > 0):

            try:#Randomly get a customer based on his available capacity and Inventory stock
                if (hw_rental.GetInventoryStock() >2):
                    customer = random.choice([c for c in customers if max(c.getNumOfTools()) - len(cust_track[c.getCustomerID()]) !=0 ])

                else:
                    customer = random.choice([c for c in customers if c.getType()!=2 and max(c.getNumOfTools()) - len(cust_track[c.getCustomerID()]) !=0])

            except:#If no available customers
                break

            cid = customer.getCustomerID()
            #Get the range of the
            choice_tools = list(set(list(range(1,min(max(customer.getNumOfTools()),max(customer.getNumOfTools())-len(cust_track[cid]),hw_rental.GetInventoryStock())+1))) & set(customer.getNumOfTools()))
            num_tools = random.choice(choice_tools)
            #Randomly choose the number of tools for the chosen customer based on all the constraints
            tools = []
            for j in range(num_tools):
                tool = hw_rental.getTool()
                tools.append(tool)
                cust_track[cid].append(tool)
            #Create a Rental transaction in the Store
            curr_trans_id += 1
            hw_rental.createRental(curr_trans_id,day,customer,tools, random.choice(customer.getNumOfDays()))
    hw_rental.generateReport() #Once all days are over, generate the report


def createCustomer(type,id):
    '''Create a customer object given the type and ID '''
    if type==1:
        return CasualCustomer(id)
    if type==2:
        return BusinessCustomer(id)
    if type==3:
        return RegularCustomer(id)


if __name__ == '__main__':
    #Generate the tools and customers and then Simulate the program

    tools = []

    for i in range(1,21):
        if i in [1,2,3,4]:
            tools.append(PaintingTool(i))
        elif i in [5,6,7,8]:
            tools.append(ConcreteTool(i))
        elif i in [9,10,11,12]:
            tools.append(PlumbingTool(i))
        elif i in [13,14,15,16]:
            tools.append(WoodworkTool(i))
        elif i in [17,18,19,20]:
            tools.append(YardworkTool(i))

    customers = []

    for i in range(11):
        if i in [1,2,3,4]:
            customers.append(createCustomer(1,i))
        elif i in [5,6,7]:
            customers.append(createCustomer(2,i))
        elif i in [8,9,10]:
            customers.append(createCustomer(3,i))

    DaysSimulator(customers,tools,35)
