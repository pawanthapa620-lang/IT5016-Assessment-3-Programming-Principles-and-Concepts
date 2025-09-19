# Global variable to track the requisitionn ID of the system
Requisition_ID_counter = 10000 

class RequisitionSystem:
    
    def __init__(self):
        """
        This is the way of Initialize requisition object
        The software principles that i have used is 
        K.I.S.S which is  simple easy to understand, and navigate."""
        self.staff_date = 0
        self.staff_id = 0
        self.staff_name = 0
        self.requisition=[] #it helps to stor the data
        self.approved=0
        self.panding=0
        self.Notapproved=0

        
        

    """the software principle that i have used is K.I.S.S (keep it simple) this principle helps  is kept things simple and straightforward,
    making it easy to read and understand.
    as i have used input function which directly collect the values and each input is directly store in their attribute"""
    def Staff_info(self):
        global Requisition_ID_counter
        self.staff_date = input("Enter date: ")# allows the used to input the date 
        self.staff_id = input("Enter staff ID: ")# allows the used to enter the staff id
        self.staff_name = input("Enter staff name: ")# allows the used to enter the name of the staff

        Requisition_ID_counter += 1#it helps to increease the variable by 1
        self.requisition_id = Requisition_ID_counter
        """print the data """
        print(f"Date: {self.staff_date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Requisition ID: {self.requisition_id}")

    """This helps to collects item details like item name, and item cost and  the total cost. 
    i havent used any principles here as it mixed input, calculation, and display but It can be improved by following the Single Responsibility Principle: which helps to used 
    separate input, calculation, and output into its distinct functions to make the code cleaner, maintainable, and easier to extend."""
    def requisitions_details(self):
        item_number = int(input("How many items do you want to buy "))
        self.total_cost = 0
        for i in range(item_number):
            print(f"Items={i+1}")
            item_name = input("Enter the item name: ")
            item_cost = float(input("Enter the cost of the item:$ "))
            self.total_cost += item_cost
            print(f"Item name: {item_name}") 
            print(f"Item cost: {item_cost}")
            """This mentods of approval helps if the total cost is less then 500, 
            if it is more then it then it show pending. i havenot used any principes as 
            it violates the open/closed principle as changing rules need required modifying the code
            in furture i will used open/closed principle this rules helps to change or seperate rule function 
            and keep logic seperate from printion.  """
    def requisition_approval(self):
        
        if self.total_cost < 500:
            self.status = "Approved"
            self.approve_reference = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            
        else:
            self.status = "Pending"
            self.approve_reference = None
            
        print("-----approval----")
        print(f"Total cost: {self.total_cost}")
        print(f"Status: {self.status}")
        if self.approve_reference:
            print(f"Approval Reference Number: {self.approve_reference}") 
            
    """ This method helps the manager to update pending requisition 
    in the furture it can be improved using the Single Responsibility Principle (SRP).  
    Currently, it mixes input handling and status updates, making it harder to maintain and test.  
    Separating input from business logic will make the code cleaner, easier to extend, and less error-prone.
    """
    def respond_requisition(self):
        if self.status =="pending":
            respond=input("enter manager respond (Approved/NotApproved)")
            if respond=="Approved":
                self.status="Approved"
                self.approved+=1
            else:
                respond=="NotApproved"
                self.status="NotApproved"
                self.panding+=1
                
                print(f"respond:{respond}")

    """
    This helps to displays or print all requisition information of the requisitionsystem. 
    it violates the DRY principle because it repeats information already printed in Staff_info() and requisition_approval() 
    It can be improved by following the DRY (Don't Repeat Yourself) principle.  
    Create a single function to format and return requisition info, then reuse it wherever needed to avoid repeated code and make maintenance easier.
    """
    def display_requisition(self):
        print("----requisition----")
        print(f"Date: {self.staff_date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: {self.total_cost}")
        print(f"Status: {self.status}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Approval Reference Number: {self.approve_reference}")
    """
    This helps to displays statistics for this requisition object only. 
    It can be improved using the Single Responsibility Principle (SRP) and 
    Separation of Concerns (SoC) by moving statistics calculation to the system level, allowing tracking across all requisitions and keeping responsibilities clear.
    """
    def requisition_statistic(self):
        print("-----static-----")
        print(f"total approval={self.approved}")
        print(f"total panding={self.panding}")
        print(f"Notapproved={self.Notapproved}")

if __name__ == "__main__":
    RequisitionSystem()
    """this is the loop process for multiple requisition system """
for i in range(5):
    requisition=RequisitionSystem()
    requisition.Staff_info()
    requisition.requisitions_details()
    requisition.requisition_approval()
    requisition.respond_requisition()
    requisition.display_requisition()
    requisition.requisition_statistic()

