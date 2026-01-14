from Data_Operations import *

from Hashing import hash_password
from Task import Task_Operations

class User:
    def __init__(self, ID, fname, lname, email, password, mobile_number):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.mobile_number = mobile_number
        self.status = 'active'
        self.role = 'user'

class User_operations:
    @staticmethod
    def user_exists(email):
        data = read_users_data()
        logged_user = data[data["Email"] == email]

        return len(logged_user) == 1

    @staticmethod
    def check_login(email, password):
        data = read_users_data()
        logged_user = data[data["Email"] == email]

        if len(logged_user) == 1:
            logged_user["Password"][0] == hash_password(password) and logged_user["Status"][0] == 'Active'
            return logged_user
        else:
            return False

    @staticmethod
    def update_profile(ID, fname, lname, mobile_number):
        data = read_users_data()
        idx = data.index[data["ID"] == ID][0]

        data.at[idx, "First Name"] = fname
        data.at[idx, "Last Name"] = lname
        data.at[idx, "Mobile Number"] = mobile_number

        save_users_data(data)


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