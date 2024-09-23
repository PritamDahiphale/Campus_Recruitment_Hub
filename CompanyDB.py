import sqlite3  

con = sqlite3.connect("company.db")  
print("Database opened successfully")  
con.execute('''create table if not exists Company (comp_id INTEGER PRIMARY KEY AUTOINCREMENT, 
comp_name TEXT UNIQUE NOT NULL,comp_joined_date DATE NOT NULL,comp_turnover REAL,
comp_website TEXT NOT NULL)
''') 

print("Table created successfully")  
con.close() 