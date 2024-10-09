from  sqlite4  import  SQLite4
import sqlite3

database = SQLite4("database.db")
database.connect()

def ifExcist(table):
    exist = database.select(f'{table}')
    # print(exist != None , exist)    
    return exist != None
    
def createTable(name, columns=[]):
    print("creating table")
    database.create_table(name, columns)

def insert(table, data):
    database.insert(table, data)


def get(table,coloumns='*',condition=''):
    return database.select(table,coloumns,condition)

def emptyTable(table,condition="1 == 1"):
    database.delete(table, condition)
    
def create_user_table():
    conn=sqlite3.connect('database.db')
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    conn.commit()
    conn.close()
    
