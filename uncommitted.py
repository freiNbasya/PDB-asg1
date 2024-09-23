import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE
from datetime import datetime
import os

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

first_connection.start_transaction(isolation_level='READ UNCOMMITTED')
cursor1.execute("UPDATE fruits SET amount = amount + 2 WHERE fruit_name = 'apple';")


second_connection.start_transaction(isolation_level='READ UNCOMMITTED')
cursor2.execute("SELECT amount from fruits WHERE fruit_name = 'apple';")
dirty_read = cursor2.fetchone()[0]

print(f"Dirty Read (READ UNCOMMITTED): Amount of apples = {dirty_read}")

first_connection.rollback()
second_connection.commit()

cursor1.close()
cursor2.close()
first_connection.close()
second_connection.close()