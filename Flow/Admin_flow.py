import inquirer
from Task import Task_Operations
from User import Admin_operations

def view_all_users(admin):
    tasks = Admin_operations.view_all_users()

    tasks_questions = [
        inquirer.List(
            name="task",
            message="Choose task to manage",
            choices=[f"{int(j[0])}: {j[1]} {j[2]} - {j[3]} - {j[-2]}" for i, j in tasks.iterrows() if j[-1] == "User"]
        ),
        inquirer.List(
            name="operation",
            message="Activate/Deactive User?",
            choices=["Yes", "No"]
        ),
    ]

    user_id = int(inquirer.prompt(tasks_questions[:1])["task"].split(":")[0])
    print(type(user_id))
    print(user_id)

    operation = inquirer.prompt(tasks_questions[1:])["operation"]

    if operation == "Yes":
        Admin_operations.Activate_deactivate_account(user_id)

    else:
        return

def view_all_tasks(admin):
    tasks = Admin_operations.view_all_tasks()

    tasks_questions = [
        inquirer.List(
            name="task",
            message="Choose task to manage",
            choices=[f"{j[0]}: {j[1]} - {j[6]}" for i, j in tasks.iterrows()]
        ),
        inquirer.List(
            name="operation",
            message="Delete This Task?",
            choices=["Yes", "No"]
        ),
    ]

    task_id = int(inquirer.prompt(tasks_questions[:1])["task"].split(":")[0])

    print(task_id)

    operation = inquirer.prompt(tasks_questions[1:])["operation"]

    if operation == "Yes":
        Admin_operations.delete_task(task_id)
        


def Admin_flow(admin):
    questions = [
        inquirer.List(
            name="choice",
            message="Choose what you want to do",
            choices=["View All Users", "View All Tasks", "Back"]
        )
    ]

    while True:
        answers = inquirer.prompt(questions)

        if answers["choice"] == "View All Users":
            view_all_users(admin)

        elif answers["choice"] == "View All Tasks":
            view_all_tasks(admin)
        
        else:
            return