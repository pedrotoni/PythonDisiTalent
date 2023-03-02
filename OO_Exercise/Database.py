from Account import Account
from User import User
from Line import line


class Database:
    """This class represents a database, with the only attribute being the database itself,
    starting with a value of a empty list."""

    def __init__(self):
        self.database = []

    def add_user(self):
        """This might be the most tricky function in this program.
          First, it asks the user for inputs for name, email, address and phone
          Then we do a checking in the database, to see if the user's email is already registered in our database
          So we check all the users in the database, and if the user email is equal to the email we passed in the
          input field, it shows a message saying that the users is already registered in the database.
          if this condition is not true, we ask for login, password and account number inputs,
          meaning that we can only create a login/password/account if we are not already registered in the database.
          Note that the acc_number variable receives a string from the input.
          I created another variable called account that instantiates an Account object and we pass the acc_number variable
          as a parameter of the constructor,
          so we can create an Account object with a number that is passed as a string in the input field.
          Then we instantiate a User object using all those inputs we asked to the user, and append this User object to
          the database.
          """
        name = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        address = input("Digite seu endereço: ")
        phone = input("Digite seu telefone: ")

        for user in self.database:
            if user.email == email:
                print("Usuário já está cadastrado!")
                line()
                return

        login = input("Digite seu login: ")
        password = input("Digite sua senha: ")
        acc_number = input("Digite o numero de sua conta: ")
        account = Account(acc_number)

        usuario = User(
            name=name,
            email=email,
            address=address,
            phone=phone,
            login=login,
            password=password,
            account=account
        )
        line()
        self.database.append(usuario)

    def user_list(self):
        """This method prints a list of all the users registered in our database.
          we have a userlist variable starting with an empty list value.
          we also do a checking to see if the database is empty.
          If the database is empty, we just print a message saying that the database empty,
          if the database is not empty, we iterate through all the users in the database,
          and we append the users info in the userlist, and we get this userlist as the function return."""
        userlist = []
        if len(self.database) == 0:
            print("O banco de dados está vazio.")
            line()
        else:
            print("Lista de usuários: ")
            line()
            for user in self.database:
                userlist.append(user.info())
            return userlist

    def get_user(self, email):
        """This function is used to get the user by his email.
         we pass an email as a parameter -> parameter has to receive a string.
          Then we iterate through all the users in the database, and check if the user email
          is equal to the email we passed as parameters. If so, we get this user as the return of the function.
          If not, we get a None as the return."""
        for u in self.database:
            if u.email == email:
                return u
        return None

    def check_login(self, login, password):
        """this function checks if the login is being made the right way. It receives login and password (both
        strings) as parameters, and it checks if the login being passed as parameter is equal to the user login,
        and if the password passed as parameter is equal to the user password. If this condition is true,
        we turn the user isLoggedIn boolean attribute to True, meaning that the user is now logged, and a message saying
        that the user is logged is printed. If the condition is not true, a message saying that login or
        password is incorrect is showed in terminal."""
        for user in self.database:
            if user.login == login and user.password == password:
                user.isLoggedIn = True
                print(f'{user.name} está logado!')
                line()
                return True
        print("Login ou senha estão incorretos!")
        line()
        return False
