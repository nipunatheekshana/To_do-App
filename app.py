import dbms

def load_tasks(userId):
    print("loading tasks")
    data = dbms.get('tasks',['task','completed'], f"user = {userId}")
    if data == None:
        return []
    else:
        return data

def save_tasks(userId,tasks):
    try:
        if not(dbms.ifExcist('tasks')):
            dbms.createTable('tasks', ['user','task', 'completed'])
            
        dbms.emptyTable('tasks', f"user = {userId}")
        
        for task in tasks:
            dbms.insert('tasks',{'user':userId,"task": task['task'] , "completed":  task['completed']})
    except Exception as e:
        print(e) 
            
   
