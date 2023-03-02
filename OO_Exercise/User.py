from Line import line


class User:
    """this class represents an User with the following attributes:
     name, email, address, phone, login, password, account -> all of them being strings
     We also have an isLoggedIn boolean attribute starting with False value, assuming that the user starts unlogged."""

    def __init__(self, name, email, address, phone, login, password, account):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.login = login
        self.password = password
        self.isLoggedIn = False
        self.account = account

    def info(self):
        """this function works like a __str__ function, and returns the user info displayed in lines."""
        return f"\nNome: {self.name}" \
               f"\nEmail: {self.email}" \
               f"\nEndereço: {self.address}" \
               f"\nTelefone: {self.phone}" \
               f"\nConta: {self.account.acc_number}" \
               f"\n------------------------------"

    def logoff(self):
        """This function just turns the boolean attribute isLoggedIn to false, meaning that the user is now unlogged.
         Also prints a message saying that the user disconnected from the system."""
        self.isLoggedIn = False
        print(f"{self.name} se desconectou.")
        line()
