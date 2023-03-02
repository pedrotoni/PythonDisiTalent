from Database import Database

# implementation

print("Crie sua conta preenchendo os dados abaixo\n")

# instantiating the database object
db = Database()

# adding two users to the database
db.add_user()
db.add_user()

# Displaying the list of users
userList = db.user_list()

for user in userList:
    print(user)

# Testing the Account class functions
"""For this example, we are getting a user that has the fictional email aaa@gmail.com.
If the user exists (is not None) and also passed through the login checking 
(P.S.: Login must be 'aaa' and Password must be '123' in this example),
than this user is able to do some operations in his account. 
In this case we do 2 deposits (1000 and 1300) and 2 withdraws (500 and 100). After that, we display
the value in balance after these 4 operations, and then we get the operations report, showing all the
operations we made in this account. Then we just do the logoff for the user.
"""
user = db.get_user("aaa@gmail.com")

if user is not None and db.check_login("aaa", "123"):
    user.account.deposit(1000)
    user.account.withdraw(500)
    user.account.deposit(1300)
    user.account.withdraw(100)
    user.account.show_balance()
    user.account.operations_report()
    user.logoff()

