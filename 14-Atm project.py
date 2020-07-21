import time
from random import *

class Account:
    def __init__(self,id=1234,balance=0,annualInterestRate=3.4):
        self.id=id
        self.balance=balance
        self.annualInterestRate=annualInterestRate

    def getId(self):
        return self.id

    def getbalance(self):
        return self.balance

    def getannualInterestRate(self):
        return self.annualInterestRate

    def getmonthyInterestRate(self):
        return self.annualInterestRate/12.0

    def diposite(self,ammount):
        self.balance+=ammount

    def withdraw(self,ammount):
        self.balance-=ammount

obj1=Account()
while True:
    pin=int(input("Enter account Pin:"))
    id=obj1.getId()
    if pin!=id:
        print("Invalid Pin")
        break
    else:
        print("Pin is correct")

    while True:
        print("1. Veiw Balance \n 2.Withdraw\n 3.Deposite\n 4.Exit")
        selection=int(input("Enter your selection:"))
        if(selection==1):
            print(f"Your current balance is",obj1.getbalance())
        elif(selection==3):
            amount=float(input("enter amount to deposite:"))
            confirm=input(f"Is this correct amount, Yes, or No ? {amount}:")
            confirm=confirm.upper()
            if(confirm=="YES"):
                obj1.diposite(amount)
                print("Amount deposited.....")
                time.sleep(1)
                print(f"Updated Balance:",obj1.getbalance())
            elif(confirm=="NO"):
                amount = float(input("enter correct amount to deposite:"))
                obj1.diposite(amount)
                print("Amount deposited.....")
                time.sleep(1)
                print(f"Updated Balance:", obj1.getbalance())

        elif(selection==2):
            withdraw_amount=float(input("Enter amount to withdraw:"))
            confirm = input(f"Is this correct amount, Yes, or No ? {withdraw_amount}:")
            confirm = confirm.upper()
            if (confirm == "YES"):
                print("Verify withdraw...")
            else:
                break
            if (withdraw_amount<obj1.getbalance()):
                obj1.withdraw(withdraw_amount)
                print("Amount has been withdrawed.....")
                time.sleep(1)
                print(f"Updated Balance:", obj1.getbalance())
            else:
                print(f"Your current balance {obj1.getbalance()} is less than withdraw amount:{withdraw_amount}")
                print("Please do doposite....")
        elif(selection==4):
            print("Transaction is completed.....")
            random_no=randint(1000,9999)
            print(f"Transaction ID is:{random_no}")
            print(f"Monthly Interest Rate:{obj1.getmonthyInterestRate()}")
            print(f"Annual Interest Rate:{obj1.getannualInterestRate()}")
            print("Thanks for choosing us as your Bank!....")
            exit()
        else:
            print("Invalid selection......")








