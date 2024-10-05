import os
import dbms

tasks=[]

def load_tasks():
    print("loading tasks")
    data = dbms.get()
    if data == None:
        return
    else:
        for line in data:
            task={"task": f"{line[0]}", "completed": line[1]}
            tasks.append(task)

def save_tasks():
    if not(dbms.ifExcist()):
        dbms.createTable()
        
    dbms.emptyTable()
    
    for task in tasks:
        dbms.insert(task['task'], task['completed'])
        
def add_task():
    task = input("Enter task: ")
    task={"task": f"{task}", "completed": False}
    tasks.append(task)
    
def view_tasks():
    i= 0
    for task in tasks:
        if(task["completed"]):
            print(f"[x] {i} - {task['task']}")
        else:
            print(f"[ ] {i} - {task['task']}")
        i+=1
        
def delete_task():
    view_tasks()
    task_number=''
    while(not isInt(task_number)):
        task_number = input("Enter task number to delete: ")
    task_number = int(task_number)
    if(task_number >= len(tasks)):
        print("Task number is not valid")
        return
    del tasks[task_number]
    
def mark_complete():
    view_tasks()
    task_number=''
    while(not isInt(task_number)):
        task_number = input("Enter task number to mark as complete: ")
    task_number = int(task_number)
    if(task_number >= len(tasks)):
        print("Task number is not valid")
        return
    tasks[task_number]["completed"] = True
    
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def run():
    load_tasks()
    
    while True:
        save_tasks()
        comand =''
        while(not isInt(comand)):
            comand = input("Enter your camand (1-7)(if need help press 8): ")
        os.system('cls||clear')
        comand = int(comand)
        if(comand==1):
            add_task()
        elif(comand==2):
            view_tasks()
        elif(comand==3):
            delete_task()
        elif(comand==4):
            mark_complete()
        elif(comand==5):
            save_tasks()
        elif(comand==7):
            exit()
        elif(comand==8):
            print("1 - Add task\n2 - View tasks\n3 - Delete task\n4 - Mark complete\n5 - Save tasks\n6 - Exit")

run()