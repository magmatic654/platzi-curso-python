class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, ammount):
        if self.is_active:
            self.balance += ammount
            print(f"Se ha depositado {ammount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retidado ${amount}. Saldo actual ${self.balance}")
        else:
            print("No es posible retirar, cuenta inactiva")
    
    def deactivate_account(self):
        if self.is_active == True:
            self.is_active = False
            print("La cuenta ha sido desactivada")
        else:
            print("La cuenta ya está desactivada")
    
    def activate_account(self):
        if self.is_active == False:
            self.is_active = True
            print("La cuenta ha sido activada")
        else:
            print("La cuenta ya está activa")


account1 = BankAccount("Harold", 1000)
account2 = BankAccount("Lalo", 200)

#Llamada a los métodos
account1.deposit(500)
account1.deactivate_account()
account1.deposit(100)
account1.withdraw(100)
account1.activate_account()
account1.withdraw(100)

