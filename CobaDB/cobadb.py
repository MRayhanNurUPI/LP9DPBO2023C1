# COBA MYSQL CONNECTOR PYTHON
# 2100192_Muhammad Rayhan Nur_LP9_Coba DB

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_football_tp3"
)

dbcursor = mydb.cursor()

# SELECT DATA
print("== Coba Select (Before Insert) ==")
dbcursor.execute("SELECT * FROM klub")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

# INSERT DATA
sql = "INSERT INTO klub (id_klub, nama_klub) VALUES (%s, %s)"
val = (100, "Arsenal")

print("\n== Coba Insert==")
dbcursor.execute(sql, val)

mydb.commit()

print(dbcursor.rowcount, " record inserted\n")

# SELECT DATA (AFTER INSERT)
print("== Coba Select (After Insert) ==")
dbcursor.execute("SELECT * FROM klub")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

# UPDATE DATA
sql = "UPDATE klub set nama_klub = 'Newcastle United' WHERE nama_klub='Arsenal'"
print("\n== Coba Update ==")
dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, " record updated\n")

## SELECT DATA (AFTER UPDATE)
print("== Coba Select (After Update) ==")
dbcursor.execute("SELECT * FROM klub")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

# DELETE DATA
sql = "DELETE FROM klub WHERE nama_klub='Newcastle United'"
print("\n== Coba Delete ==")
dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, " record deleted\n")

print("== Coba Select (After Delete) ==")
dbcursor.execute("SELECT * FROM klub")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)