import sqlite3 as sql

# Connection to the SQLite
connection = sql.connect('db_web.db')

# Create a connection 
object = connection.cursor()

# Create users table in the db_web database 
object.execute("DROP TABLE IF EXISTS users")

# Creating users table in db_web database
sql = '''CREATE TABLE "users" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "UNAME" TEXT,
    "CONTACT" TEXT
)'''

object.execute(sql)

# Commit changes 
connection.commit()

# Close the connection 
connection.close()