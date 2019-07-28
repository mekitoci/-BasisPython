#加密模組 getpass
import getpass

_username = "Yang"
_password = "abc123"
username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("Welcome user {name} Login..." .format(name = username))
else:
    print("Invalid username or password!!")


