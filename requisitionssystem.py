Requisition_ID_counter = 10000 

class RequisitionSystem:
    
    def __init__(self):
        
        self.staff_date = 0
        self.staff_id = 0
        self.staff_name = 0
        self.requisition=[] #it helps to stor the data
        self.approved=0
        self.panding=0
        self.Notapproved=0

        
        

    
    def Staff_info(self):
        global Requisition_ID_counter
        self.staff_date = input("Enter date: ")
        self.staff_id = input("Enter staff ID: ")
        self.staff_name = input("Enter staff name: ")

        Requisition_ID_counter += 1
        self.requisition_id = Requisition_ID_counter

        print(f"Date: {self.staff_date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Requisition ID: {self.requisition_id}")

    
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


    def display_requisition(self):
        print("----requisition----")
        print(f"Date: {self.staff_date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: {self.total_cost}")
        print(f"Status: {self.status}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Approval Reference Number: {self.approve_reference}")
    
    def requisition_statistic(self):
        print("-----static-----")
        print(f"total approval={self.approved}")
        print(f"total panding={self.panding}")
        print(f"Notapproved={self.Notapproved}")

if __name__ == "__main__":
    RequisitionSystem()
for i in range(5):
    requisition=RequisitionSystem()
    requisition.Staff_info()
    requisition.requisitions_details()
    requisition.requisition_approval()
    requisition.respond_requisition()
    requisition.display_requisition()
    requisition.requisition_statistic()

