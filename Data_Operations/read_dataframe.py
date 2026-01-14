def read_users_data():
    import pandas as pd
    data = pd.read_csv("Data/users.csv")

    # data["Owner"] = data["Owner"].astype(str)
    return data

def read_tasks_data():
    import pandas as pd
    data = pd.read_csv("Data/tasks.csv")

    # data["Owner"] = data["Owner"].astype(str)
    return data