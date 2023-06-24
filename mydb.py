import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'Venu2002@',
    auth_plugin='mysql_native_password',


	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATEfDATABASE elderco")

print("All Done!")