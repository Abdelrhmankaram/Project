from Data_Operations import *
import pandas as pd
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
    
    def get_tasks(self):
        data = read_tasks_data()
        # print(self.ID)
        data["Owner"] = data["Owner"].astype(int).astype(str)

        data = data[data["Owner"] == self.ID]
        
        return data


    def update_profile(self, fname, lname, mobile_number):
        data = read_users_data()
        idx = data.index[data["ID"] == int(self.ID)][0]

        data.at[idx, "First Name"] = fname
        data.at[idx, "Last Name"] = lname
        data.at[idx, "Mobile Number"] = mobile_number

        save_users_data(data)

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

        if logged_user.empty:
            return False

        user = logged_user.iloc[0]

        if (
            user["Password"] == hash_password(password)
            and user["Status"] == "Active"
        ):
            return logged_user

        return False

    
    @staticmethod
    def insert_user(user):
        data = read_users_data()
        new_row = pd.DataFrame([{
            "ID": user["ID"],
            "First Name": user["fname"],
            "Last Name": user["lname"],
            "Email": user["email"],
            "Password": hash_password(user["password"]),
            "Mobile Number": user["mobile"],
            "Status": "Active",
            "Role": "User"
        }])
        
        data = pd.concat([data, new_row], ignore_index=True)

        save_users_data(data)

    @staticmethod
    def insert_admin(user):
        data = read_users_data()
        new_row = pd.DataFrame([{
            "ID": user["ID"],
            "First Name": user["fname"],
            "Last Name": user["lname"],
            "Email": user["email"],
            "Password": hash_password(user["password"]),
            "Mobile Number": user["mobile"],
            "Status": "Active",
            "Role": "Admin"
        }])

        data = pd.concat([data, new_row], ignore_index=True)

        save_users_data(data)