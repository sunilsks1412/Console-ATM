from user import *
from admin import *

class ATM:
    def __init__(self):
        self.admin_user = "Admin"
        self.admin_pass = "Admin123"
        self.denomination = {2000: 20, 500: 20}
        self.atm_balance = 2000*20 + 500*20
        self.user_balance = 5000
        self.current_pin = 1234



atm = ATM()

   

while True:
    print("\n")
    print("**************   Welcome to ATM  **************")
    print("1. Admin")
    print("2. User")
    print("3. Exit") 
    op = int(input(" \n   Choose your role \n   "))
    if(op==1):
        admin(atm)
    elif(op==2):
        user(atm)
    else:
        print("Thank you for using our ATM")
        break
    

