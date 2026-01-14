from Data_Operations import *

class Task:
    def __init__(self, title, description, priority, status, date_created, due_date, owner):
        self.task_id = Task_Operations.get_next_id()
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.date_created = date_created
        self.due_date = due_date
        self.owner = owner


class Task_Operations:
    @staticmethod
    def retrieve_tasks_by_userid(id):
        """
        Retrieve tasks data based on user's id
        
        :param id: ID of the logged in user to retrieve his tasks data
        """
        data = read_tasks_data()
        return data[data["Owner"] == id]

    
    @staticmethod
    def delete_task(task_id):
        """
        Delete task based on it's id
        
        :param task_id: ID of the task to be deleted
        """
        data = read_tasks_data()
        data = data[data["Task ID"] != task_id]
        save_tasks_data(data)
        return 

    @staticmethod
    def search_tasks(tasks, task_name):
        """
        Search for tasks with title
        
        :param tasks: Tasks data for the logged in user
        :param task_name: Search tasks that has a title that contains the `task_name`
        """
        search_result = tasks[tasks["Title"].str.contains(task_name, case=False, na=False)]

        return search_result


    @staticmethod
    def sort_tasks(tasks, option="due_date"):
        """
        Sort tasks based on options
        
        :param tasks: Tasks data for the logged in user
        :param option: Sort tasks by `due_date`, `priority`, or `status`
        """
        if option == "due_date":
            return tasks.sort_values(by="Due Date")

        if option == "priority":
            return tasks.sort_values(by="Priority")
        
        if option == "status":
            return tasks.sort_values(by="Status")

    @staticmethod
    def filter_tasks(tasks, priority=None, status=None, due_date=None):
        """
        Filter tasks based on entered params
        
        :param tasks: Tasks data for the logged in user
        :param priority: Priority to filter based on
        :param status: Date to filter based on
        :param due_date: Due Date to filter based on
        """
        filter_result = tasks
        if priority != None:
            filter_result = tasks[tasks["Priority"].str.contains(priority, case=False, na=False)]
        
        if status != None:
            filter_result = tasks[tasks["Status"].str.contains(status, case=False, na=False)]

        if due_date != None:
            filter_result = tasks[tasks["Due Date"].str.contains(due_date, case=False, na=False)]
        
        return filter_result
        

    @staticmethod
    def get_next_id():
        """
        Performs as an auto increamnt id for the tasks data
        """
        data = read_tasks_data()
        return int(data.tail(1)['Task ID'].iloc[0]) + 1