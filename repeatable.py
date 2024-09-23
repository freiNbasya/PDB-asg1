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

first_connection.start_transaction(isolation_level='REPEATABLE READ')
cursor1.execute("UPDATE fruits SET amount = amount + 5 WHERE fruit_name = 'apple';")

second_connection.start_transaction(isolation_level='REPEATABLE READ')
cursor2.execute("SELECT amount from fruits WHERE fruit_name = 'apple';")
print(f"REPEATABLE READ (First Read): Amount of apples = {cursor2.fetchone()[0]}")

cursor1.execute("UPDATE fruits SET amount = amount + 2 WHERE fruit_name = 'apple';")

cursor2.execute("SELECT amount from fruits WHERE fruit_name = 'apple';")
print(f"REPEATABLE READ (Second read): Amount of apples = {cursor2.fetchone()[0]}")

first_connection.rollback()
second_connection.commit()

cursor1.close()
cursor2.close()
first_connection.close()
second_connection.close()