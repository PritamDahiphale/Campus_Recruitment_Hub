import sqlite3  

# other users database and table
con = sqlite3.connect("users.db")  
print("Database opened successfully")  
con.execute("create table IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT  NOT NULL, email TEXT NOT NULL)")  
print("Table created successfully") 

# username="1906018" #3 error here
# cur=con.cursor()
# cur.execute('SELECT * FROM Users WHERE username = ?',username)
# account= cur.fetchall()
# print(account)
con.close() 


# admin database and table
con2 = sqlite3.connect("admin.db")  
print("Database opened successfully")  
con2.execute("create table IF NOT EXISTS Admin (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT  NOT NULL, email TEXT NOT NULL)")  
print("Table created successfully")  

admin_query = """INSERT INTO Admin
                          (id, username,password, email) 
                           VALUES 
                          (1,'admin','gppadmin@123','gppune@123')"""

# cur2=con2.cursor()

# cur2.execute('SELECT * FROM Admin WHERE username ="admin" AND password = "gppadmin@123"')
# data=cur2.fetchone()
# print(data)
con2.commit()
con2.close()