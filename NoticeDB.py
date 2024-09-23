import sqlite3  

con = sqlite3.connect("notice.db")  
print("Database opened successfully")  
con.execute('''create table if not exists notice (notice_id INTEGER PRIMARY KEY AUTOINCREMENT, notice_title TEXT UNIQUE NOT NULL,
notice_name TEXT UNIQUE NOT NULL,notice_date DATE NOT NULL)
''')  
print("Table created successfully")  
con.close() 