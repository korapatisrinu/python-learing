# class ATM:
#     def __init__(self,pin,balance=0):
#         self.__pin=pin
#         self.__balance=balance
#     def chek_pin(self):
#         entered_pin= input(("Enter your pin:"))
#         return entered_pin ==self.__pin
#     def deposit(self):
#         amount=int(input("  Enter the amount deposit:"))
#         self.__balance+=amount
#         print("✅ Deposited:", amount)
#     def withdraw(self):
#         amount=int(input("Enter amount to withdraw:"))
#         if amount > self.__balance:
#             print("❌Insufficient balance")
#         else:
#             self.__balance-=amount
#             print("✅ Withdrawn:",amount)
#     def show_balance(self):
#         print("💰 Current balance:",self.__balance)
# atm=ATM(pin="0107",balance=3000)
# if atm.chek_pin():
#     while True:
#           print("\n====== ATM MENU ======")
#           print("1. Deposit")
#           print("2. Withdraw")
#           print("3. Check Balance")
#           print("4. Exit")
#           choice=input("enter your choice:")
#           if choice=="1":
#               atm.deposit()
#           elif choice=="2":
#               atm.withdraw()
#           elif choice=="3":
#               atm.show_balance()
#           elif choice=="4":
#               print("🙏 Thanks for visiting ATM")
#               break 
#           else:
#               print("invilde choice")
# else:
#        print("  Worng pin")

                  
import os

FILE_NAME = "accounts.txt"


# ---------- Create file if not exists ----------
def create_default_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("nani,0107,5000\n")
            f.write("ram,1234,8000\n")


# ---------- Load accounts ----------
def load_accounts():
    accounts = {}

    with open(FILE_NAME, "r") as f:
        for line in f:
            username, pin, balance = line.strip().split(",")
            accounts[username] = {
                "pin": pin,
                "balance": int(balance)
            }

    return accounts


# ---------- Save accounts ----------
def save_accounts(accounts):
    with open(FILE_NAME, "w") as f:
        for user, data in accounts.items():
            f.write(f"{user},{data['pin']},{data['balance']}\n")


# ---------- ATM CLASS ----------
class ATM:

    def __init__(self, username, accounts):
        self.username = username
        self.accounts = accounts

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.accounts[self.username]["balance"] += amount
        print("✅ Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount > self.accounts[self.username]["balance"]:
            print("❌ Insufficient balance")
        else:
            self.accounts[self.username]["balance"] -= amount
            print("✅ Withdrawn:", amount)

    def show_balance(self):
        balance = self.accounts[self.username]["balance"]
        print("💰 Current balance:", balance)


# ---------- MAIN PROGRAM ----------

create_default_file()
accounts = load_accounts()

print("===== Welcome to ATM =====")

username = input("Enter username: ")

if username not in accounts:
    print("❌ User not found")

else:
    pin_attempts = 3

    while pin_attempts > 0:

        entered_pin = input("Enter PIN: ")

        if entered_pin == accounts[username]["pin"]:

            print("✅ Login successful")
            atm = ATM(username, accounts)

            while True:
                print("\n====== ATM MENU ======")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit")

                choice = input("Enter choice: ")

                if choice == "1":
                    atm.deposit()

                elif choice == "2":
                    atm.withdraw()

                elif choice == "3":
                    atm.show_balance()

                elif choice == "4":
                    save_accounts(accounts)
                    print("🙏 Thank you for using ATM")
                    break

                else:
                    print("❌ Invalid choice")

            break

        else:
            pin_attempts -= 1
            print(f"❌ Wrong PIN. Attempts left: {pin_attempts}")

    if pin_attempts == 0:
        print("🔒 Account locked")
