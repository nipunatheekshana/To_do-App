import dbms

def load_tasks():
    print("loading tasks")
    data = dbms.get()
    if data == None:
        return []
    else:
        return data

def save_tasks(tasks):
    if not(dbms.ifExcist()):
        dbms.createTable()
        
    dbms.emptyTable()
    
    for task in tasks:
        dbms.insert(task['task'], task['completed'])
        
   
