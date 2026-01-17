import inquirer
from Data_Operations import *
from Hashing import *
from Task import *
from User import *
from Flow import Login, Signup

while True:
    session = inquirer.prompt([inquirer.List(
        name="Log in or Sign up",
        message="Welcome to your To-Do List Application!!",
        choices=["Login", "Sign Up"]
    )])

    if list(session.values())[0] == "Login":
        Login()
    else:
        Signup()