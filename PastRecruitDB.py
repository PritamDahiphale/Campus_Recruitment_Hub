import sqlite3  

con = sqlite3.connect("recruit.db")  
print("Database opened successfully")  
con.execute('''create table if not exists recruit (comp_id INTEGER PRIMARY KEY AUTOINCREMENT, 
comp_name TEXT UNIQUE NOT NULL,recruiter_name TEXT NOT NULL, recruit_date DATE NOT NULL, selected_stud INTEGER NOT NULL,
comp_website TEXT NOT NULL)
''') 

print("Table created successfully")  
con.close() 