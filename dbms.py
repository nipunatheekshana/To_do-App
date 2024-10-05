from  sqlite4  import  SQLite4

database = SQLite4("database.db")
database.connect()

def ifExcist():
    exist = database.select('tasks')
    # print(exist != None , exist)    
    return exist != None
    
def createTable():
    print("creating table")
    database.create_table("tasks", ["task", "completed"])

def insert(task, completed):
    database.insert("tasks", {"task": task , "completed": completed})

def get():
    return database.select("tasks")

def emptyTable():
    database.delete("tasks", "1 == 1")