from User import User
from Data_Operations import *
from Task import Task_Operations

class Admin(User):
    def __init__(self, ID, fname, lname, email, password, mobile_number):
        super().__init__(ID, fname, lname, email, password, mobile_number)
        self.role = 'admin'

class Admin_operations:
    @staticmethod
    def view_all_users():
        return read_users_data()
    
    def view_all_tasks():
        return read_tasks_data()
    
    def delete_task(id):
        return Task_Operations.delete_task(id)
    
    def deactivate_account(id):
        data = read_users_data()
        idx = data.index[data["ID"] == id][0]

        data.at[idx, "Status"] = "Not Active"
        
        save_users_data(data)