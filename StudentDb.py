import sqlite3  

con = sqlite3.connect("student.db")  
print("Database opened successfully")  
# con.execute('drop table student')
con.execute('''create table IF NOT EXISTS student (stud_enroll INTEGER PRIMARY KEY, 
stud_name TEXT UNIQUE NOT NULL,birth_date DATE NOT NULL,stud_gender TEXT NOT NULL,
stud_address TEXT NOT NULL, stud_branch TEXT NOT NULL, stud_branch_code INTEGER NOT NULL, stud_marks INTEGER NOT NULL,stud_back_sub INTEGER NOT NULL, stud_in_comp TEXT NOT NULL)
''')  

print("Table created successfully")  
con.close() 