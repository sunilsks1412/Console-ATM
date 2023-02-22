
# from data import *
# from atm import mainfunc
from collections import defaultdict


atm = None
transactions = []
def check_user_balance():
    print("\n")
    print("Your balance is : ",atm.user_balance)
def deposit():
    print("\n")
    print("Deposit option")
    print("\n")
    amount=int(input("Enter the amount"))
    print("Enter the atm.denomination")
    n2=int(input("Enter the no of 2000 notes    "))
    n5=int(input("Enter the no of 500 notes     "))
    chk = (n2*2000)+(n5*500)
    if(atm.denomination[2000]+n2 <= 100 and atm.denomination[500]+n5 <= 100):
      if(chk==amount):
          atm.atm_balance+=chk
          atm.user_balance+=chk
          atm.denomination[2000]+=n2
          atm.denomination[500]+=n5
          print("\n")
          print("Amount of", amount ,"deposited successfully")
          print("\n Your new balance is",atm.user_balance)
          transactions.append("Deposited "+str(amount))
      else:
          print("The entered amount and denomination does not match")
    else:
      print("\nYou can insert only ",100-atm.denomination[2000],"2000 notes")
      print("\nYou can insert only ",100-atm.denomination[2000],"2000 notes")

def  pin_change():
    global atm
    dummy = int(input("\nEnter a current PIN"))
    if(dummy==atm.current_pin):
        np1=int(input("Enter a new PIN"))
        np2=int(input("\nRe-enter a new PIN"))
        if(np1==np2):
            atm.currrent_pin = np1
            print("\n PIN changed successfully")

def withdraw():
    amt = int(input("Enter the amount to be withdrawn"))
    if amt>atm.user_balance:
        print("\n Insufficient balance")
    elif amt>atm.atm_balance:
        print("\n Insufficient balance in ATM")
    else:
        amount = amt+0
        d1 = atm.denomination.copy()
        ab = atm.atm_balance+0
        ub = atm.user_balance+0
        for denom in d1.keys():
            count = amount//denom
            if count > d1[denom]:
                continue
            d1[denom] -= count
            ab -= count*denom
            ub -= count*denom
            amount -= count*denom
        if amount != 0:
            print(" \n Unable to withdraw amount!   ")
        else:
            collected_cash = defaultdict(lambda:0)

            for denominations in d1.keys():
                collected_cash[denominations] = atm.denomination[denominations] - d1[denominations]
            print(" \n Please collect your cash of ",amt)
            print(" \n Denomination of notes collected : ")
            for denomination in collected_cash.keys():
                if(collected_cash[denomination]==0):
                    continue
                else:
                    print(" \n ",collected_cash[denomination]," notes of ",denomination)
            atm.atm_balance = ab
            atm.user_balance = ub
            print("\n Your available balance is ",atm.user_balance)
            transactions.append("Withdrawn "+str(amt))

def mini_statement():
    print("\n")
    i=-1

    if(len(transactions)==0):
        print(" No transactions yet ")

    else:
        print("Your mini statement is : ")
        for _ in range(len(transactions)):
            if(i<-5):
                user()
                break
            print(transactions[i])
            i-=1

def user(at):
    global atm
    atm = at
    dummy = int(input("Enter a current pin \n "))
    if(dummy!= atm.current_pin):
        print("\n Incorrect PIN. Try again....")
    else:
        while True:
            print("\n")
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Mini statement")
            print("\n Press any other number to return to main menu \n")
            op = int(input("\n  Enter your choice \n"))
            print("\n")
            if(op==1):
                print(" \n Checking your balance....... \n")
                check_user_balance()
            elif(op==2):
                print(" \n Withdrawal Option \n")
                withdraw()
            elif(op==3):
                print(" \n Deposit Otion \n")
                deposit()
            elif(op==4):
                print(" \n Change PIN \n")
                pin_change()
            elif(op==5):
                print(" \n Mini statement \n")
                mini_statement()
            else:
                print(" \n Thank you for using our ATM \n")
                break