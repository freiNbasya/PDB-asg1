import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE


first_connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

second_connection= mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

cursor1 = first_connection.cursor()
cursor2 = second_connection.cursor()

first_connection.start_transaction(isolation_level='READ COMMITTED')
cursor1.execute("UPDATE fruits SET amount = amount + 10 WHERE fruit_name = 'apple';")

second_connection.start_transaction(isolation_level='READ COMMITTED')
cursor2.execute("UPDATE fruits SET amount = amount + 5 WHERE fruit_name = 'banana';")

cursor1.execute("UPDATE fruits SET amount = amount + 5 WHERE fruit_name = 'banana';")

cursor2.execute("UPDATE fruits SET amount = amount + 5 WHERE fruit_name = 'apple';")

first_connection.rollback() 
second_connection.rollback()

cursor1.close()
cursor2.close()
first_connection.close()
second_connection.close()