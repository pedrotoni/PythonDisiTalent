from Line import line


class Account:
    """this class represents an account that has the following attributes:
     - number,
     - balance (starting with 0),
     - operations (starting with a empty list - everytime we deposit
     or withdraw some money from the account, the operation will be registered in the self.operations list),
     - num_of_deposits (how many deposits we made)
     - num_of_withdraws (how many withdraws we made)
     - total_operations (how many operations we made)

     Attributes:
          acc_number() -> string"""

    def __init__(self, acc_number):
        self.acc_number = acc_number
        self.acc_balance = 0
        self.operations = []
        self.num_of_deposits = 0
        self.num_of_withdraws = 0
        self.total_operations = 0

    def deposit(self, amount):
        """this function takes an amount as parameter, and sums this amount to the self.acc_balance that starts with 0.
          everytime we deposit, we receive a message saying what was the deposit's value, append the deposit
          to the self.operations list and sum 1 to the total number of deposits/total number of operations."""
        self.acc_balance += amount
        print(f"Depósito de {amount:.2f} realizado com sucesso!")
        self.operations.append(f'Depósito: {amount:.2f}')
        self.num_of_deposits += 1
        self.total_operations += 1
        line()

    def withdraw(self, amount):
        """this function takes an amount as parameter, and subtracts this amount in the self.acc_balance that starts with 0.
          everytime we withdraw, we receive a message saying what was the withdraw's value, append the withdraw
          to the self.operations list, and sum 1 to the total number of withdraws/total number of operations.
          this function also has a balance check made with a if statement,
          so if the amount we want to withdraw is higher than the value in the account balance at that moment,
          the withdraw will not be completed and we get a message saying that the balance is insufficient"""
        if self.acc_balance < amount:
            print("Saldo insuficiente.")
            line()
        else:
            self.acc_balance -= amount
            print(f"Saque de {amount:.2f} realizado com sucesso!")
            self.operations.append(f'Saque: {amount:.2f}')
            self.num_of_withdraws += 1
            self.total_operations += 1
            line()

    def show_balance(self):
        """This function just shows/prints the value in the account balance at that point in time."""
        print(f"Saldo atual: {self.acc_balance:.2f}")
        line()

    def operations_report(self):
        """this function lists all the operations we made in our account,
         and shows us what the operation was and how much was the operations value."""
        print("Você realizou as seguintes operações bancárias: \n")
        for operation in self.operations:
            print(operation)
            line()
        print(f'Total de depósitos: {self.num_of_deposits}'
              f'\nTotal de saques: {self.num_of_withdraws}'
              f'\nTotal de operações: {self.total_operations}')
        line()
