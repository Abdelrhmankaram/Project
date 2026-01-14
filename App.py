import inquirer

name = inquirer.List(
    name="name",
    message="hello?",
    choices=[
        "world",
        "wrold",
        "woorld"
    ]
)

if list(inquirer.prompt([name]).values())[0] == "world":
    print("Correct choice")
else:
    print("Incorrect choice")