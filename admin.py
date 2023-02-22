# from data import *
# from atm import mainfunc
atm = None
def load_amount():
    global atm
    print("Load option \n")
    amount = int(input("Enter the amount \n"))
    print("Enter the atm.denomination \n")
    n2 = int(input("Enter the no of 2000 \n"))
    n5 = int(input("Enter the no of 500 \n"))
    chk = (n2*2000)+(n5*500)
    if(atm.denomination[2000]+n2 <= 100 and atm.denomination[500]+n5 <= 100):
      if(chk == amount):
          atm.atm_balance += chk
          atm.denomination[2000] += n2
          atm.denomination[500] += n5
          print("Amount of", amount ,"loaded successfully \n")
          print("The new ATM balance is",atm.atm_balance ,"\n")
      else:
          print("The entered amount and atm.denomination does not match \n")
    else:
      print("You can insert only ", 100 - atm.denomination[2000], "2000 notes \n")
      print("You can insert only ", 100 -atm.denomination[2000], "2000 notes \n")

def chk_atm_balance(atm_balance):
    print("Checking your balance....... \n")
    print("The available ATM balance is",atm_balance)
    print("\n")
def admin(at):
    global atm
    atm = at
    us_name = input("Enter username \n")
    pas = input("Enter your password \n")
    if (us_name!=atm.admin_user or pas!=atm.admin_pass):
        print("Enter valid crdentials")
        print("\n")
        admin()
        return 
    else:
        while True:
            print("\n")
            print("1. Check ATM balance")
            print("2. Load amount")
            print("Press any other number to return to main menu")
            print("\n")
            op = int(input("Enter your choice"))
            if(op==1):
                chk_atm_balance(atm.atm_balance)
            elif(op==2):
                load_amount()
            else:
                print("\n Thank you for using our ATM")
                break
        