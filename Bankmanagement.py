from saving import Saving
from Fixedaccount import Fix
import sys
class Bank(Saving, Fix):
    def __init__(self, acc_id, acc_name, password, saving_amount, minimum_hold_value, fix_amount, interest_rate):
        
        self.acc_id = acc_id
        self.acc_name = acc_name
        self.__password = password
        # account control
        self.account_status = True
        self.attempt_count = 3

        # saving
        self.amount = saving_amount
        self.minimum_hold_value = minimum_hold_value

        # fix
        self.fix_amount = fix_amount
        self.intrest_rate = interest_rate
        account_status = True
        attempt_count = 3

    #menu function
    def checkPassword(self):
        while self.account_status and self.attempt_count > 0:
            print("Enter password: ")
            input_password = input()
            if input_password == self.__password:
                print("Access granted")
                return True
            else:
                self.attempt_count -= 1
                print(f"Incorrect password. Attempts left: {self.attempt_count}")
                if self.attempt_count <= 0:
                    self.account_status = False
                    print("Account Block. Too many attempts.")
                    return False
        return False
            
    def printMenu(self,ststus):
        if ststus :
            while True:
                choice = 0
                print("1. Withdraw")
                print("2. Deposit")
                print("3. View account balance")
                print("4. Account deatils")
                print("5. Exit")
                print()
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("Enter amount to withdraw: ")
                    withdraw_amount = int(input())
                    self.withdraw(withdraw_amount)
                elif choice == 2:
                    print("saving or fix? ")
                    print(" 1.Saving")
                    print(" 2.Fix")
                    second_choice = int(input("Enter your choice: "))
                    if second_choice == 1:
                        print("Enter amount to deposit: ")
                        deposit_amount = int(input())
                        self.deposit_saving(deposit_amount)
                    elif second_choice == 2:
                        print("Enter amount to deposit: ")
                        deposit_fix_amount = int(input())
                        self.deposit_fix(deposit_fix_amount)
                    else:
                        print("Invalid input. Exited.")
                elif choice == 3:
                    print("1. Saving")
                    print("2. Fix")
                    third_choice = int(input("Enter your choice: "))
                    if third_choice == 1:
                        self.show_saving_balance()
                    elif third_choice == 2:
                        self.show_fix_balance()
                        self.show_intrest()
                    else:
                        print("Invalid input. Exited.")
                elif choice == 4:
                    print(f"Account id: {self.acc_id}")
                    print(f"Account name: {self.acc_name}")
                    print(f"Account status: {'Active' if self.account_status else 'Blocked'}")
                    print(f"Saving balance: {self.amount}")
                    print(f"Fix balance: {self.fix_amount}")
                elif choice == 5:
                    print("Exiting...")
                    sys.exit()
                else:
                    print("Invalid input. Try again.")
                print()

        else:
            sys.exit()

print("Create bank account")
print()
acc_id = input("Enter account id: ")
acc_name = input("Enter account name: ")
password = input("Enter password: ")
password_confirm = input("Enter password again: ")
if password != password_confirm:
    print("Passwords do not match.")
    sys.exit()

bank = Bank(acc_id, acc_name, password, saving_amount=0, minimum_hold_value=0, fix_amount=0, interest_rate=0)
print(f"Account created successfully. Your account id is {bank.acc_id} and account name is {bank.acc_name}.")
print()

print("need to continue or exit? ")
print("1. Continue")
print("2. Exit")

choice = int(input())

if choice == 1:
    bank.printMenu(bank.checkPassword())
elif choice == 2:
    sys.exit()
else:
    print("Invalid input. exited.")