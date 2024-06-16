import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

# prepeare cusrsor object

cusrsorObject = dataBase.cursor()

# create a database
cusrsorObject.execute("CREATE DATABASE elderco")
print("All Done!")