class Bank_Account:
    # contructor
    def __init__(self, name, secret, balance):
        self.name = name
        self._secret = secret
        self._balance = balance

    # deposite
    def deposite(self, amount, secret):
        if secret != self._secret:
            return "Worng Passcode!"
        if amount < 0:
            return "Invalid."
        else:
            self._balance += amount
            print("=" * 50)
            print(f"Deposite {amount}$ seccessfully.")
            return f"Okay {self.name} you are not broke anymore now your balance is {self._balance}$."

    # withdraw
    def withdraw(self, amount, secret):
        if secret != self._secret:
            return "Wrong Passcode!"

        if amount < 0:
            print("Invalid amount!!")
        elif amount > self._balance:
            print("You broke")
        else:
            check = self._balance - amount
            self._balance = check
            print("=" * 50)
            print(f"{self.name} You have withdraw {amount}$.")
            return f"{self.name} you have {self._balance}$ left."

    # payment
    def payment(self, service_type, amount, secret):
        if secret != self._secret:
            return "Wrong Passcode!"
        if amount > self._balance:
            return "you are really broke (លាងចាន)."
        else:
            self._balance -= amount
            print("=" * 50)
            print(f"Payment successfully to {service_type} with {amount}$.")
            return f"Okay {self.name} you are now a little broke your balance is {self._balance}$."

    # transfer
    def transfer(self, to_name, amount, secret):
        if secret != self._secret:
            return "Wrong Passcode!"
        if amount > self._balance:
            return "you are not have this much money."
        else:
            self._balance -= amount
            to_name._balance += amount
            print("=" * 50)
            print(f"{to_name.name}! {self.name} have transfer you {amount}$.")
            return f"{self.name} too rich? your balance now {self._balance}$."

    # check_balance
    def check_balance(self, secret):
        if secret != self._secret:
            return "Wrong Passcode!"
        print("=" * 50)
        return f"Your balance have {self._balance}$."

# StudentBankAccount that inheritance from Bank_Account
class StudentBankAccount(Bank_Account):
    def withdraw(self, amount, secret):
        if secret != self._secret:
            return "Wrong Passcode!"
        
        if amount > 500:
            print("You can't withdraw over 500$.")
        elif amount < 0:
            print("Invalid amount!!")
        elif amount > self._balance:
            print("You broke")
        else:
            check = self._balance - amount
            self._balance = check
            print("=" * 50)
            print(f"{self.name} You have withdraw {amount}$.")
            return f"{self.name} you have {self._balance}$ left."
        
# PremiumSaving that inherite from Bank_Account
class PremiumSaving(Bank_Account):
    def deposite(self, amount, secret):
        if secret != self._secret:
            return "Worng Passcode!"
        if amount < 0:
            return "Invalid amount."
        else:
            interest = amount * 0.02
            total = amount + interest
            self._balance += total
            print("=" * 50)
            print(f"Deposite {amount}$ seccessfully.")
            return f"Okay {self.name} you are not broke anymore now your balance is {self._balance}$."
        
# BussinessAccount that inherite from Bank_Acoount and add method Take_loan()
class BusinessAccount(Bank_Account):
    def take_loan(self, amount, secret):
        if secret != self._secret:
            return "Wrong Passcode!"
        if amount < 0:
            return "Invalid amount"
        else:
            pass


# User1
BB001 = Bank_Account(name="leng", secret="123", balance=3000)
# User2
BB002 = Bank_Account(name="Neang", secret="143", balance=1000)
# User3
BB003 = StudentBankAccount(name="joe", secret="123", balance=100)
# print(BB003.withdraw(20, "123" ))
# User4
BB004 = PremiumSaving(name="Thomas", secret="asd", balance=1000)
print(BB004.deposite(100, "asd"))
# User5
BB005 = BusinessAccount(name="Lean", secret="asd", balance=200)
print(BB005.check_balance("asd"))
# accounts = {
#     "BB001": BB001,
#     "BB002": BB002
# }
# current_account_id = input("Enter your account ID: ").strip()

# if current_account_id not in accounts:
#     print("Invalid account ID!")
#     exit()

# current_account = accounts[current_account_id]
# print(f"Welcome {current_account.name}!")

# while True:
#     print("="*50)
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Transfer")
#     print("4. Payment")
#     print("5. Check Balance")
#     print("6. Exit")
#     print("="*50)
    
#     choice = input("\nEnter your choice: ").strip()
#     if choice == "1":
#         amount = int(input("Enter the amount : "))
#         secret = input("Enter your passcode : ")
#         print(current_account.deposite(amount, secret))
#     elif choice == "2":
#         amount = int(input("Enter the amount : "))
#         secret = input("Enter your passcode : ")
#         print(current_account.withdraw(amount, secret))
#     elif choice == "3":
#         to_account_id = input("Please input other ID account: ")
        
#         if to_account_id not in accounts:
#             print("Invalid account!!")
#         elif to_account_id == current_account_id:
#             print("You cannot transfer to your own account!")
#         else:
#             amount = int(input("Enter the amount: "))
#             secret = input("Enter your passcode: ")
#             data_take = accounts[to_account_id]
#             print(current_account.transfer(data_take, amount, secret))
#     elif choice == "4":
#         service = input("Enter service type: ")
#         amount = int(input("Enter the amount: "))
#         secret = input("Enter your passcode: ")
#         print(current_account.payment(service, amount, secret))
        
#     elif choice == "5":
#         secret = input("Enter your passcode: ")
#         print(current_account.check_balance(secret))
        
#     elif choice == "6":
#         print("Thanks for using our bank system!")
#         break
#     else:
#         print("Invalid choice!!")
        

# # User1_Access
# print("=" * 50)
# print("                      USER 1                      ")
# print("=" * 50)
# print(BB001.deposite(amount=600, secret="123"))
# print(BB001.withdraw(amount=100, secret="123"))
# print(BB001.payment(service_type="Ice Americano", amount=10, secret="123"))
# print(BB001.transfer(to_name=BB002, amount=700, secret="123"))
# print(BB001.check_balance(secret="123"))

# # User2_Access
# print("=" * 50)
# print("                      USER 2                      ")
# print("=" * 50)
# print(BB002.deposite(amount=2340, secret="143"))
# print(BB002.withdraw(amount=400, secret="143"))
# print(BB002.payment(service_type="Ice Matcha Latte", amount=20, secret="143"))
# print(BB002.transfer(to_name=BB001, amount=200, secret="143"))
# print(BB002.check_balance(secret="143"))
