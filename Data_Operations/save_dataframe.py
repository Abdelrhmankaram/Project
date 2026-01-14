def save_users_data(data):
    data.to_csv("Data/users.csv", index=False)
    return data

def save_tasks_data(data):
    data.to_csv("Data/tasks.csv", index=False)