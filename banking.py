class Bank_Account:
    # contructor
    def __init__(self, name, secret, balance):
        self.name = name
        self.__secret = secret
        self.__balance = balance

    # deposite
    def deposite(self, amount, secret):
        if secret != self.__secret:
            return "Worng Passcode!"
        if amount <= 0:
            return "Invalid."

        self.__balance += amount
        print("=" * 50)
        print(f"Deposite {amount}$ seccessfully.")
        return f"Okay {self.name} you are not broke anymore now your balance is {self.__balance}$."

    # withdraw
    def withdraw(self, amount, secret):
        if secret != self.__secret:
            return "Wrong Passcode!"

        check = self.__balance - amount

        if check < 0:
            print("You have that much?")
        else:
            self.__balance = check
            print("=" * 50)
            print(f"{self.name} You have withdraw {amount}$.")
            return f"{self.name} you have {self.__balance}$ left."

    # payment
    def payment(self, service_type, amount, secret):
        if secret != self.__secret:
            return "Wrong Passcode!"
        if amount > self.__balance:
            return "you are really broke (លាងចាន)."

        self.__balance -= amount
        print("=" * 50)
        print(f"Payment successfully to {service_type} with {amount}$.")
        return f"Okay {self.name} you are now a little broke your balance is {self.__balance}$."

    # transfer
    def transfer(self, to_name, amount, secret):
        if secret != self.__secret:
            return "Wrong Passcode!"
        if amount > self.__balance:
            return "you are not have this much money."

        self.__balance -= amount
        to_name.__balance += amount
        print("=" * 50)
        print(f"{to_name.name}! {self.name} have transfer you {amount}$.")
        return f"{self.name} too rich? your balance now {self.__balance}$."

    # check_balance
    def check_balance(self, secret):
        if secret != self.__secret:
            return "Wrong Passcode!"
        print("=" * 50)
        return f"Your balance have {self.__balance}$."


# User1
BB001 = Bank_Account(name="leng", secret="123", balance=3000)
# User2
BB002 = Bank_Account(name="Neang", secret="143", balance=1000)

# User1_Access
print("=" * 50)
print("                      USER 1                      ")
print("=" * 50)
print(BB001.deposite(amount=600, secret="123"))
print(BB001.withdraw(amount=100, secret="123"))
print(BB001.payment(service_type="Ice Americano", amount=10, secret="123"))
print(BB001.transfer(to_name=BB002, amount=700, secret="123"))
print(BB001.check_balance(secret="123"))

# User2_Access
print("=" * 50)
print("                      USER 2                      ")
print("=" * 50)
print(BB002.deposite(amount=2340, secret="143"))
print(BB002.withdraw(amount=400, secret="143"))
print(BB002.payment(service_type="Ice Matcha Latte", amount=20, secret="143"))
print(BB002.transfer(to_name=BB001, amount=200, secret="143"))
print(BB002.check_balance(secret="143"))
