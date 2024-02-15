
import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'Qwerty@123',
    port = '3306',
    database = 'xyz'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM emplyee_info')
result = mycursor.fetchall()

for userA in result:
    print(userA)


