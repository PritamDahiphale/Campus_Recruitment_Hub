import sqlite3  

con = sqlite3.connect("events.db")  
print("Database opened successfully")  
con.execute('''create table if not exists event (event_id INTEGER PRIMARY KEY AUTOINCREMENT, event_title TEXT UNIQUE NOT NULL,
event_name TEXT UNIQUE NOT NULL,event_date DATE NOT NULL)
''')  
print("Table created successfully")  
con.close() 